# RemedIA e o baseline, caso a caso

O baseline é o prompt por medicamento de Ong et al. RemedIA é o pipeline em etapas. As duas fichas cobrem os mesmos 26 casos. Cada linha da ficha entra na contagem, com ou sem nota, inclusive keeps e respostas repetidas.

Uma ação propositiva é toda linha que não é keep: suspender, mudar a dose, substituir, iniciar ou outra. A criatividade é o número de ações propositivas por keep. Mais propositivas por keep é melhor. A acurácia é a taxa de Correto, Aceitável, Debatível e Incorreto nas linhas com nota. O detalhe compara a explicação das ações que os dois fizeram no mesmo fármaco, fora dos keeps: quem identificou o problema, quem explicou a ação e se isso é específico deste paciente. Uma explicação longa que erra o problema perde no detalhe.

Os keeps ficam de fora da comparação de explicações. No RemedIA a coluna de explicação desses 92 keeps está vazia. No baseline a frase é quase sempre a genérica de manter o medicamento.

## 09_01 — Frailty without overt multimorbidity

### Ações

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 1 | 2 |
| suspender | 4 | 4 |
| reduzir dose | 0 | 2 |
| aumentar dose | 0 | 0 |
| substituir | 3 | 0 |
| iniciar | 1 | 3 |
| outra | 0 | 0 |
| Total | 9 | 11 |

### Keeps e criatividade

| Algoritmo | Propositivas | Keeps | Propositivas por keep | Parcela propositiva % |
| --- | --- | --- | --- | --- |
| RemedIA | 8 | 1 | 8.0 | 88.9 |
| Baseline | 9 | 2 | 4.5 | 81.8 |

### Acurácia

| Algoritmo | N | Sem nota | Correto | Aceitável | Debatível | Incorreto | Correto % | Aceitável % | Debatível % | Incorreto % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RemedIA | 9 | 0 | 8 | 0 | 1 | 0 | 88.9 | 0.0 | 11.1 | 0.0 |
| Baseline | 11 | 0 | 6 | 1 | 2 | 2 | 54.5 | 9.1 | 18.2 | 18.2 |

### Duplicações

| Algoritmo | Duplicações |
| --- | --- |
| RemedIA | 0 |
| Baseline | 0 |

O RemedIA fez 8 ações propositivas e 1 keeps (8.0 por keep). o baseline fez 9 e 2 (4.5 por keep). no RemedIA, Correto 8, Aceitável 0, Debatável 1, Incorreto 0 (acerto amplo 88.9%, erro 0.0%). no baseline, Correto 6, Aceitável 1, Debatável 2, Incorreto 2 (acerto amplo 63.6%, erro 18.2%). nas 3 explicações da mesma ação, o detalhe ficou com o RemedIA em 1, com o baseline em 1 e empatou em 1.

### Explicações da mesma ação

**cetirizine, suspender.** Detalhe: RemedIA. Os dois suspendem pelo efeito anticolinérgico e sedativo. O RemedIA amarra a falta de indicação alérgica ao MMSE 14, às quedas e à interação com amisulprida, tramadol e trazodona.

- RemedIA, linha 2 (Correct): Cetirizine 10mg daily has no documented clinical indication or active allergic condition. In this severely frail resident with dementia (MMSE 14) and frequent falls, cetirizine adds unnecessary anticholinergic and sedative burdens, interacting with amisulpride, tramadol, and trazodone to worsen CNS depression and fall risk. Discontinuing cetirizine eliminates unneeded medication and reduces sedation without compromising care.
- Baseline, linha 7 (Correct): Discontinue unless there is an active, documented allergic indication, to reduce anticholinergic and sedative burden.

**fucibet, suspender.** Detalhe: Baseline. Os dois veem corticosteroide e antibiótico sem benefício. O baseline explica a ação: curso máximo de duas semanas, ou troca por emoliente. O RemedIA só manda suspender.

- RemedIA, linha 4 (Correct): Fucibet Cream is charted without an active dermatological diagnosis, clinical indication, or evidence of ongoing skin infection/dermatitis. Continued use of topical corticosteroids and antibiotics without indication exposes the patient to adverse effects, including skin thinning and antibiotic resistance, with no therapeutic benefit. Discontinuing fucibet_cream_apply_twice_ resolves this drug therapy problem.
- Baseline, linha 8 (Correct): Discontinue or limit to a short defined course (typically max 2 weeks) to avoid steroid-induced skin atrophy and antimicrobial resistance; switch to emollient maintenance.

**tramadol, suspender.** Detalhe: Empate. O RemedIA identifica que a fratura é de dois anos atrás e cita convulsão e serotonina. O baseline explica o que fazer com o opioide: retirar aos poucos e reavaliar a dor.

- RemedIA, linha 5 (Correct): Tramadol was started for a fractured neck of femur sustained two years ago, but there is no documented active fracture pain or valid clinical indication for ongoing scheduled opioid therapy. Continued use contributes to severe risks including worsening cognitive impairment (MMSE 14), frequent falls, and CNS depression, alongside drug interactions with amisulpride and trazodone (increased seizure and serotonin syndrome risks). Discontinuation is indicated to prevent adverse events.
- Baseline, linha 3 (Correct): Gradually taper and discontinue, assessing for ongoing pain, to reduce sedation, confusion, and fall risk.

### Mesmo fármaco, ação diferente

| Fármaco | RemedIA | Baseline |
| --- | --- | --- |
| amisulpride | substituir | reduzir dose |
| bendroflumethiazide | substituir | suspender |
| diprobase | suspender | manter |
| trazodone | substituir | reduzir dose |

## 09_02 — Frailty with multimorbidity

### Ações

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 3 | 5 |
| suspender | 2 | 9 |
| reduzir dose | 5 | 3 |
| aumentar dose | 2 | 0 |
| substituir | 5 | 0 |
| iniciar | 0 | 0 |
| outra | 0 | 0 |
| Total | 17 | 17 |

### Keeps e criatividade

| Algoritmo | Propositivas | Keeps | Propositivas por keep | Parcela propositiva % |
| --- | --- | --- | --- | --- |
| RemedIA | 14 | 3 | 4.7 | 82.4 |
| Baseline | 12 | 5 | 2.4 | 70.6 |

### Acurácia

| Algoritmo | N | Sem nota | Correto | Aceitável | Debatível | Incorreto | Correto % | Aceitável % | Debatível % | Incorreto % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RemedIA | 17 | 0 | 8 | 1 | 2 | 6 | 47.1 | 5.9 | 11.8 | 35.3 |
| Baseline | 17 | 0 | 14 | 1 | 0 | 2 | 82.4 | 5.9 | 0.0 | 11.8 |

### Duplicações

| Algoritmo | Duplicações |
| --- | --- |
| RemedIA | 0 |
| Baseline | 0 |

O RemedIA fez 14 ações propositivas e 3 keeps (4.7 por keep). o baseline fez 12 e 5 (2.4 por keep). no RemedIA, Correto 8, Aceitável 1, Debatável 2, Incorreto 6 (acerto amplo 52.9%, erro 35.3%). no baseline, Correto 14, Aceitável 1, Debatável 0, Incorreto 2 (acerto amplo 88.2%, erro 11.8%). nas 3 explicações da mesma ação, o detalhe ficou com o RemedIA em 1, com o baseline em 0 e empatou em 2.

### Explicações da mesma ação

**edoxaban, reduzir dose.** Detalhe: Empate. Os dois justificam 30 mg pelo peso até 60 kg e pelo clearance entre 15 e 50. O acréscimo do clopidogrel no RemedIA não muda o problema nem a dose.

- RemedIA, linha 14 (Incorrect): Edoxaban 60 mg once daily is excessively high for stroke prevention in nonvalvular atrial fibrillation given the patient's severe renal impairment (CrCl 20 mL/min) and low body weight (43 kg). Product labeling mandates dose reduction to 30 mg once daily for CrCl 15–50 mL/min or weight ≤ 60 kg to prevent excessive drug accumulation and mitigate major bleeding risks, while maintaining effective thromboembolic prophylaxis. Concomitant clopidogrel further magnifies bleeding vulnerability in this frail patient.
- Baseline, linha 6 (Correct): Reduce dose to Edoxaban 30mg tablets, one tablet daily, due to body weight ≤60 kg and CrCl 15–50 mL/min.

**perindopril, reduzir dose.** Detalhe: RemedIA. Os dois baixam para 2 mg pela função renal. O RemedIA liga a dose à pressão em pé de 84/40 e às quedas, que é o problema deste paciente.

- RemedIA, linha 17 (Correct): Perindopril 4mg daily exceeds safe renal dosing thresholds in severe renal impairment (CrCl 20 mL/min) and contributes directly to symptomatic orthostatic hypotension (standing BP 84/40 mmHg) and fall risk. Reducing the dose to 2mg once daily aligns with renal dosing guidance, mitigating hypotension and recurrent fall risks while sustaining blood pressure control and cardiovascular/cerebrovascular protection across her documented indications.
- Baseline, linha 15 (Correct): Reduce dose to Perindopril 2mg tablets once daily (or temporarily withhold) and monitor sitting/standing blood pressure and renal function.

**zopiclone, suspender.** Detalhe: Empate. O RemedIA aponta a ausência de indicação de insônia na demência e nas quedas. O baseline explica a retirada: desmame, pelo risco de sedação, delirium e queda noturna.

- RemedIA, linha 5 (Correct): Zopiclone 7.5mg is prescribed without a documented medical indication such as insomnia or sleep disturbance. In this severely frail 87-year-old patient with vascular dementia and a history of falls, zopiclone significantly increases the risks of worsening cognitive impairment, excessive sedation, and recurrent falls. Discontinuation is required to resolve this unnecessary and hazardous drug therapy.
- Baseline, linha 17 (Correct): Taper and discontinue the medication to reduce sedation, delirium, and nocturnal fall risk.

### Mesmo fármaco, ação diferente

| Fármaco | RemedIA | Baseline |
| --- | --- | --- |
| alendronic | substituir | suspender |
| atorvastatin | manter | reduzir dose |
| clopidogrel | manter | suspender |
| digoxin | reduzir dose | suspender |
| gliclazide | substituir | suspender |
| indapamide | substituir | suspender |
| levothyroxine | aumentar dose | manter, suspender |
| metformin | reduzir dose | suspender |
| mirtazapine | suspender | manter |
| omeprazole | substituir | manter |
| paracetamol | reduzir dose | manter |
| tolterodine | substituir | suspender |

## 09_03 — Care home resident with multimorbidity

### Ações

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 5 | 4 |
| suspender | 4 | 5 |
| reduzir dose | 2 | 3 |
| aumentar dose | 0 | 0 |
| substituir | 2 | 0 |
| iniciar | 1 | 1 |
| outra | 0 | 0 |
| Total | 14 | 13 |

### Keeps e criatividade

| Algoritmo | Propositivas | Keeps | Propositivas por keep | Parcela propositiva % |
| --- | --- | --- | --- | --- |
| RemedIA | 9 | 5 | 1.8 | 64.3 |
| Baseline | 9 | 4 | 2.2 | 69.2 |

### Acurácia

| Algoritmo | N | Sem nota | Correto | Aceitável | Debatível | Incorreto | Correto % | Aceitável % | Debatível % | Incorreto % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RemedIA | 14 | 0 | 7 | 1 | 4 | 2 | 50.0 | 7.1 | 28.6 | 14.3 |
| Baseline | 13 | 0 | 7 | 3 | 3 | 0 | 53.8 | 23.1 | 23.1 | 0.0 |

### Duplicações

| Algoritmo | Duplicações |
| --- | --- |
| RemedIA | 0 |
| Baseline | 0 |

O RemedIA fez 9 ações propositivas e 5 keeps (1.8 por keep). o baseline fez 9 e 4 (2.2 por keep). no RemedIA, Correto 7, Aceitável 1, Debatável 4, Incorreto 2 (acerto amplo 57.1%, erro 14.3%). no baseline, Correto 7, Aceitável 3, Debatável 3, Incorreto 0 (acerto amplo 76.9%, erro 0.0%). nas 5 explicações da mesma ação, o detalhe ficou com o RemedIA em 1, com o baseline em 1 e empatou em 3.

### Explicações da mesma ação

**amlodipine, reduzir dose.** Detalhe: RemedIA. Os dois reduzem para 5 mg pelo risco de queda. O RemedIA mostra a pressão 110/60, a fratura de fêmur e o lisinopril junto, que explicam por que 10 mg está alto.

- RemedIA, linha 13 (Correct): In this 82-year-old severely frail patient (CFS 7, BMI 17 kg/m2) with a history of falls and fractured neck of femur, amlodipine 10mg daily combined with lisinopril 20mg has resulted in overtight blood pressure control (BP 110/60 mmHg). High-dose amlodipine increases risks of orthostatic hypotension and further fall-related trauma. Reducing amlodipine to 5mg once daily de-escalates antihypertensive intensity while maintaining essential cardiovascular prophylaxis and blood pressure control at a safer target.
- Baseline, linha 3 (Correct): Reduce amlodipine dose to 5mg once daily to prevent over-treatment of blood pressure and reduce fall risk.

**folic, suspender.** Detalhe: Empate. Os dois suspendem ácido fólico sem deficiência documentada. O RemedIA lista o que foi procurado; o baseline condiciona a suspensão ao hemograma e ao folato.

- RemedIA, linha 6 (Correct): Patient is prescribed high-dose folic acid 5mg daily without any documented clinical indication, history of folate deficiency, macrocytic anaemia, or treatment with a folate antagonist (e.g. methotrexate). Discontinuing unnecessary folic acid resolves the drug therapy problem and safely reduces medication burden in this severely frail older adult.
- Baseline, linha 7 (Correct): Discontinue folic acid if recent full blood count and serum folate levels are within normal limits.

**gabapentin, suspender.** Detalhe: Empate. Os dois citam dose alta para o clearance de 39, ausência de dor e risco de queda. O baseline acrescenta o desmame; o RemedIA, a dose de 2700 mg e os outros depressores.

- RemedIA, linha 7 (Correct): Gabapentin (gabapentin_300mg) lacks an active documented medical indication (such as epilepsy or active neuropathic pain). In this severely frail 82-year-old patient with renal impairment (CrCl 39 mL/min), dementia, and fall history, high-dose gabapentin (2700mg/day) combined with lorazepam and sertraline carries excessive CNS depression, sedation, and fall risks. Discontinuation is indicated.
- Baseline, linha 4 (Correct): Taper and discontinue gabapentin, as the patient reports no current pain, the current dose is excessively high for his renal function (CrCl 39 mL/min), and it carries a high risk of sedation and falls.

