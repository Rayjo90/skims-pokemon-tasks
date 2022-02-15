"""Install this library."""
import requests

# Task 1
def fetch_details_from_pokemon(url, name: str):
    """This method will fetch details from pokemon server and get the json response like postman."""
    try:
        # making url based on name.. after making urls it will looks loke "https://pokeapi.co/api/v2/pokemon/{name}".
        url = url + f"/{name.lower()}"
        response = requests.get(url)
        response.raise_for_status()

        # returning if there is no error json object
        return response.json()
    except Exception as err:
        print("Error occured while fetching details from pokemon. ", err)


# gives names of pokemons
names = ["pikachu", "eevee", "snorlax", "charizard", "garchomp"]


# 2 apis needed.
url1 = "https://pokeapi.co/api/v2/pokemon"
url2 = "https://pokeapi.co/api/v2/pokemon-species"

pokemons = []

# iterate through names one by one.
for name in names:
    try:
        pokemon = {}

        # fetching details for every pokemon name from above method
        res = fetch_details_from_pokemon(url1, name)
        # print(res)

        # storing details of pokemon dictionary
        pokemon["name"] = res.get("name", None)
        pokemon["height"] = res.get("height", 0)
        pokemon["weight"] = res.get("weight", 0)

        # will store 2 random moves if there is in json object otherwise 0.
        moves = res.get("moves", [])
        if len(moves) == 1:
            pokemon["moves1"] = moves[0]["move"]["name"]
        elif len(moves) >= 2:
            pokemon["moves1"] = moves[0]["move"]["name"]
            pokemon["moves2"] = moves[1]["move"]["name"]

        # fetching color and base_happiness from 2nd api.
        res = fetch_details_from_pokemon(url2, name)
        pokemon["color"] = res.get("color", {}).get("name", None)

        # will store base_happiness if there is in json object otherwise 0.
        pokemon["base_happines"] = res.get("base_happiness", 0)
        pokemons.append(pokemon)
    except Exception as err:
        print("Error: ", err)


# Task 2

base_happiness = []

for pokemon in pokemons:
    print(pokemon)
    base_happiness.append(pokemon["base_happines"])


print(base_happiness)  


# list of elements to calculate mean
n = len(base_happiness)  
get_sum = sum(base_happiness)  
mean = get_sum / n  

print("Mean / Average is: " + str(mean))  


# list of elements to calculate median
n = len(base_happiness)  
base_happiness.sort()  

# if n is even then we need to find average of middle two number.
if n % 2 == 0:
    median1 = base_happiness[n // 2]  
    median2 = base_happiness[n // 2 - 1]  
    median = (median1 + median2) / 2  
else:  
    median = base_happiness[n // 2]  
print("Median is: " + str(median)) 
