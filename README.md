# Lista 2: Algebra Linear Computacional

## Aluno: Lucas Amaral

**Exercício 3:**

Faça um programa de computador que transforme um sinal x ∈ R n em uma aproximação \~x, contida em um subespaço U. Dada uma base B para este subespaço, obtenha \[x]B ∈ R^k, onde k = dim (U).

**Instalação dos pacotes**

Criar seu ambiente virtual.

```
pip install -r requirements.txt
```

**Da implementação**
A implementação é bem simples. 
Na main:
1) Toma o vetor x que representa o sinal. Há exemplos 3-dimensionais no código.
2) Toma a base B, checa se a base tem mais dimensões que x.
3) Checa se a base é ortonormal:
        --- Se não: aplica Gram-Schimidt para encontrar a base ortonormal
        --- Se sim: continua
4) Aplica a operação matrix-vetor de B^T @ x, chamado x_B
5) Aplica a operação matrix-vetor de B @ x_B para encontrar a aproximação de x, x_approx.


**Nota:** Funções auxiliares: *check_orthonormal* e *gram_schmidt*.
    