**lisinopril, suspender.** Detalhe: Baseline. Os dois chamam as duas apresentações de duplicata, e essa leitura está errada: são doses que se somam. O baseline ainda explica juntar tudo em 10 mg uma vez ao dia, ou suspender se a pressão cair. O RemedIA só retira o comprimido de 10 mg e deixa o de 20 mg.

- RemedIA, linha 8 (Incorrect): Lisinopril 10mg is a duplicate same-ingredient MAR order co-existing with lisinopril 20mg daily for hypertension and cardiovascular prophylaxis. Given the patient's severe frailty (Rockwood 7), low blood pressure (110/60 mmHg), and history of falls, dual active orders risk inadvertent cumulative dosing, severe hypotension, acute kidney injury, and recurrent falls. Discontinuing the redundant lisinopril 10mg order resolves this duplicate therapy while preserving antihypertensive and prophylactic coverage under the remaining single regimen line.
- Baseline, linha 2 (Correct): Consolidate the duplicate orders (10mg and 20mg) and reduce dose to 10mg once daily (or discontinue if hypotension persists).

**lorazepam, suspender.** Detalhe: Empate. Os dois suspendem pelo risco de sedação, piora cognitiva e queda. O RemedIA marca a falta de indicação; o baseline marca o desmame.

- RemedIA, linha 9 (Correct): Lorazepam 500mcg nocte has no documented medical indication and significantly increases the risk of falls, worsening cognitive impairment, sedation, and additive CNS depression with sertraline in this severely frail elderly patient with dementia and a prior fractured neck of femur. Discontinuing lorazepam resolves this unnecessary drug therapy problem and mitigates fall and delirium risks.
- Baseline, linha 5 (Correct): Gradually taper and discontinue lorazepam to reduce sedation, cognitive worsening, and fall risk.

### Mesmo fármaco, ação diferente

| Fármaco | RemedIA | Baseline |
| --- | --- | --- |
| aspirin | substituir | manter |
| atorvastatin | manter | reduzir dose |
| gliclazide | substituir | suspender |
| lisinopril | suspender, reduzir dose | suspender |
| paracetamol | manter | reduzir dose |

## 09_04 — Care home resident with multimorbidity including dementia

### Ações

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 3 | 4 |
| suspender | 6 | 6 |
| reduzir dose | 0 | 0 |
| aumentar dose | 0 | 0 |
| substituir | 2 | 1 |
| iniciar | 2 | 1 |
| outra | 0 | 0 |
| Total | 13 | 12 |

### Keeps e criatividade

| Algoritmo | Propositivas | Keeps | Propositivas por keep | Parcela propositiva % |
| --- | --- | --- | --- | --- |
| RemedIA | 10 | 3 | 3.3 | 76.9 |
| Baseline | 8 | 4 | 2.0 | 66.7 |

### Acurácia

| Algoritmo | N | Sem nota | Correto | Aceitável | Debatível | Incorreto | Correto % | Aceitável % | Debatível % | Incorreto % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RemedIA | 13 | 0 | 10 | 1 | 1 | 1 | 76.9 | 7.7 | 7.7 | 7.7 |
| Baseline | 12 | 0 | 6 | 2 | 1 | 3 | 50.0 | 16.7 | 8.3 | 25.0 |

### Duplicações

| Algoritmo | Duplicações |
| --- | --- |
| RemedIA | 0 |
| Baseline | 0 |

O RemedIA fez 10 ações propositivas e 3 keeps (3.3 por keep). o baseline fez 8 e 4 (2.0 por keep). no RemedIA, Correto 10, Aceitável 1, Debatável 1, Incorreto 1 (acerto amplo 84.6%, erro 7.7%). no baseline, Correto 6, Aceitável 2, Debatável 1, Incorreto 3 (acerto amplo 66.7%, erro 25.0%). nas 4 explicações da mesma ação, o detalhe ficou com o RemedIA em 0, com o baseline em 0 e empatou em 4.

### Explicações da mesma ação

**furosemide, suspender.** Detalhe: Empate. Os dois identificam a ordem extra de furosemida e o risco de desidratação e eletrólitos. O RemedIA cita a ureia; o baseline nomeia a ordem se necessário.

- RemedIA, linha 4 (Correct): Discontinue furosemide_40mg_alpha to resolve duplicate same-ingredient orders of furosemide across scheduled and PRN regimens for peripheral oedema, reducing the risk of excessive diuresis, pre-renal azotemia (urea 22.0 mmol/L), and electrolyte loss.
- Baseline, linha 8 (Correct): Discontinue the PRN furosemide order to prevent dehydration, electrolyte derangements, and dosing ambiguity.

**lorazepam, suspender.** Detalhe: Empate. Os dois retiram o benzodiazepínico regular e o se necessário por queda e sedação. O baseline acrescenta a redução gradual e a medida não farmacológica para a agitação.

- RemedIA, linha 6 (Correct): Lorazepam 500 micrograms (lorazepam_500) has no valid medical indication or documented behavioral assessment justifying ongoing benzodiazepine therapy. In this severely frail 78-year-old resident with mixed dementia, high fall risk, and concurrent tramadol use, lorazepam poses an unacceptable risk of additive CNS depression, cognitive worsening, and recurrent injurious falls. Discontinuation is required to resolve this DTP.
- Baseline, linha 5 (Correct): Plan a gradual dose reduction and discontinuation of regular and PRN lorazepam to minimize fall risk, sedation, and cognitive worsening, utilizing non-pharmacological approaches for agitation.

**metoclopramide, suspender.** Detalhe: Empate. Os dois citam o limite de cinco dias e o efeito extrapiramidal. O RemedIA acrescenta que já se passaram duas semanas e a interação com tramadol.

- RemedIA, linha 8 (Correct): Metoclopramide was initiated two weeks ago for acute nausea and has been taken regularly. Regulatory guidelines recommend a maximum treatment duration of 5 days to reduce the risk of potentially irreversible neurological adverse effects like extrapyramidal symptoms and tardive dyskinesia. In this 78-year-old frail resident with dementia, continuing regular metoclopramide lacks an ongoing valid indication, particularly given the elevated fall and adverse interaction risks with concurrent tramadol. Discontinuation is required to ensure patient safety.
- Baseline, linha 1 (Correct): Discontinue metoclopramide due to the risk of extrapyramidal side effects and exceeding the recommended 5-day duration of therapy.

**omeprazole, suspender.** Detalhe: Empate. Os dois suspendem inibidor de bomba sem úlcera ou sangramento documentado. O baseline liga a náusea à carga de comprimidos; o RemedIA, ao risco de fratura.

- RemedIA, linha 9 (Correct): Omeprazole was initiated without an identifiable clinical indication such as acid-peptic disease or high-risk gastroprotection. In a 78-year-old frail resident with a history of an injurious fall and fractured humerus, unnecessary PPI exposure presents unjustified risks of recurrent fracture and falls. Deprescribing omeprazole eliminates these risks without compromising therapy.
- Baseline, linha 9 (Correct): Discontinue omeprazole if there is no confirmed history of peptic ulcer disease or upper GI bleed, as nausea was related to tablet burden and formulation intolerance.

### Mesmo fármaco, ação diferente

| Fármaco | RemedIA | Baseline |
| --- | --- | --- |
| laxido | suspender | manter |
| metformin | substituir | suspender |
| paracetamol | manter | substituir |
| senna | suspender | manter |
| tramadol | substituir | suspender |

## 09_05 — Younger adult with intellectual disability in a care home

### Ações

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 1 | 2 |
| suspender | 1 | 2 |
| reduzir dose | 1 | 4 |
| aumentar dose | 1 | 0 |
| substituir | 4 | 0 |
| iniciar | 0 | 0 |
| outra | 0 | 0 |
| Total | 8 | 8 |

### Keeps e criatividade

| Algoritmo | Propositivas | Keeps | Propositivas por keep | Parcela propositiva % |
| --- | --- | --- | --- | --- |
| RemedIA | 7 | 1 | 7.0 | 87.5 |
| Baseline | 6 | 2 | 3.0 | 75.0 |

### Acurácia

| Algoritmo | N | Sem nota | Correto | Aceitável | Debatível | Incorreto | Correto % | Aceitável % | Debatível % | Incorreto % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RemedIA | 8 | 0 | 5 | 1 | 1 | 1 | 62.5 | 12.5 | 12.5 | 12.5 |
| Baseline | 8 | 0 | 4 | 3 | 1 | 0 | 50.0 | 37.5 | 12.5 | 0.0 |

### Duplicações

| Algoritmo | Duplicações |
| --- | --- |
| RemedIA | 0 |
| Baseline | 0 |

O RemedIA fez 7 ações propositivas e 1 keeps (7.0 por keep). o baseline fez 6 e 2 (3.0 por keep). no RemedIA, Correto 5, Aceitável 1, Debatável 1, Incorreto 1 (acerto amplo 75.0%, erro 12.5%). no baseline, Correto 4, Aceitável 3, Debatável 1, Incorreto 0 (acerto amplo 87.5%, erro 0.0%). não há ação igual, fora de keep, para comparar a explicação.

### Mesmo fármaco, ação diferente

| Fármaco | RemedIA | Baseline |
| --- | --- | --- |
| lamotrigine | suspender, substituir | reduzir dose |
| metoclopramide | substituir | suspender |
| mirtazapine | aumentar dose | reduzir dose |
| phenytoin | reduzir dose | suspender |
| rufinamide | substituir | manter |
| sodium | substituir | reduzir dose |

## 09_06 — Multimorbidity without frailty (acute pain, depression, COPD and high-risk combinations)

### Ações

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 2 | 6 |
| suspender | 3 | 8 |
| reduzir dose | 2 | 3 |
| aumentar dose | 3 | 1 |
| substituir | 9 | 1 |
| iniciar | 6 | 5 |
| outra | 0 | 0 |
| Total | 25 | 24 |

### Keeps e criatividade

| Algoritmo | Propositivas | Keeps | Propositivas por keep | Parcela propositiva % |
| --- | --- | --- | --- | --- |
| RemedIA | 23 | 2 | 11.5 | 92.0 |
| Baseline | 18 | 6 | 3.0 | 75.0 |

### Acurácia

| Algoritmo | N | Sem nota | Correto | Aceitável | Debatível | Incorreto | Correto % | Aceitável % | Debatível % | Incorreto % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RemedIA | 25 | 0 | 13 | 1 | 3 | 8 | 52.0 | 4.0 | 12.0 | 32.0 |
| Baseline | 24 | 0 | 18 | 1 | 3 | 2 | 75.0 | 4.2 | 12.5 | 8.3 |

### Duplicações

| Algoritmo | Duplicações |
| --- | --- |
| RemedIA | 0 |
| Baseline | 2 |

Resposta repetida, defeito do modelo. A linha continua contada na tabela de ações.

- Baseline. Linhas 10, 11 são o mesmo plano, escrito duas vezes, para o bisoprolol. A linha 10 (Atenolol 50mg tablets) diz: Switch atenolol to bisoprolol 2.5mg orally once daily (titrating according to heart rate and blood pressure) for optimized rate control in AF and post-MI management. A linha 11 (Bisoprolol tablets) diz: Initiate bisoprolol 2.5mg orally once daily to replace atenolol, titrating as tolerated for rate control. O especialista anotou na linha 11: "Recomendação duplicada?".
- Baseline. Linhas 15, 16 repetem a frase "Discontinue liquid presentation.". Alvos: Levothyroxine 50micrograms/5ml liquid; Levothyroxine 25micrograms/5ml liquid. É a mesma resposta copiada em mais de uma linha.

O RemedIA fez 23 ações propositivas e 2 keeps (11.5 por keep). o baseline fez 18 e 6 (3.0 por keep). no RemedIA, Correto 13, Aceitável 1, Debatável 3, Incorreto 8 (acerto amplo 56.0%, erro 32.0%). no baseline, Correto 18, Aceitável 1, Debatável 3, Incorreto 2 (acerto amplo 79.2%, erro 8.3%). nas 10 explicações da mesma ação, o detalhe ficou com o RemedIA em 3, com o baseline em 5 e empatou em 2.

### Explicações da mesma ação

**amlodipine, reduzir dose.** Detalhe: Baseline. Os dois reduzem para 5 mg pelo edema. O baseline explica que o inchaço pode ser do pioglitazona e do diclofenaco, e que a troca só entra se o edema continuar depois de tirá-los. O RemedIA atribui o edema só à dose da anlodipino.

- RemedIA, linha 24 (Incorrect): Amlodipine 10 mg once daily is causing dose-dependent adverse peripheral edema (ankle swelling). Reducing the dose to 5 mg once daily resolves or significantly improves edema while maintaining antihypertensive efficacy and cardioprotective benefits for hypertension and coronary heart disease, especially alongside newly optimized background therapy.
- Baseline, linha 14 (Debatable): Reduce dose to 5mg daily (or consider switching to an alternative agent if ankle edema persists post-discontinuation of pioglitazone and diclofenac).

**apixaban, iniciar.** Detalhe: Empate. Os dois iniciam apixabana 5 mg duas vezes ao dia pelo CHA2DS2-VASc 5 na fibrilação. O RemedIA acrescenta a preferência sobre a varfarina, sem mudar o problema nem a dose.

- RemedIA, linha 7 (Correct): Patient has atrial fibrillation with a CHA2DS2-VASc score of 5 (female, hypertension, diabetes, CHD/vascular disease, eGFR 55 mL/min/1.73m2). Atenolol is prescribed for rate control, but oral anticoagulation is guideline-indicated to reduce stroke risk. Direct oral anticoagulants are preferred over warfarin. Apixaban 5 mg twice daily is recommended to provide stroke prevention alongside existing rate control, with renal function and bleeding parameters monitored.
- Baseline, linha 4 (Correct): Initiate apixaban 5mg orally twice daily for stroke prevention in atrial fibrillation (CHA₂DS₂-VASc = 5).

**atenolol, substituir.** Detalhe: RemedIA. Os dois trocam atenolol por bisoprolol 2,5 mg. O RemedIA explica por que o atenolol é pior aqui: seletividade beta-1, pós-infarto, controle de frequência e DPOC.

- RemedIA, linha 12 (Correct): Atenolol is inferior to evidence-based beta-1 selective agents for secondary prevention post-NSTEMI, rate control in atrial fibrillation, and hypertension, and may exacerbate COPD symptoms. Switching Atenolol to Bisoprolol 2.5 mg once daily provides superior cardioprotective efficacy and rate control with higher beta-1 selectivity, which is safer for her underlying COPD. This replacement covers CHD, AF, hypertension, and cardiovascular prophylaxis while addressing ongoing palpitations.
- Baseline, linha 10 (Correct): Switch atenolol to bisoprolol 2.5mg orally once daily (titrating according to heart rate and blood pressure) for optimized rate control in AF and post-MI management.

