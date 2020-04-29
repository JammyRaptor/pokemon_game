import sqlite3
from sqlite3 import Error

def pokemon_details(id):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute(f"SELECT * FROM pokemon WHERE id={id}")
    result = cur.fetchall()
    results = {'ID': result[0], 'Name': result[1], 'Type 1': result[2], 'Type 2': result[3], 'Total': result[4], 'HP': result[5], 'Attack': result[6], 'Defence': result[7], 'Sp. Atk': result[8], 'Sp. Def': result[9], 'Speed': result[10], 'Generation': result[11], 'Legendary': result[12]}
    return results