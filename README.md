# OFX Transaction Processor

This Python script processes OFX (Open Financial Exchange) files to extract financial transactions, categorize them based on predefined keywords, and generate a summarized report of expenses by category, as well as a detailed CSV export of all transactions.

## Features

-   **OFX File Parsing**: Automatically reads and parses OFX files from a specified directory.
-   **Transaction Categorization**: Categorizes transactions into predefined categories (e.g., 'Transporte', 'Alimentação', 'Casa', 'Roupas', 'Lazer', 'Saúde', 'Educação', 'Trabalho', 'Viagem', 'Serviços', 'Investimentos') based on keywords found in transaction descriptions.
-   **Expense Summary**: Provides a clear summary of total expenses for each category.
-   **CSV Export**: Generates a CSV file (`transacoes.csv`) containing all processed transactions with their date, amount, description, and assigned category.

## Requirements

-   Python 3.x
-   `ofxparse` library

To install the required library, run:

```bash
pip install ofxparse
```

## How to Use

1.  **Place your OFX files**: Put all your `.ofx` files in a directory named `ofx_files` in the same directory as the `codigo.py` script.
2.  **Run the script**: Execute the Python script from your terminal:

    ```bash
    python codigo.py
    ```

## Output

The script will generate two main outputs:

1.  **Console Output**: A summary of expenses per category will be printed to the console.
2.  **`transacoes.csv`**: A CSV file will be created in the script's directory, containing all transactions with the following columns: `Data`, `Valor`, `Descrição`, `Categoria`.

## Example

Assuming you have `ofx_files/my_bank_statement.ofx`, running the script will produce output similar to this:

```
Processando arquivos OFX...

Resumo de Despesas por Categoria:
--------------------------------
Alimentação: R$ -500.00
Transporte: R$ -150.00
Casa: R$ -300.00
Lazer: R$ -200.00
Saúde: R$ -100.00
--------------------------------
Total Geral: R$ -1250.00

Transações exportadas para transacoes.csv
```

And a `transacoes.csv` file with your categorized transactions.