**atorvastatin, iniciar.** Detalhe: RemedIA. Os dois iniciam atorvastatina 80 mg na doença coronária. O RemedIA identifica a omissão: infarto sem supra, coronariopatia no cateterismo e diabetes sem estatina.

- RemedIA, linha 6 (Correct): Patient has established coronary heart disease (prior non-STEMI and angiogram confirming widespread CAD) and diabetes, but lacks guideline-directed lipid-lowering therapy. Adding high-intensity statin therapy with atorvastatin provides essential secondary cardiovascular prevention and plaque stabilization, addressing the missing disease-modifying role alongside aspirin and antianginal agents to reduce recurrent ischemic events.
- Baseline, linha 5 (Correct): Initiate atorvastatin 80mg orally once daily at bedtime for secondary prevention of coronary heart disease.

**empagliflozin, iniciar.** Detalhe: RemedIA. Os dois iniciam empagliflozina 10 mg por benefício cárdio-renal. O RemedIA amarra a escolha à HbA1c 86, ao IMC 35, à taxa de filtração 55 e ao risco de hipoglicemia com a gliclazida.

- RemedIA, linha 8 (Correct): Severe glycemic suboptimality (HbA1c 86 mmol/mol) alongside coronary heart disease (prior non-STEMI), obesity (BMI 35 kg/m2), and eGFR 55 ml/min/1.73m2 requires escalation. Empagliflozin provides established cardiovascular and renal protection while improving glycemic control without hypoglycemia risk alongside gliclazide, metformin, and pioglitazone. Initiated at 10 mg once daily, empagliflozin is chosen over alternative GLP-1 receptor agonists (not on the regimen) to directly confer cardio-renal benefits and promote glycemic reduction.
- Baseline, linha 6 (Correct): Initiate empagliflozin 10mg orally once daily to improve glycemic control and provide cardiovascular and renal protection.

**furosemide, suspender.** Detalhe: Empate. Os dois reconhecem a cascata: edema de pioglitazona, anlodipino e anti-inflamatório, com função ventricular normal. A ação e o problema são os mesmos.

- RemedIA, linha 3 (Correct): Furosemide 40mg daily represents a prescribing cascade initiated to manage peripheral edema/ankle swelling induced by high-dose amlodipine (and exacerbated by pioglitazone), rather than guideline-directed hypertension care. Normal LV systolic function confirms absence of heart failure with reduced ejection fraction. Loop diuretics are ineffective as monotherapy for essential hypertension in this setting. Discontinuing furosemide removes unnecessary therapy and mitigates risks of electrolyte imbalance, dehydration, and renal strain.
- Baseline, linha 13 (Correct): Taper and discontinue as ankle swelling is likely medication-induced (pioglitazone, amlodipine, NSAID) and LV function is normal.

**levothyroxine, suspender.** Detalhe: Baseline. O RemedIA trata as duas soluções como duplicata e suspende só a de 50 microgramas, como se a paciente estivesse em excesso de hormônio. As duas doses se somam. O baseline manda suspender a apresentação líquida, sem inventar esse excesso. A frase é curta e está repetida nas duas linhas.

- RemedIA, linha 4 (Incorrect): Patient has duplicate same-ingredient orders of levothyroxine oral liquid (levothyroxine_50 and levothyroxine_25). Discontinuing levothyroxine_50 resolves the duplicate therapy order, reducing complexity and the risk of excess thyroid hormone replacement associated with her palpitations and history of CAD/AF.
- Baseline, linha 15, 16 (Correct, Correct): Discontinue liquid presentation.
- Baseline, linha 16 (Correct): Discontinue liquid presentation.

**lisinopril, suspender.** Detalhe: Baseline. O RemedIA chama o comprimido de 10 mg de ordem redundante e o retira, deixando 20 mg. O baseline manda retirar o de 10 mg e consolidar com o de 20 mg numa formulação única, que é a leitura da dose partida.

- RemedIA, linha 5 (Incorrect): The patient has duplicate active orders for lisinopril (10mg daily and 20mg daily), creating unintended duplicate same-ingredient therapy and an associated risk of dosing error or adverse effects. Discontinuing the lower-strength redundant order lisinopril_10mg resolves the duplicate therapy problem while preserving blood pressure control, coronary heart disease management, and cardiovascular event prophylaxis through the remaining lisinopril_20mg order.
- Baseline, linha 8 (Correct): Discontinue the 10mg tablet and consolidate with the 20mg tablet into a single daily formulation.

**lisinopril, aumentar dose.** Detalhe: Baseline. O baseline sobe para 30 mg num comprimido só, que é a soma de 10 e 20. O RemedIA explica uma meta de 40 mg a partir do comprimido de 20 mg e ignora o outro.

- RemedIA, linha 19 (Incorrect): Lisinopril 20mg once daily has not achieved target blood pressure (<130/80 mmHg, current BP 150/85 mmHg) for hypertension and secondary cardiovascular event prophylaxis following non-STEMI in this high-risk patient with diabetes and chronic kidney disease. Increasing Lisinopril to the target dose of 40mg once daily provides enhanced blood pressure control and optimal cardioprotection. Renal function and serum potassium should be monitored.
- Baseline, linha 9 (Correct): Increase dose to 30mg orally once daily (single tablet) to simplify regimen and assist blood pressure control.

**metformin, reduzir dose.** Detalhe: Baseline. Os dois veem 3000 mg acima do máximo e citam a taxa de filtração 55. O baseline reduz para 1000 mg duas vezes ao dia, o máximo de 2000 mg, com as refeições. O RemedIA desce para 500 mg duas vezes ao dia e trata a taxa 55 como se já impusesse esse teto.

- RemedIA, linha 25 (Debatable): Metformin 3000 mg daily exceeds the maximum recommended dose (2000–2550 mg daily) and is excessive given mild-to-moderate renal impairment (eGFR 55 mL/min/1.73m2, where max dose is typically 1000–1500 mg daily), increasing risk of lactic acidosis and GI intolerance. Reducing dose to 500 mg twice daily (1000 mg daily) mitigates toxicity while maintaining glycemic control.
- Baseline, linha 7 (Correct): Reduce dose to 1,000mg twice daily with meals (maximum 2,000mg daily) in view of renal function (eGFR 55 mL/min/1.73m²).

### Mesmo fármaco, ação diferente

| Fármaco | RemedIA | Baseline |
| --- | --- | --- |
| aspirin | manter | suspender |
| bendroflumethiazide | substituir | suspender |
| clenil | substituir | manter |
| co-codamol | substituir | manter |
| diclofenac | substituir | suspender |
| gabapentin | substituir | manter |
| gliclazide | aumentar dose | manter |
| levothyroxine | suspender, aumentar dose | suspender, iniciar |
| omeprazole | substituir | reduzir dose |
| pioglitazone | substituir | suspender |
| salbutamol | substituir | manter |

## 09_07 — High risk combination – antiplatelet and anticoagulant

### Ações

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 4 | 3 |
| suspender | 4 | 4 |
| reduzir dose | 1 | 3 |
| aumentar dose | 0 | 0 |
| substituir | 3 | 0 |
| iniciar | 1 | 0 |
| outra | 0 | 0 |
| Total | 13 | 10 |

### Keeps e criatividade

| Algoritmo | Propositivas | Keeps | Propositivas por keep | Parcela propositiva % |
| --- | --- | --- | --- | --- |
| RemedIA | 9 | 4 | 2.2 | 69.2 |
| Baseline | 7 | 3 | 2.3 | 70.0 |

### Acurácia

| Algoritmo | N | Sem nota | Correto | Aceitável | Debatível | Incorreto | Correto % | Aceitável % | Debatível % | Incorreto % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RemedIA | 13 | 0 | 3 | 2 | 4 | 4 | 23.1 | 15.4 | 30.8 | 30.8 |
| Baseline | 10 | 0 | 6 | 3 | 1 | 0 | 60.0 | 30.0 | 10.0 | 0.0 |

### Duplicações

| Algoritmo | Duplicações |
| --- | --- |
| RemedIA | 0 |
| Baseline | 0 |

O RemedIA fez 9 ações propositivas e 4 keeps (2.2 por keep). o baseline fez 7 e 3 (2.3 por keep). no RemedIA, Correto 3, Aceitável 2, Debatável 4, Incorreto 4 (acerto amplo 38.5%, erro 30.8%). no baseline, Correto 6, Aceitável 3, Debatável 1, Incorreto 0 (acerto amplo 90.0%, erro 0.0%). nas 3 explicações da mesma ação, o detalhe ficou com o RemedIA em 1, com o baseline em 0 e empatou em 2.

### Explicações da mesma ação

**co-codamol, suspender.** Detalhe: RemedIA. O RemedIA aponta opioide sem diagnóstico de dor e a interação que reduz o efeito do clopidogrel. O baseline deixa a porta aberta para uso curto se necessário, sem esse problema.

- RemedIA, linha 6 (Debatable): Co-codamol 30/500 is prescribed PRN without an active documented indication or ongoing pain diagnosis. In an 81-year-old frail patient, concurrent opioid therapy poses significant risks of falls, sedation, and additive CNS depression with zopiclone and citalopram, while also reducing clopidogrel antiplatelet efficacy. Discontinuing co-codamol eliminates unnecessary medication burden and DDI risks without impairing care.
- Baseline, linha 6 (Acceptable): Review ongoing pain management; discontinue or restrict strictly to short-term PRN use, avoiding routine use due to fall, confusion, and constipation risks.

**edoxaban, reduzir dose.** Detalhe: Empate. Os dois reduzem para 30 mg pelo clearance de 27 e pelo peso de 52 kg. O critério e a dose são os mesmos.

- RemedIA, linha 13 (Correct): Edoxaban 60 mg once daily is excessively dosed for this patient given her renal impairment (calculated CrCl 27 mL/min) and low body weight (52 kg). Dosing criteria require a dose reduction to 30 mg once daily for CrCl 15–50 mL/min or weight ≤ 60 kg to avoid excessive drug accumulation and mitigate major bleeding risks, while preserving efficacy for stroke prophylaxis in atrial fibrillation and secondary vascular prevention. Concomitant clopidogrel further exacerbates bleeding hazard, reinforcing the necessity of dose reduction.
- Baseline, linha 1 (Correct): Reduce dose to 30mg orally once daily due to renal impairment (CrCl 27mL/min) and low body weight (52kg).

**zopiclone, suspender.** Detalhe: Empate. Os dois retiram o hipnótico por sedação, confusão e queda. O RemedIA marca a falta de indicação e a fratura; o baseline, o plano de desmame.

- RemedIA, linha 8 (Correct): Zopiclone 3.75mg (zopiclone_3p75mg) is prescribed without a documented medical indication or active sleep disorder. In an 81-year-old moderately frail patient (Rockwood CFS 6) with history of fracture, zopiclone significantly increases the risk of falls, cognitive impairment, and CNS depression, especially alongside citalopram. Discontinuation eliminates unnecessary drug exposure and mitigates serious fall and sedation risks.
- Baseline, linha 5 (Correct): Formulate a deprescribing plan to gradually taper and discontinue zopiclone to reduce sedation, confusion, and fall risk.

### Mesmo fármaco, ação diferente

| Fármaco | RemedIA | Baseline |
| --- | --- | --- |
| bendroflumethiazide | substituir | suspender |
| citalopram | suspender, substituir | reduzir dose |
| clopidogrel | manter | suspender |
| levothyroxine | manter, suspender | reduzir dose |
| omeprazole | substituir | manter |

## 09_08 — Chronic pain – opioids

### Ações

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 5 | 8 |
| suspender | 4 | 4 |
| reduzir dose | 3 | 3 |
| aumentar dose | 1 | 0 |
| substituir | 3 | 0 |
| iniciar | 4 | 1 |
| outra | 0 | 0 |
| Total | 20 | 16 |

### Keeps e criatividade

| Algoritmo | Propositivas | Keeps | Propositivas por keep | Parcela propositiva % |
| --- | --- | --- | --- | --- |
| RemedIA | 15 | 5 | 3.0 | 75.0 |
| Baseline | 8 | 8 | 1.0 | 50.0 |

### Acurácia

| Algoritmo | N | Sem nota | Correto | Aceitável | Debatível | Incorreto | Correto % | Aceitável % | Debatível % | Incorreto % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RemedIA | 20 | 0 | 11 | 3 | 3 | 3 | 55.0 | 15.0 | 15.0 | 15.0 |
| Baseline | 16 | 0 | 11 | 4 | 1 | 0 | 68.8 | 25.0 | 6.2 | 0.0 |

### Duplicações

| Algoritmo | Duplicações |
| --- | --- |
| RemedIA | 0 |
| Baseline | 0 |

O RemedIA fez 15 ações propositivas e 5 keeps (3.0 por keep). o baseline fez 8 e 8 (1.0 por keep). no RemedIA, Correto 11, Aceitável 3, Debatável 3, Incorreto 3 (acerto amplo 70.0%, erro 15.0%). no baseline, Correto 11, Aceitável 4, Debatável 1, Incorreto 0 (acerto amplo 93.8%, erro 0.0%). nas 4 explicações da mesma ação, o detalhe ficou com o RemedIA em 2, com o baseline em 1 e empatou em 1.

### Explicações da mesma ação

**longtec, suspender.** Detalhe: Baseline. O RemedIA trata o Longtec 5 mg como duplicata inútil do de 40 mg. A suspensão pode ser certa, mas o problema não é esse. O baseline explica a retirada do opioide: cerca de 10% a cada duas a quatro semanas, com vigilância de abstinência e dor.

- RemedIA, linha 6 (Debatable): Longtec 5mg twice daily represents a redundant, duplicate modified-release oxycodone order alongside Longtec 40mg twice daily for Chronic Lower Back Pain. Having concurrent duplicate orders of the identical modified-release formulation increases the risk of cumulative opioid toxicity, confusion, and oversedation without clear therapeutic benefit. Discontinuing the redundant lower-dose Longtec 5mg order resolves the duplication while retaining the primary Longtec 40mg line for baseline pain control.
- Baseline, linha 1 (Correct): Initiate a slow, patient-agreed gradual taper (e.g., reduce daily dose by ~10% every 2–4 weeks) with close monitoring for withdrawal and pain levels.

**quinine, suspender.** Detalhe: Empate. Os dois suspendem quinino pela toxicidade e pela indicação fraca. O RemedIA cita o intervalo QT com a mirtazapina; o baseline, a revisão de cãibra e a falta de eficácia sustentada.

