#!/usr/bin/env python3

# Prova 2 - Estruturas de Dados FATEC
# Copyright (c) 2026 Rodrigo de Freitas
# SPDX-License-Identifier: MIT

import sys

from list_struct import List
from stack_struct import Stack
from queue_struct import Queue

estruturas = {
    "--list": List,
    "--stack": Stack,
    "--queue": Queue,
}

def mostrar_ajuda():
    print("Uso: main.py <estrutura> <método> [valores...]")
    print()
    print("Estruturas disponíveis:")
    print("  --list:  --min, --max, --sum, --avg, --len, --append, --reverse")
    print("  --stack: --buscar, --editar, --remover, --remover_repetidos")
    print("  --queue: --imprimir_fila, --buscar, --editar, --remover, --remover_repetidos")
    print()
    print("Exemplos:")
    print("  main.py --list --min 1 2 3 4 5")
    print("  main.py --stack --buscar 1 2 3 4 5")

def main():
    metodos_lista = {
        "--min": "min",
        "--max": "max",
        "--sum": "sum",
        "--avg": "avg",
        "--len": "len",
        "--reverse": "reverse",
        "--append": "append",
    }

    metodos_pilha = {
        "--buscar": "buscar",
        "--editar": "editar",
        "--remover": "remover",
        "--remover_repetidos": "remover_repetidos",
    }

    metodos_fila = {
        "--imprimir_fila": "imprimir_fila",
        "--buscar": "buscar",
        "--editar": "editar",
        "--remover": "remover",
        "--remover_repetidos": "remover_repetidos",
    }

    if len(sys.argv) == 2 and sys.argv[1] in ("--help", "-h"):
        mostrar_ajuda()
        return

    if len(sys.argv) < 3:
        print("Uso: main.py <estrutura> <método> <valores...>")
        print("Use main --help ou -h para consultar os comandos disponíveis.")
        return

    estrutura = sys.argv[1]
    metodo = sys.argv[2]

    try:
        # Converte os valores após a estrutura e o método em inteiros.
        valores = [int(arg) for arg in sys.argv[3:]]
    except ValueError:
        print("Erro: os valores devem ser números inteiros.")
        return
    
    #Instancia a estrutura solicitada e insere os valores.
    if estrutura not in estruturas:
        print(f"Erro: estrutura '{estrutura}' inválida.")
        return

    if estrutura == "--list":
        metodos = metodos_lista
    elif estrutura == "--stack":
        metodos = metodos_pilha
    elif estrutura == "--queue":
        metodos = metodos_fila

    if metodo not in metodos:
        print(f"Erro: método '{metodo}' inválido para {estrutura}.")
        return

    instancia = estruturas[estrutura]()

    for valor in valores:
        instancia.inserir_lista(valor)

    funcao = getattr(instancia, metodos[metodo])
    resultado = funcao()

    print(resultado)

if __name__ == "__main__":
    main()
