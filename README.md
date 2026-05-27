# Lista 2: Algebra Linear Computacional

## Aluno: Lucas Amaral

#### **Exercício 3:**

Faça um programa de computador que transforme um sinal x ∈ R n em uma aproximação \~x, contida em um subespaço U. Dada uma base B para este subespaço, obtenha \[x]B ∈ R^k, onde k = dim (U).

**O projeto está disposto publicamente no github no endereço**
```
https://github.com/Lucas-Amaral-Santos/algebra_linear_computacional.git
```


**Instalação dos pacotes**

Criar seu ambiente virtual.

```
pip install -r requirements.txt
```

Executar o código **lista2exerc3.py**

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


**Nota:** Funções auxiliares: *check_orthonormal* e *gram_schmidt*. Tem exemplos de algumas bases B e alguns sinais x.




#### **Exercício 4:**
Faça um programa de computador que encontre uma aproximação de um dado 
x ∈ R^n obtida pela consideração de apenas os k maiores coeficientes de [x]B. k < n  ́
e um inteiro positivo fornecido como parâmetro de entrada, e B deve ser uma base de 
wavelets de Haar, ou de séries de Fourier.

**O projeto está disposto publicamente no github no endereço**
```
https://github.com/Lucas-Amaral-Santos/algebra_linear_computacional.git
```


**Instalação dos pacotes**

Criar seu ambiente virtual.

```
pip install -r requirements.txt
```

Executar o código **lista2exerc4.py**

**Da implementação**
Dos parâmetros (no __init__):
1) Toma um sinal senoidal gerado a partir de n pontos.
2) Toma o k, que filtrgará os k maiores valores do sinal na base de Fourier.
3) Gera uma array de n pontos que será o t dos n pontos 
4) Chama a main que executará a Fourier, tomando como argumento o sinal x gerado, k e o base type (no caso fourier).

Na main:

5) Chama a Fourier transform (pode ser na calculado por uma formula ou pela geração de matriz)
6) Com os coeficientes na nova base, chama a função *get_k_bigger_coefficients*
        6.1) Ordena os valores na nova base
        6.2) Pega os coeficientes
        6.3) Aplica um slice em uma array cópia
        6.4) Filtra os coeficientes remanescentes na cópia
7) Aplica a inversa e volta a base original


**Nota:** Funções auxiliares: *fourier_transform* e *fourier_transform_formula* (duas maneiras implementadas), *get_k_bigger_coefficients*. Tem um exemplo com cosseno com 8 pontos k=1 e k=2.
    


