#!/bin/bash

sleep 1

# Mata qualquer instância antiga da polybar
killall -q polybar

# Aguarda até que todas tenham sido encerradas
while pgrep -u $UID -x polybar >/dev/null; do sleep 0.1; done

# Inicia cada barra em background
polybar workspace_bar &
polybar systray_bar &
polybar bitcoin_bar &
polybar date_bar &
polybar batery_bar &
polybar pulseaudio_bar &
polybar wifi_bar &
polybar powermenu_bar &