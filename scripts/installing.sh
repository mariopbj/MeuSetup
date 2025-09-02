#!/bin/bash

echo "Atualizando a lista de pacotes..."
sudo apt update

echo "Instalando pacotes principais..."
sudo apt install -y \
    xorg \
    i3 \
    kitty \
    fonts-dejavu \
    fonts-liberation \
    fonts-font-awesome \
    build-essential \
    curl \
    lightdm \
    firefox-esr \
    pulseaudio \
    alsa-utils \
    pamixer \
    feh \
    unzip \
    network-manager \
    picom \
    rofi \
    celluloid \
    clementine \
    flameshot \
    neofetch \
    btop

# Instalar settings do gnome
sudo apt install -y --no-install-recommends gnome-control-center

echo "Instalando dependências da Polybar..."
sudo apt install -y \
    cmake \
    python3-pybind11 \
    libxcb1-dev \
    libxcb-util0-dev \
    libxcb-randr0-dev \
    libxcb-composite0-dev \
    python3-xcbgen \
    xcb-proto \
    libxcb-image0-dev \
    libxcb-ewmh-dev \
    libxcb-icccm4-dev \
    libxcb-xkb-dev \
    libxcb-xrm-dev \
    libasound2-dev \
    libpulse-dev \
    libjsoncpp-dev \
    libmpdclient-dev \
    libiw-dev \
    libnl-3-dev \
    libnl-genl-3-dev \
    pkg-config \
    python3-sphinx \
    libcairo2-dev \
    libfontconfig1-dev \
    libuv1-dev


echo "Instalando dependências do Neovim..."
sudo apt install -y \
    nodejs \
    python3-pip \
    npm


echo "Todas as dependências foram instaladas com sucesso!"
echo "Instalação concluída!"