- RemedIA, linha 8 (Correct): There is no documented indication (such as nocturnal leg cramps or malaria) for quinine sulphate. Discontinuing it eliminates unnecessary drug therapy and mitigates the risk of QT prolongation, especially given the concurrent use of mirtazapine.
- Baseline, linha 7 (Correct): Discontinue medication after reviewing indication for leg cramps, given risk of toxicity and lack of sustained efficacy.

**shortec, reduzir dose.** Detalhe: RemedIA. O RemedIA calcula a dose de resgate contra o Longtec e cita o peso de 32 kg e a confusão, e por isso baixa para 5 mg. O baseline só pede menos uso durante o desmame, sem essa conta.

- RemedIA, linha 20 (Correct): Shortec 10 mg PRN exceeds the standard breakthrough dose proportion relative to background Longtec 10 mg twice daily (total daily dose 20 mg; standard breakthrough is 1/10th to 1/6th of total daily dose, or ~2.5–5 mg). In a frail 74-year-old female weighing 32 kg with episodic confusion, 10 mg poses significant CNS depression and sedation risks. Reducing Shortec to 5 mg PRN provides safe, proportional breakthrough analgesia for chronic lower back pain.
- Baseline, linha 2 (Correct): Gradually reduce frequency and limit use to severe breakthrough pain during the Longtec taper, with the ultimate goal of discontinuation.

**zopiclone, suspender.** Detalhe: RemedIA. Os dois suspendem pelo risco de queda. O RemedIA nomeia o que torna a suspensão urgente aqui: diazepam, mirtazapina e oxicodona em dose alta.

- RemedIA, linha 9 (Correct): Zopiclone (zopiclone_3p75mg) lacks a documented clinical indication or diagnosis on the problem list. Discontinuing it eliminates unnecessary drug therapy and mitigates the risk of additive central nervous system depression, sedation, confusion, and falls in this frail elderly patient who is concomitantly taking diazepam, mirtazapine, and high-dose oxycodone.
- Baseline, linha 4 (Correct): Taper and discontinue slowly to reduce hypnotic burden, confusion, and fall risk; reinforce sleep hygiene.

### Mesmo fármaco, ação diferente

| Fármaco | RemedIA | Baseline |
| --- | --- | --- |
| clopidogrel | aumentar dose | manter |
| diazepam | substituir | reduzir dose |
| longtec | suspender, reduzir dose | suspender |
| nitrofurantoin | substituir | suspender |
| omeprazole | substituir | manter |
| oxybutynin | suspender | reduzir dose |
| paracetamol | reduzir dose | manter |

## 09_09 — Chronic pain – anticonvulsants

### Ações

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 1 | 2 |
| suspender | 0 | 1 |
| reduzir dose | 0 | 1 |
| aumentar dose | 0 | 0 |
| substituir | 3 | 0 |
| iniciar | 0 | 0 |
| outra | 0 | 0 |
| Total | 4 | 4 |

### Keeps e criatividade

| Algoritmo | Propositivas | Keeps | Propositivas por keep | Parcela propositiva % |
| --- | --- | --- | --- | --- |
| RemedIA | 3 | 1 | 3.0 | 75.0 |
| Baseline | 2 | 2 | 1.0 | 50.0 |

### Acurácia

| Algoritmo | N | Sem nota | Correto | Aceitável | Debatível | Incorreto | Correto % | Aceitável % | Debatível % | Incorreto % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RemedIA | 4 | 0 | 4 | 0 | 0 | 0 | 100.0 | 0.0 | 0.0 | 0.0 |
| Baseline | 4 | 0 | 2 | 2 | 0 | 0 | 50.0 | 50.0 | 0.0 | 0.0 |

### Duplicações

| Algoritmo | Duplicações |
| --- | --- |
| RemedIA | 0 |
| Baseline | 0 |

O RemedIA fez 3 ações propositivas e 1 keeps (3.0 por keep). o baseline fez 2 e 2 (1.0 por keep). no RemedIA, Correto 4, Aceitável 0, Debatável 0, Incorreto 0 (acerto amplo 100.0%, erro 0.0%). no baseline, Correto 2, Aceitável 2, Debatável 0, Incorreto 0 (acerto amplo 100.0%, erro 0.0%). não há ação igual, fora de keep, para comparar a explicação.

### Mesmo fármaco, ação diferente

| Fármaco | RemedIA | Baseline |
| --- | --- | --- |
| gabapentin | substituir | reduzir dose |
| paracetamol | substituir | manter |
| tramadol | substituir | suspender |

## 09_10 — Chronic pain – Antidepressants

### Ações

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 4 | 5 |
| suspender | 0 | 1 |
| reduzir dose | 0 | 1 |
| aumentar dose | 0 | 0 |
| substituir | 3 | 0 |
| iniciar | 1 | 1 |
| outra | 0 | 0 |
| Total | 8 | 8 |

### Keeps e criatividade

| Algoritmo | Propositivas | Keeps | Propositivas por keep | Parcela propositiva % |
| --- | --- | --- | --- | --- |
| RemedIA | 4 | 4 | 1.0 | 50.0 |
| Baseline | 3 | 5 | 0.6 | 37.5 |

### Acurácia

| Algoritmo | N | Sem nota | Correto | Aceitável | Debatível | Incorreto | Correto % | Aceitável % | Debatível % | Incorreto % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RemedIA | 8 | 0 | 1 | 1 | 3 | 3 | 12.5 | 12.5 | 37.5 | 37.5 |
| Baseline | 8 | 0 | 4 | 3 | 0 | 1 | 50.0 | 37.5 | 0.0 | 12.5 |

### Duplicações

| Algoritmo | Duplicações |
| --- | --- |
| RemedIA | 0 |
| Baseline | 0 |

O RemedIA fez 4 ações propositivas e 4 keeps (1.0 por keep). o baseline fez 3 e 5 (0.6 por keep). no RemedIA, Correto 1, Aceitável 1, Debatável 3, Incorreto 3 (acerto amplo 25.0%, erro 37.5%). no baseline, Correto 4, Aceitável 3, Debatável 0, Incorreto 1 (acerto amplo 87.5%, erro 12.5%). nas 1 explicações da mesma ação, o detalhe ficou com o RemedIA em 1, com o baseline em 0 e empatou em 0.

### Explicações da mesma ação

**pregabalin, iniciar.** Detalhe: RemedIA. Os dois iniciam 75 mg duas vezes ao dia na dor neuropática diabética. O RemedIA explica a lacuna: duloxetina, amitriptilina e tramadol não controlaram a dor, e a filtração permite a dose.

- RemedIA, linha 5 (Debatable): The patient experiences uncontrolled diabetic peripheral neuropathic pain despite multimodal therapy with duloxetine, amitriptyline, and tramadol. Adding pregabalin introduces a distinct guideline-recommended mechanism (calcium channel alpha-2-delta ligand) to act synergistically alongside existing therapies for improved pain control. Renal function is normal (eGFR >60 ml/min/1.73m2), supporting standard initial dosing with monitoring for somnolence and dizziness.
- Baseline, linha 4 (Acceptable): Initiate at 75mg twice daily (or 75mg at night initially) and titrate according to response and tolerability for diabetic peripheral neuropathic pain.

### Mesmo fármaco, ação diferente

| Fármaco | RemedIA | Baseline |
| --- | --- | --- |
| amitriptyline | manter | reduzir dose |
| duloxetine | substituir | manter |
| tramadol | substituir | suspender |

## 09_11 — Type 2 diabetes mellitus with severe frailty

### Ações

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 9 | 12 |
| suspender | 7 | 8 |
| reduzir dose | 1 | 4 |
| aumentar dose | 0 | 0 |
| substituir | 4 | 0 |
| iniciar | 3 | 2 |
| outra | 0 | 0 |
| Total | 24 | 26 |

### Keeps e criatividade

| Algoritmo | Propositivas | Keeps | Propositivas por keep | Parcela propositiva % |
| --- | --- | --- | --- | --- |
| RemedIA | 15 | 9 | 1.7 | 62.5 |
| Baseline | 14 | 12 | 1.2 | 53.8 |

### Acurácia

| Algoritmo | N | Sem nota | Correto | Aceitável | Debatível | Incorreto | Correto % | Aceitável % | Debatível % | Incorreto % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RemedIA | 24 | 0 | 11 | 7 | 5 | 1 | 45.8 | 29.2 | 20.8 | 4.2 |
| Baseline | 26 | 0 | 15 | 7 | 3 | 1 | 57.7 | 26.9 | 11.5 | 3.8 |

### Duplicações

| Algoritmo | Duplicações |
| --- | --- |
| RemedIA | 0 |
| Baseline | 0 |

O RemedIA fez 15 ações propositivas e 9 keeps (1.7 por keep). o baseline fez 14 e 12 (1.2 por keep). no RemedIA, Correto 11, Aceitável 7, Debatável 5, Incorreto 1 (acerto amplo 75.0%, erro 4.2%). no baseline, Correto 15, Aceitável 7, Debatável 3, Incorreto 1 (acerto amplo 84.6%, erro 3.8%). nas 7 explicações da mesma ação, o detalhe ficou com o RemedIA em 4, com o baseline em 0 e empatou em 3.

### Explicações da mesma ação

**ascorbic, suspender.** Detalhe: Empate. Os dois suspendem ácido ascórbico sem indicação, para reduzir comprimidos. O RemedIA explicita a dose de 2000 mg; a ação é a mesma.

- RemedIA, linha 10 (Correct): Ascorbic acid 500mg tablets (prescribed as two tablets twice daily, total 2000mg/day) has no documented clinical diagnosis or valid medical indication. Although ascorbic acid can enhance iron absorption, routine high-dose supplementation is unnecessary and adds significant pill burden in a severely frail patient with polypharmacy. Discontinuing ascorbic acid eliminates an unnecessary drug therapy without compromising care.
- Baseline, linha 4 (Correct): Discontinue ascorbic acid as there is no clear clinical indication, reducing pill burden.

**atorvastatin, iniciar.** Detalhe: RemedIA. Os dois iniciam 20 mg na prevenção secundária, com decisão compartilhada diante da fragilidade. O RemedIA explica por que não é 80 mg: colesterol 6,3, revascularização prévia, escala de fragilidade 8 e enzimas normais.

- RemedIA, linha 18 (Acceptable): Patient has established ischaemic heart disease (prior MI and CABG) and elevated cholesterol (6.3 mmol/L) but lacks foundational lipid-lowering therapy. Guidelines mandate high-intensity statin therapy for secondary cardiovascular prevention. Atorvastatin coexists with current GTN and liraglutide, reducing recurrent cardiovascular events and mortality. A moderate starting dose of 20 mg once daily is prudent given severe frailty (CFS 8) and polypharmacy, balancing plaque stabilization against myopathy risk. LFTs are normal, supporting safe initiation.
- Baseline, linha 26 (Acceptable): Initiate atorvastatin 20 mg once daily for secondary cardiovascular prevention, subject to shared decision-making regarding goals of care.

**ferrous, suspender.** Detalhe: RemedIA. Os dois condicionam a suspensão a estoques normais. O RemedIA já usa o hemograma normal e explica a ligação com a levotiroxina.

- RemedIA, linha 11 (Correct): Ferrous fumarate 210mg lacks a documented indication; FBC is normal with no diagnosed iron deficiency anemia. Discontinuing it eliminates pill burden, reduces GI adverse effects, and resolves a clinically significant binding interaction with levothyroxine.
- Baseline, linha 14 (Correct): Review ongoing indication; discontinue if ferritin/iron stores are normal and FBC remains stable to reduce GI side effects and pill burden.

**folic, suspender.** Detalhe: Empate. Os dois suspendem porque o folato está acima de 20 e o hemograma é normal. O problema e a ação coincidem.

- RemedIA, linha 12 (Correct): Folic acid 5mg daily is prescribed without a documented indication or co-prescribed antifolate therapy. Recent blood tests reveal an elevated serum folate level (>20 ng/mL) and normal full blood count, with no evidence of ongoing folate deficiency or anemia (ferrous fumarate has already been discontinued). Continuing high-dose folic acid represents unnecessary drug therapy with potential risk of masking vitamin B12 deficiency. Therefore, folic acid should be safely discontinued.
- Baseline, linha 3 (Correct): Discontinue folic acid as serum folate levels are elevated (>20 ng/mL) and FBC is normal.

**oxycodone, suspender.** Detalhe: RemedIA. O RemedIA explica que a oxicodona ficou do câncer de colo, sem dor atual, e cita DPOC, oxigênio e o risco respiratório com pregabalina, mirtazapina e venlafaxina. O baseline pede revisão e desmame se a dor estiver estável.

- RemedIA, linha 14 (Correct): Oxycodone modified-release was initiated historically for cervical cancer diagnosed 8 months ago, but there is no documented active cancer-related pain or current indication justifying ongoing round-the-clock opioid therapy. In this severely frail 71-year-old patient (Rockwood score 8) with severe COPD on LTOT, concurrent use of oxycodone with multiple CNS depressants (pregabalin, mirtazapine, venlafaxine) creates an unacceptable risk of sedation, fall-related injury, and life-threatening respiratory depression. Discontinuing oxycodone eliminates unnecessary opioid exposure safely.
- Baseline, linha 8 (Correct): Review pain indication and initiate a structured downward titration to deprescribe if chronic pain is stable.

**pregabalin, suspender.** Detalhe: Empate. Os dois retiram pregabalina sem indicação clara, pelo risco de tontura, sedação e queda. O desmame está nos dois.

- RemedIA, linha 15 (Correct): Pregabalin 25mg is prescribed without a documented medical indication (such as neuropathic pain, epilepsy, or generalized anxiety disorder). In a severely frail patient (Rockwood Clinical Frailty Scale 8) with ongoing fall prevention measures, pregabalin adds unnecessary risk of CNS depression, sedation, and falls, especially alongside mirtazapine. Discontinuing pregabalin removes unnecessary drug therapy and mitigates fall and sedative risks.
- Baseline, linha 9 (Correct): Review indication and consider tapering to discontinue to reduce dizziness, sedation, and fall risk.

**solifenacin, suspender.** Detalhe: RemedIA. Os dois suspendem pela carga anticolinérgica e pela queda. O RemedIA mostra que não há bexiga hiperativa e nomeia o umeclidínio e o risco de QT com a venlafaxina.

