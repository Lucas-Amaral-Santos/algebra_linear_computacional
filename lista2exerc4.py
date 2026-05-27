import numpy as np

"""
Exercício 4: Faça um programa de computador que encontre uma aproximação de um dado 
x ∈ R^n obtida pela consideração de apenas os k maiores coeficientes de [x]B. k < n  ́
e um inteiro positivo fornecido como parâmetro de entrada, e B deve ser uma base de 
wavelets de Haar, ou de séries de Fourier.

Aluno: Lucas Amaral
"""
#
#  FUNÇÕES AUXILIARES
#

# Função para transformar um vetor para a base de Fourier
def fourier_transform(x, inverse=False):
    n = len(x)
    F = np.zeros((n, n), dtype=complex)
    for k in range(n):
        for j in range(n):
            F[k, j] = np.exp(-2j * np.pi * k * j / n)
    if inverse:
        F = np.conjugate(np.transpose(F)) / n
    return np.dot(F, x) 

# Função para calcular a transformada de Fourier usando a fórmula direta (sem matriz)
def fourier_transform_formula(x, inverse=False):
    n = len(x)
    F = np.zeros(n, dtype=complex)
    for k in range(n):
        if inverse:
            F[k] = sum(x[j] * np.exp(2j * np.pi * k * j / n) for j in range(n)) / n
        else:
            F[k] = sum(x[j] * np.exp(-2j * np.pi * k * j / n) for j in range(n))
    return F

def get_k_bigger_coefficients(coefficients, k):
    # Setar para 0 os coeficientes que não estão entre os k maiores
    sorted_indices = np.argsort(np.abs(coefficients))  # Índices dos coeficientes ordenados por valor absoluto
    largest_indices = sorted_indices[-k:]  # fatia de k para os maiores e retorna índices dos k maiores coeficientes
    coefficients_compressed = np.zeros_like(coefficients)
    coefficients_compressed[largest_indices] = coefficients[largest_indices]  # Mantendo apenas os k maiores coeficientes, os outros são setados para 0
    
    return coefficients_compressed

#
#  FIM FUNÇÕES AUXILIARES
#

def main(x, base_type, k):
    
    print(f"Sinal original x: {x}\n")    
    
    if base_type == "fourier":
        coefficients = fourier_transform(x)  # Calculando os coeficientes de x na base de Fourier com matriz
        # coefficients = fourier_transform_formula(x)  # Calculando os coeficientes de x na base de Fourier usando a fórmula direta
    
    print(f"Coeficientes de x na base {base_type}: {coefficients}\n")
    
    coefficients_compressed = get_k_bigger_coefficients(coefficients, k)
    print(f"Coeficientes de x na base {base_type} após compressão (mantendo apenas os {k} maiores): {coefficients_compressed}\n")
    
    # Retornando a base de Fourier ou Haar para o domínio canônico
    if base_type == "fourier":
        # Para a base de Fourier, a matriz inversa é a conjugada transposta dividida por n
        approximation = fourier_transform(coefficients_compressed, inverse=True)  # Aproximação de x usando os k maiores coeficientes na base de Fourier

    print(f"Aproximação de x usando os {k} maiores coeficientes: {approximation}\n")
    
    nnz = np.sum(np.abs(coefficients_compressed) > 1e-10)  # tolerância para erros de ponto flutuante
    print(f"Non-zeros: {nnz} of {len(x)} (compression: {(1 - nnz/len(x))*100:.2f}%)")

if __name__ == "__main__":    
    # PARÂMETROS DE ENTRADA
    base_type = "fourier"  # Opções: "haar" ou "fourier"
    k = 1  # Número de maiores coeficientes a considerar
    
    # Definindo o sinal x na base canônica
    # Exemplo com um sinal senoidal com 8 pontos
    n = 8
    t = np.arange(n)
    x = np.cos(2 * np.pi * t / n)  # Sinal
    
    print("=== k=1 (apenas o maior coeficiente) ===")
    main(x, "fourier", k=1)

    print("=== k=2 (os dois maiores — deve reconstruir x exatamente) ===")
    main(x, "fourier", k=2)