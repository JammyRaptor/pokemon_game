import sqlite3
from sqlite3 import Error

with open('pokemon_data.txt', 'r') as file:
    p = file.read()

rows = p.split('\n')
pokemons = []
for row in rows:
    pokemons.append(row.split(','))

headings = pokemons.pop(0)

con = sqlite3.connect('database.db')
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS pokemon(id integer PRIMARY KEY, Name text, Type1 text,type2 text,Total integer,HP integer,Attack integer,Defense integer,SpAtk integer,SpDef integer, Speed integer,Generation integer,Legendary boolean)")
con.commit()
# id,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary
for p in pokemons:
    pokemon = (int(p[0]), p[1], p[2], p[3], int(p[4]), int(p[5]),int(p[6]),int(p[7]),int(p[8]),int(p[9]),int(p[10]),int(p[11]),p[12])
    try:
        cur.execute('INSERT INTO pokemon(id, Name, Type1, Type2, Total, HP, Attack, Defense, SpAtk, SpDef, Speed, Generation, Legendary) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)', pokemon)
        con.commit()
    except:
        pass