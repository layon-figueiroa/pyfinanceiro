# 💸 PyFinanceiro

## 📋 Descrição

O **PyFinanceiro** é um script desenvolvido em Python para realizar análises de registros financeiros armazenados em um arquivo CSV.

O conjunto de dados contém duas colunas:

* **Data**
* **Lucros/Perdas**

O objetivo do projeto é processar essas informações e gerar um relatório financeiro contendo indicadores relevantes sobre o período analisado.

---

## 🎯 Funcionalidades

O script calcula automaticamente:

* Total de meses analisados;
* Valor total líquido de Lucros/Perdas;
* Média de Lucros/Perdas;
* Média das variações mensais de Lucros/Perdas;
* Maior aumento nos lucros (data e valor);
* Maior redução nos lucros (data e valor).

Além disso:

* Exibe os resultados no terminal;
* Gera um arquivo `relatorio.txt` contendo a análise financeira.

---

## 📂 Estrutura do Projeto

```text
pyfinanceiro/
│
├── registros/
│   └── dados_financeiros.csv
├── relatorios/
│   └── analise_financeira.txt
├── functions.py
├── main.py
└── README.md
```

---

## 📄 Formato do Arquivo CSV

O arquivo deve possuir o seguinte formato:

```csv
Data,Lucros/Perdas
Jan-2010,867884
Feb-2010,984655
Mar-2010,322013
Apr-2010,-69417
```

---

## ▶️ Como Executar

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
```

### 2. Acessar a pasta do projeto

```bash
cd pyfinanceiro
```

### 3. Executar o script

```bash
python main.py
```

---

## 📊 Exemplo de Saída

```text
Analise Financeira
----------------------------
Total de meses: 86
Total: $ 38382578
Média: $ 446309.05
Variação da média: $ -2315.12
Maior aumento nos lucros: Feb-2012 ($ 1926159)
Maior redução nos lucros: Sep-2013 ($ -2196167)
```

---

## 🧠 Conceitos Aplicados

Durante o desenvolvimento deste projeto foram utilizados conceitos fundamentais de Python:

* Leitura de arquivos (`open`)
* Manipulação de listas
* List Comprehension
* Generator Expressions
* Funções nativas (`sum`, `max`, `min`, `len`)
* Manipulação de strings
* Escrita de arquivos texto
* Estruturas de repetição
* Cálculos estatísticos básicos

---

## 🛠️ Tecnologias Utilizadas

* Python 3

---

## 📚 Objetivo Educacional

Este projeto foi desenvolvido com foco em praticar:

* Manipulação de arquivos CSV;
* Estruturas de dados em Python;
* Processamento de informações financeiras;
* Geração de relatórios automatizados.

---

Desenvolvido como exercício de lógica de programação e análise de dados utilizando Python.
