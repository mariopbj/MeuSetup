#!/bin/bash

echo "Atualizando a lista de pacotes..."
sudo apt update

echo "Instalando pacotes principais..."
sudo apt install -y \
    xorg \
    i3 \
    rxvt-unicode \
    fonts-dejavu \
    fonts-liberation \
    build-essential \
    curl \
    lightdm \
    firefox-esr \
    pulseaudio \
    alsa-utils \
    pamixer \
    feh \
    picom \
    rofi \
    gnome-control-center \
    celluloid \
    clementine \
    flameshot \
    neofetch \
    btop

echo "Instalação concluída!"