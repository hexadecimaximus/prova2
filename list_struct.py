#!/usr/bin/env python3

# Prova 2 - Estruturas de Dados FATEC
# Copyright (c) 2026 Rodrigo de Freitas
# SPDX-License-Identifier: MIT

""" TODO
- : min()
- : max()
- : sum()
- : avg()
- : len()

2.
- função que concatene uma segunda lista no final da sua lista principal: append(outra_lista)
- (*
"""


from node import Node

class List:
    def __init__(self):
        self.cabeca = None

    def esta_vazia(self):
        if self.cabeca:
            return False
        else:
            return True

    def inserir_lista(self, dado):
        """
        insere dados no início da lista
        """
        novo = Node(dado)
        novo.prox = self.cabeca
        self.cabeca = novo

    def min(self):
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

    def max(self):
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

    def sum(self):
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

    def len(self):
        """
        função que retorna a quantidade de elemento da lista
        """
        total = 0
        aux = self.cabeca

        while aux:
            total += 1
            aux = aux.prox

        return total

    def avg(self):
        """
        função que retorna a média dos elementos da lista
        """
        tamanho = self.len()

        if tamanho == 0:
            raise ValueError("Não é possível calcular a média de uma lista vazia.")

        return self.sum() / tamanho

    def reverse(self):
        """
        função que inverte uma lista
        Nota: como os ítens são inseridos no começo da lista, na verdade
        essa lista só faz percorrer e imprimir a lista :P
        """
        aux = self.cabeca

        while aux:
            print(aux.dado, end=" ")
            aux = aux.prox

        

