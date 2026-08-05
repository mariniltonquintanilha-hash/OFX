![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-0B5394?style=for-the-badge&logo=python&logoColor=white)

# OFX — Processador de Transações OFX

> Leitor de arquivos **OFX** (Open Financial Exchange) com categorização automática de despesas e exportação para CSV.

## 📌 Sobre o Projeto

Aplicação desktop que lê e processa extratos bancários no formato OFX, extrai as transações, categoriza automaticamente os gastos por palavras-chave e gera um resumo de despesas por categoria, além de um arquivo CSV completo.

## ✨ Funcionalidades

- 📂 **Leitura de OFX**: parsing automático de arquivos OFX com seleção via interface
- 🗂️ **Categorização automática**: categorias como Transporte, Alimentação, Casa, Roupas, Lazer, Saúde, Educação, Trabalho, Viagem, Serviços e Investimentos
- 📊 **Resumo de despesas**: total por categoria em uma visão clara
- 📤 **Exportação CSV**: gera `transacoes.csv` com data, valor, descrição e categoria

## 🚀 Como Executar

```bash
# instalar dependências
pip install ofxparse

# executar a aplicação
python codigo.py
```

## 📁 Estrutura do Projeto

```
├── codigo.py    → Aplicação principal
└── README.md
```

## 📄 Licença

Projeto desenvolvido para fins de portfólio.
