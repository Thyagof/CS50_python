import requests
from random import randint
from pyfiglet import Figlet
import inflect

p = inflect.engine()
figlet = Figlet()

class Pokemon:
    GENERATIONS = {
        1: [1, 150],
        2: [151, 251],
        3: [252, 386],
        4: [387, 493],
        5: [494, 649],
        6: [650, 721],
        7: [722, 809],
        8: [810, 905],
        9: [906, 1025]
    }  

    def __init__(self, poke_id, name, type1, type2, height, weight):
        self.poke_id = poke_id
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.height = height
        self.weight = weight
        
        for gen in Pokemon.GENERATIONS:
            if self.poke_id >= Pokemon.GENERATIONS[gen][0] and self.poke_id <= Pokemon.GENERATIONS[gen][1]:
                self.gen = gen
                break

    @property
    def poke_id(self):
        return self._poke_id

    @poke_id.setter
    def poke_id(self, poke_id):
        self._poke_id = poke_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name != "":
            self._name = name.capitalize() 
    
    @property
    def type1(self):
        return self._type1

    @type1.setter
    def type1(self, type1):
        if type1 != "":
            self._type1 = type1.capitalize() 

    @property
    def type2(self):
        return self._type2

    @type2.setter
    def type2(self, type2):
        if type2 == None:
            self._type2 = "None"
        else: 
            self._type2 = type2.capitalize() 

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height
    
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

def main():
    figlet.setFont(font="big")
    print(figlet.renderText("POKEDLE"))
    figlet.setFont(font="drpepper")
    print(figlet.renderText("A Pokemon Wordle-like"))
    game()
    while True:
        print("\nPlay again?") 
        print("Press 1 to continue")
        print("Press 2 to quit")
        x = int(input())
        if x == 1:
            game()
        elif x == 2:
            break
        else:
            print("invalid command")

def game():
    while True:
        try:
            gen_a = int(input("Select the starting generation: "))
            if not valid_gen(gen_a):
                print("Invalid generation")
            else:
                break
        except:
            pass
    
    while True:
        try:
            gen_b = int(input("Select the ending generation: "))
            if not valid_gen(gen_a, gen_b):
                print("Invalid generation")
            else:
                break
        except:
            pass

    start, ending = get_gen_index(gen_a, gen_b)
    poke_number = randint(start,ending)
    poke = get_pokemon(poke_number)
    i = 0
    while i < 9:
        print("\nYou have " + str(9-i) + p.plural(" guess", 9-i))
        guess = input("Who's that pokémon? ").lower()
        if guess != poke.name.lower():
            poke_guess = get_pokemon(guess)
            if poke_guess != None:
                if poke.gen > poke_guess.gen:
                    print("Gen: " + str(poke_guess.gen) + " 🔺")
                elif poke.gen < poke_guess.gen:
                    print("Gen: " + str(poke_guess.gen) + " 🔻")
                else: 
                    print("Gen: " + str(poke.gen) + " ✅")
                print("Name: " + poke_guess.name + " ❌")
                if poke.type1 != poke_guess.type1:
                    print("Type 1: " + poke_guess.type1 + " ❌")
                else:
                    print("Type 1: " + poke_guess.type1 + " ✅")
                if poke.type2 != poke_guess.type2:
                    print("Type 2: " + poke_guess.type2 + " ❌")
                else: 
                    print("Type 2: " + poke_guess.type2 + " ✅")
                if poke.height > poke_guess.height:
                    print("Height: " + str(poke_guess.height) + " 🔺")
                else:
                    print("Height: " + str(poke_guess.height) + " 🔻")
                if poke.weight > poke_guess.weight:
                    print("Weight: " + str(poke_guess.weight) + " 🔺")
                else:
                    print("Weight: " + str(poke_guess.weight) + " 🔻", end="\n\n")
                i += 1
            else:
                print("Pokémon not found, try again.")
        else:    
            break
    if i != 9:
        print("\nYou won!")
        print("The secret Pokémon was:")
        print("Gen: " + str(poke.gen) + " ✅")
        print("Name: " + poke.name + " ✅")
        print("Type 1: " + poke.type1 + " ✅")
        print("Type 2: " + poke.type2 + " ✅")
        print("Height: " + str(poke.height) + " ✅")
        print("Weight: " + str(poke.weight) + " ✅")
    else:
        print("\nYou lose!")
        print("The secret Pokémon was: " + poke.name)

def valid_gen(gen_a, gen_b=None):
    if gen_b == None:
        if gen_a < 1 or gen_a > 9:
            return False
        else:
            return True
    else:
        if gen_b < gen_a or gen_b > 9:
            return False
        else:
            return True

def get_gen_index(gen_a, gen_b):
    start_index = Pokemon.GENERATIONS[gen_a][0]
    end_index = Pokemon.GENERATIONS[gen_b][1]
    return start_index, end_index

def get_pokemon(poke):
    try:
        response = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(poke))
    except requests.RequestException:
        return None
    
    try:
        r = response.json()
    except requests.exceptions.JSONDecodeError:
        return None

    if len(r["types"]) == 1:
        poke = Pokemon(r["id"],
                    r["name"], 
                    r["types"][0]["type"]["name"],
                    None,
                    r["height"],
                    r["weight"])
    else:
        poke = Pokemon(r["id"],
                    r["name"], 
                    r["types"][0]["type"]["name"],
                    r["types"][1]["type"]["name"],
                    r["height"],
                    r["weight"])
    return poke

if __name__ == "__main__":
    main()