"""Find staged recommendations that use an earlier acceptance in the same note.

Reads ../derived/rows_remedia.csv. Every exported row is a committed action,
listed in acceptance order within its note.

A candidate is a changed row whose recommendation text either
  (a) names a product an earlier row added or switched to, when that product
      is not on the note's starting medication list, or
  (b) names a product an earlier row stopped or switched away from, together
      with a phrase stating that the change was made.

String matching only proposes candidates. Each candidate is then read and
decided in handoff_decisions.csv (kept = yes/no, with a reason). When that file
exists, the script also writes handoff_summary.csv from the kept rows.

Usage: python count_handoffs.py
"""

from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROWS = HERE.parent / "derived" / "rows_remedia.csv"
CANDIDATES = HERE / "handoff_candidates.csv"
DECISIONS = HERE / "handoff_decisions.csv"
SUMMARY = HERE / "handoff_summary.csv"

INTRODUCING = {"add", "replace"}
STOPPING = {"discontinue", "replace"}
STATE_CUE = re.compile(
    r"\b(already|has been|have been|was|were|now|newly|previously|recently|this cycle|"
    r"just|removed|discontinued|stopped|replaced|added|started|switched)\b",
    re.IGNORECASE,
)
ACCEPTED = {"Correct", "Acceptable"}


def product(line: str) -> str:
    """Product name of one action side, lower case, without dose or problem."""
    line = line.strip()
    if not line or line.startswith("("):
        return ""
    name = re.split(r" - | @ ", line, maxsplit=1)[0]
    return re.sub(r"[®™]", "", name).strip().lower()


def parse_action(action: str) -> tuple[str, str, str]:
    verb, _, rest = action.partition(" | ")
    source, _, target = rest.partition(" → ")
    return verb.strip(), product(source), product(target)


def sentences_naming(text: str, name: str) -> list[str]:
    pattern = re.compile(r"(?<![a-z])" + re.escape(name) + r"(?![a-z])", re.IGNORECASE)
    return [s.strip() for s in re.split(r"(?<=[.;])\s+", text) if pattern.search(s)]


def find_candidates(rows: list[dict]) -> list[dict]:
    by_case: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        by_case[row["case"]].append(row)

    out: list[dict] = []
    for case, case_rows in sorted(by_case.items()):
        case_rows.sort(key=lambda r: int(r["order"]))
        parsed = [parse_action(r["action"]) for r in case_rows]
        starting = {src for _, src, _ in parsed if src}

        introduced: list[tuple[str, int, str]] = []
        stopped: list[tuple[str, int, str]] = []
        for row, (verb, src, dst) in zip(case_rows, parsed):
            order = int(row["order"])
            text = row["recommendation"] or ""
            if verb != "kept" and text:
                for name, earlier, earlier_action in introduced:
                    if name in (src, dst):
                        continue
                    for sentence in sentences_naming(text, name):
                        out.append(_candidate(row, verb, "a", name, earlier, earlier_action, sentence))
                        break
                for name, earlier, earlier_action in stopped:
                    if name in (src, dst):
                        continue
                    for sentence in sentences_naming(text, name):
                        if STATE_CUE.search(sentence):
                            out.append(_candidate(row, verb, "b", name, earlier, earlier_action, sentence))
                            break
            if verb in INTRODUCING and dst and dst not in starting:
                introduced.append((dst, order, row["action"]))
            if verb in STOPPING and src:
                stopped.append((src, order, row["action"]))
    return out


def _candidate(row, verb, kind, name, earlier, earlier_action, sentence) -> dict:
    return {
        "case": row["case"],
        "order": row["order"],
        "action_class": row["action_class"],
        "flag": row["flag"],
        "kind": kind,
        "product": name,
        "earlier_order": earlier,
        "earlier_action": earlier_action,
        "sentence": sentence,
        "rec_evaluation": row["rec_evaluation"],
    }


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def summarize(candidates: list[dict]) -> list[dict]:
    decisions = {
        (d["case"], d["order"], d["product"]): d
        for d in csv.DictReader(DECISIONS.open(encoding="utf-8"))
    }
    missing = [c for c in candidates if (c["case"], c["order"], c["product"]) not in decisions]
    if missing:
        raise SystemExit(f"{len(missing)} candidates have no decision in {DECISIONS.name}")

    kept = [c for c in candidates if decisions[(c["case"], c["order"], c["product"])]["kept"] == "yes"]
    rows = {(c["case"], c["order"]): c for c in kept}
    kinds = defaultdict(set)
    for c in kept:
        kinds[c["kind"]].add((c["case"], c["order"]))
    accepted = sum(1 for c in rows.values() if c["rec_evaluation"] in ACCEPTED)
    return [
        {"measure": "candidate_rows", "value": len({(c["case"], c["order"]) for c in candidates})},
        {"measure": "handoff_rows", "value": len(rows)},
        {"measure": "handoff_notes", "value": len({case for case, _ in rows})},
        {"measure": "rows_using_an_added_product", "value": len(kinds["a"])},
        {"measure": "rows_using_a_stopped_product", "value": len(kinds["b"])},
        {"measure": "handoff_rows_correct_or_acceptable", "value": accepted},
    ]


def main() -> None:
    rows = list(csv.DictReader(ROWS.open(encoding="utf-8")))
    candidates = find_candidates(rows)
    write_csv(CANDIDATES, candidates)
    print(f"{len(candidates)} candidates -> {CANDIDATES.name}")
    if DECISIONS.exists():
        summary = summarize(candidates)
        write_csv(SUMMARY, summary)
        for item in summary:
            print(f"{item['measure']}: {item['value']}")


if __name__ == "__main__":
    main()
