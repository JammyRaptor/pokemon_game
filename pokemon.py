from database import fetch

class pokemon:
    def __init__(self, id):
        details = fetch.pokemon_details(id)
        self.ID = details['ID']
        self.Name = details['Name']
        self.Type1 = details['Type 1']
        self.Type2 = details['Type 2']
        self.Total = details['Total']
        self.HP = details['HP']
        self.Attack = details['Attack']
        self.Defence = details['Defence']
        self.Sp.Atk = details['Sp. Atk']
        self.Sp.Def = details['Sp. Def']
        self.Speed = details['Speed']
        self.Generation = details['Generation']
        self.Legendary = details['Legendary']