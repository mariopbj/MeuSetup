#!/usr/bin/env python3

import time
from datetime import datetime
import btc_info

ARQUIVO = "/home/mpbj/MeuSetup/scripts/btc-scripts/btc-data.txt"


def obter_dados():
    preco = btc_info.preco_btc()
    precos_200 = btc_info.preco_ult_200()

    if preco is None or precos_200 is None:
        return None

    mayer = btc_info.calcular_mayer(preco, precos_200)
    rsi = btc_info.calcular_rsi()
    fng = btc_info.fear_and_greed()
    dias_halving = btc_info.dias_desde_halving()

    return preco, mayer, rsi, fng, dias_halving


def salvar_dados(dados):
    if dados is None:
        return

    preco, mayer, rsi, fng, halving = dados
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(ARQUIVO, "w") as f:
        f.write(f"{timestamp}\n")
        f.write(f"{preco}\n")
        f.write(f"{mayer}\n")
        f.write(f"{rsi}\n")
        f.write(f"{fng}\n")
        f.write(f"{halving}\n")


while True:
    dados = obter_dados()

    salvar_dados(dados)
    time.sleep(600)  # 600s = 10 minutos