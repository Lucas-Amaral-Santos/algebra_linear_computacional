import numpy as np

"""
Exercício 3: Faça um programa de computador que transforme um sinal x ∈ R
n em uma aproximação ~x, contida em um subespaço U. Dada uma base B para 
este subespaço, obtenha [x]B ∈ R^k, onde k = dim (U).

Aluno: Lucas Amaral
"""

# Função para verificar se a base é ortonormal
def check_orthonormal(B):
    A = np.dot(B.T, B)
    identity = np.eye(A.shape[0])
    if not np.allclose(A, identity):
        return False
    return True

# Função que toma uma base não ortonormal e retorna uma base ortonormal usando o processo de Gram-Schmidt
def gram_schmidt(B):
    orthonormal_basis = []
    for v in B.T:  # Transpondo para iterar sobre as colunas
        w = v.copy()
        for u in orthonormal_basis:
            w -= np.dot(w, u) * u  # Subtraindo a projeção de w em u
        w_norm = np.linalg.norm(w)  # Calculando a norma de w
        if w_norm > 1e-10:  # Evitando divisão por zero
            orthonormal_basis.append(w / w_norm)  # Normalizando o vetor
    return np.array(orthonormal_basis).T  # Retornando a base ortonormal transposta para manter a mesma estrutura de entrada



def main():
    # Definindo o sinal x na base canônica
    # Exemplo com um sinal de dimensão 3
    x = np.array([3, 1, 4]) 
    x = np.array([2.0, 5.0, 3.0])

    print(f"Sua dimensão é: {len(x)}\n\n")
    
    # Tomando os vetores da base B
    # Exemplo com uma base canônica para um subespaço de dimensão 2 em R^3
    B = np.array([
        [1/np.sqrt(2),  1/np.sqrt(6)],
        [1/np.sqrt(2), -1/np.sqrt(6)],
        [0.0,           2/np.sqrt(6)]
    ])
    
    B = np.array([
        [1.0, 0.0],
        [0.0, 1.0],
        [0.0, 0.0]
    ])
    
    B = np.array([
        [1.0, 1.0],
        [1.0, 0.0],
        [0.0, 1.0]
    ])
    
    if B.shape[1] > x.shape[0]:
        print("A base B tem mais vetores do que a dimensão do sinal x. Por favor, ajuste a base.")
        return
    
    # Checar se a base é ortonormal, se não for, aplicar Gram-Schmidt
    if not check_orthonormal(B):
        print("A base B não é ortonormal. Aplicando Gram-Schmidt...")
        B = gram_schmidt(B)
    else:
        print("A base B é ortonormal.")
        
        
    # Calculando a aproximação ~x
    x_B = np.dot(B.T, x)
    
    x_approx = np.dot(B, x_B)

    print("Sinal original x:", x)
    print("Coordenadas [x]B:", x_B)
    print("Aproximação ~x:", x_approx)

if __name__ == "__main__":
    main()