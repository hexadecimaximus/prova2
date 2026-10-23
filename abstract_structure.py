#!/usr/bin/env python3

# Prova 2 - Estruturas de Dados FATEC
# Copyright (c) 2026 Rodrigo de Freitas
# SPDX-License-Identifier: MIT

from abc import ABC, abstractmethod

class AbstractStructure(ABC):
    """
    Stack e Queue compartilham dos mesmos métodos: buscar, editar, remover e remover_repetidos.
    Mas cada classe implementará o seu (override) de acordo com suas necessidades
    """

    @abstractmethod
    def buscar(self, info: int) -> bool:
        pass

    @abstractmethod
    def editar(self, info: int, novo_info: int) -> bool:
        pass

    @abstractmethod
    def remover(self, info: int) -> bool:
        pass

    @abstractmethod
    def remover_repetidos(self) -> None:
        pass 