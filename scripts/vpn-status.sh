#!/bin/bash

WG_IFACE=$(wg show interfaces)

if [ -n "$WG_IFACE" ]; then
    echo "VPN: $WG_IFACE"
else
    echo "Desconectado"
fi