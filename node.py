#!/usr/bin/env python3

class Node:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

    def __str__(self):
        return str(self.dado)
