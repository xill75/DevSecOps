# test_script.py

def main():
    print("Iniciando o teste...")

    # Operação matemática simples
    num1 = 5
    num2 = 3
    resultado_esperado = 8
    resultado_obtido = num1 + num2

    # Verifica o resultado
    if resultado_obtido == resultado_esperado:
        print("Teste bem-sucedido! O resultado da soma é correto.")
        return 0  # Código de saída 0 indica sucesso
    else:
        print("Falha no teste. O resultado da soma está incorreto.")
        return 1  # Código de saída 1 indica falha

if __name__ == "__main__":
    exit(main())
