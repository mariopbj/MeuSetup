#!/bin/bash

WG_IFACE=$(wg show interfaces)

if [ -n "$WG_IFACE" ]; then
    sudo wg-quick down "$WG_IFACE"
else
    sudo wg-quick up servidor1
fi