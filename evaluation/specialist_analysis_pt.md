> **Path note (English archive layout):** graded Excel files are now `../specialist_workbooks/specialist_grades_remedia.xlsx` and `specialist_grades_baseline.xlsx`. The per-case Portuguese report is `case_report_pt.md` (formerly `relatorio_por_caso.md`). Internal Portuguese prose below may still use the old filenames.

# Avaliação do especialista: RemedIA e baseline

O especialista devolveu as duas fichas dos 26 casos de polifarmácia escocesa (`scot_09_01`–`scot_09_26`). RemedIA é o pipeline em etapas da corrida `scottish_polypharmacy_full_20261014`. O baseline é o prompt por medicamento de Ong et al., na ficha `avaliacao_especialista_baseline.xlsx`. O texto de cada linha é o mesmo da ficha em branco; o que entrou aqui são as notas, as observações e as lacunas preenchidas.

A ficha do RemedIA em `scot_09_15` (ansiedade) não traz nenhuma recomendação: a aba existe, o cabeçalho existe, e a tabela de linhas está vazia. Esse caso entra na tabela por caso com N = 0 e fica fora das taxas e da comparação caso a caso.

A nota comparável entre os braços é `Rec Evaluation`. As quatro palavras da ficha são as da legenda: **Correct** (apropriada), **Acceptable** (razoável), **Debatable** (não é errada, mas não é razoável), **Incorrect** (errada).

O relatório `relatorio_por_caso.md` compara cada caso com o baseline. Lá, criatividade é o número de ações propositivas por keep, a acurácia é a taxa das quatro notas, e o detalhe compara a explicação das ações iguais no mesmo fármaco. A última seção soma os 26 casos e lista em quais cada algoritmo foi melhor.

## Como as taxas foram contadas

Cada linha da ficha é uma recomendação. Entram no denominador só as linhas com uma das quatro notas. Todas as linhas do RemedIA e do baseline estão avaliadas.

- **Acerto amplo:** Correct + Acceptable, sobre as linhas avaliadas.
- **Acerto estrito:** só Correct.
- **Taxa de erro:** só Incorrect. Debatable não entra no acerto nem no erro; fica na coluna própria.
- **Com keep:** todas as linhas avaliadas, inclusive as que mantêm o medicamento.
- **Sem keep:** as mesmas contas, tirando a classe `keep`.
- **Tipo de sugestão:** a ação exportada. No RemedIA é o verbo da coluna `Action_input_output` (`kept`, `discontinue`, `reduce_dosage`, `increase_dosage`, `replace`, `add`). No baseline a ficha não traz o verbo; a classe é o primeiro verbo clínico da frase `Recommendation` (ou `Kept:` quando o modelo não nomeou o medicamento). Se a frase começa por review, plan ou consolidate e ainda assim suspende ou reduz a dose, vale esse verbo. Troca de formulação do mesmo fármaco entra em `replace`. A levotiroxina de 100 microgramas em `scot_09_02` é keep: a suspensão é a linha de 50 microgramas.
- **Criativa:** a linha inicia um medicamento que não é o da linha (`add`) ou troca o fármaco (`replace`). Manter, suspender e mudar a dose do mesmo fármaco são conservadoras. No baseline, uma suspensão que no meio da frase também cita um substituto continua contada como suspensão; essas frases estão listadas à parte e não entram na taxa de criatividade.
- **Resposta repetida:** o mesmo plano em duas linhas, ou a mesma frase copiada em duas linhas. Continua na contagem. É um defeito da resposta do modelo, anotado no caso. As frases genéricas que o prompt manda escrever em todo medicamento mantido ou suspenso (`Keep the medication in the regimen` e `Discontinue the medication`) não entram.

Os 26 casos são vinhetas de ensino. As tabelas descrevem esta amostra. Não há teste de hipótese nem afirmação sobre outros pacientes.

## Criatividade: quantas recomendações de cada tipo

Cada linha é uma recomendação exportada, com ou sem nota. A última linha é o total. Iniciar e substituir são as ações criativas: propõem um fármaco que não é o da linha. As outras ações mantêm, suspendem ou ajustam a dose do mesmo fármaco.

| Tipo de ação | RemedIA (n) | RemedIA (%) | Baseline (n) | Baseline (%) |
| --- | --- | --- | --- | --- |
| manter | 92 | 30.2 | 113 | 36.9 |
| suspender | 65 | 21.3 | 110 | 35.9 |
| reduzir dose | 23 | 7.5 | 37 | 12.1 |
| aumentar dose | 13 | 4.3 | 6 | 2.0 |
| substituir | 75 | 24.6 | 5 | 1.6 |
| iniciar | 37 | 12.1 | 35 | 11.4 |
| outra | 0 | 0.0 | 0 | 0.0 |
| Total | 305 | 100.0 | 306 | 100.0 |

Iniciar mais substituir soma 112 de 305 recomendações no RemedIA (36.7%) e 40 de 306 no baseline (13.1%). O RemedIA concentra a criatividade na substituição (75 linhas). O baseline quase não substitui e põe o fármaco novo na linha de início.

## Precisão clínica: número de cada nota por tipo de ação

Cada célula é o número de linhas com aquela nota. A última linha é o total. No RemedIA, suspender soma 65 linhas avaliadas em 65 exportadas; o total avaliado é 305 de 305.

| Tipo de ação | Correto Rem | Aceitável Rem | Debatível Rem | Incorreto Rem | Correto C | Aceitável C | Debatível C | Incorreto C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| manter | 33 | 23 | 15 | 21 | 42 | 34 | 22 | 15 |
| suspender | 56 | 0 | 2 | 7 | 104 | 5 | 1 | 0 |
| reduzir dose | 13 | 1 | 3 | 6 | 24 | 8 | 4 | 1 |
| aumentar dose | 3 | 1 | 3 | 6 | 5 | 0 | 1 | 0 |
| substituir | 34 | 14 | 16 | 11 | 5 | 0 | 0 | 0 |
| iniciar | 17 | 6 | 10 | 4 | 23 | 10 | 2 | 0 |
| outra | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Total | 156 | 45 | 49 | 55 | 203 | 57 | 30 | 16 |

## Resultado geral

| Recorte | Algoritmo | N | Correct | Acceptable | Debatable | Incorrect | Acerto amplo % | Acerto estrito % | Erro % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Todas (com keep) | RemedIA | 305 | 156 | 45 | 49 | 55 | 65.9 | 51.1 | 18.0 |
| Todas (com keep) | Baseline | 306 | 203 | 57 | 30 | 16 | 85.0 | 66.3 | 5.2 |
| Sem keep | RemedIA | 213 | 123 | 22 | 34 | 34 | 68.1 | 57.7 | 16.0 |
| Sem keep | Baseline | 193 | 161 | 23 | 8 | 1 | 95.3 | 83.4 | 0.5 |
| Só keep | RemedIA | 92 | 33 | 23 | 15 | 21 | 60.9 | 35.9 | 22.8 |
| Só keep | Baseline | 113 | 42 | 34 | 22 | 15 | 67.3 | 37.2 | 13.3 |

No conjunto, o baseline acerta mais e erra menos. O acerto amplo é 85.0% contra 65.9% do RemedIA (+19.1 pontos). O acerto estrito é 66.3% contra 51.1% (+15.2 pontos). A taxa de erro é 5.2% contra 18.0% (-12.8 pontos).

Tirar os keeps não inverte a comparação e aumenta o acerto amplo dos dois: sem keep, 95.3% no baseline e 68.1% no RemedIA, com erro de 0.5% e 16.0%. Manter o medicamento é uma classe fraca nos dois (acerto amplo 60.9% no RemedIA e 67.3% no baseline). No RemedIA o erro dentro dos keeps é 22.8%, acima do erro do baseline nessa classe (13.3%). O especialista muitas vezes anotou que o fármaco mantido deveria ter sido suspenso ou ter a dose revista.

Caso a caso, nos 25 casos em que os dois braços têm linhas, o acerto amplo do baseline fica acima do RemedIA em 17, abaixo em 5 e empata em 3. Sem keep, nos 25 casos em que os dois têm alguma linha que não é keep, são 15 acima, 5 abaixo e 5 empates.

## Cada caso

