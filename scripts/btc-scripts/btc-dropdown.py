#!/usr/bin/env python3

import tkinter as tk
import os

# caminho relativo ao próprio script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARQUIVO = os.path.join(BASE_DIR, "btc-data.txt")

def obter_dados():
    try:
        with open(ARQUIVO) as f:
            linhas = f.read().splitlines()

        return {
            "preco": float(linhas[1]),
            "mayer": linhas[2],
            "rsi": linhas[3],
            "fng": linhas[4],
            "halving": linhas[5]
        }
    except:
        return None


# =========================
# 🔹 Cores dinâmicas
# =========================

def cor_mayer(valor):
    try:
        valor = float(valor)
        if valor <= 0.8:
            return "#ff4444"    # verde (zona histórica de fundo)
        elif valor < 1:
            return "#ffaa00"   # neutro
        elif valor <= 2:
            return "#00ff88"# topo histórico
        else:
            return "#ffffff"
    except:
        return "white"


def cor_rsi(valor):
    try:
        valor = float(valor)
        if valor <= 30:
            return "#ff4444"    # sobrevendido
        elif valor >= 70:
            return "#00ff88"  # sobrecomprado
        else:
            return "#ffffff"
    except:
        return "white"
    

import re

def cor_fng(valor):
    try:
        # extrai número da string
        numero = re.search(r'\d+', str(valor))
        if not numero:
            return "white"

        valor = float(numero.group())

        if valor <= 20:
            return "#ff4444"   # Extreme Fear
        elif valor <= 40:
            return "#ff8800"   # Fear
        elif valor <= 50:
            return "#ffaa00"   # Neutral
        elif valor <= 70:
            return "#88ff00"   # Greed
        else:
            return "#00ff88"   # Extreme Greed

    except:
        return "white"
    

def cor_halving(dias):
    try:
        dias = int(dias)

        if 545 <= dias <= 565:
            return "#00ff88"   # zona mais provável
        elif 515 <= dias <= 585:
            return "#ffaa00"   # zona histórica
        else:
            return "white"

    except:
        return "white"


# =========================
# 🔹 Criar janela
# =========================

root = tk.Tk()
root.overrideredirect(True)
root.attributes("-topmost", True)
root.configure(bg="#050608")

# aumentei altura para caber tudo
root.geometry("300x210+320+35")

dados = obter_dados()

frame = tk.Frame(root, bg="#050608", padx=15, pady=12)
frame.pack()


titulo = tk.Label(
    frame,
    text="₿ Bitcoin Dashboard",
    bg="#050608",
    fg="white",
    font=("monospace", 12, "bold")
)
titulo.pack(anchor="w")


if dados is None:
    erro = tk.Label(
        frame,
        text="Erro ao obter dados",
        bg="#050608",
        fg="red",
        font=("monospace", 11)
    )
    erro.pack(anchor="w")

else:

    # 🔹 Preço
    tk.Label(
        frame,
        text=f"Preço: ${dados['preco']:,.2f}",
        bg="#050608",
        fg="white",
        font=("monospace", 11)
    ).pack(anchor="w")

    # 🔹 Mayer
    tk.Label(
        frame,
        text=f"Mayer: {dados['mayer']}",
        bg="#050608",
        fg=cor_mayer(dados["mayer"]),
        font=("monospace", 11)
    ).pack(anchor="w")

    # 🔹 RSI
    tk.Label(
        frame,
        text=f"RSI: {dados['rsi']}",
        bg="#050608",
        fg=cor_rsi(dados["rsi"]),
        font=("monospace", 11)
    ).pack(anchor="w")

    # 🔹 Fear & Greed
    tk.Label(
        frame,
        text=f"Fear & Greed: {dados['fng']}",
        bg="#050608",
        fg=cor_fng(dados["fng"]),
        font=("monospace", 11)
    ).pack(anchor="w")

    # 🔹 Halving
    tk.Label(
        frame,
        text=f"Dias pós-halving: {dados['halving']}",
        bg="#050608",
        fg=cor_halving(dados["halving"]),
        font=("monospace", 11)
    ).pack(anchor="w")


# 🔹 Fecha ao perder foco
root.bind("<Button-1>", lambda e: root.destroy())

root.mainloop()