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
    print("  main.py --list --append abc def -- ghi jkl")
    print("  main.py --stack --buscar 10 20 30 -- 20")
    print("  main.py --queue --remover 10 20 30 -- 20")

def main():
    metodos = {
        "--list": {
            "--min": "min",
            "--max": "max",
            "--sum": "sum",
            "--avg": "avg",
            "--len": "len",
            "--append": "append",
            "--reverse": "reverse",
        },
        "--stack": {
            "--buscar": "buscar",
            "--editar": "editar",
            "--remover": "remover",
            "--remover_repetidos": "remover_repetidos",
        },
        "--queue": {
            "--imprimir_fila": "imprimir_fila",
            "--buscar": "buscar",
            "--editar": "editar",
            "--remover": "remover",
            "--remover_repetidos": "remover_repetidos",
        },
    }

    if len(sys.argv) == 2 and sys.argv[1] in ("--help", "-h"):
        mostrar_ajuda()
        return

    if len(sys.argv) < 3:
        mostrar_ajuda()
        return

    estrutura = sys.argv[1]
    metodo = sys.argv[2]
    argumentos = sys.argv[3:]

    if estrutura not in estruturas:
        print(f"Erro: estrutura '{estrutura}' inválida.")
        return

    if metodo not in metodos[estrutura]:
        print(f"Erro: método '{metodo}' inválido para {estrutura}.")
        return

    valores = []
    info = None
    novo_info = None

    try:
        if metodo == "--append":
            if (
                "--" not in argumentos
                or argumentos.index("--") == 0
                or argumentos.index("--") == len(argumentos) - 1
            ):
                raise ValueError(
                    "Informe valores antes e depois do separador '--'."
                )

            valores = argumentos

        elif estrutura in ("--stack", "--queue"):
            if metodo in ("--buscar", "--editar", "--remover"):
                if "--" not in argumentos:
                    raise ValueError(
                        "Separe os elementos dos argumentos da operação usando '--'."
                    )

                separador = argumentos.index("--")
                elementos = argumentos[:separador]
                operacao = argumentos[separador + 1:]

                if not elementos:
                    raise ValueError("Informe os elementos da estrutura.")

                if metodo in ("--buscar", "--remover") and len(operacao) != 1:
                    raise ValueError("Informe exatamente um valor após '--'.")

                if metodo == "--editar" and len(operacao) != 2:
                    raise ValueError(
                        "Informe o valor a editar e o novo valor após '--'."
                    )

                valores = [int(valor) for valor in elementos]

                if metodo == "--editar":
                    info = int(operacao[0])
                    novo_info = int(operacao[1])
                elif metodo in ("--buscar", "--remover"):
                    info = int(operacao[0])

            else:
                if "--" in argumentos:
                    raise ValueError(
                        "Não use '--' nesta operação."
                    )

                valores = [int(valor) for valor in argumentos]

        else:
            valores = [int(valor) for valor in argumentos]

    except ValueError as erro:
        print(f"Erro: {erro}")
        return

    instancia = estruturas[estrutura]()

    # Prepara a estrutura antes de executar a operação.
    if metodo != "--append":
        for valor in valores:
            if estrutura == "--list":
                instancia.inserir_lista(valor)
            elif estrutura == "--stack":
                instancia.empilhar(valor)
            elif estrutura == "--queue":
                instancia.enfileirar(valor)

    funcao = getattr(instancia, metodos[estrutura][metodo])

    try:
        if metodo == "--append":
            resultado = funcao(valores)

        elif metodo == "--buscar":
            resultado = funcao(info)
            if resultado:
                print(f"Elemento {info} encontrado.")
            else:
                print(f"Elemento {info} não encontrado.")

        elif metodo == "--editar":
            resultado = funcao(info, novo_info)
            if resultado:
                print(f"Elemento {info} alterado para {novo_info}.")
                
                # percorre a pilha, mostrando o dado editado/alterado
                aux = instancia.topo
                while aux:
                    print(aux.dado, end=" ")
                    aux = aux.prox
                print()
            else:
                print(f"Elemento {info} não encontrado. Nenhuma alteração realizada.")

        elif metodo == "--remover":
            resultado = funcao(info, novo)
            if resultado is not None:
                print(resultado)

        elif metodo == "--imprimir_fila" or metodo == "--reverse":
            funcao()

        elif metodo == "--remover_repetidos":
            resultado = funcao()
            if resultado is not None:
                print(resultado)

        else:
            resultado = funcao()
            print(resultado)

    except (ValueError, NotImplementedError) as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()

