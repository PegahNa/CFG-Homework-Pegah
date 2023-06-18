# In the API session you used the Pokémon API to retrieve a single Pokémon.
# Now use a list to store 6 Pokémon IDs. In a for loop call the API to retrieve the data
# for each Pokémon. Save their names, height and weight in to a file called
# 'pokemon.txt

import requests

def save_pokemon_data(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    data = response.json()

    name = data["name"]
    height = data["height"]
    weight = data["weight"]

    with open("pokemon.txt", "a") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Height: {height}\n")
        file.write(f"Weight: {weight}\n")
        file.write("\n")

def main():
    pokemon_ids = [1, 2, 3, 4, 5, 6]

    for pokemon_id in pokemon_ids:
        save_pokemon_data(pokemon_id)

if __name__ == "__main__":
    main()