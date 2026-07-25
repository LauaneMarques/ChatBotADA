#!/bin/sh

# Inicia o servidor de Custom Actions em segundo plano na porta 5055
rasa run actions --port 5055 &

# Aguarda 5 segundos para garantir que o Action Server subiu
sleep 5

# Inicia o servidor principal do Rasa
rasa run --enable-api --cors "*" --port 5005