N é o número de linhas avaliadas. Acerto amplo, acerto estrito e erro estão em porcentagem. A segunda tabela tira os keeps.

### RemedIA, com keep

| Caso | Título | N | C | A | D | I | Amplo | Estrito | Erro |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 09_01 | Frailty without overt multimorbidity | 9 | 8 | 0 | 1 | 0 | 88.9 | 88.9 | 0.0 |
| 09_02 | Frailty with multimorbidity | 17 | 8 | 1 | 2 | 6 | 52.9 | 47.1 | 35.3 |
| 09_03 | Care home resident with multimorbidity | 14 | 7 | 1 | 4 | 2 | 57.1 | 50.0 | 14.3 |
| 09_04 | Care home resident with multimorbidity including dementia | 13 | 10 | 1 | 1 | 1 | 84.6 | 76.9 | 7.7 |
| 09_05 | Younger adult with intellectual disability in a care home | 8 | 5 | 1 | 1 | 1 | 75.0 | 62.5 | 12.5 |
| 09_06 | Multimorbidity without frailty (acute pain, depression, COPD and high-risk combinations) | 25 | 13 | 1 | 3 | 8 | 56.0 | 52.0 | 32.0 |
| 09_07 | High risk combination – antiplatelet and anticoagulant | 13 | 3 | 2 | 4 | 4 | 38.5 | 23.1 | 30.8 |
| 09_08 | Chronic pain – opioids | 20 | 11 | 3 | 3 | 3 | 70.0 | 55.0 | 15.0 |
| 09_09 | Chronic pain – anticonvulsants | 4 | 4 | 0 | 0 | 0 | 100.0 | 100.0 | 0.0 |
| 09_10 | Chronic pain – Antidepressants | 8 | 1 | 1 | 3 | 3 | 25.0 | 12.5 | 37.5 |
| 09_11 | Type 2 diabetes mellitus with severe frailty | 24 | 11 | 7 | 5 | 1 | 75.0 | 45.8 | 4.2 |
| 09_12 | Chronic Constipation | 17 | 10 | 1 | 2 | 4 | 64.7 | 58.8 | 23.5 |
| 09_13 | Adult with Parkinson’s disease | 8 | 4 | 2 | 2 | 0 | 75.0 | 50.0 | 0.0 |
| 09_14 | Depression and Health Inequalities | 3 | 3 | 0 | 0 | 0 | 100.0 | 100.0 | 0.0 |
| 09_15 | Anxiety | 0 | 0 | 0 | 0 | 0 | — | — | — |
| 09_16 | Post traumatic stress disorder with “street benzo” use | 1 | 1 | 0 | 0 | 0 | 100.0 | 100.0 | 0.0 |
| 09_17 | Bipolar disorder and lithium | 4 | 2 | 0 | 1 | 1 | 50.0 | 50.0 | 25.0 |
| 09_18 | Antipsychotics in dementia | 8 | 1 | 1 | 2 | 4 | 25.0 | 12.5 | 50.0 |
| 09_19 | Antipsychotic use following recent hospital discharge | 6 | 3 | 2 | 0 | 1 | 83.3 | 50.0 | 16.7 |
| 09_20 | Antibiotics - penicillin allergy de-labelling | 11 | 7 | 0 | 3 | 1 | 63.6 | 63.6 | 9.1 |
| 09_21 | Antibiotics in end-of-life care | 15 | 6 | 3 | 2 | 4 | 60.0 | 40.0 | 26.7 |
| 09_22 | Medication Sick Day Guidance (in nursing home resident) | 15 | 9 | 4 | 1 | 1 | 86.7 | 60.0 | 6.7 |
| 09_23 | Osteoporosis and risk of falls | 15 | 9 | 3 | 2 | 1 | 80.0 | 60.0 | 6.7 |
| 09_24 | Palliative Care (Cardiovascular) | 23 | 9 | 3 | 6 | 5 | 52.2 | 39.1 | 21.7 |
| 09_25 | Palliative Care – End of Life Care | 16 | 7 | 4 | 1 | 4 | 68.8 | 43.8 | 25.0 |
| 09_26 | Drug dependency and requests for medication out of hours | 8 | 4 | 4 | 0 | 0 | 100.0 | 50.0 | 0.0 |

### RemedIA, sem keep

| Caso | N | C | A | D | I | Amplo | Estrito | Erro | N criativas | Amplo criativas | Erro criativas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 09_01 | 8 | 8 | 0 | 0 | 0 | 100.0 | 100.0 | 0.0 | 4 | 100.0 | 0.0 |
| 09_02 | 14 | 7 | 1 | 1 | 5 | 57.1 | 50.0 | 35.7 | 5 | 60.0 | 20.0 |
| 09_03 | 9 | 6 | 0 | 1 | 2 | 66.7 | 66.7 | 22.2 | 3 | 66.7 | 0.0 |
| 09_04 | 10 | 9 | 1 | 0 | 0 | 100.0 | 90.0 | 0.0 | 4 | 100.0 | 0.0 |
| 09_05 | 7 | 4 | 1 | 1 | 1 | 71.4 | 57.1 | 14.3 | 4 | 100.0 | 0.0 |
| 09_06 | 23 | 13 | 0 | 3 | 7 | 56.5 | 56.5 | 30.4 | 15 | 73.3 | 13.3 |
| 09_07 | 9 | 2 | 1 | 3 | 3 | 33.3 | 22.2 | 33.3 | 4 | 25.0 | 25.0 |
| 09_08 | 15 | 9 | 0 | 3 | 3 | 60.0 | 60.0 | 20.0 | 7 | 42.9 | 28.6 |
| 09_09 | 3 | 3 | 0 | 0 | 0 | 100.0 | 100.0 | 0.0 | 3 | 100.0 | 0.0 |
| 09_10 | 4 | 0 | 0 | 3 | 1 | 0.0 | 0.0 | 25.0 | 4 | 0.0 | 25.0 |
| 09_11 | 15 | 9 | 2 | 4 | 0 | 73.3 | 60.0 | 0.0 | 7 | 42.9 | 0.0 |
| 09_12 | 10 | 4 | 0 | 2 | 4 | 40.0 | 40.0 | 40.0 | 7 | 28.6 | 42.9 |
| 09_13 | 3 | 3 | 0 | 0 | 0 | 100.0 | 100.0 | 0.0 | 2 | 100.0 | 0.0 |
| 09_14 | 1 | 1 | 0 | 0 | 0 | 100.0 | 100.0 | 0.0 | 1 | 100.0 | 0.0 |
| 09_15 | 0 | 0 | 0 | 0 | 0 | — | — | — | 0 | — | — |
| 09_16 | 1 | 1 | 0 | 0 | 0 | 100.0 | 100.0 | 0.0 | 1 | 100.0 | 0.0 |
| 09_17 | 3 | 2 | 0 | 1 | 0 | 66.7 | 66.7 | 0.0 | 2 | 50.0 | 0.0 |
| 09_18 | 6 | 1 | 1 | 2 | 2 | 33.3 | 16.7 | 33.3 | 4 | 25.0 | 50.0 |
| 09_19 | 4 | 3 | 1 | 0 | 0 | 100.0 | 75.0 | 0.0 | 1 | 100.0 | 0.0 |
| 09_20 | 9 | 6 | 0 | 2 | 1 | 66.7 | 66.7 | 11.1 | 3 | 33.3 | 0.0 |
| 09_21 | 13 | 6 | 3 | 2 | 2 | 69.2 | 46.2 | 15.4 | 8 | 50.0 | 25.0 |
| 09_22 | 9 | 6 | 1 | 1 | 1 | 77.8 | 66.7 | 11.1 | 3 | 33.3 | 33.3 |
| 09_23 | 5 | 4 | 1 | 0 | 0 | 100.0 | 80.0 | 0.0 | 3 | 100.0 | 0.0 |
| 09_24 | 13 | 6 | 1 | 5 | 1 | 53.8 | 46.2 | 7.7 | 4 | 50.0 | 0.0 |
| 09_25 | 11 | 6 | 4 | 0 | 1 | 90.9 | 54.5 | 9.1 | 9 | 100.0 | 0.0 |
| 09_26 | 8 | 4 | 4 | 0 | 0 | 100.0 | 50.0 | 0.0 | 4 | 100.0 | 0.0 |

