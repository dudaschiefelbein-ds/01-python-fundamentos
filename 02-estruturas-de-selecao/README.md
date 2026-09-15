# 📁 02 - Estruturas de Seleção

Neste módulo, explorei as estruturas de tomada de decisão em Python. Aprendi a direcionar o fluxo do código com base em condições lógicas utilizando tanto as estruturas tradicionais quanto recursos mais recentes da linguagem.

### 🧠 Conceitos Praticados:
* **Condicionais Simples e Compostas:** Uso prático de `if`, `elif` e `else` para testar múltiplos cenários numéricos.
* **Estrutura de Seleção Avançada (`match/case`):** Implementação do controle de fluxo por correspondência de padrões (similar ao *switch/case* de outras linguagens), introduzido no Python 3.10.
* **Conversão de Tipos (Casting):** Uso do `int(input())` para garantir a leitura correta de dados numéricos inseridos pelo usuário.

---

### 💻 Arquivos Criados no Módulo:

#### 1. `calcula_media.py`
* **Descrição:** Cria uma lógica que recebe quatro notas pré-definidas, realiza a soma e calcula a média aritmética simples. 
* **Fluxo de Decisão:** 
  * Se a média for maior ou igual a `7`, exibe **Aprovado**.
  * Se a média for menor ou igual a `5`, exibe **Reprovado**.
  * Caso esteja entre os dois valores, aciona o caso geral (`else`) exibindo **Em Recuperação**.

#### 2. `dia_semana.py`
* **Descrição:** Um programa interativo que solicita ao usuário um número de 1 a 7 e traduz essa entrada no dia da semana equivalente.
* **Destaque Técnico:** Utiliza `match dia` para estruturar os casos de forma limpa e o `case other` para tratar de forma segura qualquer entrada inválida fora do intervalo esperado.
