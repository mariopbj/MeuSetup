#!/bin/bash

#SERVERS=("servidor1" "2" "3" "...")

CURRENT=$(wg show interfaces)

if [ -z "$CURRENT" ]; then
    sudo wg-quick up "${SERVERS[0]}"
    exit
fi

for i in "${!SERVERS[@]}"; do
    if [ "${SERVERS[$i]}" = "$CURRENT" ]; then
        sudo wg-quick down "$CURRENT"
        NEXT_INDEX=$(( (i + 1) % ${#SERVERS[@]} ))
        sudo wg-quick up "${SERVERS[$NEXT_INDEX]}"
        exit
    fi
done