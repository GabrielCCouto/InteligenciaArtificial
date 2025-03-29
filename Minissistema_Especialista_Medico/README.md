# Trabalho - Especialista Médico

## Pontos a serem feitos

- [x] Levantamento de Doenças
- [x] Levantamento de Sintomas
- [x] Levantamento de Regras
- [x] Confiança de cada sintoma nas regras
- [ ] Criação do sistema
- [ ] Validação do sistema

## Descrição do problema

- Desenvolver um sistema especialista capaz de fornecer diagnósticos iniciais de doenças comuns, levando em consideração
  os principais sintomas entre eles.

## Doenças Levantadas

| Doenças       |
|---------------|
| **Gripe**     |
| **Sinusite**  |
| **Covid-19**  |
| **Dengue**    |
| **Pneumonia** |

## Sintomas Levantados

### Sintomas gerais

| Sintomas                  | Doenças relacionadas                 |
|---------------------------|--------------------------------------|
| Febre                     | Sinusite, Covid-19                   |
| Febre Alta                | Gripe, Dengue, Pneumonia             |
| Dor de Cabeça             | Gripe, Sinusite, Covid-19, Dengue    |
| Dor no Corpo              | Gripe, Dengue                        |
| Tosse                     | Gripe, Sinusite, Covid-19, Pneumonia |
| Dor de Garganta           | Gripe, Covid-19, Pneumonia           |
| Coriza                    | Sinusite, Covid-19                   |
| Catarro                   | Sinusite, Covid-19                   |
| Perda de Olfato           | Sinusite, Covid-19                   |
| Dificuldade para Respirar | Covid-19, Pneumonia                  |
| Dor atrás dos Olhos       | Dengue, Sinusite                     |

### Sintomas específicos

| Sintomas                     | Doenças relacionadas |
|------------------------------|----------------------|
| Pressão na Face              | Sinusite             |
| Perda de Paladar             | Covid-19             |
| Pressão no Peito             | Covid-19             |
| Dor nas Articulações         | Dengue               |
| Manchas Vermelhas no Corpo   | Dengue               |

### Confiança

A confiança de cada doença ficou da seguinte maneira:

| Sintomas                     | Doenças relacionadas                         | CNF |  
|------------------------------|----------------------------------------------|-----|  
| Febre                        | Sinusite, Covid-19, Gripe, Dengue, Pneumonia | 20% |  
| Febre Alta                   | Gripe, Dengue, Pneumonia                     | 40% |  
| Dor de Cabeça                | Gripe, Sinusite, Covid-19, Dengue            | 25% |  
| Dor no Corpo (1)             | Gripe                                        | 40% |  
| Dor no Corpo (2)             | Dengue                                       | 60% | 
| Tosse Seca                   | Gripe, Sinusite, Covid-19, Pneumonia         | 30% |  
| Tosse Produtiva (1)          | Sinusite                                     | 40% |  
| Tosse Produtiva (2)          | Pneumonia                                    | 30% | 
| Dor de Garganta              | Gripe, Covid-19, Pneumonia                   | 20% | 
| Coriza                       | Sinusite, Covid-19, Gripe                    | 30% |  
| Catarro                      | Covid-19, Pneumonia, Gripe                   | 30% |  
| Perda de Olfato              | Sinusite, Covid-19                           | 50% |  
| Dificuldade para Respirar    | Covid-19, Pneumonia                          | 70% |  
| Dor atrás dos Olhos (1)      | Dengue                                       | 70% |  
| Dor atrás dos Olhos (2)      | Sinusite                                     | 60% |  
| Pressão na Face              | Sinusite                                     | 95% |  
| Perda de Paladar             | Covid-19                                     | 95% |  
| Pressão no Peito             | Covid-19                                     | 95% |  
| Dor nas Articulações         | Dengue                                       | 95% |  
| Manchas Vermelhas no Corpo   | Dengue                                       | 95% |  

## Variáveis

