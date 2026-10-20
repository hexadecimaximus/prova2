#!/usr/bin/env python3

from abc import ABC, abstractmethod

class AbstractStructure(ABC):
    """
    Stack e Queue compartilham dos mesmos métodos: buscar, editar e remover.
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