- RemedIA, linha 16 (Correct): Solifenacin (solifenacin_5mg) has no documented indication (such as overactive bladder) in the medical record. In this severely frail 71-year-old patient (Rockwood CFS 8) with fall prevention needs, solifenacin introduces unnecessary anticholinergic burden and interacts with umeclidinium in Trelegy Ellipta and mirtazapine, worsening fall and cognitive risks, and carries additive QT risk with venlafaxine. Discontinuing solifenacin resolves the drug therapy problem without requiring replacement.
- Baseline, linha 5 (Correct): Deprescribe and discontinue solifenacin to reduce anticholinergic burden and fall risk.

### Mesmo fármaco, ação diferente

| Fármaco | RemedIA | Baseline |
| --- | --- | --- |
| doxazosin | substituir | suspender |
| furosemide | substituir | reduzir dose |
| insulin | manter | manter, suspender, reduzir dose |
| lactulose | suspender | manter |
| metformin | reduzir dose | manter |
| mirtazapine | substituir | reduzir dose |
| venlafaxine | substituir | reduzir dose |

## 09_12 — Chronic Constipation

### Ações

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 7 | 6 |
| suspender | 2 | 6 |
| reduzir dose | 1 | 2 |
| aumentar dose | 0 | 0 |
| substituir | 4 | 1 |
| iniciar | 3 | 0 |
| outra | 0 | 0 |
| Total | 17 | 15 |

### Keeps e criatividade

| Algoritmo | Propositivas | Keeps | Propositivas por keep | Parcela propositiva % |
| --- | --- | --- | --- | --- |
| RemedIA | 10 | 7 | 1.4 | 58.8 |
| Baseline | 9 | 6 | 1.5 | 60.0 |

### Acurácia

| Algoritmo | N | Sem nota | Correto | Aceitável | Debatível | Incorreto | Correto % | Aceitável % | Debatível % | Incorreto % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RemedIA | 17 | 0 | 10 | 1 | 2 | 4 | 58.8 | 5.9 | 11.8 | 23.5 |
| Baseline | 15 | 0 | 14 | 1 | 0 | 0 | 93.3 | 6.7 | 0.0 | 0.0 |

### Duplicações

| Algoritmo | Duplicações |
| --- | --- |
| RemedIA | 0 |
| Baseline | 0 |

O RemedIA fez 10 ações propositivas e 7 keeps (1.4 por keep). o baseline fez 9 e 6 (1.5 por keep). no RemedIA, Correto 10, Aceitável 1, Debatável 2, Incorreto 4 (acerto amplo 64.7%, erro 23.5%). no baseline, Correto 14, Aceitável 1, Debatável 0, Incorreto 0 (acerto amplo 100.0%, erro 0.0%). nas 2 explicações da mesma ação, o detalhe ficou com o RemedIA em 2, com o baseline em 0 e empatou em 0.

### Explicações da mesma ação

**aspirin, suspender.** Detalhe: RemedIA. Os dois suspendem o ácido acetilsalicílico porque a apixabana já anticoagula e o sangramento sobe. O RemedIA acrescenta a anemia ferropriva e a ausência de síndrome coronária recente.

- RemedIA, linha 9 (Correct): Aspirin is redundant for stroke prevention in atrial flutter and cardiovascular prophylaxis because the patient is already receiving therapeutic anticoagulation with apixaban. Concomitant use of aspirin and apixaban substantially elevates major bleeding risk without clear indication (no recent ACS or stenting) and exacerbates iron deficiency anaemia. Stopping aspirin resolves this redundant antithrombotic therapy and mitigates bleeding and anaemia risks.
- Baseline, linha 3 (Correct): Discontinue to reduce gastrointestinal and systemic bleeding risk, as there is no compelling indication for concurrent therapy with apixaban.

**oxypro, reduzir dose.** Detalhe: RemedIA. Os dois reduzem o opioide por depressão respiratória e constipação. O RemedIA traduz 80 mg por dia em equivalente de morfina e propõe 20 mg duas vezes ao dia. O baseline não fixa a dose.

- RemedIA, linha 17 (Correct): Oxypro 40 mg twice daily (80 mg/day oxycodone, ~120 MME/day) exceeds recommended thresholds for chronic non-cancer back pain (>50 MME/day), escalating risks of respiratory depression, worsening obstructive sleep apnoea, and severe constipation. Tapering to 20 mg twice daily reduces opioid burden towards safer levels while non-opioid multimodal analgesia (paracetamol, topical lidocaine) continues. Dose de-escalation mitigates toxicity and respiratory compromise while maintaining pain control.
- Baseline, linha 1 (Correct): Gradually taper dose under close clinical supervision with the goal of significant reduction or discontinuation to mitigate respiratory depression risk and reduce constipation.

### Mesmo fármaco, ação diferente

| Fármaco | RemedIA | Baseline |
| --- | --- | --- |
| atorvastatin | iniciar | suspender |
| ferrous | substituir | suspender |
| gabapentin | substituir | reduzir dose |
| senna | manter | substituir |
| shortec | substituir | suspender |
| solifenacin | substituir | suspender |

## 09_13 — Adult with Parkinson’s disease

### Ações

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 5 | 4 |
| suspender | 1 | 1 |
| reduzir dose | 0 | 1 |
| aumentar dose | 0 | 1 |
| substituir | 2 | 1 |
| iniciar | 0 | 0 |
| outra | 0 | 0 |
| Total | 8 | 8 |

### Keeps e criatividade

| Algoritmo | Propositivas | Keeps | Propositivas por keep | Parcela propositiva % |
| --- | --- | --- | --- | --- |
| RemedIA | 3 | 5 | 0.6 | 37.5 |
| Baseline | 4 | 4 | 1.0 | 50.0 |

### Acurácia

| Algoritmo | N | Sem nota | Correto | Aceitável | Debatível | Incorreto | Correto % | Aceitável % | Debatível % | Incorreto % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RemedIA | 8 | 0 | 4 | 2 | 2 | 0 | 50.0 | 25.0 | 25.0 | 0.0 |
| Baseline | 8 | 0 | 5 | 1 | 2 | 0 | 62.5 | 12.5 | 25.0 | 0.0 |

### Duplicações

| Algoritmo | Duplicações |
| --- | --- |
| RemedIA | 0 |
| Baseline | 0 |

O RemedIA fez 3 ações propositivas e 5 keeps (0.6 por keep). o baseline fez 4 e 4 (1.0 por keep). no RemedIA, Correto 4, Aceitável 2, Debatável 2, Incorreto 0 (acerto amplo 75.0%, erro 0.0%). no baseline, Correto 5, Aceitável 1, Debatável 2, Incorreto 0 (acerto amplo 75.0%, erro 0.0%). não há ação igual, fora de keep, para comparar a explicação.

### Mesmo fármaco, ação diferente

| Fármaco | RemedIA | Baseline |
| --- | --- | --- |
| co-codamol | substituir | reduzir dose |
| colecalciferol | manter | aumentar dose |
| peptac | suspender | manter |
| pregabalin | manter | suspender |

## 09_14 — Depression and Health Inequalities

### Ações

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 2 | 2 |
| suspender | 0 | 0 |
| reduzir dose | 0 | 0 |
| aumentar dose | 0 | 1 |
| substituir | 1 | 0 |
| iniciar | 0 | 1 |
| outra | 0 | 0 |
| Total | 3 | 4 |

### Keeps e criatividade

| Algoritmo | Propositivas | Keeps | Propositivas por keep | Parcela propositiva % |
| --- | --- | --- | --- | --- |
| RemedIA | 1 | 2 | 0.5 | 33.3 |
| Baseline | 2 | 2 | 1.0 | 50.0 |

### Acurácia

| Algoritmo | N | Sem nota | Correto | Aceitável | Debatível | Incorreto | Correto % | Aceitável % | Debatível % | Incorreto % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RemedIA | 3 | 0 | 3 | 0 | 0 | 0 | 100.0 | 0.0 | 0.0 | 0.0 |
| Baseline | 4 | 0 | 2 | 1 | 1 | 0 | 50.0 | 25.0 | 25.0 | 0.0 |

### Duplicações

| Algoritmo | Duplicações |
| --- | --- |
| RemedIA | 0 |
| Baseline | 0 |

O RemedIA fez 1 ações propositivas e 2 keeps (0.5 por keep). o baseline fez 2 e 2 (1.0 por keep). no RemedIA, Correto 3, Aceitável 0, Debatável 0, Incorreto 0 (acerto amplo 100.0%, erro 0.0%). no baseline, Correto 2, Aceitável 1, Debatável 1, Incorreto 0 (acerto amplo 75.0%, erro 0.0%). não há ação igual, fora de keep, para comparar a explicação.

### Mesmo fármaco, ação diferente

| Fármaco | RemedIA | Baseline |
| --- | --- | --- |
| citalopram | substituir | aumentar dose |

## 09_15 — Anxiety

### Ações

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 0 | 1 |
| suspender | 0 | 0 |
| reduzir dose | 0 | 0 |
| aumentar dose | 0 | 0 |
| substituir | 0 | 0 |
| iniciar | 0 | 0 |
| outra | 0 | 0 |
| Total | 0 | 1 |

### Keeps e criatividade

| Algoritmo | Propositivas | Keeps | Propositivas por keep | Parcela propositiva % |
| --- | --- | --- | --- | --- |
| RemedIA | 0 | 0 | — | — |
| Baseline | 0 | 1 | 0.0 | 0.0 |

### Acurácia

| Algoritmo | N | Sem nota | Correto | Aceitável | Debatível | Incorreto | Correto % | Aceitável % | Debatível % | Incorreto % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RemedIA | 0 | 0 | 0 | 0 | 0 | 0 | — | — | — | — |
| Baseline | 1 | 0 | 1 | 0 | 0 | 0 | 100.0 | 0.0 | 0.0 | 0.0 |

### Duplicações

| Algoritmo | Duplicações |
| --- | --- |
| RemedIA | 0 |
| Baseline | 0 |

O RemedIA não tem linhas neste caso. A aba existe e a tabela de recomendações está vazia, então criatividade, acurácia e detalhe não têm denominador do lado do RemedIA.

## 09_16 — Post traumatic stress disorder with “street benzo” use

### Ações

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 0 | 0 |
| suspender | 0 | 2 |
| reduzir dose | 0 | 0 |
| aumentar dose | 0 | 0 |
| substituir | 1 | 0 |
| iniciar | 0 | 3 |
| outra | 0 | 0 |
| Total | 1 | 5 |

### Keeps e criatividade

| Algoritmo | Propositivas | Keeps | Propositivas por keep | Parcela propositiva % |
| --- | --- | --- | --- | --- |
| RemedIA | 1 | 0 | — | 100.0 |
| Baseline | 5 | 0 | — | 100.0 |

### Acurácia

| Algoritmo | N | Sem nota | Correto | Aceitável | Debatível | Incorreto | Correto % | Aceitável % | Debatível % | Incorreto % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RemedIA | 1 | 0 | 1 | 0 | 0 | 0 | 100.0 | 0.0 | 0.0 | 0.0 |
| Baseline | 5 | 0 | 5 | 0 | 0 | 0 | 100.0 | 0.0 | 0.0 | 0.0 |

### Duplicações

| Algoritmo | Duplicações |
| --- | --- |
| RemedIA | 0 |
| Baseline | 0 |

O RemedIA fez 1 ações propositivas e 0 keeps (sem keep). o baseline fez 5 e 0 (sem keep). no RemedIA, Correto 1, Aceitável 0, Debatável 0, Incorreto 0 (acerto amplo 100.0%, erro 0.0%). no baseline, Correto 5, Aceitável 0, Debatável 0, Incorreto 0 (acerto amplo 100.0%, erro 0.0%). não há ação igual, fora de keep, para comparar a explicação.

### Mesmo fármaco, ação diferente

| Fármaco | RemedIA | Baseline |
| --- | --- | --- |
| solpadeine | substituir | suspender |

## 09_17 — Bipolar disorder and lithium

### Ações

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 1 | 3 |
| suspender | 0 | 1 |
| reduzir dose | 1 | 1 |
| aumentar dose | 0 | 0 |
| substituir | 2 | 0 |
| iniciar | 0 | 0 |
| outra | 0 | 0 |
| Total | 4 | 5 |

### Keeps e criatividade

| Algoritmo | Propositivas | Keeps | Propositivas por keep | Parcela propositiva % |
| --- | --- | --- | --- | --- |
| RemedIA | 3 | 1 | 3.0 | 75.0 |
| Baseline | 2 | 3 | 0.7 | 40.0 |

### Acurácia

| Algoritmo | N | Sem nota | Correto | Aceitável | Debatível | Incorreto | Correto % | Aceitável % | Debatível % | Incorreto % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RemedIA | 4 | 0 | 2 | 0 | 1 | 1 | 50.0 | 0.0 | 25.0 | 25.0 |
| Baseline | 5 | 0 | 3 | 1 | 0 | 1 | 60.0 | 20.0 | 0.0 | 20.0 |

### Duplicações

| Algoritmo | Duplicações |
| --- | --- |
| RemedIA | 0 |
| Baseline | 0 |

O RemedIA fez 3 ações propositivas e 1 keeps (3.0 por keep). o baseline fez 2 e 3 (0.7 por keep). no RemedIA, Correto 2, Aceitável 0, Debatável 1, Incorreto 1 (acerto amplo 50.0%, erro 25.0%). no baseline, Correto 3, Aceitável 1, Debatável 0, Incorreto 1 (acerto amplo 80.0%, erro 20.0%). nas 1 explicações da mesma ação, o detalhe ficou com o RemedIA em 1, com o baseline em 0 e empatou em 0.

### Explicações da mesma ação

**lithium, reduzir dose.** Detalhe: RemedIA. Os dois baixam o Priadel para 600 mg. O RemedIA explica o nível de 0,98, o tremor, a sonolência, a faixa-alvo no idoso e a nova dosagem em cinco a sete dias. O baseline só diz como compor os 600 mg.

- RemedIA, linha 4 (Correct): Lithium dose of 800 mg daily has resulted in an elevated serum level of 0.98 mmol/L along with drowsiness and fine tremor in this 67-year-old patient. In older adults on maintenance therapy for bipolar type 1 disorder, target serum lithium levels are typically 0.4-0.6 mmol/L (or 0.6-0.8 mmol/L generally). Reducing Priadel to 600 mg once daily at night will lower serum concentration toward target range, resolving tremor and drowsiness while maintaining mood stabilization. Repeat serum lithium levels in 5-7 days.
- Baseline, linha 1 (Correct): Reduce dose to Priadel® 600mg (e.g., one 400mg tablet and one 200mg tablet) once daily at night.

### Mesmo fármaco, ação diferente

| Fármaco | RemedIA | Baseline |
| --- | --- | --- |
| atorvastatin | substituir | manter |
| quinine | manter | suspender |
| ramipril | substituir | manter |

