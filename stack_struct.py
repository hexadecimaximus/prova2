#!/usr/bin/env python3

# Prova 2 - Estruturas de Dados FATEC
# Copyright (c) 2026 Rodrigo de Freitas
# SPDX-License-Identifier: MIT

from node import Node
from abstract_structure import AbstractStructure
from typing_extensions import override # necessário para decorators override

# a classe atual herda de AbstractStructure
class Stack(AbstractStructure):
    def __init__(self):
        self.topo = None
        # classe base usa o construtor padrão de Python, não necessita de `super().__init__()`

    def esta_vazia(self) -> bool:
        return self.topo is None

    def empilhar(self, dado: int) -> None:
        novo = Node(dado)
        novo.prox = self.topo
        self.topo = novo

    @override
    def buscar(self, info: int) -> bool:
        """
        Busca um elemento na pilha.
        Retorna True se encontrado; caso contrário, False.
        """
        aux = self.topo

        while aux:
            if aux.dado == info:
                return True
            aux = aux.prox

        return False
    
    @override
    def editar(self, info: int, novo_info: int) -> bool:
        """
        Busca um elemento na pilha e altera seu valor.
        Retorna True se editado; caso contrário, False.
        Forma de uso:
        main.py --stack --editar <elements> -- <valor_antigo> <novo_valor>
        Ex: main.py --stack --editar 1 2 3 4 5 6 -- 3 6 (altera o valor de 3 para 6)
        """
        aux = self.topo

        while aux:
            if aux.dado == info:
                aux.dado = novo_info
                return True

            aux = aux.prox

        return False
    
    @override
    def remover(self, info: int) -> bool:
        """
        Busca e remove um elemento da pilha.
        Retorna True se removido; caso contrário, False.
        main.py --stack --remover <elements> -- <valor_a_ser_removido>
        Ex: main.py --stack --remover 1 2 3 4 5 6 -- 3 (remove o valor 3)
        """
        aux = self.topo
        anterior = None

        while aux:
            if aux.dado == info:
                if anterior is None:
                    self.topo = aux.prox
                else:
                    anterior.prox = aux.prox

                return True

            anterior = aux
            aux = aux.prox

        return False

    def remover_repetidos(self) -> None:
        """
        Remove os valores repetidos da pilha,
        preservando a primeira ocorrência encontrada a partir do topo.
        Ex:  main.py --stack --remover_repetidos 10 20 30 20 40 10 (removerá os números repetidos)
        """
        atual = self.topo

        while atual:
            anterior = atual
            aux = atual.prox

            while aux:
                if aux.dado == atual.dado:
                    anterior.prox = aux.prox
                    aux = anterior.prox
                else:
                    anterior = aux
                    aux = aux.prox

            atual = atual.prox


