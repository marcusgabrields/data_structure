"""Implementações de funções hash"""


def hash_by_module(key, table_positions=10):
    table_positions = table_positions
    return key % table_positions