## 09_18 — Antipsychotics in dementia

### Ações

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 2 | 3 |
| suspender | 1 | 4 |
| reduzir dose | 1 | 0 |
| aumentar dose | 0 | 0 |
| substituir | 3 | 0 |
| iniciar | 1 | 3 |
| outra | 0 | 0 |
| Total | 8 | 10 |

### Keeps e criatividade

| Algoritmo | Propositivas | Keeps | Propositivas por keep | Parcela propositiva % |
| --- | --- | --- | --- | --- |
| RemedIA | 6 | 2 | 3.0 | 75.0 |
| Baseline | 7 | 3 | 2.3 | 70.0 |

### Acurácia

| Algoritmo | N | Sem nota | Correto | Aceitável | Debatível | Incorreto | Correto % | Aceitável % | Debatível % | Incorreto % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RemedIA | 8 | 0 | 1 | 1 | 2 | 4 | 12.5 | 12.5 | 25.0 | 50.0 |
| Baseline | 10 | 0 | 6 | 1 | 1 | 2 | 60.0 | 10.0 | 10.0 | 20.0 |

### Duplicações

| Algoritmo | Duplicações |
| --- | --- |
| RemedIA | 0 |
| Baseline | 0 |

O RemedIA fez 6 ações propositivas e 2 keeps (3.0 por keep). o baseline fez 7 e 3 (2.3 por keep). no RemedIA, Correto 1, Aceitável 1, Debatável 2, Incorreto 4 (acerto amplo 25.0%, erro 50.0%). no baseline, Correto 6, Aceitável 1, Debatável 1, Incorreto 2 (acerto amplo 70.0%, erro 20.0%). nas 1 explicações da mesma ação, o detalhe ficou com o RemedIA em 0, com o baseline em 0 e empatou em 1.

### Explicações da mesma ação

**solifenacin, suspender.** Detalhe: Empate. Os dois suspendem de imediato: anticolinérgico contra o donepezila, delirium, queda e constipação. O QT de 470 ms no RemedIA não muda a ação.

- RemedIA, linha 3 (Correct): Solifenacin has no documented clinical indication (such as overactive bladder) in the medical record. Moreover, its strong anticholinergic properties oppose donepezil, worsen cognitive impairment and confusion in mixed dementia, contribute to constipation (no bowel movement for 3 days), and prolong QTc (470ms). Discontinuing solifenacin removes unnecessary drug therapy and mitigates severe antimuscarinic toxicity.
- Baseline, linha 2 (Correct): Discontinue immediately due to anticholinergic adverse effects, antagonism of donepezil, and contribution to delirium, falls, and constipation.

### Mesmo fármaco, ação diferente

| Fármaco | RemedIA | Baseline |
| --- | --- | --- |
| aspirin | substituir | manter |
| donepezil | reduzir dose | suspender |
| hydroxyzine | substituir | suspender |
| risperidone | substituir | suspender |

## 09_19 — Antipsychotic use following recent hospital discharge

### Ações

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 2 | 1 |
| suspender | 3 | 6 |
| reduzir dose | 0 | 0 |
| aumentar dose | 0 | 0 |
| substituir | 0 | 0 |
| iniciar | 1 | 1 |
| outra | 0 | 0 |
| Total | 6 | 8 |

### Keeps e criatividade

| Algoritmo | Propositivas | Keeps | Propositivas por keep | Parcela propositiva % |
| --- | --- | --- | --- | --- |
| RemedIA | 4 | 2 | 2.0 | 66.7 |
| Baseline | 7 | 1 | 7.0 | 87.5 |

### Acurácia

| Algoritmo | N | Sem nota | Correto | Aceitável | Debatível | Incorreto | Correto % | Aceitável % | Debatível % | Incorreto % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RemedIA | 6 | 0 | 3 | 2 | 0 | 1 | 50.0 | 33.3 | 0.0 | 16.7 |
| Baseline | 8 | 0 | 8 | 0 | 0 | 0 | 100.0 | 0.0 | 0.0 | 0.0 |

### Duplicações

| Algoritmo | Duplicações |
| --- | --- |
| RemedIA | 0 |
| Baseline | 1 |

Resposta repetida, defeito do modelo. A linha continua contada na tabela de ações.

- Baseline. Linhas 7, 8 repetem a frase "Ensure medication is confirmed discontinued and removed from the active regimen as the course is complete.". Alvos: Amoxicillin 500mg capsules; Trimethoprim 200mg tablets. É a mesma resposta copiada em mais de uma linha.

O RemedIA fez 4 ações propositivas e 2 keeps (2.0 por keep). o baseline fez 7 e 1 (7.0 por keep). no RemedIA, Correto 3, Aceitável 2, Debatável 0, Incorreto 1 (acerto amplo 83.3%, erro 16.7%). no baseline, Correto 8, Aceitável 0, Debatável 0, Incorreto 0 (acerto amplo 100.0%, erro 0.0%). nas 3 explicações da mesma ação, o detalhe ficou com o RemedIA em 1, com o baseline em 1 e empatou em 1.

### Explicações da mesma ação

**amitriptyline, suspender.** Detalhe: Baseline. Os dois veem a carga anticolinérgica e a sedação depois do delirium. O baseline explica a retirada: 25 mg por uma a duas semanas, depois 10 mg, depois parar. O RemedIA manda suspender 50 mg sem esse caminho.

- RemedIA, linha 3 (Correct): Amitriptyline (amitriptyline_50mg) has no documented indication in the chart and adds significant anticholinergic burden, CNS depression, and delirium risk in this 78-year-old patient who recently suffered delirium and is presenting with confusion and sleepiness. Discontinuing amitriptyline directly addresses this unnecessary therapy and reduces active sedation and cognitive slowing.
- Baseline, linha 2 (Correct): Taper and discontinue gradually (e.g., reduce to 25mg at night for 1–2 weeks, then 10mg, then stop) to reduce anticholinergic burden and sedation; explore alternative non-pharmacological measures or safer alternatives if prescribed for neuropathic pain or sleep.

**oxybutynin, suspender.** Detalhe: RemedIA. Os dois suspendem pelo efeito anticolinérgico e pela cognição. O RemedIA identifica o problema: a paciente é continente e não tem bexiga hiperativa.

- RemedIA, linha 4 (Correct): Oxybutynin lacks a documented indication as the patient is explicitly continent with no history of overactive bladder. Its potent anticholinergic properties are directly contributing to her cognitive slowing, confusion, and drowsiness, exacerbating frailty and recent post-delirium vulnerability. Discontinuing oxybutynin resolves this unnecessary drug therapy problem and eliminates additive anticholinergic exposure.
- Baseline, linha 3 (Correct): Discontinue to minimize anticholinergic burden and cognitive impairment; re-evaluate urinary symptoms post-cessation and consider non-pharmacological bladder training or a uroselective agent (e.g., mirabegron) if urgency recurs.

**risperidone, suspender.** Detalhe: Empate. Os dois retiram a risperidona porque o delirium da infecção passou. O RemedIA descreve a internação curta; o baseline, o desmame em uma a duas semanas.

- RemedIA, linha 5 (Correct): Risperidone 500 mcg twice daily was initiated for acute delirium during a short admission for suspected infection. The acute episode has resolved, leaving no ongoing indication for antipsychotic therapy. Continued use contributes to documented excessive sedation, cognitive slowing, functional decline, and risks metabolic deterioration and orthostasis in this 78-year-old patient. Discontinuation safely addresses the lack of valid medical indication.
- Baseline, linha 1 (Correct): Deprescribe and taper off over 1 to 2 weeks (e.g., reduce to 250 micrograms once daily for a few days, then discontinue), as the acute infection and acute delirium have resolved.

### Mesmo fármaco, ação diferente

| Fármaco | RemedIA | Baseline |
| --- | --- | --- |
| bendroflumethiazide | manter | suspender |

## 09_20 — Antibiotics - penicillin allergy de-labelling

### Ações

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 2 | 6 |
| suspender | 4 | 2 |
| reduzir dose | 1 | 0 |
| aumentar dose | 1 | 1 |
| substituir | 1 | 0 |
| iniciar | 2 | 1 |
| outra | 0 | 0 |
| Total | 11 | 10 |

### Keeps e criatividade

| Algoritmo | Propositivas | Keeps | Propositivas por keep | Parcela propositiva % |
| --- | --- | --- | --- | --- |
| RemedIA | 9 | 2 | 4.5 | 81.8 |
| Baseline | 4 | 6 | 0.7 | 40.0 |

### Acurácia

| Algoritmo | N | Sem nota | Correto | Aceitável | Debatível | Incorreto | Correto % | Aceitável % | Debatível % | Incorreto % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RemedIA | 11 | 0 | 7 | 0 | 3 | 1 | 63.6 | 0.0 | 27.3 | 9.1 |
| Baseline | 10 | 0 | 4 | 4 | 1 | 1 | 40.0 | 40.0 | 10.0 | 10.0 |

### Duplicações

| Algoritmo | Duplicações |
| --- | --- |
| RemedIA | 0 |
| Baseline | 0 |

O RemedIA fez 9 ações propositivas e 2 keeps (4.5 por keep). o baseline fez 4 e 6 (0.7 por keep). no RemedIA, Correto 7, Aceitável 0, Debatável 3, Incorreto 1 (acerto amplo 63.6%, erro 9.1%). no baseline, Correto 4, Aceitável 4, Debatável 1, Incorreto 1 (acerto amplo 80.0%, erro 10.0%). nas 4 explicações da mesma ação, o detalhe ficou com o RemedIA em 2, com o baseline em 0 e empatou em 2.

### Explicações da mesma ação

**amoxicillin, iniciar.** Detalhe: Empate. Os dois iniciam amoxicilina 500 mg de 12 em 12 horas, ajustada ao clearance, e tratam a alergia antiga como intolerância gastrointestinal. O RemedIA cita a sensibilidade da cultura; o baseline, a duração de 7 a 14 dias.

- RemedIA, linha 7 (Correct): Patient has an active upper urinary tract infection (E. coli, CRP 72 mg/L, fever, back pain) managed only supportively with paracetamol. The isolate is sensitive to amoxicillin, gentamicin, and aztreonam. The reported penicillin allergy was non-allergic gastrointestinal intolerance (nausea/diarrhoea >20 years ago), making amoxicillin safe and indicated. Given CrCl 25 mL/min, amoxicillin dose-adjusted to 500 mg every 12 hours provides effective targeted oral antimicrobial eradication, preventing worsening sepsis while avoiding nephrotoxic alternatives like gentamicin.
- Baseline, linha 1 (Correct): Initiate amoxicillin oral capsules 500 mg every 12 hours (dose-adjusted for eCrCl <30 mL/min) to complete a 7- to 14-day total course for upper UTI, after updating allergy status.

**atorvastatin, suspender.** Detalhe: Empate. Os dois suspendem a estatina de alta intensidade sem indicação clara, pela idade e pela fragilidade. Os números de peso e de filtração não mudam a ação.

- RemedIA, linha 3 (Correct): Atorvastatin 80mg is prescribed without any documented indication such as ASCVD or familial hypercholesterolemia. In an 85-year-old frail female patient (CFS 5, weight 47kg, eGFR 25 mL/min) presenting with acute infection and delirium, high-intensity statin therapy carries unnecessary risks of adverse drug events without clear benefit. Discontinuing atorvastatin_80mg resolves this unnecessary drug therapy.
- Baseline, linha 4 (Correct): Discontinue permanently due to lack of clear indication, advanced age, low BMI, and frailty.

**furosemide, aumentar dose.** Detalhe: RemedIA. Os dois sobem para 40 mg e pedem função renal e eletrólitos. O RemedIA explica por que 20 mg não basta: edema até os joelhos, dispneia e clearance de 25.

- RemedIA, linha 9 (Incorrect): Patient has persistent fluid retention with marked pitting oedema to both knees, ankle swelling, and worsening breathlessness in the setting of HFpEF and renal impairment (CrCl 25 mL/min). The current dose of Furosemide 20mg once daily is inadequate to achieve effective diuresis given reduced renal clearance. Increasing Furosemide to 40mg once daily is recommended to promote decongestion and relieve symptoms. Monitor renal function, blood pressure, and electrolytes closely.
- Baseline, linha 2 (Correct): Increase dose to 40 mg orally once daily in the morning and monitor fluid balance, weight, renal function, and electrolytes.

**lisinopril, suspender.** Detalhe: RemedIA. Os dois seguram o inibidor da enzima conversora na doença aguda. O RemedIA explica a suspensão temporária: pressão 108/56, potássio 5,2, clearance 25, pouca ingestão, e a indicação que volta quando estabilizar.

- RemedIA, linha 4 (Correct): Lisinopril is held due to acute safety concerns in the setting of acute infection, poor oral intake, borderline low BP (108/56 mmHg), hyperkalemia (potassium 5.2 mmol/L), and renal impairment (CrCl 25 mL/min). Continuing an ACE inhibitor during acute hypovolemia and systemic illness heightens the risk of worsening acute kidney injury. Long-term therapy remains indicated for HFpEF once the patient stabilizes. Discontinuing temporarily mitigates renal and hemodynamic risks while maintaining cardiovascular safety.
- Baseline, linha 3 (Acceptable): Continue to withhold until blood pressure, renal function, and acute delirium stabilize.

### Mesmo fármaco, ação diferente

| Fármaco | RemedIA | Baseline |
| --- | --- | --- |
| macrogol | suspender | manter |
| paracetamol | reduzir dose | manter |
| senna | suspender | manter |
| trelegy | substituir | manter |

## 09_21 — Antibiotics in end-of-life care

### Ações

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 2 | 0 |
| suspender | 5 | 9 |
| reduzir dose | 0 | 0 |
| aumentar dose | 0 | 0 |
| substituir | 4 | 0 |
| iniciar | 4 | 5 |
| outra | 0 | 0 |
| Total | 15 | 14 |

### Keeps e criatividade

| Algoritmo | Propositivas | Keeps | Propositivas por keep | Parcela propositiva % |
| --- | --- | --- | --- | --- |
| RemedIA | 13 | 2 | 6.5 | 86.7 |
| Baseline | 14 | 0 | — | 100.0 |

### Acurácia

| Algoritmo | N | Sem nota | Correto | Aceitável | Debatível | Incorreto | Correto % | Aceitável % | Debatível % | Incorreto % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RemedIA | 15 | 0 | 6 | 3 | 2 | 4 | 40.0 | 20.0 | 13.3 | 26.7 |
| Baseline | 14 | 0 | 11 | 3 | 0 | 0 | 78.6 | 21.4 | 0.0 | 0.0 |

### Duplicações

