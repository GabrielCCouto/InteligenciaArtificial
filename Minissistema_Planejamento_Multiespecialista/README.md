# Torre de Hanói – Solver Ótimo em Python

Este repositório contém duas implementações diferentes para resolver o clássico quebra‑cabeça **Torre de Hanói**, comparando abordagens de **planejamento (GPS/STRIPS)** e o **algoritmo recursivo clássico**.

---

## 📖 Visão Geral

- 🎯 **Objetivo**: Mover N discos de uma haste (A) para outra (C), obedecendo às regras (um disco por vez; nunca colocar maior sobre menor).  
- ⚖️ **Desafio**: Encontrar **um caminho** de forma automática.

---

## 🚀 Implementações

| Método | Caminho Ótimo? | Complexidade | Uso | Arquivo |
|---------|:-------------:|:------------:|:---:|:-------|
| GPS (STRIPS) | ❌ | Exponencial (3ⁿ) | `python Plano_Hanoi_GPS.py` | `Plano_Hanoi_GPS.py` |
| Recursivo Clássico | ✅ | Exponencial (2ⁿ) | `python Plano_Hanoi_recurssivo.py` | `Plano_Hanoi_recurssivo.py` |

---

## 📈 Complexidades

| N (discos) | Movimentos Ótimos | Estados Possíveis (3ⁿ) |
|------------|-------------------|------------------------|
| 3          | 7                 | 27                     |
| 4          | 15                | 81                     |
| 5          | 31                | 243                    |

---

## ✏️ Exemplo de Saída (N=4, Recurssivo)

```
1 - mover disco 1 de A para C
2 - mover disco 2 de A para B
3 - mover disco 1 de C para B
4 - mover disco 3 de A para C
5 - mover disco 1 de B para A
6 - mover disco 2 de B para C
7 - mover disco 1 de A para C
8 - mover disco 4 de A para C
...
15 - mover disco 1 de A para C
```

---

## 📚 Diferença entre GPS e Recurssivo

- GPS encontra **qualquer** caminho válido, mas **não garante** o número mínimo de movimentos.

- O algoritmo recursivo produz diretamente o **caminho ótimo** em O(2ⁿ) de tempo e O(n) de memória.

---