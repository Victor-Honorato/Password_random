import random
import string

# Função para gerar uma senha aleatória com o tamanho especificado
def gerar_senha(tamanho):
    # Define os caracteres possíveis para a senha
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # Usa list comprehension para criar a senha aleatória
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Função principal que lida com a entrada do usuário e gera as senhas
def main():
    try:
        # Solicita ao usuário o número de senhas desejadas
        quantidade_senhas = int(input("Digite o número de senhas desejadas: "))
        # Solicita ao usuário o comprimento desejado para cada senha
        tamanho_senha = int(input("Digite o comprimento desejado para cada senha: "))

        # Verifica se os valores inseridos são válidos
        if quantidade_senhas <= 0 or tamanho_senha <= 0:
            print("Por favor, insira valores válidos para o número e o tamanho das senhas.")
            return

        # Gera uma lista de senhas usando list comprehension
        senhas = [gerar_senha(tamanho_senha) for _ in range(quantidade_senhas)]

        # Exibe as senhas geradas
        print("\nSenhas geradas:")
        for i, senha in enumerate(senhas, start=1):
            print(f"Senha {i}: {senha}")

    except ValueError:
        print("Por favor, insira valores numéricos para o número e o tamanho das senhas.")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