| Variável             | Domínio                                                      | Nível         |
|----------------------|--------------------------------------------------------------|---------------|
| temperatura          | {36, 42} em celsius                                          | RAIZ          |
| espirro              | {sim} U {não}                                                | RAIZ          |
| nariz_entupido       | {sim} U {não}                                                | RAIZ          |
| tosse                | {não} U {seca, produtiva}                                    | RAIZ          |
| dificuldade_engolir  | {sim} U {não}                                                | RAIZ          |
| dor_cabeca           | {sim} U {não}                                                | RAIZ          |
| dor_corpo            | {sim} U {não}                                                | RAIZ          |
| dor_articulacao      | {sim} U {não}                                                | RAIZ          |
| pressao_peito        | {sim} U {não}                                                | RAIZ          |
| dificuldade_respirar | {sim} U {não}                                                | RAIZ          |
| perda_olfato         | {sim} U {não}                                                | RAIZ          |
| perda_paladar        | {sim} U {não}                                                | RAIZ          |
| manchas_vermelhas    | {sim} U {não}                                                | RAIZ          |
| dor_olhos            | {sim} U {não}                                                | RAIZ          |
| febre                | {sim} U {não}                                                | INTERMEDIÁRIO |
| febre_alta           | {sim} U {não}                                                | INTERMEDIÁRIO |
| coriza               | {sim} U {não}                                                | INTERMEDIÁRIO |
| catarro              | {sim} U {não}                                                | INTERMEDIÁRIO |
| dor_garganta         | {sim} U {não}                                                | INTERMEDIÁRIO |
| pressao_face         | {sim} U {não}                                                | INTERMEDIÁRIO |
| doenca               | {gripe, sinusite, covid19, dengue, pneumonia} U {indefinido} | FOLHA         |

## Regras do Sistema

```
REGRA 01: SE temperatura <= 37
          ENTÃO febre = não E febre_alta = não

REGRA 02: SE temperatura > 37 E temperatura < 39
          ENTÃO febre = sim E febre_alta = não

REGRA 03: SE temperatura >= 39
          ENTÃO febre = sim E febre_alta = sim

REGRA 04: SE espirro = sim OU nariz_entupido = sim
          ENTÃO coriza = sim

REGRA 05: SE tosse = produtiva
          ENTÃO catarro = sim

REGRA 06: SE tosse = seca OU tosse = produtiva OU dificuldade_engolir = sim
          ENTÃO dor_garganta = sim
          
REGRA 07: SE coriza = sim E dor_olhos = sim
          ENTÃO pressao_face = sim

REGRA 08: SE febre = sim
          ENTÃO doenca = sinusite (20%)
              E doenca = covid19 (20%)
              E doenca = gripe (20%)
              E doenca = dengue (20%)
              E doenca = pneumonia (20%) 

REGRA 09: SE febre_alta = sim
          ENTÃO doenca = gripe (40%)
              E doenca = dengue (40%)
              E doenca = pneumonia (40%)

REGRA 10: SE dor_cabeca = sim
          ENTÃO doenca = gripe (25%)
              E doenca = sinusite (25%)
              E doenca = covid19 (25%)
              E doenca = dengue (25%)

REGRA 11: SE dor_corpo = sim
          ENTÃO doenca = gripe (40%)
              E doenca = dengue (60%)

REGRA 12: SE tosse = seca
          ENTÃO doenca = gripe (30%)
              E doenca = sinusite (30%)
              E doenca = covid19 (30%)
              E doenca = pneumonia (30%)

REGRA 13: SE tosse = produtiva
          ENTÃO doenca = pneumonia (30%)
              E doenca = sinusite (40%)

REGRA 14: SE dor_garganta = sim
          ENTÃO doenca = gripe (20%)
              E doenca = covid19 (20%)
              E doenca = pneumonia (20%)

REGRA 15: SE coriza = sim
          ENTÃO doenca = sinusite (30%)
              E doenca = covid19 (30%)
              E doenca = gripe (30%)

REGRA 16: SE catarro = sim
          ENTÃO doenca = pneumonia (30%)
              E doenca = covid19 (30%)
              E doenca = gripe (30%)

REGRA 17: SE perda_olfato = sim
          ENTÃO doenca = sinusite (50%)
              E doenca = covid19 (50%)

REGRA 18: SE dificuldade_respirar = sim
          ENTÃO doenca = pneumonia (70%)
              E doenca = covid19 (70%)

REGRA 19: SE dor_olhos = sim
          ENTÃO doenca = dengue (70%)
              E doenca = sinusite (60%)
              
REGRA 20: SE pressao_face = sim
          ENTÃO doenca = sinusite (95%)
              
REGRA 21: SE perda_paladar = sim OU pressao_peito = sim
          ENTÃO doenca = covid19 (95%)
              
REGRA 22: SE dor_articulacao = sim OU manchas_vermelhas = sim
          ENTÃO doenca = dengue (95%)

REGRA 23: SE febre = não
           E tosse = não 
           E dor_cabeca = não 
           E dor_corpo = não 
           E dor_articulacao = não 
           E dor_garganta = não 
           E coriza = não 
           E catarro = não 
           E perda_olfato = não 
           E dificuldade_respirar = não 
           E dor_olhos = não
           E pressao_peito = não 
           E perda_paladar = não 
           E manchas_vermelhas = não 
           E pressao_face = não
          ENTÃO doenca = indefinido
```
