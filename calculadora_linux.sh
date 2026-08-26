#!/bin/bash

clear

echo "==============================="
echo "          BEM VINDO A          "
echo "       SUPER CALCULADORA       "
echo "==============================="

echo "Usuario identificado: $(whoami)"
echo "Data/Hora atual $(date +'%d/%m/%Y às %H:%M')"

echo ""
echo "Iniciando:"
echo ""

python3 calculadora.py

echo "==============================="
echo "      Finalizando sessão       "
echo "==============================="

