#!/usr/bin/env python3

# Prova 2 - Estruturas de Dados FATEC
# Copyright (c) 2026 Rodrigo de Freitas
# SPDX-License-Identifier: MIT

class Node:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

    def __str__(self) -> str:
        return str(self.dado)