### Baseline, com keep

| Caso | Título | N | C | A | D | I | Amplo | Estrito | Erro |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 09_01 | Frailty without overt multimorbidity | 11 | 6 | 1 | 2 | 2 | 63.6 | 54.5 | 18.2 |
| 09_02 | Frailty with multimorbidity | 17 | 14 | 1 | 0 | 2 | 88.2 | 82.4 | 11.8 |
| 09_03 | Care home resident with multimorbidity | 13 | 7 | 3 | 3 | 0 | 76.9 | 53.8 | 0.0 |
| 09_04 | Care home resident with multimorbidity including dementia | 12 | 6 | 2 | 1 | 3 | 66.7 | 50.0 | 25.0 |
| 09_05 | Younger adult with intellectual disability in a care home | 8 | 4 | 3 | 1 | 0 | 87.5 | 50.0 | 0.0 |
| 09_06 | Multimorbidity without frailty (acute pain, depression, COPD and high-risk combinations) | 24 | 18 | 1 | 3 | 2 | 79.2 | 75.0 | 8.3 |
| 09_07 | High risk combination – antiplatelet and anticoagulant | 10 | 6 | 3 | 1 | 0 | 90.0 | 60.0 | 0.0 |
| 09_08 | Chronic pain – opioids | 16 | 11 | 4 | 1 | 0 | 93.8 | 68.8 | 0.0 |
| 09_09 | Chronic pain – anticonvulsants | 4 | 2 | 2 | 0 | 0 | 100.0 | 50.0 | 0.0 |
| 09_10 | Chronic pain – Antidepressants | 8 | 4 | 3 | 0 | 1 | 87.5 | 50.0 | 12.5 |
| 09_11 | Type 2 diabetes mellitus with severe frailty | 26 | 15 | 7 | 3 | 1 | 84.6 | 57.7 | 3.8 |
| 09_12 | Chronic Constipation | 15 | 14 | 1 | 0 | 0 | 100.0 | 93.3 | 0.0 |
| 09_13 | Adult with Parkinson’s disease | 8 | 5 | 1 | 2 | 0 | 75.0 | 62.5 | 0.0 |
| 09_14 | Depression and Health Inequalities | 4 | 2 | 1 | 1 | 0 | 75.0 | 50.0 | 0.0 |
| 09_15 | Anxiety | 1 | 1 | 0 | 0 | 0 | 100.0 | 100.0 | 0.0 |
| 09_16 | Post traumatic stress disorder with “street benzo” use | 5 | 5 | 0 | 0 | 0 | 100.0 | 100.0 | 0.0 |
| 09_17 | Bipolar disorder and lithium | 5 | 3 | 1 | 0 | 1 | 80.0 | 60.0 | 20.0 |
| 09_18 | Antipsychotics in dementia | 10 | 6 | 1 | 1 | 2 | 70.0 | 60.0 | 20.0 |
| 09_19 | Antipsychotic use following recent hospital discharge | 8 | 8 | 0 | 0 | 0 | 100.0 | 100.0 | 0.0 |
| 09_20 | Antibiotics - penicillin allergy de-labelling | 10 | 4 | 4 | 1 | 1 | 80.0 | 40.0 | 10.0 |
| 09_21 | Antibiotics in end-of-life care | 14 | 11 | 3 | 0 | 0 | 100.0 | 78.6 | 0.0 |
| 09_22 | Medication Sick Day Guidance (in nursing home resident) | 14 | 6 | 5 | 3 | 0 | 78.6 | 42.9 | 0.0 |
| 09_23 | Osteoporosis and risk of falls | 14 | 7 | 5 | 1 | 1 | 85.7 | 50.0 | 7.1 |
| 09_24 | Palliative Care (Cardiovascular) | 24 | 18 | 3 | 3 | 0 | 87.5 | 75.0 | 0.0 |
| 09_25 | Palliative Care – End of Life Care | 16 | 15 | 1 | 0 | 0 | 100.0 | 93.8 | 0.0 |
| 09_26 | Drug dependency and requests for medication out of hours | 9 | 5 | 1 | 3 | 0 | 66.7 | 55.6 | 0.0 |

### Baseline, sem keep

| Caso | N | C | A | D | I | Amplo | Estrito | Erro | N criativas | Amplo criativas | Erro criativas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 09_01 | 9 | 6 | 1 | 1 | 1 | 77.8 | 66.7 | 11.1 | 3 | 100.0 | 0.0 |
| 09_02 | 12 | 12 | 0 | 0 | 0 | 100.0 | 100.0 | 0.0 | 0 | — | — |
| 09_03 | 9 | 6 | 2 | 1 | 0 | 88.9 | 66.7 | 0.0 | 1 | 100.0 | 0.0 |
| 09_04 | 8 | 6 | 1 | 1 | 0 | 87.5 | 75.0 | 0.0 | 2 | 100.0 | 0.0 |
| 09_05 | 6 | 3 | 3 | 0 | 0 | 100.0 | 50.0 | 0.0 | 0 | — | — |
| 09_06 | 18 | 17 | 0 | 1 | 0 | 94.4 | 94.4 | 0.0 | 6 | 100.0 | 0.0 |
| 09_07 | 7 | 5 | 2 | 0 | 0 | 100.0 | 71.4 | 0.0 | 0 | — | — |
| 09_08 | 8 | 8 | 0 | 0 | 0 | 100.0 | 100.0 | 0.0 | 1 | 100.0 | 0.0 |
| 09_09 | 2 | 1 | 1 | 0 | 0 | 100.0 | 50.0 | 0.0 | 0 | — | — |
| 09_10 | 3 | 2 | 1 | 0 | 0 | 100.0 | 66.7 | 0.0 | 1 | 100.0 | 0.0 |
| 09_11 | 14 | 9 | 4 | 1 | 0 | 92.9 | 64.3 | 0.0 | 2 | 50.0 | 0.0 |
| 09_12 | 9 | 9 | 0 | 0 | 0 | 100.0 | 100.0 | 0.0 | 1 | 100.0 | 0.0 |
| 09_13 | 4 | 4 | 0 | 0 | 0 | 100.0 | 100.0 | 0.0 | 1 | 100.0 | 0.0 |
| 09_14 | 2 | 0 | 1 | 1 | 0 | 50.0 | 0.0 | 0.0 | 1 | 100.0 | 0.0 |
| 09_15 | 0 | 0 | 0 | 0 | 0 | — | — | — | 0 | — | — |
| 09_16 | 5 | 5 | 0 | 0 | 0 | 100.0 | 100.0 | 0.0 | 3 | 100.0 | 0.0 |
| 09_17 | 2 | 2 | 0 | 0 | 0 | 100.0 | 100.0 | 0.0 | 0 | — | — |
| 09_18 | 7 | 6 | 1 | 0 | 0 | 100.0 | 85.7 | 0.0 | 3 | 100.0 | 0.0 |
| 09_19 | 7 | 7 | 0 | 0 | 0 | 100.0 | 100.0 | 0.0 | 1 | 100.0 | 0.0 |
| 09_20 | 4 | 3 | 1 | 0 | 0 | 100.0 | 75.0 | 0.0 | 1 | 100.0 | 0.0 |
| 09_21 | 14 | 11 | 3 | 0 | 0 | 100.0 | 78.6 | 0.0 | 5 | 100.0 | 0.0 |
| 09_22 | 4 | 3 | 0 | 1 | 0 | 75.0 | 75.0 | 0.0 | 1 | 0.0 | 0.0 |
| 09_23 | 5 | 5 | 0 | 0 | 0 | 100.0 | 100.0 | 0.0 | 0 | — | — |
| 09_24 | 14 | 13 | 1 | 0 | 0 | 100.0 | 92.9 | 0.0 | 3 | 100.0 | 0.0 |
| 09_25 | 15 | 14 | 1 | 0 | 0 | 100.0 | 93.3 | 0.0 | 3 | 100.0 | 0.0 |
| 09_26 | 5 | 4 | 0 | 1 | 0 | 80.0 | 80.0 | 0.0 | 1 | 100.0 | 0.0 |

### Os dois braços, caso a caso

