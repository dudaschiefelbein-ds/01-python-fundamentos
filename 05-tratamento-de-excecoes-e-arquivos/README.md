# 📁 Módulo 05 - Tratamento de Exceções e Arquivos

Neste módulo, aprendi a construir aplicações Python mais seguras, resilientes a erros e capazes de interagir com o sistema operacional por meio da persistência de dados em arquivos externos (`.txt`, `.json` e `.csv`).

### 🧠 Conceitos Praticados:
* **Tratamento de Erros (`try/except/else/finally`):** Captura de falhas em tempo de execução para evitar que o programa trave.
* **Gerenciamento de Contexto (`with`):** Abertura e fechamento automatizado de arquivos de forma segura, prevenindo vazamentos de memória.
* **Manipulação de Arquivos Planos (TXT):** Escrita (`w`), leitura (`r+`) e anexação (`a+`) de cadeias de caracteres simples.
* **Serialização de Dados (JSON):** Conversão de estruturas de dados do Python (como listas de dicionários) em arquivos textuais padronizados `.json`.
* **Manipulação de Tabelas (CSV):** Geração e formatação de arquivos separados por delimitadores utilizando a biblioteca nativa `csv`.

---

### 💻 Arquivos Criados no Módulo:

#### 1. [tratamento_erros.py](./tratamento_erros.py)
* **Descrição:** Demonstração prática do fluxo completo de tratamento de exceções com uma calculadora de divisão.
* **Estruturas Utilizadas:**
  * `ValueError`: Captura quando o usuário digita letras em vez de números.
  * `ZeroDivisionError`: Captura tentativas de divisão por zero.
  * `Exception as erro`: Bloco genérico para capturar qualquer falha não mapeada.
  * `else`: Executado somente se o programa rodar sem nenhum erro.
  * `finally`: Bloco que roda obrigatoriamente no fim, independente de falhas.

#### 2. [manipulacao_txt.py](./manipulacao_txt.py)
* **Descrição:** Criação e leitura de arquivos `.txt`, demonstrando a evolução do método tradicional para o método recomendado.
* **Recursos Utilizados:**
  * Método tradicional com `open()` e a obrigatoriedade do `.close()`.
  * Método moderno utilizando o gerenciador de contexto `with open(...)` combinado com loops `for` para varrer e ler linhas sequencialmente.
  * Gera o arquivo de suporte: [pessoas.txt](./pessoas.txt).

#### 3. [manipulacao_json.py](./manipulacao_json.py)
* **Descrição:** Armazenamento estruturado de dados complexos através da biblioteca nativa `json`.
* **Recursos Utilizados:**
  * `json.dump()`: Função responsável por serializar a lista de dicionários do Python direto para um arquivo de texto formatado.
  * Parâmetro `indent=4` para garantir a legibilidade visual do arquivo gerado.
  * Gera o arquivo de suporte: [pessoas.json](./pessoas.json).

#### 4. [manipulacao_csv.py](./manipulacao_csv.py)
* **Descrição:** Geração de tabelas de dados separadas por delimitadores ponto e vírgula (`;`).
* **Recursos Utilizados:**
  * `csv.writer()`: Configuração do formatador e do delimitador do documento.
  * `writerow()`: Gravação de uma linha única isolada (usada para criar o cabeçalho).
  * `writerows()`: Gravação em lote de uma lista contendo múltiplas sublistas de dados.
  * Gera o arquivo de suporte: [carros.csv](./carros.csv).