| Algoritmo | Duplicações |
| --- | --- |
| RemedIA | 0 |
| Baseline | 0 |

O RemedIA fez 13 ações propositivas e 2 keeps (6.5 por keep). o baseline fez 14 e 0 (sem keep). no RemedIA, Correto 6, Aceitável 3, Debatável 2, Incorreto 4 (acerto amplo 60.0%, erro 26.7%). no baseline, Correto 11, Aceitável 3, Debatável 0, Incorreto 0 (acerto amplo 100.0%, erro 0.0%). nas 6 explicações da mesma ação, o detalhe ficou com o RemedIA em 3, com o baseline em 1 e empatou em 2.

### Explicações da mesma ação

**amlodipine, suspender.** Detalhe: Baseline. O RemedIA trata a suspensão como pausa até a pressão voltar, com os números 100/55, desidratação e rim. No fim de vida, o baseline identifica o problema certo: hipotensão e transição para cuidado de conforto.

- RemedIA, linha 3 (Correct): Amlodipine is indicated for hypertension and ischaemic heart disease, but the patient presents with acute hypotension (BP 100/55 mmHg, pulse 110 bpm), dehydration, and acute renal impairment. Continuing a vasodilator risks exacerbating hypoperfusion and renal injury. A temporary safety discontinuation is required until acute illness resolves and hemodynamics stabilize.
- Baseline, linha 1 (Correct): Discontinue the medication due to hypotension and transition to comfort-focused care.

**macrogol, suspender.** Detalhe: RemedIA. Os dois suspendem o laxante pelas fezes líquidas. O RemedIA liga a falta de indicação de constipação à desidratação, à ureia 22 e ao clearance 21.

- RemedIA, linha 4 (Correct): Macrogol 3350 is prescribed without an active documented indication for constipation. The patient is currently experiencing incontinence of loose stools and dehydration with impaired renal function (creatinine clearance 21 mL/min, urea 22.0 mmol/L). Discontinuing macrogol_3350_sachets_one_ directly resolves the unnecessary laxative therapy, preventing further fluid loss, worsening dehydration, and fecal incontinence.
- Baseline, linha 4 (Correct): Discontinue the medication due to current loose stools and swallowing impairment.

**nystatin, iniciar.** Detalhe: RemedIA. Os dois prescrevem nistatina 100 000 unidades quatro vezes ao dia na candidíase oral. O RemedIA explica a escolha: cobertura local, sem a interação do fluconazol com a sinvastatina nem a toxicidade renal no clearance 21.

- RemedIA, linha 10 (Correct): Patient has severe oral candidiasis contributing to dysphagia and dehydration, with no antifungal therapy prescribed. Adding nystatin oral suspension provides localized topical antifungal coverage without systemic CYP3A4 interactions with charted simvastatin or renal toxicity given the patient's low CrCl (21 mL/min). Chosen over systemic fluconazole, which is not on the regimen, to avoid significant CYP-mediated drug interactions. Treating oral candidiasis will relieve oral discomfort and improve oral intake.
- Baseline, linha 14 (Correct): Prescribe nystatin 100,000 units/mL oral suspension, 1 mL applied gently to the oral cavity four times daily for oral candidiasis.

**quinine, suspender.** Detalhe: Empate. Os dois suspendem quinino sem indicação aguda e com risco desfavorável. A trombocitopenia e a sinvastatina, no RemedIA, não mudam a ação.

- RemedIA, linha 5 (Correct): Quinine sulfate has no documented clinical indication (e.g., malaria, leg cramps) in this severely frail patient with renal impairment and acute deterioration. Discontinuing it avoids unnecessary risks, including thrombocytopenia and CYP3A4 inhibition with charted simvastatin.
- Baseline, linha 6 (Correct): Discontinue the medication due to unfavourable risk-benefit profile and lack of acute indication.

**senna, suspender.** Detalhe: Empate. Os dois suspendem sena pelas fezes líquidas e pela dificuldade de engolir. O RemedIA acrescenta a ureia; o problema é o mesmo.

- RemedIA, linha 6 (Correct): Senna 7.5mg is charted without an active indication for constipation. The patient is severely frail, dehydrated (urea 22.0 mmol/L), and actively incontinent of loose stools, which Senna exacerbates. Discontinuing Senna directly addresses the drug therapy problem of unnecessary medication contributing to diarrhea and worsening dehydration.
- Baseline, linha 7 (Correct): Discontinue the medication due to active loose stools and swallowing impairment.

**thiamine, suspender.** Detalhe: RemedIA. O baseline diz que a tiamina não é essencial no cuidado de conforto. O RemedIA explica por que a indicação acabou: abstinência há cinco anos, e a confusão atual é pneumonia, hipercalcemia e desidratação, não Wernicke.

- RemedIA, linha 7 (Correct): Thiamine was historically started for alcohol excess, but the patient has been abstinent for 5 years. The current acute confusion is multifactorial delirium driven by community-acquired pneumonia, hypercalcaemia of malignancy, and dehydration, rather than active Wernicke encephalopathy or acute alcohol withdrawal. Additionally, the patient has difficulty swallowing. Continuing oral thiamine lacks a valid medical indication at this time and adds unnecessary pill burden. Deprescribing thiamine_100mg resolves this unnecessary therapy without compromising delirium management.
- Baseline, linha 9 (Correct): Discontinue the medication as it is non-essential in this acute/comfort-care setting.

### Mesmo fármaco, ação diferente

| Fármaco | RemedIA | Baseline |
| --- | --- | --- |
| aspirin | manter | suspender |
| co-beneldopa | substituir | suspender |
| paracetamol | substituir | suspender |
| simvastatin | substituir | suspender |

## 09_22 — Medication Sick Day Guidance (in nursing home resident)

### Ações

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 6 | 10 |
| suspender | 6 | 1 |
| reduzir dose | 0 | 2 |
| aumentar dose | 0 | 0 |
| substituir | 1 | 0 |
| iniciar | 2 | 1 |
| outra | 0 | 0 |
| Total | 15 | 14 |

### Keeps e criatividade

| Algoritmo | Propositivas | Keeps | Propositivas por keep | Parcela propositiva % |
| --- | --- | --- | --- | --- |
| RemedIA | 9 | 6 | 1.5 | 60.0 |
| Baseline | 4 | 10 | 0.4 | 28.6 |

### Acurácia

| Algoritmo | N | Sem nota | Correto | Aceitável | Debatível | Incorreto | Correto % | Aceitável % | Debatível % | Incorreto % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RemedIA | 15 | 0 | 9 | 4 | 1 | 1 | 60.0 | 26.7 | 6.7 | 6.7 |
| Baseline | 14 | 0 | 6 | 5 | 3 | 0 | 42.9 | 35.7 | 21.4 | 0.0 |

### Duplicações

| Algoritmo | Duplicações |
| --- | --- |
| RemedIA | 0 |
| Baseline | 1 |

Resposta repetida, defeito do modelo. A linha continua contada na tabela de ações.

- Baseline. Linhas 5, 6 repetem a frase "Continue while on opioid therapy, but step down/titrate according to bowel frequency and potential opioid dose reduction.". Alvos: Macrogol 3350 sachets; Senna 7.5mg tablets. É a mesma resposta copiada em mais de uma linha.

O RemedIA fez 9 ações propositivas e 6 keeps (1.5 por keep). o baseline fez 4 e 10 (0.4 por keep). no RemedIA, Correto 9, Aceitável 4, Debatável 1, Incorreto 1 (acerto amplo 86.7%, erro 6.7%). no baseline, Correto 6, Aceitável 5, Debatável 3, Incorreto 0 (acerto amplo 78.6%, erro 0.0%). nas 2 explicações da mesma ação, o detalhe ficou com o RemedIA em 1, com o baseline em 0 e empatou em 1.

### Explicações da mesma ação

**aspirin, iniciar.** Detalhe: Empate. Os dois iniciam ácido acetilsalicílico 75 mg na doença isquêmica. Nenhum dos dois explica a idade de 83 anos, que é o ponto que torna a indicação debatível.

- RemedIA, linha 13 (Debatable): Patient has established Ischaemic Heart Disease receiving atorvastatin and ramipril, but lacks guideline-directed antiplatelet therapy for secondary prevention. Initiating low-dose aspirin 75mg daily provides essential antiplatelet coverage to reduce the risk of atherothrombotic events, recurrent myocardial infarction, and cardiovascular mortality, fulfilling an uncovered distinct therapeutic role alongside lipid-lowering and ACE inhibitor therapy. Clopidogrel was considered as an alternative non-charted option, but aspirin is standard first-line secondary prevention.
- Baseline, linha 1 (Debatable): Initiate aspirin 75mg dispersible/gastro-resistant tablets one tablet daily for secondary prevention of ischaemic heart disease.

**prochlorperazine, suspender.** Detalhe: RemedIA. Os dois suspendem porque a náusea aguda passou. O RemedIA acrescenta que a paciente come, e nomeia sedação com mirtazapina, hipotensão com tansulosina e efeito extrapiramidal.

- RemedIA, linha 12 (Correct): Prochlorperazine was prescribed for acute illness with nausea and vomiting without a continuing or documented medical indication. The patient is eating normally, and continuing this unnecessary therapy exposes this frail older resident to risks of additive CNS depression with mirtazapine, orthostatic hypotension with tamsulosin, and extrapyramidal adverse effects. Discontinuing prochlorperazine resolves the unnecessary therapy and mitigates fall and sedation risks.
- Baseline, linha 2 (Correct): Discontinue prochlorperazine as the acute episode of nausea and vomiting has resolved.

### Mesmo fármaco, ação diferente

| Fármaco | RemedIA | Baseline |
| --- | --- | --- |
| co-codamol | suspender | reduzir dose |
| dapagliflozin | suspender | manter |
| furosemide | substituir | manter |
| lansoprazole | suspender | reduzir dose |
| macrogol | suspender | manter |
| senna | suspender | manter |

## 09_23 — Osteoporosis and risk of falls

### Ações

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 10 | 9 |
| suspender | 2 | 3 |
| reduzir dose | 0 | 1 |
| aumentar dose | 0 | 1 |
| substituir | 2 | 0 |
| iniciar | 1 | 0 |
| outra | 0 | 0 |
| Total | 15 | 14 |

### Keeps e criatividade

| Algoritmo | Propositivas | Keeps | Propositivas por keep | Parcela propositiva % |
| --- | --- | --- | --- | --- |
| RemedIA | 5 | 10 | 0.5 | 33.3 |
| Baseline | 5 | 9 | 0.6 | 35.7 |

### Acurácia

| Algoritmo | N | Sem nota | Correto | Aceitável | Debatível | Incorreto | Correto % | Aceitável % | Debatível % | Incorreto % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RemedIA | 15 | 0 | 9 | 3 | 2 | 1 | 60.0 | 20.0 | 13.3 | 6.7 |
| Baseline | 14 | 0 | 7 | 5 | 1 | 1 | 50.0 | 35.7 | 7.1 | 7.1 |

### Duplicações

| Algoritmo | Duplicações |
| --- | --- |
| RemedIA | 0 |
| Baseline | 0 |

O RemedIA fez 5 ações propositivas e 10 keeps (0.5 por keep). o baseline fez 5 e 9 (0.6 por keep). no RemedIA, Correto 9, Aceitável 3, Debatável 2, Incorreto 1 (acerto amplo 80.0%, erro 6.7%). no baseline, Correto 7, Aceitável 5, Debatável 1, Incorreto 1 (acerto amplo 85.7%, erro 7.1%). nas 1 explicações da mesma ação, o detalhe ficou com o RemedIA em 1, com o baseline em 0 e empatou em 0.

### Explicações da mesma ação

**devils, suspender.** Detalhe: RemedIA. Os dois suspendem a garra-do-diabo pelo sangramento com a varfarina. O RemedIA também explica a acidez contra o lansoprazol e a analgesia que já existe com paracetamol e diclofenaco.

- RemedIA, linha 12 (Correct): Devil's Claw provides redundant analgesic therapy alongside paracetamol and topical diclofenac for osteoarthritis. Furthermore, it stimulates gastric acid production, directly antagonising lansoprazole and worsening active dyspepsia, while also interacting with warfarin to increase bleeding risk. Discontinuing Devil's Claw eliminates redundant therapy, reduces gastrointestinal irritation, and resolves significant drug-drug interaction risks without compromising pain control.
- Baseline, linha 2 (Correct): Discontinue use immediately due to potential drug interactions and bleeding risks with warfarin.

### Mesmo fármaco, ação diferente

| Fármaco | RemedIA | Baseline |
| --- | --- | --- |
| alendronic | substituir | suspender |
| calcium | substituir | manter |
| diclofenac | manter | suspender |
| paracetamol | manter | aumentar dose |
| zopiclone | suspender | reduzir dose |

## 09_24 — Palliative Care (Cardiovascular)

### Ações

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 10 | 10 |
| suspender | 2 | 9 |
| reduzir dose | 3 | 1 |
| aumentar dose | 4 | 1 |
| substituir | 3 | 1 |
| iniciar | 1 | 2 |
| outra | 0 | 0 |
| Total | 23 | 24 |

### Keeps e criatividade

| Algoritmo | Propositivas | Keeps | Propositivas por keep | Parcela propositiva % |
| --- | --- | --- | --- | --- |
| RemedIA | 13 | 10 | 1.3 | 56.5 |
| Baseline | 14 | 10 | 1.4 | 58.3 |

### Acurácia

| Algoritmo | N | Sem nota | Correto | Aceitável | Debatível | Incorreto | Correto % | Aceitável % | Debatível % | Incorreto % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RemedIA | 23 | 0 | 9 | 3 | 6 | 5 | 39.1 | 13.0 | 26.1 | 21.7 |
| Baseline | 24 | 0 | 18 | 3 | 3 | 0 | 75.0 | 12.5 | 12.5 | 0.0 |

### Duplicações

| Algoritmo | Duplicações |
| --- | --- |
| RemedIA | 0 |
| Baseline | 0 |

O RemedIA fez 13 ações propositivas e 10 keeps (1.3 por keep). o baseline fez 14 e 10 (1.4 por keep). no RemedIA, Correto 9, Aceitável 3, Debatável 6, Incorreto 5 (acerto amplo 52.2%, erro 21.7%). no baseline, Correto 18, Aceitável 3, Debatável 3, Incorreto 0 (acerto amplo 87.5%, erro 0.0%). nas 4 explicações da mesma ação, o detalhe ficou com o RemedIA em 1, com o baseline em 0 e empatou em 3.

### Explicações da mesma ação