A diferença é o acerto amplo do baseline menos o do RemedIA, em pontos percentuais.

| Caso | N Rem | Amplo Rem | Erro Rem | N C | Amplo C | Erro C | Δ amplo | N Rem sem keep | Amplo Rem sem keep | N C sem keep | Amplo C sem keep | Δ amplo sem keep |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 09_01 | 9 | 88.9 | 0.0 | 11 | 63.6 | 18.2 | -25.3 | 8 | 100.0 | 9 | 77.8 | -22.2 |
| 09_02 | 17 | 52.9 | 35.3 | 17 | 88.2 | 11.8 | +35.3 | 14 | 57.1 | 12 | 100.0 | +42.9 |
| 09_03 | 14 | 57.1 | 14.3 | 13 | 76.9 | 0.0 | +19.8 | 9 | 66.7 | 9 | 88.9 | +22.2 |
| 09_04 | 13 | 84.6 | 7.7 | 12 | 66.7 | 25.0 | -17.9 | 10 | 100.0 | 8 | 87.5 | -12.5 |
| 09_05 | 8 | 75.0 | 12.5 | 8 | 87.5 | 0.0 | +12.5 | 7 | 71.4 | 6 | 100.0 | +28.6 |
| 09_06 | 25 | 56.0 | 32.0 | 24 | 79.2 | 8.3 | +23.2 | 23 | 56.5 | 18 | 94.4 | +37.9 |
| 09_07 | 13 | 38.5 | 30.8 | 10 | 90.0 | 0.0 | +51.5 | 9 | 33.3 | 7 | 100.0 | +66.7 |
| 09_08 | 20 | 70.0 | 15.0 | 16 | 93.8 | 0.0 | +23.8 | 15 | 60.0 | 8 | 100.0 | +40.0 |
| 09_09 | 4 | 100.0 | 0.0 | 4 | 100.0 | 0.0 | +0.0 | 3 | 100.0 | 2 | 100.0 | +0.0 |
| 09_10 | 8 | 25.0 | 37.5 | 8 | 87.5 | 12.5 | +62.5 | 4 | 0.0 | 3 | 100.0 | +100.0 |
| 09_11 | 24 | 75.0 | 4.2 | 26 | 84.6 | 3.8 | +9.6 | 15 | 73.3 | 14 | 92.9 | +19.5 |
| 09_12 | 17 | 64.7 | 23.5 | 15 | 100.0 | 0.0 | +35.3 | 10 | 40.0 | 9 | 100.0 | +60.0 |
| 09_13 | 8 | 75.0 | 0.0 | 8 | 75.0 | 0.0 | +0.0 | 3 | 100.0 | 4 | 100.0 | +0.0 |
| 09_14 | 3 | 100.0 | 0.0 | 4 | 75.0 | 0.0 | -25.0 | 1 | 100.0 | 2 | 50.0 | -50.0 |
| 09_15 | 0 | — | — | 1 | 100.0 | 0.0 | — | 0 | — | 0 | — | — |
| 09_16 | 1 | 100.0 | 0.0 | 5 | 100.0 | 0.0 | +0.0 | 1 | 100.0 | 5 | 100.0 | +0.0 |
| 09_17 | 4 | 50.0 | 25.0 | 5 | 80.0 | 20.0 | +30.0 | 3 | 66.7 | 2 | 100.0 | +33.3 |
| 09_18 | 8 | 25.0 | 50.0 | 10 | 70.0 | 20.0 | +45.0 | 6 | 33.3 | 7 | 100.0 | +66.7 |
| 09_19 | 6 | 83.3 | 16.7 | 8 | 100.0 | 0.0 | +16.7 | 4 | 100.0 | 7 | 100.0 | +0.0 |
| 09_20 | 11 | 63.6 | 9.1 | 10 | 80.0 | 10.0 | +16.4 | 9 | 66.7 | 4 | 100.0 | +33.3 |
| 09_21 | 15 | 60.0 | 26.7 | 14 | 100.0 | 0.0 | +40.0 | 13 | 69.2 | 14 | 100.0 | +30.8 |
| 09_22 | 15 | 86.7 | 6.7 | 14 | 78.6 | 0.0 | -8.1 | 9 | 77.8 | 4 | 75.0 | -2.8 |
| 09_23 | 15 | 80.0 | 6.7 | 14 | 85.7 | 7.1 | +5.7 | 5 | 100.0 | 5 | 100.0 | +0.0 |
| 09_24 | 23 | 52.2 | 21.7 | 24 | 87.5 | 0.0 | +35.3 | 13 | 53.8 | 14 | 100.0 | +46.2 |
| 09_25 | 16 | 68.8 | 25.0 | 16 | 100.0 | 0.0 | +31.2 | 11 | 90.9 | 15 | 100.0 | +9.1 |
| 09_26 | 8 | 100.0 | 0.0 | 9 | 66.7 | 0.0 | -33.3 | 8 | 100.0 | 5 | 80.0 | -20.0 |

## Cada caso, por tipo de ação

Cada caso tem as duas tabelas do recorte global. A primeira conta as recomendações de cada tipo. A segunda conta Correto, Aceitável, Debatível e Incorreto. A última linha é o total. Um tipo só aparece quando algum dos braços tem pelo menos uma linha dessa classe.

Uma resposta repetida continua nessas contagens. O comentário embaixo da tabela registra o defeito: o modelo escreveu o mesmo plano duas vezes, ou copiou a mesma frase em duas linhas.

Há 4 respostas repetidas, em Baseline.

### 09_01 — Frailty without overt multimorbidity

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 1 | 2 |
| suspender | 4 | 4 |
| reduzir dose | 0 | 2 |
| substituir | 3 | 0 |
| iniciar | 1 | 3 |
| Total | 9 | 11 |

| Tipo de ação | Correto Rem | Aceitável Rem | Debatível Rem | Incorreto Rem | Correto C | Aceitável C | Debatível C | Incorreto C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| manter | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 |
| suspender | 4 | 0 | 0 | 0 | 4 | 0 | 0 | 0 |
| reduzir dose | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| substituir | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| iniciar | 1 | 0 | 0 | 0 | 2 | 1 | 0 | 0 |
| Total | 8 | 0 | 1 | 0 | 6 | 1 | 2 | 2 |

### 09_02 — Frailty with multimorbidity

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 3 | 5 |
| suspender | 2 | 9 |
| reduzir dose | 5 | 3 |
| aumentar dose | 2 | 0 |
| substituir | 5 | 0 |
| Total | 17 | 17 |

| Tipo de ação | Correto Rem | Aceitável Rem | Debatível Rem | Incorreto Rem | Correto C | Aceitável C | Debatível C | Incorreto C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| manter | 1 | 0 | 1 | 1 | 2 | 1 | 0 | 2 |
| suspender | 2 | 0 | 0 | 0 | 9 | 0 | 0 | 0 |
| reduzir dose | 3 | 0 | 0 | 2 | 3 | 0 | 0 | 0 |
| aumentar dose | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 |
| substituir | 2 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| Total | 8 | 1 | 2 | 6 | 14 | 1 | 0 | 2 |

### 09_03 — Care home resident with multimorbidity

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 5 | 4 |
| suspender | 4 | 5 |
| reduzir dose | 2 | 3 |
| substituir | 2 | 0 |
| iniciar | 1 | 1 |
| Total | 14 | 13 |

| Tipo de ação | Correto Rem | Aceitável Rem | Debatível Rem | Incorreto Rem | Correto C | Aceitável C | Debatível C | Incorreto C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| manter | 1 | 1 | 3 | 0 | 1 | 1 | 2 | 0 |
| suspender | 3 | 0 | 0 | 1 | 5 | 0 | 0 | 0 |
| reduzir dose | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 0 |
| substituir | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| iniciar | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| Total | 7 | 1 | 4 | 2 | 7 | 3 | 3 | 0 |

### 09_04 — Care home resident with multimorbidity including dementia

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 3 | 4 |
| suspender | 6 | 6 |
| substituir | 2 | 1 |
| iniciar | 2 | 1 |
| Total | 13 | 12 |

