#!/usr/bin/env python3

import sys

from list_struct import List
from stack_struct import Stack
from queue_struct import Queue

estruturas = {
    "list": List,
    "stack": Stack,
    "queue": Queue,
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
        # Converte os argumentos após a estrutura e o método em inteiros.
        valores = [int(arg) for arg in sys.argv[3:]]
    except ValueError:
        print("Erro: os valores devem ser números inteiros.")
        return
    
    #TODO - Instanciar a estrutura solicitada e inserir os valores.

if __name__ == "__main__":
    main()
