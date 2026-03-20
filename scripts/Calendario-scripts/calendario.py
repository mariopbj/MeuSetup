#!/usr/bin/env python3

from datetime import datetime
import os
import sys
import tkinter as tk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARQUIVO = os.path.join(BASE_DIR, "habito_data.txt")


# =========================
# 🔹 Dados
# =========================

def carregar():
    try:
        with open(ARQUIVO) as f:
            nome, inicio_str, fim_str = f.read().splitlines()
            inicio = datetime.strptime(inicio_str, "%Y-%m-%d")
            fim = datetime.strptime(fim_str, "%Y-%m-%d")
            return nome, inicio, fim
    except:
        return None, None, None


def salvar(nome, inicio, fim):
    with open(ARQUIVO, "w") as f:
        f.write(f"{nome}\n{inicio.strftime('%Y-%m-%d')}\n{fim.strftime('%Y-%m-%d')}")


def definir():
    nome = input("Nome do hábito: ")
    inicio = input("Data início (YYYY-MM-DD): ")
    fim = input("Data fim (YYYY-MM-DD): ")

    salvar(
        nome,
        datetime.strptime(inicio, "%Y-%m-%d"),
        datetime.strptime(fim, "%Y-%m-%d"),
    )

    print("Salvo!")


# =========================
# 🔹 Cálculo
# =========================

def calcular():
    nome, inicio, fim = carregar()
    if not inicio:
        return None

    hoje = datetime.now()

    total = (fim - inicio).days
    passados = max(0, (hoje - inicio).days)
    restantes = max(0, (fim - hoje).days)

    progresso = int((passados / total) * 100) if total > 0 else 0
    progresso = min(100, max(0, progresso))

    return nome, inicio, fim, passados, restantes, progresso


# =========================
# 🔹 Barra
# =========================

def barra(progresso, tamanho=10):
    cheio = int((progresso / 100) * tamanho)
    vazio = tamanho - cheio
    return "█" * cheio + "░" * vazio


# =========================
# 🔹 Output Polybar
# =========================

def output_polybar():
    data = calcular()
    if not data:
        return " Definir"

    _, _, _, _, _, progresso = data

    if progresso < 30:
        cor = "%{F#ff4444}"
    elif progresso < 70:
        cor = "%{F#ffaa00}"
    else:
        cor = "%{F#00ff88}"

    return f"{cor}[{barra(progresso)}] %{{F-}}{progresso}%"


# =========================
# 🔹 Popup (dropdown)
# =========================

def abrir_popup():
    data = calcular()

    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.configure(bg="#050608")

    # posição (ajusta se quiser)
    root.geometry("190x110+353+40")

    frame = tk.Frame(root, bg="#050608", padx=15, pady=12)
    frame.pack()

    titulo = tk.Label(
        frame,
        text="Habit Tracker",
        bg="#050608",
        fg="white",
        font=("monospace", 12, "bold")
    )
    titulo.pack(anchor="w")

    if not data:
        tk.Label(
            frame,
            text="Nenhuma meta definida",
            bg="#050608",
            fg="red",
            font=("monospace", 11)
        ).pack(anchor="w")

    else:
        nome, inicio, fim, passados, restantes, progresso = data

        tk.Label(
            frame,
            text=f"Hábito: {nome}",
            bg="#050608",
            fg="white",
            font=("monospace", 10)
        ).pack(anchor="w")

        tk.Label(
            frame,
            text=f" Passou: {passados} dias",
            bg="#050608",
            fg="#00ff88",
            font=("monospace", 11)
        ).pack(anchor="w")

        tk.Label(
            frame,
            text=f" Resta: {restantes} dias",
            bg="#050608",
            fg="#ffaa00",
            font=("monospace", 11)
        ).pack(anchor="w")

    # fecha ao clicar ou perder foco
    root.bind("<FocusOut>", lambda e: root.destroy())
    root.bind("<Button-1>", lambda e: root.destroy())

    root.mainloop()


# =========================
# 🔹 Main
# =========================

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "set":
            definir()
        elif sys.argv[1] == "popup":
            abrir_popup()
    else:
        print(output_polybar())