| Tipo de ação | Correto Rem | Aceitável Rem | Debatível Rem | Incorreto Rem | Correto C | Aceitável C | Debatível C | Incorreto C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| manter | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 3 |
| suspender | 6 | 0 | 0 | 0 | 5 | 0 | 1 | 0 |
| substituir | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| iniciar | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| Total | 10 | 1 | 1 | 1 | 6 | 2 | 1 | 3 |

### 09_05 — Younger adult with intellectual disability in a care home

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 1 | 2 |
| suspender | 1 | 2 |
| reduzir dose | 1 | 4 |
| aumentar dose | 1 | 0 |
| substituir | 4 | 0 |
| Total | 8 | 8 |

| Tipo de ação | Correto Rem | Aceitável Rem | Debatível Rem | Incorreto Rem | Correto C | Aceitável C | Debatível C | Incorreto C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| manter | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| suspender | 0 | 0 | 0 | 1 | 2 | 0 | 0 | 0 |
| reduzir dose | 1 | 0 | 0 | 0 | 1 | 3 | 0 | 0 |
| aumentar dose | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| substituir | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Total | 5 | 1 | 1 | 1 | 4 | 3 | 1 | 0 |

### 09_06 — Multimorbidity without frailty (acute pain, depression, COPD and high-risk combinations)

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 2 | 6 |
| suspender | 3 | 8 |
| reduzir dose | 2 | 3 |
| aumentar dose | 3 | 1 |
| substituir | 9 | 1 |
| iniciar | 6 | 5 |
| Total | 25 | 24 |

| Tipo de ação | Correto Rem | Aceitável Rem | Debatível Rem | Incorreto Rem | Correto C | Aceitável C | Debatível C | Incorreto C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| manter | 0 | 1 | 0 | 1 | 1 | 1 | 2 | 2 |
| suspender | 1 | 0 | 0 | 2 | 8 | 0 | 0 | 0 |
| reduzir dose | 0 | 0 | 1 | 1 | 2 | 0 | 1 | 0 |
| aumentar dose | 1 | 0 | 0 | 2 | 1 | 0 | 0 | 0 |
| substituir | 5 | 0 | 2 | 2 | 1 | 0 | 0 | 0 |
| iniciar | 6 | 0 | 0 | 0 | 5 | 0 | 0 | 0 |
| Total | 13 | 1 | 3 | 8 | 18 | 1 | 3 | 2 |

Resposta repetida, defeito do modelo:

- Baseline. Linhas 10, 11 são o mesmo plano, escrito duas vezes, para o bisoprolol. A linha 10 (Atenolol 50mg tablets) diz: Switch atenolol to bisoprolol 2.5mg orally once daily (titrating according to heart rate and blood pressure) for optimized rate control in AF and post-MI management. A linha 11 (Bisoprolol tablets) diz: Initiate bisoprolol 2.5mg orally once daily to replace atenolol, titrating as tolerated for rate control. O especialista anotou na linha 11: "Recomendação duplicada?".
- Baseline. Linhas 15, 16 repetem a frase "Discontinue liquid presentation.". Alvos: Levothyroxine 50micrograms/5ml liquid; Levothyroxine 25micrograms/5ml liquid. É a mesma resposta copiada em mais de uma linha.

### 09_07 — High risk combination – antiplatelet and anticoagulant

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 4 | 3 |
| suspender | 4 | 4 |
| reduzir dose | 1 | 3 |
| substituir | 3 | 0 |
| iniciar | 1 | 0 |
| Total | 13 | 10 |

| Tipo de ação | Correto Rem | Aceitável Rem | Debatível Rem | Incorreto Rem | Correto C | Aceitável C | Debatível C | Incorreto C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| manter | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 |
| suspender | 1 | 0 | 1 | 2 | 3 | 1 | 0 | 0 |
| reduzir dose | 1 | 0 | 0 | 0 | 2 | 1 | 0 | 0 |
| substituir | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| iniciar | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| Total | 3 | 2 | 4 | 4 | 6 | 3 | 1 | 0 |

### 09_08 — Chronic pain – opioids

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 5 | 8 |
| suspender | 4 | 4 |
| reduzir dose | 3 | 3 |
| aumentar dose | 1 | 0 |
| substituir | 3 | 0 |
| iniciar | 4 | 1 |
| Total | 20 | 16 |

| Tipo de ação | Correto Rem | Aceitável Rem | Debatível Rem | Incorreto Rem | Correto C | Aceitável C | Debatível C | Incorreto C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| manter | 2 | 3 | 0 | 0 | 3 | 4 | 1 | 0 |
| suspender | 3 | 0 | 1 | 0 | 4 | 0 | 0 | 0 |
| reduzir dose | 3 | 0 | 0 | 0 | 3 | 0 | 0 | 0 |
| aumentar dose | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| substituir | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
| iniciar | 2 | 0 | 1 | 1 | 1 | 0 | 0 | 0 |
| Total | 11 | 3 | 3 | 3 | 11 | 4 | 1 | 0 |

### 09_09 — Chronic pain – anticonvulsants

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 1 | 2 |
| suspender | 0 | 1 |
| reduzir dose | 0 | 1 |
| substituir | 3 | 0 |
| Total | 4 | 4 |

| Tipo de ação | Correto Rem | Aceitável Rem | Debatível Rem | Incorreto Rem | Correto C | Aceitável C | Debatível C | Incorreto C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| manter | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| suspender | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| reduzir dose | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| substituir | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Total | 4 | 0 | 0 | 0 | 2 | 2 | 0 | 0 |

### 09_10 — Chronic pain – Antidepressants

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 4 | 5 |
| suspender | 0 | 1 |
| reduzir dose | 0 | 1 |
| substituir | 3 | 0 |
| iniciar | 1 | 1 |
| Total | 8 | 8 |

| Tipo de ação | Correto Rem | Aceitável Rem | Debatível Rem | Incorreto Rem | Correto C | Aceitável C | Debatível C | Incorreto C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| manter | 1 | 1 | 0 | 2 | 2 | 2 | 0 | 1 |
| suspender | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| reduzir dose | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| substituir | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 |
| iniciar | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |
| Total | 1 | 1 | 3 | 3 | 4 | 3 | 0 | 1 |

### 09_11 — Type 2 diabetes mellitus with severe frailty

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 9 | 12 |
| suspender | 7 | 8 |
| reduzir dose | 1 | 4 |
| substituir | 4 | 0 |
| iniciar | 3 | 2 |
| Total | 24 | 26 |

| Tipo de ação | Correto Rem | Aceitável Rem | Debatível Rem | Incorreto Rem | Correto C | Aceitável C | Debatível C | Incorreto C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| manter | 2 | 5 | 1 | 1 | 6 | 3 | 2 | 1 |
| suspender | 7 | 0 | 0 | 0 | 7 | 1 | 0 | 0 |
| reduzir dose | 0 | 1 | 0 | 0 | 2 | 2 | 0 | 0 |
| substituir | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 |
| iniciar | 0 | 1 | 2 | 0 | 0 | 1 | 1 | 0 |
| Total | 11 | 7 | 5 | 1 | 15 | 7 | 3 | 1 |

### 09_12 — Chronic Constipation

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 7 | 6 |
| suspender | 2 | 6 |
| reduzir dose | 1 | 2 |
| substituir | 4 | 1 |
| iniciar | 3 | 0 |
| Total | 17 | 15 |

| Tipo de ação | Correto Rem | Aceitável Rem | Debatível Rem | Incorreto Rem | Correto C | Aceitável C | Debatível C | Incorreto C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| manter | 6 | 1 | 0 | 0 | 5 | 1 | 0 | 0 |
| suspender | 1 | 0 | 0 | 1 | 6 | 0 | 0 | 0 |
| reduzir dose | 1 | 0 | 0 | 0 | 2 | 0 | 0 | 0 |
| substituir | 1 | 0 | 1 | 2 | 1 | 0 | 0 | 0 |
| iniciar | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
| Total | 10 | 1 | 2 | 4 | 14 | 1 | 0 | 0 |

### 09_13 — Adult with Parkinson’s disease

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 5 | 4 |
| suspender | 1 | 1 |
| reduzir dose | 0 | 1 |
| aumentar dose | 0 | 1 |
| substituir | 2 | 1 |
| Total | 8 | 8 |

