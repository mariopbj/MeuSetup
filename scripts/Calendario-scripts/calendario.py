#!/usr/bin/env python3

from datetime import datetime
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARQUIVO = os.path.join(BASE_DIR, "habito_data.txt")
ESTADO = os.path.join(BASE_DIR, "modo.txt")


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
# 🔹 Estado (modo)
# =========================

def set_modo(modo):
    with open(ESTADO, "w") as f:
        f.write(modo)


def get_modo():
    try:
        with open(ESTADO) as f:
            return f.read().strip()
    except:
        return "padrao"


def alternar_modo():
    modo = get_modo()

    if modo == "padrao":
        set_modo("passados")
    elif modo == "passados":
        set_modo("restantes")
    else:
        set_modo("padrao")


# =========================
# 🔹 Cálculo
# =========================

def calcular():
    nome, inicio, fim = carregar()
    if not inicio:
        return None

    hoje = datetime.now()

    total = (fim - inicio).days
    passados = (hoje - inicio).days
    restantes = (fim - hoje).days

    passados = max(0, passados)
    restantes = max(0, restantes)

    progresso = int((passados / total) * 100) if total > 0 else 0
    progresso = min(100, max(0, progresso))

    return nome, inicio, fim, passados, restantes, progresso


# =========================
# 🔹 Barra de progresso
# =========================

def barra(progresso, tamanho=10):
    cheio = int((progresso / 100) * tamanho)
    vazio = tamanho - cheio
    return "█" * cheio + "░" * vazio


# =========================
# 🔹 Outputs
# =========================

def output_padrao():
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


def output_passados():
    data = calcular()
    if not data:
        return " 0d"

    passados = data[3]
    return f" Passou: {passados}d"


def output_restantes():
    data = calcular()
    if not data:
        return " 0d"

    restantes = data[4]
    return f" Resta: {restantes}d"


def output():
    modo = get_modo()

    if modo == "passados":
        return output_passados()
    elif modo == "restantes":
        return output_restantes()
    else:
        return output_padrao()


# =========================
# 🔹 Main
# =========================

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "set":
            definir()
        elif sys.argv[1] == "toggle":
            alternar_modo()
    else:
        print(output())