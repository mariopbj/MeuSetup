#!/bin/bash

# Diretório dos wallpapers
WALLPAPER_DIR="$HOME/WallPapers"
# Arquivo onde o último wallpaper é salvo
LAST_WALLPAPER_FILE="$HOME/.config/wallpaper_last"

# Se o script for chamado com "--restore", ele apenas carrega o último wallpaper e sai
if [ "$1" == "--restore" ]; then
    if [ -f "$LAST_WALLPAPER_FILE" ]; then
        LAST_WALLPAPER=$(cat "$LAST_WALLPAPER_FILE")
        feh --bg-fill "$LAST_WALLPAPER"
    fi
    exit 0
fi

# Escolher um wallpaper com rofi
SELECTED_WALLPAPER=$(ls "$WALLPAPER_DIR" | rofi -dmenu -i -p "Escolha um wallpaper")

# Se o usuário cancelar, sair
[ -z "$SELECTED_WALLPAPER" ] && exit 1

# Caminho completo do wallpaper
WALLPAPER_PATH="$WALLPAPER_DIR/$SELECTED_WALLPAPER"

# Aplicar o wallpaper
feh --bg-fill "$WALLPAPER_PATH"

# Salvar o último wallpaper escolhido
echo "$WALLPAPER_PATH" > "$LAST_WALLPAPER_FILE"

# Notificação
notify-send "Wallpaper alterado!" "Novo wallpaper: $SELECTED_WALLPAPER"