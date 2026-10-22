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
    print("  main.py --list --sum 10 20 30")
    print("  main.py --stack --buscar 10 20 30 -- 20")


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
        print("Use main.py --help ou -h para consultar os comandos disponíveis.")
        return

    estrutura = sys.argv[1]
    metodo = sys.argv[2]

    if estrutura not in estruturas:
        print(f"Erro: estrutura '{estrutura}' inválida.")
        return

    if estrutura == "--list":
        metodos = metodos_lista
    elif estrutura == "--stack":
        metodos = metodos_pilha
    else:
        metodos = metodos_fila

    if metodo not in metodos:
        print(f"Erro: método '{metodo}' inválido para {estrutura}.")
        return

    argumentos = sys.argv[3:]
    info_busca = None

    try:
        if metodo == "--append":
            valores = argumentos

            if "--" not in valores:
                print("Erro: o método --append exige o separador '--'.")
                print("Uso: main.py --list --append <valores> -- <valores>")
                return

            if (
                valores == ["--"]
                or valores[0] == "--"
                or valores[-1] == "--"
            ):
                print("Erro: informe valores antes e depois de '--'.")
                print("Uso: main.py --list --append <valores> -- <valores>")
                return

        elif metodo == "--buscar":
            if "--" not in argumentos:
                print("Erro: separe os elementos do valor procurado com '--'.")
                print("Uso: main.py --stack --buscar <elementos> -- <valor>")
                return

            separador = argumentos.index("--")
            elementos = argumentos[:separador]
            procurado = argumentos[separador + 1:]

            if not elementos or len(procurado) != 1:
                print("Erro: informe os elementos e exatamente um valor para buscar.")
                print("Uso: main.py --stack --buscar <elementos> -- <valor>")
                return

            valores = [int(arg) for arg in elementos]
            info_busca = int(procurado[0])

        else:
            valores = [int(arg) for arg in argumentos]

    except ValueError:
        print("Erro: os valores devem ser números inteiros.")
        return

    instancia = estruturas[estrutura]()
    funcao = getattr(instancia, metodos[metodo])

    if metodo == "--append":
        try:
            funcao(valores)
        except ValueError as erro:
            print(f"Erro: {erro}")
        return

    # Mantém a inserção usada pelo código original.
    # Confira se Stack e Queue também possuem inserir_lista().
    for valor in valores:
        instancia.inserir_lista(valor)

    if metodo == "--buscar":
        resultado = funcao(info_busca)

        if resultado:
            print(f"Elemento {info_busca} encontrado.")
        else:
            print(f"Elemento {info_busca} não encontrado.")
    else:
        resultado = funcao()
        print(resultado)


if __name__ == "__main__":
    main()
