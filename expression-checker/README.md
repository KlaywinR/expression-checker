# Verificador de Balanceamento de Expressões Matemáticas

Programa em Python que verifica se uma expressão matemática contendo
parênteses `()`, colchetes `[]` e chaves `{}` está corretamente
balanceada, utilizando uma **pilha (stack)** como estrutura de dados.

## Descrição do problema

Uma expressão é considerada **balanceada** quando:

1. Todo símbolo de abertura (`(`, `[`, `{`) possui um fechamento
   correspondente (`)`, `]`, `}`).
2. Os fechamentos ocorrem na ordem correta (o último símbolo aberto
   deve ser o primeiro a ser fechado — lógica LIFO).

### Exemplos

| Expressão | Resultado |
|---|---|
| `(a + b)` | Balanceada |
| `{[a * (b + c)]}` | Balanceada |
| `a + {b - [c * d]}` | Balanceada |
| `a + (b` | Não balanceada (abertura sem fechamento) |
| `a + {b - [c * d}` | Não balanceada (ordem de fechamento incorreta) |

## Estrutura do projeto

```
.
├── main.py          # Ponto de entrada da interface
├── expression_checker/
│   ├── __init__.py   # Exporta a função principal
│   ├── validator.py  # Regra de balanceamento
│   └── examples.py   # Exemplos e bateria de testes
└── README.md        # Este arquivo
```

Essa divisão separa responsabilidades: `validator.py` pode ser reutilizado
em outros programas, enquanto `main.py` cuida apenas da interação com o
usuário.

## Algoritmo (uso da pilha)

1. Percorre a expressão da esquerda para a direita, caractere por
   caractere.
2. **Símbolo de abertura** (`(`, `[`, `{`) → é empilhado.
3. **Símbolo de fechamento** (`)`, `]`, `}`):
   - Se a pilha estiver vazia → expressão desbalanceada
     (fechamento sem abertura correspondente).
   - Caso contrário, desempilha o topo e verifica se ele é o
     símbolo de abertura correspondente ao fechamento atual. Se não
     for → expressão desbalanceada (ordem incorreta).
4. Caracteres que não são símbolos de agrupamento (letras, números,
   operadores, espaços) são ignorados.
5. Ao final da leitura, se a pilha **não estiver vazia**, existem
   aberturas sem fechamento → expressão desbalanceada.
6. Se todas as verificações passarem, a expressão está
   **balanceada**.

**Complexidade:** O(n) de tempo e O(n) de espaço, onde `n` é o
tamanho da expressão (no pior caso, todos os caracteres são
símbolos de abertura e vão para a pilha).

## Como executar

Requisitos: Python 3.6 ou superior (não usa bibliotecas externas).

```bash
cd expression-checker
python main.py
```

O programa entra em modo interativo:

```
Verificador de Balanceamento de Expressões
Digite uma expressão (ou 'sair' para encerrar, 'testar' para rodar exemplos)

>> (a + b)
Resultado: expressão BALANCEADA ✔
>> a + (b
Resultado: expressão NÃO BALANCEADA ✘
>> testar
=== Expressões que deveriam estar BALANCEADAS ===
...
>> sair
```

## Uso como função (importação)

```python
from expression_checker import is_balanced

is_balanced("(a + b)")            # True
is_balanced("a + {b - [c * d}")   # False
```

## Casos de teste incluídos

O programa possui a função `testar_expressoes()`, executável pelo
comando `testar` no modo interativo, que valida:

- Balanceadas: `(a + b)`, `{[a * (b + c)]}`, `a + {b - [c * d]}`, `{[a * b], (a + b)}`
- Não balanceadas: `a + (b`, `a + {b - [c * d}`

> **Observação:** a expressão `{[a * b], (a + b)}` é balanceada segundo
> a regra de pareamento.

## Possíveis extensões

- Ignorar parênteses/colchetes/chaves dentro de strings de texto
  (ex.: `"(exemplo)"` dentro da expressão).
- Indicar a posição (índice) do erro de balanceamento.
- Suporte a outros pares de símbolos (ex.: `<` e `>`).