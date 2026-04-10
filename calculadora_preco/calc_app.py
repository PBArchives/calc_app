import tkinter as tk
from tkinter import ttk, messagebox

def calcular():
    try:
        custo = float(entry_custo.get())
        margem = float(entry_margem.get()) / 100

        icms = float(entry_icms.get()) / 100
        pis = float(entry_pis.get()) / 100
        cofins = float(entry_cofins.get()) / 100

        impostos_totais = icms + pis + cofins

        if margem + impostos_totais >= 1:
            messagebox.showerror("Erro", "Margem + impostos não pode ser >= 100%")
            return

        # Preço de venda correto
        preco_venda = custo / (1 - margem - impostos_totais)

        # Valores
        valor_impostos = custo * impostos_totais
        lucro = preco_venda * margem
        custo_final = custo + valor_impostos

        # Exibir
        resultado_venda.set(f"R$ {preco_venda:.2f}")
        resultado_lucro.set(f"R$ {lucro:.2f}")
        resultado_impostos.set(f"R$ {valor_impostos:.2f}")
        resultado_custo_final.set(f"R$ {custo_final:.2f}")

    except ValueError:
        messagebox.showerror("Erro", "Digite valores válidos!")

# Janela
janela = tk.Tk()
janela.title("Simulador de Preço")
janela.geometry("420x400")
janela.resizable(False, False)

# Tema dark
style = ttk.Style()
style.theme_use("clam")

bg_color = "#1e1e1e"
fg_color = "#ffffff"
entry_bg = "#2d2d2d"

janela.configure(bg=bg_color)

style.configure(".", background=bg_color, foreground=fg_color, fieldbackground=entry_bg)
style.configure("TLabel", font=("Segoe UI", 10))
style.configure("Header.TLabel", font=("Segoe UI", 14, "bold"))

# Frame
frame = ttk.Frame(janela)
frame.pack(fill="both", expand=True, padx=20, pady=20)

# Título
ttk.Label(frame, text="📊 Simulador de preço final", style="Header.TLabel")\
    .grid(row=0, column=0, columnspan=2, pady=(0, 15))

# Função auxiliar
def criar_input(texto, linha):
    ttk.Label(frame, text=texto).grid(row=linha, column=0, sticky="w")
    entry = ttk.Entry(frame)
    entry.grid(row=linha, column=1, pady=5)
    return entry

# Inputs
entry_custo = criar_input("Custo do produto (R$):", 1)
entry_margem = criar_input("Margem de lucro (%):", 2)
entry_icms = criar_input("ICMS (%):", 3)
entry_pis = criar_input("PIS (%):", 4)
entry_cofins = criar_input("COFINS (%):", 5)

# Botão
ttk.Button(frame, text="Calcular", command=calcular)\
    .grid(row=6, column=0, columnspan=2, pady=15, sticky="ew")

# Resultados
def criar_resultado(texto, linha, var, destaque=False):
    ttk.Label(frame, text=texto).grid(row=linha, column=0, sticky="w")
    ttk.Label(
        frame,
        textvariable=var,
        font=("Segoe UI", 11, "bold") if destaque else None
    ).grid(row=linha, column=1, sticky="e")

resultado_venda = tk.StringVar(value="R$ 0.00")
resultado_lucro = tk.StringVar(value="R$ 0.00")
resultado_impostos = tk.StringVar(value="R$ 0.00")
resultado_custo_final = tk.StringVar(value="R$ 0.00")

criar_resultado("Preço de venda:", 7, resultado_venda, True)
criar_resultado("Lucro:", 8, resultado_lucro)
criar_resultado("Impostos:", 9, resultado_impostos)
criar_resultado("Custo final:", 10, resultado_custo_final)

# Loop
janela.mainloop()