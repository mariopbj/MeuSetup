#!/usr/bin/env python3

import time
from datetime import datetime
import subprocess
from pathlib import Path
import btc_info

BASE = Path.home() / "MeuSetup/scripts/btc-scripts"

ARQUIVO = BASE / "btc-data.txt"
ATH_FILE = BASE / "btc-ath.txt"

SOM_ALARME = BASE / "alarm/ath.mp3"
WALLPAPER_ATH = BASE / "alarm/honeybadger-dont-care.png"


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
    preco, mayer, rsi, fng, halving = dados
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(ARQUIVO, "w") as f:
        f.write(f"{timestamp}\n{preco}\n{mayer}\n{rsi}\n{fng}\n{halving}\n")


def ler_ath():
    try:
        return float(Path(ATH_FILE).read_text().strip())
    except:
        return 0


def salvar_ath(valor):
    ATH_FILE.write_text(str(valor))


def tocar_alarme():
    try:
        subprocess.Popen(["mpg123", "-q", str(SOM_ALARME)])
    except:
        pass


def trocar_wallpaper():
    try:
        subprocess.Popen(["feh", "--bg-fill", str(WALLPAPER_ATH)])
    except:
        pass


def verificar_ath(preco_atual):
    ath = ler_ath()

    if preco_atual > ath:
        salvar_ath(preco_atual)
        tocar_alarme()
        trocar_wallpaper()



time.sleep(5)  # aguardar 5 segundos para garantir que o sistema esteja pronto
while True:
    dados = obter_dados()

    if dados:
        salvar_dados(dados)
        verificar_ath(dados[0])

    time.sleep(600)