| Tipo de ação | Correto Rem | Aceitável Rem | Debatível Rem | Incorreto Rem | Correto C | Aceitável C | Debatível C | Incorreto C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| manter | 1 | 2 | 2 | 0 | 1 | 1 | 2 | 0 |
| suspender | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| reduzir dose | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| aumentar dose | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| substituir | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| Total | 4 | 2 | 2 | 0 | 5 | 1 | 2 | 0 |

### 09_14 — Depression and Health Inequalities

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 2 | 2 |
| aumentar dose | 0 | 1 |
| substituir | 1 | 0 |
| iniciar | 0 | 1 |
| Total | 3 | 4 |

| Tipo de ação | Correto Rem | Aceitável Rem | Debatível Rem | Incorreto Rem | Correto C | Aceitável C | Debatível C | Incorreto C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| manter | 2 | 0 | 0 | 0 | 2 | 0 | 0 | 0 |
| aumentar dose | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| substituir | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| iniciar | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| Total | 3 | 0 | 0 | 0 | 2 | 1 | 1 | 0 |

### 09_15 — Anxiety

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 0 | 1 |
| Total | 0 | 1 |

| Tipo de ação | Correto Rem | Aceitável Rem | Debatível Rem | Incorreto Rem | Correto C | Aceitável C | Debatível C | Incorreto C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| manter | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| Total | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |

### 09_16 — Post traumatic stress disorder with “street benzo” use

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| suspender | 0 | 2 |
| substituir | 1 | 0 |
| iniciar | 0 | 3 |
| Total | 1 | 5 |

| Tipo de ação | Correto Rem | Aceitável Rem | Debatível Rem | Incorreto Rem | Correto C | Aceitável C | Debatível C | Incorreto C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| suspender | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 |
| substituir | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| iniciar | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 |
| Total | 1 | 0 | 0 | 0 | 5 | 0 | 0 | 0 |

### 09_17 — Bipolar disorder and lithium

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 1 | 3 |
| suspender | 0 | 1 |
| reduzir dose | 1 | 1 |
| substituir | 2 | 0 |
| Total | 4 | 5 |

| Tipo de ação | Correto Rem | Aceitável Rem | Debatível Rem | Incorreto Rem | Correto C | Aceitável C | Debatível C | Incorreto C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| manter | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 1 |
| suspender | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| reduzir dose | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| substituir | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| Total | 2 | 0 | 1 | 1 | 3 | 1 | 0 | 1 |

### 09_18 — Antipsychotics in dementia

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 2 | 3 |
| suspender | 1 | 4 |
| reduzir dose | 1 | 0 |
| substituir | 3 | 0 |
| iniciar | 1 | 3 |
| Total | 8 | 10 |

| Tipo de ação | Correto Rem | Aceitável Rem | Debatível Rem | Incorreto Rem | Correto C | Aceitável C | Debatível C | Incorreto C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| manter | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 2 |
| suspender | 1 | 0 | 0 | 0 | 4 | 0 | 0 | 0 |
| reduzir dose | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| substituir | 0 | 0 | 1 | 2 | 0 | 0 | 0 | 0 |
| iniciar | 0 | 1 | 0 | 0 | 2 | 1 | 0 | 0 |
| Total | 1 | 1 | 2 | 4 | 6 | 1 | 1 | 2 |

### 09_19 — Antipsychotic use following recent hospital discharge

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 2 | 1 |
| suspender | 3 | 6 |
| iniciar | 1 | 1 |
| Total | 6 | 8 |

| Tipo de ação | Correto Rem | Aceitável Rem | Debatível Rem | Incorreto Rem | Correto C | Aceitável C | Debatível C | Incorreto C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| manter | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 |
| suspender | 3 | 0 | 0 | 0 | 6 | 0 | 0 | 0 |
| iniciar | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 |
| Total | 3 | 2 | 0 | 1 | 8 | 0 | 0 | 0 |

Resposta repetida, defeito do modelo:

- Baseline. Linhas 7, 8 repetem a frase "Ensure medication is confirmed discontinued and removed from the active regimen as the course is complete.". Alvos: Amoxicillin 500mg capsules; Trimethoprim 200mg tablets. É a mesma resposta copiada em mais de uma linha.

### 09_20 — Antibiotics - penicillin allergy de-labelling

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 2 | 6 |
| suspender | 4 | 2 |
| reduzir dose | 1 | 0 |
| aumentar dose | 1 | 1 |
| substituir | 1 | 0 |
| iniciar | 2 | 1 |
| Total | 11 | 10 |

| Tipo de ação | Correto Rem | Aceitável Rem | Debatível Rem | Incorreto Rem | Correto C | Aceitável C | Debatível C | Incorreto C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| manter | 1 | 0 | 1 | 0 | 1 | 3 | 1 | 1 |
| suspender | 4 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| reduzir dose | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| aumentar dose | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 |
| substituir | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| iniciar | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 |
| Total | 7 | 0 | 3 | 1 | 4 | 4 | 1 | 1 |

### 09_21 — Antibiotics in end-of-life care

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 2 | 0 |
| suspender | 5 | 9 |
| substituir | 4 | 0 |
| iniciar | 4 | 5 |
| Total | 15 | 14 |

| Tipo de ação | Correto Rem | Aceitável Rem | Debatível Rem | Incorreto Rem | Correto C | Aceitável C | Debatível C | Incorreto C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| manter | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 |
| suspender | 5 | 0 | 0 | 0 | 9 | 0 | 0 | 0 |
| substituir | 0 | 2 | 1 | 1 | 0 | 0 | 0 | 0 |
| iniciar | 1 | 1 | 1 | 1 | 2 | 3 | 0 | 0 |
| Total | 6 | 3 | 2 | 4 | 11 | 3 | 0 | 0 |

### 09_22 — Medication Sick Day Guidance (in nursing home resident)

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 6 | 10 |
| suspender | 6 | 1 |
| reduzir dose | 0 | 2 |
| substituir | 1 | 0 |
| iniciar | 2 | 1 |
| Total | 15 | 14 |

| Tipo de ação | Correto Rem | Aceitável Rem | Debatível Rem | Incorreto Rem | Correto C | Aceitável C | Debatível C | Incorreto C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| manter | 3 | 3 | 0 | 0 | 3 | 5 | 2 | 0 |
| suspender | 6 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| reduzir dose | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 |
| substituir | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| iniciar | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 |
| Total | 9 | 4 | 1 | 1 | 6 | 5 | 3 | 0 |

Resposta repetida, defeito do modelo:

- Baseline. Linhas 5, 6 repetem a frase "Continue while on opioid therapy, but step down/titrate according to bowel frequency and potential opioid dose reduction.". Alvos: Macrogol 3350 sachets; Senna 7.5mg tablets. É a mesma resposta copiada em mais de uma linha.

### 09_23 — Osteoporosis and risk of falls

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 10 | 9 |
| suspender | 2 | 3 |
| reduzir dose | 0 | 1 |
| aumentar dose | 0 | 1 |
| substituir | 2 | 0 |
| iniciar | 1 | 0 |
| Total | 15 | 14 |

| Tipo de ação | Correto Rem | Aceitável Rem | Debatível Rem | Incorreto Rem | Correto C | Aceitável C | Debatível C | Incorreto C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| manter | 5 | 2 | 2 | 1 | 2 | 5 | 1 | 1 |
| suspender | 2 | 0 | 0 | 0 | 3 | 0 | 0 | 0 |
| reduzir dose | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| aumentar dose | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| substituir | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| iniciar | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Total | 9 | 3 | 2 | 1 | 7 | 5 | 1 | 1 |

### 09_24 — Palliative Care (Cardiovascular)

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 10 | 10 |
| suspender | 2 | 9 |
| reduzir dose | 3 | 1 |
| aumentar dose | 4 | 1 |
| substituir | 3 | 1 |
| iniciar | 1 | 2 |
| Total | 23 | 24 |

| Tipo de ação | Correto Rem | Aceitável Rem | Debatível Rem | Incorreto Rem | Correto C | Aceitável C | Debatível C | Incorreto C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| manter | 3 | 2 | 1 | 4 | 5 | 2 | 3 | 0 |
| suspender | 2 | 0 | 0 | 0 | 8 | 1 | 0 | 0 |
| reduzir dose | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 0 |
| aumentar dose | 2 | 0 | 2 | 0 | 1 | 0 | 0 | 0 |
| substituir | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 |
| iniciar | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 0 |
| Total | 9 | 3 | 6 | 5 | 18 | 3 | 3 | 0 |

