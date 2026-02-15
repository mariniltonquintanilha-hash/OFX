import tkinter
from tkinter import ttk, filedialog
from ofxparse import OfxParser
import codecs
import os

def carregar_arquivo_ofx():
    """
    Abre uma janela de diálogo para o usuário selecionar um arquivo .ofx,
    lê o arquivo e preenche a tabela com as transações.
    """
    # Abre o seletor de arquivos, começando no diretório atual
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione o arquivo OFX",
        filetypes=(("Arquivos OFX", "*.ofx"), ("Todos os arquivos", "*.*")),
        initialdir=os.getcwd()
    )

    if not caminho_arquivo:
        return # O usuário cancelou a seleção

    # Limpa a tabela de quaisquer dados anteriores
    for i in tree.get_children():
        tree.delete(i)

    # Tenta ler e processar o arquivo
    try:
        with codecs.open(caminho_arquivo, 'r', encoding='utf-8') as f:
            ofx = OfxParser.parse(f)

        # Preenche a tabela com as transações do arquivo
        statement = ofx.account.statement
        for transaction in statement.transactions:
            tree.insert("", "end", values=(
                transaction.date.strftime('%d/%m/%Y'),
                (transaction.payee or transaction.memo or ""),
                f"{transaction.type}",
                f"{transaction.amount:.2f}"
            ))
    except Exception as e:
        # Mostra uma mensagem de erro se algo der errado
        label_status.config(text=f"Erro ao ler o arquivo: {e}")


# --- Configuração da Interface Gráfica ---
root = tkinter.Tk()
root.title("Visualizador de Extrato OFX")
root.geometry("800x600")

# Frame principal
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(expand=True, fill="both")

# Botão para carregar o arquivo
btn_carregar = ttk.Button(main_frame, text="Carregar Arquivo OFX", command=carregar_arquivo_ofx)
btn_carregar.pack(pady=10)

# Label de status
label_status = ttk.Label(main_frame, text="Selecione um arquivo para começar.")
label_status.pack(pady=5)

# Tabela (TreeView) para mostrar as transações
colunas = ("data", "descricao", "tipo", "valor")
tree = ttk.Treeview(main_frame, columns=colunas, show="headings")

# Define os cabeçalhos
tree.heading("data", text="Data")
tree.heading("descricao", text="Descrição")
tree.heading("tipo", text="Tipo")
tree.heading("valor", text="Valor (R$)")

# Define a largura das colunas
tree.column("data", width=100, anchor="center")
tree.column("descricao", width=350)
tree.column("tipo", width=100, anchor="center")
tree.column("valor", width=120, anchor="e")

tree.pack(expand=True, fill="both")

# Inicia a aplicação
root.mainloop()