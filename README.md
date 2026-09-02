# 📐 Verificador de Balanceamento de Expressões

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![Status](https://img.shields.io/badge/status-concluído-brightgreen)
![License](https://img.shields.io/badge/licença-MIT-lightgrey)

Programa em Python que verifica se uma expressão matemática contendo
parênteses `()`, colchetes `[]` e chaves `{}` está corretamente
balanceada, utilizando a estrutura de dados **pilha (stack)**.

Desenvolvido como atividade prática da disciplina de **Estrutura de
Dados Lineares** — Tecnologia em Análise e Desenvolvimento de Sistemas
(TADS), IFRN Campus Pau dos Ferros.

---

## 📋 Sumário

- [Sobre o projeto](#-sobre-o-projeto)
- [Regras de balanceamento](#-regras-de-balanceamento)
- [Algoritmo](#-algoritmo)
- [Como executar](#-como-executar)
- [Exemplos de uso](#-exemplos-de-uso)
- [Estrutura do projeto](#-estrutura-do-projeto)
- [Testes](#-testes)
- [Complexidade](#-complexidade)
- [Possíveis melhorias](#-possíveis-melhorias)
- [Autor](#-autor)
- [Licença](#-licença)

---

## 📖 Sobre o projeto

Uma expressão matemática é considerada **balanceada** quando todo
símbolo de abertura possui um fechamento correspondente, respeitando a
ordem correta de fechamento. Este projeto implementa essa verificação
de forma eficiente utilizando o princípio **LIFO** (*Last In, First
Out*) da pilha.

## ✅ Regras de balanceamento

Uma expressão está balanceada se:

1. Todo `(`, `[` ou `{` possui um fechamento correspondente (`)`, `]`, `}`).
2. Os fechamentos ocorrem na ordem correta.

| Expressão | Resultado |
|---|:---:|
| `(a + b)` | ✔️ Balanceada |
| `{[a * (b + c)]}` | ✔️ Balanceada |
| `a + {b - [c * d]}` | ✔️ Balanceada |
| `a + (b` | ❌ Não balanceada |
| `a + {b - [c * d}` | ❌ Não balanceada |

## ⚙️ Algoritmo

1. Percorre a expressão da esquerda para a direita.
2. Símbolo de abertura → empilha (`push`).
3. Símbolo de fechamento → desempilha (`pop`) o topo e verifica se
   corresponde ao tipo de abertura esperado.
   - Pilha vazia no momento do fechamento → **desbalanceada**.
   - Símbolo do topo não corresponde → **desbalanceada**.
4. Ao final, pilha vazia → **balanceada**; pilha não vazia → **desbalanceada**.

```python
def esta_balanceada(expressao: str) -> bool:
    pilha = []
    pares = {')': '(', ']': '[', '}': '{'}

    for c in expressao:
        if c in pares.values():
            pilha.append(c)
        elif c in pares:
            if not pilha or pilha.pop() != pares[c]:
                return False

    return len(pilha) == 0
```

## 🚀 Como executar

**Pré-requisitos:** Python 3.6+ (sem dependências externas).

```bash
git clone https://github.com/seu-usuario/verificador-balanceamento.git
cd verificador-balanceamento
python3 balanceador.py
```

## 💻 Exemplos de uso

**Modo interativo (terminal):**

```
>> (a + b)
Resultado: expressão BALANCEADA ✔
>> a + (b
Resultado: expressão NÃO BALANCEADA ✘
```

**Como módulo importável:**

```python
from balanceador import esta_balanceada

esta_balanceada("(a + b)")            # True
esta_balanceada("a + {b - [c * d}")   # False
```

## 📁 Estrutura do projeto

```
.
├── balanceador.py   # Código-fonte principal (função + CLI)
├── README.md        # Documentação do repositório
└── LICENSE           # Licença do projeto (opcional)
```

## 🧪 Testes

Testes embutidos executáveis via comando `testar` no modo interativo,
cobrindo casos balanceados e não balanceados. Sugestão para expansão:
migrar para `unittest` ou `pytest`:

```python
import unittest
from balanceador import esta_balanceada

class TestBalanceamento(unittest.TestCase):
    def test_balanceadas(self):
        self.assertTrue(esta_balanceada("(a + b)"))
        self.assertTrue(esta_balanceada("{[a * (b + c)]}"))

    def test_nao_balanceadas(self):
        self.assertFalse(esta_balanceada("a + (b"))
        self.assertFalse(esta_balanceada("a + {b - [c * d}"))

if __name__ == "__main__":
    unittest.main()
```

## ⏱️ Complexidade

| Complexidade | Valor |
|---|---|
| Tempo | O(n) |
| Espaço | O(n) — pior caso: todos os caracteres são aberturas |

## 🔧 Possíveis melhorias

- [ ] Ignorar símbolos de agrupamento dentro de strings de texto.
- [ ] Reportar a posição (índice) do erro de balanceamento.
- [ ] Suporte a outros pares de símbolos (`<`, `>`).
- [ ] Cobertura de testes com `pytest` e integração contínua (CI).

## 👤 Autor

**Klaywin Ryan Aquino Dias**
Estudante de Tecnologia em Análise e Desenvolvimento de Sistemas — IFRN Campus Pau dos Ferros

## 📄 Licença

Este projeto está sob a licença MIT — veja o arquivo `LICENSE` para mais detalhes.
