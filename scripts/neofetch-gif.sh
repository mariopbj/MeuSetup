#!/bin/bash

clear

# Diretório dos GIFs
GIF_DIR="$HOME/.config/neofetch/gifs"
# Arquivo onde o último GIF é salvo
LAST_GIF_FILE="$HOME/.config/neofetch/gif_last"

# Se o script for chamado com "--restore", ele apenas mostra o último GIF e sai
if [ "$1" == "--restore" ]; then
    if [ -f "$LAST_GIF_FILE" ]; then
        LAST_GIF=$(cat "$LAST_GIF_FILE")
        neofetch | sed 's/^/                                          /'
        kitty +kitten icat --place=40x20@1x1 "$LAST_GIF"
    fi
    exit 0
fi

# Escolher um GIF com rofi
SELECTED_GIF=$(ls "$GIF_DIR" | rofi -dmenu -i -p "Escolha um GIF")

# Se o usuário cancelar, sair
[ -z "$SELECTED_GIF" ] && exit 1

# Caminho completo do GIF
GIF_PATH="$GIF_DIR/$SELECTED_GIF"

# Mostrar no Neofetch
neofetch | sed 's/^/                                          /'
kitty +kitten icat --place=40x20@1x1 "$GIF_PATH"

# Salvar o último GIF escolhido
echo "$GIF_PATH" > "$LAST_GIF_FILE"

# Notificação
notify-send "GIF alterado!" "Novo GIF: $SELECTED_GIF"