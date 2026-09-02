"""Ponto de entrada da interface interativa."""

from expression_checker import is_balanced
from expression_checker.examples import run_examples


def main():
    print("Verificador de Balanceamento de Expressões")
    print("Digite uma expressão (ou 'sair' para encerrar, 'testar' para rodar exemplos)\n")

    while True:
        prohibited = input(">> ").strip()

        if prohibited.lower() == "sair":
            break
        elif prohibited.lower() == "testar":
            run_examples()
        else:
            if is_balanced(prohibited):
                print("Resultado: expressão BALANCEADA ")
            else:
                print("Resultado: expressão NÃO BALANCEADA ")


if __name__ == "__main__":
    main()