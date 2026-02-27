#!/usr/bin/env python3

import requests
import statistics
from datetime import datetime
import os

# =========================
# PREÇO BTC
# =========================

def preco_btc():
    try:
        r = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={"ids": "bitcoin", "vs_currencies": "usd"},
            timeout=10
        )
        return r.json()["bitcoin"]["usd"]
    except:
        return None


# =========================
# 200 DIAS (para Mayer)
# =========================

def preco_ult_200():
    try:
        r = requests.get(
            "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart",
            params={"vs_currency": "usd", "days": 200},
            timeout=10
        )
        dados = r.json()["prices"]
        return [p[1] for p in dados]
    except:
        return None


def calcular_mayer(preco_atual, precos_200):
    try:
        media_200 = statistics.mean(precos_200)
        return round(preco_atual / media_200, 2)
    except:
        return None

# =========================
# FEAR & GREED
# =========================

def fear_and_greed():
    try:
        r = requests.get(
            "https://api.alternative.me/fng/",
            timeout=10
        )
        data = r.json()["data"][0]
        return f"{data['value_classification']} ({int(data['value'])})"
    except:
        return None
    

# =========================
# DIAS DESDE ÚLTIMO HALVING
# =========================

def dias_desde_halving(arquivo="~/MeuSetup/scripts/btc-scripts/ult-halving.txt"):
    try:
        caminho = os.path.expanduser(arquivo)

        with open(caminho, "r") as f:
            data_str = f.read().strip()

        data_halving = datetime.strptime(data_str, "%d/%m/%Y")
        hoje = datetime.now()

        return (hoje - data_halving).days

    except Exception as e:
        return None