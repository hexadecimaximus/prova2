#!/usr/bin/env python3

# Prova 2 - Estruturas de Dados FATEC
# Copyright (c) 2026 Rodrigo de Freitas
# SPDX-License-Identifier: MIT

"""
TODO
- função que busque um elemento de uma pilha. buscar(info)
- função que edite um elemento de uma pilha. editar(info)
- função que busque e remova um elemento de uma pilha. remover(info)
- função que remova a todos os valores repetidos de uma pilha. remover_repetidos()
"""

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
        raise NotImplementedError("Método ainda não implementado.")

    @override
    def remover(self, info: int) -> bool:
        raise NotImplementedError("Método ainda não implementado.")

