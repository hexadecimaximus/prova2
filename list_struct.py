#!/usr/bin/env python3

# Prova 2 - Estruturas de Dados FATEC
# Copyright (c) 2026 Rodrigo de Freitas
# SPDX-License-Identifier: MIT

from node import Node
from typing import Optional, Union # se Python for superior a 3.10, não precisa dessa linha

class List():
    def __init__(self):
        self.cabeca = None

    def esta_vazia(self) -> bool:
        if self.cabeca:
            return False
        else:
            return True

    def inserir_lista(self, dado: Union[int, str]) -> None:
        """
        insere dados no início da lista
        """
        novo = Node(dado)
        novo.prox = self.cabeca
        self.cabeca = novo

    def min(self) -> int:
        """
        função que retorna o menor elemento da lista
        """
        if self.esta_vazia():
            raise ValueError("Não é possível obter o mínimo de uma lista vazia.")

        aux = self.cabeca
        min_value = aux.dado

        while aux:
            if aux.dado < min_value:
                min_value = aux.dado

            aux = aux.prox

        return min_value

    def max(self) -> int:
        """
        função que retorna o maior elemento da lista
        """
        if self.esta_vazia():
            raise ValueError("Não é possível obter o máximo de uma lista vazia")

        aux = self.cabeca
        max_value = aux.dado

        while aux:
            if aux.dado > max_value:
                max_value = aux.dado

            aux = aux.prox
        
        return max_value

    def sum(self) -> int:
        """
        função que retorna a soma dos elementos da lista
        """
        
        # função anônima responsável pela soma
        somar = lambda a, b: a + b

        total = 0
        aux = self.cabeca

        while aux:
            total = somar(total, aux.dado)
            aux = aux.prox

        return total

    def len(self) -> int:
        """
        função que retorna a quantidade de elemento da lista
        """
        total = 0
        aux = self.cabeca

        while aux:
            total += 1
            aux = aux.prox

        return total

    def avg(self) -> float:
        """
        função que retorna a média dos elementos da lista
        """
        tamanho = self.len()

        if tamanho == 0:
            raise ValueError("Não é possível calcular a média de uma lista vazia.")

        return self.sum() / tamanho

    def reverse(self) -> None:
        """
        função que inverte uma lista
        Nota: como os itens são inseridos no início da lista,
        a ordem dos elementos já está invertida em relação
        à sequência de inserção. Portanto, basta percorrer
        e imprimir os nós. :P
        """
        aux = self.cabeca

        while aux:
            print(aux.dado, end=" ")
            aux = aux.prox


    def append(self, args: list[str]) -> None:
        """
        Concatena os valores, ignorando o separador '--'.
        """
        if not args:
            raise ValueError("Informe os valores para concatenar.")

        for valor in reversed(args):
            if valor != "--":
                self.inserir_lista(valor)

        aux = self.cabeca

        while aux:
            print(aux.dado, end="")

            aux = aux.prox

            if aux:
                print("", end="")

        print()

            