### 09_25 — Palliative Care – End of Life Care

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 5 | 1 |
| suspender | 1 | 11 |
| reduzir dose | 1 | 1 |
| substituir | 6 | 0 |
| iniciar | 3 | 3 |
| Total | 16 | 16 |

| Tipo de ação | Correto Rem | Aceitável Rem | Debatível Rem | Incorreto Rem | Correto C | Aceitável C | Debatível C | Incorreto C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| manter | 1 | 0 | 1 | 3 | 1 | 0 | 0 | 0 |
| suspender | 1 | 0 | 0 | 0 | 10 | 1 | 0 | 0 |
| reduzir dose | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 |
| substituir | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| iniciar | 2 | 1 | 0 | 0 | 3 | 0 | 0 | 0 |
| Total | 7 | 4 | 1 | 4 | 15 | 1 | 0 | 0 |

### 09_26 — Drug dependency and requests for medication out of hours

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 0 | 4 |
| suspender | 3 | 3 |
| reduzir dose | 0 | 1 |
| aumentar dose | 1 | 0 |
| substituir | 4 | 0 |
| iniciar | 0 | 1 |
| Total | 8 | 9 |

| Tipo de ação | Correto Rem | Aceitável Rem | Debatível Rem | Incorreto Rem | Correto C | Aceitável C | Debatível C | Incorreto C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| manter | 0 | 0 | 0 | 0 | 1 | 1 | 2 | 0 |
| suspender | 3 | 0 | 0 | 0 | 3 | 0 | 0 | 0 |
| reduzir dose | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| aumentar dose | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| substituir | 1 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| iniciar | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| Total | 4 | 4 | 0 | 0 | 5 | 1 | 3 | 0 |

## Por tipo de sugestão

A classe `other` só aparece no baseline: a frase não é manter, suspender, ajustar dose, trocar nem iniciar. Linhas sem nota, se houver, entram na coluna da classe e ficam fora da porcentagem.

| Tipo | N Rem | Amplo Rem | Estrito Rem | Erro Rem | N C | Amplo C | Estrito C | Erro C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| manter | 92 | 60.9 | 35.9 | 22.8 | 113 | 67.3 | 37.2 | 13.3 |
| suspender | 65 | 86.2 | 86.2 | 10.8 | 110 | 99.1 | 94.5 | 0.0 |
| reduzir dose | 23 | 60.9 | 56.5 | 26.1 | 37 | 86.5 | 64.9 | 2.7 |
| aumentar dose | 13 | 30.8 | 23.1 | 46.2 | 6 | 83.3 | 83.3 | 0.0 |
| substituir | 75 | 64.0 | 45.3 | 14.7 | 5 | 100.0 | 100.0 | 0.0 |
| iniciar | 37 | 62.2 | 45.9 | 10.8 | 35 | 94.3 | 65.7 | 0.0 |

Contagem completa de cada tipo:

| Algoritmo | Tipo | N | C | A | D | I | Amplo | Estrito | Erro | Debatable % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RemedIA | manter | 92 | 33 | 23 | 15 | 21 | 60.9 | 35.9 | 22.8 | 16.3 |
| RemedIA | suspender | 65 | 56 | 0 | 2 | 7 | 86.2 | 86.2 | 10.8 | 3.1 |
| RemedIA | reduzir dose | 23 | 13 | 1 | 3 | 6 | 60.9 | 56.5 | 26.1 | 13.0 |
| RemedIA | aumentar dose | 13 | 3 | 1 | 3 | 6 | 30.8 | 23.1 | 46.2 | 23.1 |
| RemedIA | substituir | 75 | 34 | 14 | 16 | 11 | 64.0 | 45.3 | 14.7 | 21.3 |
| RemedIA | iniciar | 37 | 17 | 6 | 10 | 4 | 62.2 | 45.9 | 10.8 | 27.0 |
| Baseline | manter | 113 | 42 | 34 | 22 | 15 | 67.3 | 37.2 | 13.3 | 19.5 |
| Baseline | suspender | 110 | 104 | 5 | 1 | 0 | 99.1 | 94.5 | 0.0 | 0.9 |
| Baseline | reduzir dose | 37 | 24 | 8 | 4 | 1 | 86.5 | 64.9 | 2.7 | 10.8 |
| Baseline | aumentar dose | 6 | 5 | 0 | 1 | 0 | 83.3 | 83.3 | 0.0 | 16.7 |
| Baseline | substituir | 5 | 5 | 0 | 0 | 0 | 100.0 | 100.0 | 0.0 | 0.0 |
| Baseline | iniciar | 35 | 23 | 10 | 2 | 0 | 94.3 | 65.7 | 0.0 | 5.7 |

## Criatividade

Criatividade aqui é a parcela de sugestões que propõem outro fármaco, não um juízo estético. Uma troca ou um início podem ser clinicamente certos. A pergunta é quantas linhas fazem isso e como o especialista as notou, ao lado das linhas conservadoras.

| Recorte | Algoritmo | N | % das avaliadas | Acerto amplo % | Acerto estrito % | Erro % | Debatable % |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Criativas (add + replace) | RemedIA | 112 | 36.7 | 63.4 | 45.5 | 13.4 | 23.2 |
| Criativas (add + replace) | Baseline | 40 | 13.1 | 95.0 | 70.0 | 0.0 | 5.0 |
| Conservadoras | RemedIA | 193 | 63.3 | 67.4 | 54.4 | 20.7 | 11.9 |
| Conservadoras | Baseline | 266 | 86.9 | 83.5 | 65.8 | 6.0 | 10.5 |

O mesmo recorte, separado em iniciar e substituir:

| Tipo | Algoritmo | N | % das avaliadas | Amplo | Estrito | Erro | Debatable % |
| --- | --- | --- | --- | --- | --- | --- | --- |
| iniciar | RemedIA | 37 | 12.1 | 62.2 | 45.9 | 10.8 | 27.0 |
| iniciar | Baseline | 35 | 11.4 | 94.3 | 65.7 | 0.0 | 5.7 |
| substituir | RemedIA | 75 | 24.6 | 64.0 | 45.3 | 14.7 | 21.3 |
| substituir | Baseline | 5 | 1.6 | 100.0 | 100.0 | 0.0 | 0.0 |

O RemedIA propõe outro fármaco com mais frequência: 112 de 305 linhas avaliadas (36.7%), contra 40 de 306 (13.1%) no baseline. Nas criativas, o acerto amplo é 63.4% no RemedIA e 95.0% no baseline, e o erro é 13.4% e 0.0%. Nas conservadoras, o acerto amplo é 67.4% e 83.5%. No RemedIA, criar custa acerto (as criativas ficam abaixo das conservadoras). No baseline, as poucas linhas criativas foram quase todas aceitas; o que puxa a taxa conservadora para baixo são os keeps.

O baseline quase não usa a classe substituir (5 linhas, 5 Correct). O fármaco novo aparece como início, na linha daquele alvo: 35 inícios, acerto amplo 94.3%, erro 0.0%. O RemedIA troca muito mais (75 substituições, acerto amplo 64.0%, erro 14.7%, Debatable 21.3%) e inicia em volume parecido (37 inícios, acerto amplo 62.2%, erro 10.8%). Nas observações, o padrão que se repete na troca é este: a suspensão estava certa e o fármaco posto no lugar não estava.

Nas classes conservadoras a distância também é grande, e não só nos keeps. Suspender tem acerto amplo 86.2% no RemedIA (erro 10.8%) e 99.1% no baseline (erro 0.0%). Aumentar a dose é a classe com mais erro no RemedIA: 46.2% em 13 linhas. Sete observações dizem a mesma coisa sobre pares de apresentações do mesmo fármaco: não eram duplicatas, a dose era a soma das duas, e o modelo suspendeu uma e aumentou a outra.

Há 7 linhas do baseline classificadas como suspensão ou redução que, na mesma frase, citam outro produto ou outra via. Elas não entram na contagem criativa acima:

