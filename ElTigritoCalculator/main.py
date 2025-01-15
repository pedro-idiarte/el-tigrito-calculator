import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json

# Nome do arquivo JSON
FILENAME = "el_trigrito_data.json"

# Função para carregar dados do arquivo JSON
def load_data():
    try:
        with open(FILENAME, "r") as file:
            data = json.load(file)
            return data["inseridos"], data["retirados"]
    except FileNotFoundError:
        return [], []

# Função para salvar dados no arquivo JSON
def save_data(inseridos, retirados):
    data = {"inseridos": inseridos, "retirados": retirados}
    with open(FILENAME, "w") as file:
        json.dump(data, file)

# Função para recarregar os dados do arquivo JSON
def reload_data():
    global inseridos, retirados
    inseridos, retirados = load_data()
    update_resultados()

# Função para inserir um valor
def inserir_valor():
    valor = entry_valor.get()
    if valor:
        inseridos.append(valor)
        save_data(inseridos, retirados)
        update_resultados()
        entry_valor.delete(0, tk.END)
    else:
        messagebox.showwarning("Atenção", "Digite um valor para inserir.")

# Função para retirar um valor
def retirar_valor():
    valor = entry_valor.get()
    if valor:
        retirados.append(valor)
        save_data(inseridos, retirados)
        update_resultados()
        entry_valor.delete(0, tk.END)
    else:
        messagebox.showwarning("Atenção", "Digite um valor para retirar.")

# Função para atualizar os resultados na tela
def update_resultados():
    lista_inseridos.delete(0, tk.END)
    lista_retirados.delete(0, tk.END)
    for item in inseridos[-10:]:
        lista_inseridos.insert(tk.END, item)
    for item in retirados[-10:]:
        lista_retirados.insert(tk.END, item)
    total_inseridos = sum(map(float, inseridos))
    total_retirados = sum(map(float, retirados))
    label_soma.config(text=f"Soma: {total_retirados - total_inseridos:.2f}")
    label_totais.config(text=f"Total Inserido: {total_inseridos:.2f} | Total Retirado: {total_retirados:.2f}")

# Configuração inicial dos dados
inseridos, retirados = load_data()

# Criação da interface gráfica
root = tk.Tk()
root.title("El Trigrito")

# Adicionar ícone de tigre
root.iconbitmap("C:/Users/pedro/OneDrive/_Estudos/ElTigrito/images/tigre.ico")  # Substitua pelo caminho para o seu ícone de tigre

frame_top = tk.Frame(root)
frame_top.pack(pady=10)

label_inserir = tk.Label(frame_top, text="Inserir/Retirar Valor:")
label_inserir.grid(row=0, column=0, padx=5)

entry_valor = tk.Entry(frame_top)
entry_valor.grid(row=0, column=1, padx=5)

btn_inserir = tk.Button(frame_top, text="Inserir", command=inserir_valor)
btn_inserir.grid(row=0, column=2, padx=5)

btn_retirar = tk.Button(frame_top, text="Retirar", command=retirar_valor)
btn_retirar.grid(row=0, column=3, padx=5)

btn_recarregar = tk.Button(frame_top, text="🔄", command=reload_data)
btn_recarregar.grid(row=0, column=4, padx=5)

frame_bottom = tk.Frame(root)
frame_bottom.pack(pady=10)

label_resultados = tk.Label(frame_bottom, text="Resultados:")
label_resultados.grid(row=0, column=0, columnspan=2)

lista_inseridos = tk.Listbox(frame_bottom, height=10, width=20)
lista_inseridos.grid(row=1, column=0, padx=5)

lista_retirados = tk.Listbox(frame_bottom, height=10, width=20)
lista_retirados.grid(row=1, column=1, padx=5)

label_totais = tk.Label(root, text="Total Inserido: 0.00 | Total Retirado: 0.00")
label_totais.pack(pady=5)

label_soma = tk.Label(root, text="Soma: 0.00")
label_soma.pack(pady=5)

# Inicializar os resultados na interface
update_resultados()

root.mainloop()
