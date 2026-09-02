"""Expressoes usadas pela bateria de exemplos."""

from .validator import is_balanced

BALANCED_EXPRESSIONS = [
    "(a + b)",
    "{[a * (b + c)]}",
    "a + {b - [c * d]}",
    "{[a * b], (a + b)}",
]

UNBALANCED_EXPRESSIONS = [
    "a + (b",
    "a + {b - [c * d}",
]


def run_examples() -> None:
    """Imprime o resultado dos exemplos balanceados e nao balanceados."""
    print("=== Expressoes que deveriam estar BALANCEADAS ===")
    for expression in BALANCED_EXPRESSIONS:
        result = is_balanced(expression)
        status = "OK" if result else "FALHOU"
        print(f"[{status}] '{expression}' -> {result}")

    print("\n=== Expressoes que deveriam estar NAO BALANCEADAS ===")
    for expression in UNBALANCED_EXPRESSIONS:
        result = is_balanced(expression)
        status = "OK" if not result else "FALHOU"
        print(f"[{status}] '{expression}' -> {result}")
