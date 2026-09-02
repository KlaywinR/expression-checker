"""Funcoes para verificar o balanceamento de expressoes."""


def is_balanced(expression: str) -> bool:
    """Retorna True quando os delimitadores da expressao estao balanceados."""
    stack = []
    matching_pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    opening_symbols = set(matching_pairs.values())

    for character in expression:
        if character in opening_symbols:
            stack.append(character)
        elif character in matching_pairs:
            if not stack or stack.pop() != matching_pairs[character]:
                return False

    return not stack
