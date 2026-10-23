#!/usr/bin/env python3

# Prova 2 - Estruturas de Dados FATEC
# Copyright (c) 2026 Rodrigo de Freitas
# SPDX-License-Identifier: MIT

"""
TODO
- imprimir uma fila: imprimir_fila()
- buscar elemento da fila: buscar(info)
- editar um elemento da fila: editar(info)
- buscar e remover um elemento da fila: remover(info)
- remover todas as repetições da fila: remover_repetidos()
"""

from node import Node
from abstract_structure import AbstractStructure
from typing_extensions import override # necessário para decorators override

# Queue herda de AbstractStructure apenas
class Queue(AbstractStructure):
    def __init__(self):
        self.inicio = None
        self.fim = None

    def enfileirar(self, valor: int) -> None:
        """
        Insere um elemento no final da fila.
        """
        novo = Node(valor)

        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.prox = novo
            self.fim = novo

    def imprimir_fila(self) -> None:
        """
        Imprime os elementos da fila, do início ao fim.
        """
        aux = self.inicio

        while aux:
            print(aux.dado, end=" ")
            aux = aux.prox

        print()
    
    @override
    def buscar(self, info: int) -> bool:
        """
        Busca um elemento na fila.
        Retorna True se encontrado; False caso contrário.
        main.py --queue --buscar <elementos> -- <elemento_a_ser_buscado>
        Ex: main.py --queue --buscar 1 2 3 4 5 6 -- 6
        """
        aux = self.inicio

        while aux:
            if aux.dado == info:
                return True
            aux = aux.prox

        return False

    @override
    def editar(self, info: int, novo_info: int) -> bool:
        """
        Edita um elemento da fila.
        Retorna True se o elemento foi encontrado e editado;
        False caso contrário.
        main.py --queue --buscar <elementos> -- <valor_antigo> <novo_valor>
        Ex: main.py --queue --editar 1 2 3 4 5 6 -- 3 6 (altera o valor de 3 para 6)
        """
        aux = self.inicio

        while aux:
            if aux.dado == info:
                aux.dado = novo_info
                return True

            aux = aux.prox

        return False      

    @override
    def remover(self, info: int) -> bool:
        """
        Remove um elemento da fila.
        Retorna True se o elemento foi removido;
        False caso contrário.
        main.py --queue --remover <elementos> -- <valor_a_ser_removido>
        Ex: main.py --queue --remover 1 2 3 4 5 6 -- 3 (remove o valor 3)
        """
        aux = self.inicio
        anterior = None

        while aux:
            if aux.dado == info:
                if anterior is None:
                    self.inicio = aux.prox
                else:
                    anterior.prox = aux.prox

                if aux == self.fim:
                    self.fim = anterior

    @override
    def remover_repetidos(self) -> None:
        """
        Remove os elementos repetidos da fila,
        preservando a primeira ocorrência de cada valor.
        Ex:  main.py --stack --remover_repetidos 10 20 30 20 40 10 (removerá os números repetidos)
        """
        atual = self.inicio

        while atual:
            anterior = atual
            aux = atual.prox

            while aux:
                if aux.dado == atual.dado:
                    anterior.prox = aux.prox

                    if aux == self.fim:
                        self.fim = anterior

                    aux = anterior.prox
                else:
                    anterior = aux
                    aux = aux.prox

            atual = atual.prox

    