- `scot_09_04` #6 (Debatable, suspender): Withhold or discontinue metformin temporarily while acute nausea resolves; if glycemic management remains necessary, consider switching to a well-tolerated once-daily agent with minimal GI burden and low hypoglycemia risk (e.g., linagliptin 5mg daily).
- `scot_09_06` #14 (Debatable, reduzir dose): Reduce dose to 5mg daily (or consider switching to an alternative agent if ankle edema persists post-discontinuation of pioglitazone and diclofenac).
- `scot_09_06` #18 (Correct, reduzir dose): Reduce dose to 20mg daily or switch to famotidine 20mg twice daily to minimize interaction with citalopram.
- `scot_09_13` #3 (Correct, reduzir dose): Reduce dose to one tablet four times daily with a view to tapering down further or switching to regular Paracetamol 500mg tablets/soluble tablets (two tablets QDS) to reduce sedation, constipation, and fall risk.
- `scot_09_25` #2 (Correct, suspender): Discontinue and switch to subcutaneous morphine 2.5mg to 5mg every 2 to 4 hours as required for breakthrough pain and breathlessness.
- `scot_09_25` #11 (Correct, suspender): Discontinue oral tablets and switch to metoclopramide 10mg subcutaneously every 8 hours as required (or 30mg/24 hours via continuous subcutaneous infusion).
- `scot_09_26` #4 (Correct, suspender): Review and formulate a reduction plan to taper off the codeine component, transitioning to plain paracetamol for baseline analgesia.

## Notas de DTP no RemedIA

O baseline não tem coluna de DTP. No RemedIA, `DTP Evaluation` e `Rec Evaluation` coincidem em 301 de 305 linhas em que as duas estão preenchidas. A tabela abaixo é a nota do DTP, não a da recomendação.

| Tipo | N | C | A | D | I | Amplo | Estrito | Erro |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| todas | 305 | 155 | 45 | 49 | 56 | 65.6 | 50.8 | 18.4 |
| manter | 92 | 33 | 23 | 14 | 22 | 60.9 | 35.9 | 23.9 |
| suspender | 65 | 56 | 0 | 2 | 7 | 86.2 | 86.2 | 10.8 |
| reduzir dose | 23 | 13 | 1 | 3 | 6 | 60.9 | 56.5 | 26.1 |
| aumentar dose | 13 | 3 | 1 | 3 | 6 | 30.8 | 23.1 | 46.2 |
| substituir | 75 | 33 | 14 | 17 | 11 | 62.7 | 44.0 | 14.7 |
| iniciar | 37 | 17 | 6 | 10 | 4 | 62.2 | 45.9 | 10.8 |

A nota da recomendação por flag de problema, no RemedIA. As 92 linhas `keep` não trazem flag.

| Flag | N | C | A | D | I | Amplo | Erro |
| --- | --- | --- | --- | --- | --- | --- | --- |
| (keep, sem flag) | 92 | 33 | 23 | 15 | 21 | 60.9 | 22.8 |
| no_valid_indication | 49 | 47 | 0 | 1 | 1 | 95.9 | 2.0 |
| dose_too_high | 23 | 13 | 1 | 3 | 6 | 60.9 | 26.1 |
| safer_drug_required | 21 | 10 | 3 | 5 | 3 | 61.9 | 14.3 |
| interaction_undesirable_reaction | 20 | 8 | 4 | 5 | 3 | 60.0 | 15.0 |
| needs_adjunct_escalation_add | 20 | 7 | 4 | 6 | 3 | 55.0 | 15.0 |
| needs_distinct_role_adjunct_add | 15 | 8 | 2 | 4 | 1 | 66.7 | 6.7 |
| duplicate_same_ingredient_orders | 8 | 1 | 0 | 1 | 6 | 12.5 | 75.0 |
| inappropriate_dosage_form | 8 | 4 | 4 | 0 | 0 | 100.0 | 0.0 |
| condition_refractory | 7 | 3 | 2 | 2 | 0 | 71.4 | 0.0 |
| dose_too_low | 7 | 3 | 1 | 1 | 2 | 57.1 | 28.6 |
| interaction_reduces_active_drug | 6 | 0 | 0 | 2 | 4 | 0.0 | 66.7 |
| non_dose_related_undesirable_reaction | 6 | 4 | 0 | 0 | 2 | 66.7 | 33.3 |
| not_most_effective_for_indication | 6 | 2 | 1 | 1 | 2 | 50.0 | 33.3 |
| not_effective_for_problem | 4 | 3 | 0 | 0 | 1 | 75.0 | 25.0 |
| redundant_distinct_agent | 4 | 4 | 0 | 0 | 0 | 100.0 | 0.0 |
| contraindicated_risk_factors | 3 | 0 | 0 | 3 | 0 | 0.0 | 0.0 |
| temporary_safety_discontinue | 3 | 3 | 0 | 0 | 0 | 100.0 | 0.0 |
| condition_requires_initiation | 1 | 1 | 0 | 0 | 0 | 100.0 | 0.0 |
| preventive_therapy_required | 1 | 1 | 0 | 0 | 0 | 100.0 | 0.0 |
| treating_avoidable_adr_from_other_med | 1 | 1 | 0 | 0 | 0 | 100.0 | 0.0 |

## Lacunas que o especialista escreveu

A tabela de lacunas julga o que a revisão não fez. Ela não entra nas taxas acima. Poucas linhas foram preenchidas.

### RemedIA

- `scot_09_01` lacuna 1: Tramadol — Descontinuado, deveria ter sido acrescentado algum analgésico fixo.
- `scot_09_01` lacuna 2: Melatonina — a adição é controvérsia
- `scot_09_02` lacuna 1: Clopidogrel - PRM1 — suspensão
- `scot_09_02` lacuna 2: Levotiroxina — precisa de exame para saber se essa dose já não está muito alta. A dose inicial deve ser 1.6 mcg/kg.
- `scot_09_19` lacuna 1: PRM 2 — Deveria ser iniciado tratamento para HAS

### Baseline

- `scot_09_12` lacuna 1: Falta medicamentos para adição de novos medicamentos. — (em branco)

## Onde estão os arquivos

| Arquivo | Conteúdo |
| --- | --- |
| `avaliacao_especialista_remedia.xlsx` | Ficha devolvida do RemedIA, 26 abas |
| `avaliacao_especialista_baseline.xlsx` | Ficha devolvida do baseline, 26 abas |
| `rows_remedia.csv`, `rows_baseline.csv` | Uma linha por recomendação, com a classe e a nota |
| `gaps.csv` | Lacunas preenchidas |
| `tables/overall.csv` | Taxas gerais, com e sem keep, criativas e conservadoras |
| `tables/volume_by_type.csv` | Número de recomendações de cada tipo, com o total na última linha |
| `tables/precision_by_type.csv` | Número de Correto, Aceitável, Debatível e Incorreto por tipo, com o total na última linha |
| `tables/volume_by_case.csv` | O mesmo número de cada tipo, um bloco por caso |
| `tables/precision_by_case.csv` | As quatro notas por tipo, um bloco por caso |
| `tables/repeated_recommendations.csv` | Respostas repetidas, com o comentário de cada uma |
| `relatorio_por_caso.md` | Cada caso contra o baseline: ações, keeps, duplicações, criatividade, acurácia e detalhe das explicações, com o review geral no fim |
| `tables/creativity_by_case.csv` | Ações propositivas por keep, em cada caso |
| `tables/accuracy_by_case.csv` | As quatro notas e as quatro taxas, em cada caso |
| `tables/duplications_by_case.csv` | Respostas repetidas por caso |
| `tables/explanation_pairs.csv` | Ações iguais no mesmo fármaco e o veredito do detalhe |
| `tables/case_winners.csv` | Casos em que cada algoritmo foi melhor, por eixo |
| `tables/by_type.csv` | Taxas por tipo de sugestão |
| `tables/by_case.csv` | Taxas por caso, com keep, sem keep e nas criativas |
| `tables/dtp_by_type.csv`, `tables/rec_by_flag.csv` | Nota de DTP e nota da recomendação por flag, só RemedIA |

Para refazer as tabelas a partir das fichas: `cd Pharmacotherapy_agentic_v4 && PYTHONPATH=. python3 tests/score_specialist_remedia_baseline.py`.

