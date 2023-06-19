# In the API session you used the Pokémon API to retrieve a single Pokémon.
# Now use a list to store 6 Pokémon IDs. In a for loop call the API to retrieve the data
# for each Pokémon. Save their names, height and weight in to a file called
# 'pokemon.txt

import requests

pokemon_ids = [1, 2, 3, 4, 5, 6]

with open('pokemon.txt', 'w') as file:
    for pokemon_id in pokemon_ids:
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}'
        response = requests.get(url)

        if response.status_code == 200:
            pokemon_data = response.json()
            pokemon_name = pokemon_data['name']
            pokemon_height = pokemon_data['height']
            pokemon_weight = pokemon_data['weight']

            file.write(f"Name: {pokemon_name}\n")
            file.write(f"Height: {pokemon_height}\n")
            file.write(f"Weight: {pokemon_weight}\n")
            file.write('\n')  # Add a newline between each Pokémon's data

print("Pokémon data has been saved to 'pokemon.txt'")