**diazepam, suspender.** Detalhe: Empate. Os dois retiram o diazepam regular pela sedação com opioide. O RemedIA cita DPOC e pregabalina; o baseline, o desmame e a possibilidade de uma dose baixa se necessário para ansiedade.

- RemedIA, linha 11 (Correct): Diazepam (False) has no documented clinical indication and carries a severe risk of additive central nervous system and respiratory depression, particularly in the context of underlying COPD and concurrent therapy with opioids (morphine) and pregabalin. Discontinuing diazepam eliminates this unnecessary risk without compromising therapy for any diagnosed condition.
- Baseline, linha 5 (Correct): Taper and discontinue regular daily dosing due to excessive sedation and fall risk when combined with escalating opioids; consider low-dose PRN if indicated for anxiety.

**folic, suspender.** Detalhe: Empate. Os dois suspendem ácido fólico sem indicação, para reduzir comprimidos. A disfagia citada pelo RemedIA não muda a ação.

- RemedIA, linha 12 (Correct): Folic acid 5mg daily has no documented clinical indication (such as folate deficiency anemia or methotrexate therapy) in this patient with advanced metastatic lung cancer. Discontinuing it safely reduces pill burden, polypharmacy, and swallowing discomfort given her poor oral intake and dysphagia.
- Baseline, linha 7 (Correct): Discontinue the medication due to lack of ongoing indication and to reduce pill burden.

**macrogol, aumentar dose.** Detalhe: Empate. Os dois sobem o macrogol para duas doses ao dia na constipação com morfina. O RemedIA nomeia amitriptilina e solifenacina; o baseline diz a posologia com mais clareza, um sachê duas vezes ao dia.

- RemedIA, linha 15 (Correct): Macrogol 3350 at 1 sachet (13.125 g) daily is insufficient to prevent and treat constipation in this patient with active constipation receiving regular and PRN morphine, amitriptyline, and solifenacin. Dosage format adjusted to grams (26.25 g) to address validation failure: recommended_dosage: Dosage format unclear - missing units or frequency: '2 sachets'. Increasing to 26.25 g (2 sachets) daily provides effective osmotic laxation alongside charted senna.
- Baseline, linha 10 (Correct): Increase the dose to one sachet twice daily to address ongoing constipation.

**pregabalin, reduzir dose.** Detalhe: RemedIA. Os dois reduzem pela filtração de 40 e pela sedação com opioide. O RemedIA explica o teto: no máximo 300 mg por dia, e por isso 150 mg duas vezes ao dia.

- RemedIA, linha 22 (Correct): Pregabalin 300 mg twice daily (600 mg/day) exceeds recommended renal dosing limits for the patient's eGFR of 40 mL/min/1.73 m2, which restricts the maximum daily dose to 300 mg/day. This excessive dose increases the risk of severe CNS depression, cognitive impairment, and sedation, especially alongside opioids. Reducing pregabalin to 150 mg twice daily (300 mg/day) aligns with renal guidelines to maintain neuropathic analgesia for bone metastases while minimizing toxicity.
- Baseline, linha 16 (Correct): Reduce the dose to 100 mg twice daily (or 150 mg twice daily) to account for renal impairment (eGFR 40 mL/min) and minimize excessive sedation.

### Mesmo fármaco, ação diferente

| Fármaco | RemedIA | Baseline |
| --- | --- | --- |
| alogliptin | manter | suspender |
| amitriptyline | manter | suspender |
| atorvastatin | manter | suspender |
| edoxaban | reduzir dose | manter |
| levothyroxine | aumentar dose | manter |
| metformin | manter | suspender |
| morphine | aumentar dose | suspender, substituir |
| ramipril | reduzir dose | suspender |
| sertraline | substituir | manter |
| solifenacin | substituir | suspender |
| trelegy | substituir | manter |

## 09_25 — Palliative Care – End of Life Care

### Ações

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 5 | 1 |
| suspender | 1 | 11 |
| reduzir dose | 1 | 1 |
| aumentar dose | 0 | 0 |
| substituir | 6 | 0 |
| iniciar | 3 | 3 |
| outra | 0 | 0 |
| Total | 16 | 16 |

### Keeps e criatividade

| Algoritmo | Propositivas | Keeps | Propositivas por keep | Parcela propositiva % |
| --- | --- | --- | --- | --- |
| RemedIA | 11 | 5 | 2.2 | 68.8 |
| Baseline | 15 | 1 | 15.0 | 93.8 |

### Acurácia

| Algoritmo | N | Sem nota | Correto | Aceitável | Debatível | Incorreto | Correto % | Aceitável % | Debatível % | Incorreto % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RemedIA | 16 | 0 | 7 | 4 | 1 | 4 | 43.8 | 25.0 | 6.2 | 25.0 |
| Baseline | 16 | 0 | 15 | 1 | 0 | 0 | 93.8 | 6.2 | 0.0 | 0.0 |

### Duplicações

| Algoritmo | Duplicações |
| --- | --- |
| RemedIA | 0 |
| Baseline | 0 |

O RemedIA fez 11 ações propositivas e 5 keeps (2.2 por keep). o baseline fez 15 e 1 (15.0 por keep). no RemedIA, Correto 7, Aceitável 4, Debatável 1, Incorreto 4 (acerto amplo 68.8%, erro 25.0%). no baseline, Correto 15, Aceitável 1, Debatável 0, Incorreto 0 (acerto amplo 100.0%, erro 0.0%). nas 1 explicações da mesma ação, o detalhe ficou com o RemedIA em 1, com o baseline em 0 e empatou em 0.

### Explicações da mesma ação

**zopiclone, suspender.** Detalhe: RemedIA. O baseline só escreve suspender o medicamento. O RemedIA explica o problema: sem indicação de sono, desempenho muito baixo, saturação de 85% e depressão respiratória com fentanil e morfina.

- RemedIA, linha 6 (Correct): Zopiclone (zopiclone_7p5mg) lacks a documented clinical indication or sleep disorder diagnosis. In this frail patient with poor performance status (AKPS 20%), baseline confusion, hypoxemia (SpO2 85%), and concomitant opioid therapy (fentanyl, morphine), continuing zopiclone poses severe risks of additive CNS and respiratory depression. Discontinuing zopiclone removes unnecessary pharmacotherapy risk without compromising palliative symptom management.
- Baseline, linha 7 (Correct): Discontinue the medication.

### Mesmo fármaco, ação diferente

| Fármaco | RemedIA | Baseline |
| --- | --- | --- |
| fluconazole | substituir | suspender |
| fluoxetine | substituir | suspender |
| ibuprofen | substituir | suspender |
| insulin | manter | suspender, reduzir dose |
| laxido | manter | suspender |
| metoclopramide | manter | suspender |
| morphine | substituir | suspender |
| omeprazole | substituir | suspender |
| paracetamol | substituir | suspender |
| ramipril | reduzir dose | suspender |

## 09_26 — Drug dependency and requests for medication out of hours

### Ações

| Tipo de ação | RemedIA | Baseline |
| --- | --- | --- |
| manter | 0 | 4 |
| suspender | 3 | 3 |
| reduzir dose | 0 | 1 |
| aumentar dose | 1 | 0 |
| substituir | 4 | 0 |
| iniciar | 0 | 1 |
| outra | 0 | 0 |
| Total | 8 | 9 |

### Keeps e criatividade

| Algoritmo | Propositivas | Keeps | Propositivas por keep | Parcela propositiva % |
| --- | --- | --- | --- | --- |
| RemedIA | 8 | 0 | — | 100.0 |
| Baseline | 5 | 4 | 1.2 | 55.6 |

### Acurácia

| Algoritmo | N | Sem nota | Correto | Aceitável | Debatível | Incorreto | Correto % | Aceitável % | Debatível % | Incorreto % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RemedIA | 8 | 0 | 4 | 4 | 0 | 0 | 50.0 | 50.0 | 0.0 | 0.0 |
| Baseline | 9 | 0 | 5 | 1 | 3 | 0 | 55.6 | 11.1 | 33.3 | 0.0 |

### Duplicações

| Algoritmo | Duplicações |
| --- | --- |
| RemedIA | 0 |
| Baseline | 0 |

O RemedIA fez 8 ações propositivas e 0 keeps (sem keep). o baseline fez 5 e 4 (1.2 por keep). no RemedIA, Correto 4, Aceitável 4, Debatável 0, Incorreto 0 (acerto amplo 100.0%, erro 0.0%). no baseline, Correto 5, Aceitável 1, Debatável 3, Incorreto 0 (acerto amplo 66.7%, erro 0.0%). nas 2 explicações da mesma ação, o detalhe ficou com o RemedIA em 1, com o baseline em 0 e empatou em 1.

### Explicações da mesma ação

**gabapentin, suspender.** Detalhe: Empate. Os dois suspendem a gabapentina porque ela duplica a pregabalina e aumenta a toxicidade com opioide. O mecanismo e a ação são os mesmos.

- RemedIA, linha 2 (Correct): Gabapentin represents duplicate gabapentinoid therapy alongside concurrent pregabalin for chronic hip and back pain with radiculopathy. Co-prescribing two distinct alpha-2-delta ligands provides redundant mechanism of action while substantially heightening risks of severe CNS and respiratory depression, particularly in the context of concurrent opioid therapy (methadone, co-codamol, tramadol). Discontinuing gabapentin eliminates therapeutic duplication while maintaining pregabalin for neuropathic pain control.
- Baseline, linha 1 (Correct): Discontinue therapy (therapeutic duplication with pregabalin; high risk of toxicity).

**tramadol, suspender.** Detalhe: RemedIA. Os dois retiram o tramadol pelo opioide acumulado e pelo risco de serotonina. O RemedIA nomeia metadona, co-codamol, sertralina e amitriptilina, e inclui a convulsão. O baseline descreve o desmame.

- RemedIA, linha 3 (Correct): Tramadol represents redundant opioid therapy alongside co-codamol and methadone, compounding risks of central nervous system and respiratory depression, serotonin syndrome (with sertraline and amitriptyline), and seizures. Chronic hip and back pain remains covered by ongoing analgesics. Discontinuing tramadol eliminates unnecessary opioid duplication and significant toxicological hazards without compromising baseline coverage.
- Baseline, linha 3 (Correct): Discontinue therapy via a planned taper to reduce additive opioid burden, respiratory depression risk, and serotonin syndrome risk.

### Mesmo fármaco, ação diferente

| Fármaco | RemedIA | Baseline |
| --- | --- | --- |
| amitriptyline | substituir | reduzir dose |
| bisacodyl | suspender | manter |
| co-codamol | substituir | suspender |
| methadone | substituir | manter |
| pregabalin | aumentar dose | manter |
| sertraline | substituir | manter |

## Review geral

A soma usa cada linha uma vez. Não é a média das porcentagens de cada caso.

### Criatividade

| Algoritmo | Ações | Propositivas | Keeps | Propositivas por keep | Parcela propositiva % |
| --- | --- | --- | --- | --- | --- |
| RemedIA | 305 | 213 | 92 | 2.3 | 69.8 |
| Baseline | 306 | 193 | 113 | 1.7 | 63.1 |

O RemedIA é mais criativo neste critério: 2.3 ações propositivas por keep no RemedIA e 1.7 no baseline. O RemedIA propõe mais mudanças e mantém menos linhas.

### Acurácia

| Algoritmo | N | Sem nota | Correto | Aceitável | Debatível | Incorreto | Correto % | Aceitável % | Debatível % | Incorreto % | Acerto amplo % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RemedIA | 305 | 0 | 156 | 45 | 49 | 55 | 51.1 | 14.8 | 16.1 | 18.0 | 65.9 |
| Baseline | 306 | 0 | 203 | 57 | 30 | 16 | 66.3 | 18.6 | 9.8 | 5.2 | 85.0 |

No conjunto, o acerto amplo do baseline é 85.0% e o do RemedIA é 65.9%. Correto é 51.1% no RemedIA e 66.3% no baseline. Aceitável é 14.8% e 18.6%. Debatível é 16.1% e 9.8%. Incorreto é 18.0% e 5.2%. A linha sem nota do RemedIA entra no N e fica fora das taxas.

### Detalhe das explicações

| Veredito | Pares |
| --- | --- |
| RemedIA | 28 |
| Baseline | 10 |
| Empate | 29 |

Há 67 ações iguais, fora de keep, em que os dois escreveram uma recomendação sobre o mesmo fármaco. O detalhe ficou com o RemedIA em 28, com o baseline em 10 e empatou em 29. O placar mede quem identificou o problema e quem justificou a ação com dose, modo de retirada ou um fato deste paciente. Não é a nota do especialista, que está na acurácia.

### Duplicações

O RemedIA repetiu 0 respostas. O baseline repetiu 4. Essas linhas continuam dentro das ações e dos keeps.

### Em quais casos cada algoritmo foi melhor

Um caso entra quando os dois têm denominador: pelo menos uma linha na criatividade e na acurácia, e pelo menos um par não-keep no detalhe. `09_15` fica de fora dos três eixos porque o RemedIA não tem linhas. Criatividade: mais ações propositivas por keep; se os dois não têm keep, vale a parcela propositiva. Acurácia: maior taxa de Correto + Aceitável, e menor taxa de Incorreto no empate dessa taxa. Detalhe: mais pares do caso. Os três eixos não se fundem num vencedor só.

**Criatividade.**

- RemedIA (14): 09_01, 09_02, 09_04, 09_05, 09_06, 09_08, 09_09, 09_10, 09_11, 09_17, 09_18, 09_20, 09_22, 09_26
- Baseline (10): 09_03, 09_07, 09_12, 09_13, 09_14, 09_19, 09_21, 09_23, 09_24, 09_25
- Empate (1): 09_16

**Acurácia.**

- RemedIA (5): 09_01, 09_04, 09_14, 09_22, 09_26
- Baseline (17): 09_02, 09_03, 09_05, 09_06, 09_07, 09_08, 09_10, 09_11, 09_12, 09_17, 09_18, 09_19, 09_20, 09_21, 09_23, 09_24, 09_25
- Empate (3): 09_09, 09_13, 09_16

**Detalhe.**

- RemedIA (14): 09_02, 09_07, 09_08, 09_10, 09_11, 09_12, 09_17, 09_20, 09_21, 09_22, 09_23, 09_24, 09_25, 09_26
- Baseline (1): 09_06
- Empate (5): 09_01, 09_03, 09_04, 09_18, 09_19

Criatividade: o RemedIA foi melhor em 14 casos, o baseline em 10 e houve empate em 1. Acurácia: o RemedIA foi melhor em 5 casos, o baseline em 17 e houve empate em 3. Detalhe: o RemedIA foi melhor em 14 casos, o baseline em 1 e houve empate em 5.

