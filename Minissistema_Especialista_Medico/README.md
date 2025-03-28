# Trabalho - Especialista Médico

## Pontos a serem feitos
- [x] Levantamento de Doenças
- [x] Levantamento de Sintomas
- [x] Levantamento de Regras
- [ ] Confiança de cada sintoma nas regras
- [ ] Criação do sistema
- [ ] Validação do sistema

## Descrição do problema

- Desenvolver um sistema especialista capaz de fornecer diagnósticos iniciais de doenças comuns, levando em consideração os principais sintomas entre eles.

## Doenças Levantadas

| Doença               | Descrição |
|--------------------|-----------|
| **Gripe**         | Infecção viral que causa febre, tosse, dor no corpo e fadiga. |
| **Resfriado Comum** | Infecção viral leve que afeta o trato respiratório superior, causando espirros, coriza e nariz entupido. |
| **Covid-19**      | Doença viral causada pelo SARS-CoV-2, com sintomas como febre, tosse seca, perda de olfato e falta de ar. |
| **Dengue**        | Infecção viral transmitida pelo mosquito Aedes aegypti, caracterizada por febre alta, dores no corpo e manchas na pele. |
| **Amigdalite**    | Inflamação das amígdalas, causando dor intensa na garganta, dificuldade para engolir e febre. |
| **Gastrite**      | Inflamação do revestimento do estômago, resultando em dor abdominal, azia e náusea. |
| **Infecção Urinária** | Infecção bacteriana que afeta o trato urinário, causando ardência ao urinar e dor no baixo ventre. |

## Sintomas Levantados  

| Sintoma            | Descrição |
|--------------------|-----------|
| **Febre**         | Aumento anormal da temperatura corporal, comum em infecções virais e bacterianas. |
| **Tosse seca**    | Tosse sem produção de muco, característica de infecções respiratórias. |
| **Perda de olfato e paladar** | Dificuldade ou incapacidade de sentir cheiros e sabores, comum na Covid-19. |
| **Dor muscular intensa** | Dores fortes nos músculos, sintoma marcante da dengue. |
| **Dor atrás dos olhos** | Sensação de pressão ou dor na região ocular, frequente na dengue. |
| **Dor de garganta** | Irritação ou inflamação na garganta, comum na amigdalite e gripe. |
| **Dificuldade para engolir** | Sensação de dor ou obstrução ao engolir alimentos, associada à amigdalite. |
| **Coriza**        | Corrimento nasal transparente, comum em gripes e resfriados. |
| **Nariz entupido** | Obstrução nasal, dificultando a respiração pelo nariz. |
| **Espirros**      | Reflexo involuntário causado por irritação nasal, comum em resfriados e alergias. |
| **Cansaço**       | Sensação de fadiga e fraqueza, comum em infecções virais. |
| **Ardência ao urinar** | Sensação de queimação ao urinar, característica de infecção urinária. |
| **Urina escura**  | Urina de coloração mais intensa ou com odor forte, indicando possível infecção. |
| **Azia**         | Sensação de queimação no estômago, comum na gastrite. |
| **Náusea**       | Sensação de enjoo ou vontade de vomitar, presente em gastrite e infecções. |

## Regras do Sistema  

```
REGRA 01: SE febre E tosse seca E perda de olfato/paladar
          ENTÃO suspeita de Covid-19  

REGRA 02: SE febre E dor muscular intensa E dor atrás dos olhos  
          ENTÃO suspeita de Dengue  

REGRA 03: SE dor intensa na garganta E dificuldade para engolir  
          ENTÃO suspeita de Amigdalite  

REGRA 04: SE nariz entupido E coriza E espirros  
          ENTÃO suspeita de Resfriado Comum  

REGRA 05: SE febre E coriza E dor no corpo  
          ENTÃO suspeita de Gripe  

REGRA 06: SE dor ou queimação no estômago E azia  
          ENTÃO suspeita de Gastrite  

REGRA 07: SE ardência ao urinar E urina escura E necessidade frequente de urinar  
          ENTÃO suspeita de Infecção Urinária  

REGRA 08: SE febre alta repentina E manchas vermelhas na pele  
          ENTÃO forte suspeita de Dengue  

REGRA 09: SE tosse seca E falta de ar  
          ENTÃO suspeita de Covid-19  

REGRA 10: SE febre baixa E leve dor de garganta  
          ENTÃO suspeita de Resfriado Comum  

REGRA 11: SE dor de garganta E febre alta E inchaço nas amígdalas  
          ENTÃO forte suspeita de Amigdalite  

REGRA 12: SE náusea E sensação de estômago cheio  
          ENTÃO suspeita de Gastrite  

REGRA 13: SE nariz entupido E espirros E sem febre  
          ENTÃO suspeita de Alergia Respiratória  

REGRA 14: SE febre moderada E tosse produtiva E dor no peito  
          ENTÃO suspeita de Pneumonia  

REGRA 15: SE febre alta E dor de cabeça intensa E rigidez na nuca  
          ENTÃO suspeita de Meningite  
```


