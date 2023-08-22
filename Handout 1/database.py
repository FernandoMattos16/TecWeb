import sqlite3

def Database(nome):
    conn = sqlite3.connect(nome)
    return conn