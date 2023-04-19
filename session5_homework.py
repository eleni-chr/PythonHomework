# Question 1
# You're having coffee/tea/beverage of your choice with a friend that is learning to program in Python. They're curious
# about why they would use pip. Explain what pip is and one benefit of using pip.

# My answer to Question 1
# PIP is a package manager used to install libraries that other people have written. The benefit is that you don't have
# to write everything yourself from scratch.

# Question 2
# This program should save my data to a file, but it doesn't work when I run it. What is the problem and how do I fix it?
# poem = 'I like Python and I am not very good at poems'
# with open('poem.txt', 'r') as poem_file:
#     poem_file.write(poem)

# My answer to Question 2
# The 'r' should be changed to 'w+'

poem = 'I like Python and I am not very good at poems'
with open('poem.txt', 'w+') as poem_file:
    poem_file.write(poem)

# Question 3
# In this session you used the Pokemon API to retrieve a single Pokemon. I want a program that can retrieve multiple
# Pokemon and save their names and moves to a file.
# Use a list to store about 6 Pokemon IDs. Then in a for loop call the API to retrieve the data for each Pokemon. Save
# their names and moves into a file called 'pokemon.txt'

# My answer to Question 3
import requests

# Replace with the list of Pokemon IDs you want to retrieve
pokemon_ids = [1, 2, 3, 4, 5, 6]

# URL for the Pokemon API
api_url = "https://pokeapi.co/api/v2/pokemon/"

# Open a file called 'pokemon.txt' in write mode
with open('pokemon.txt', 'w') as file:
    # Iterate through the list of Pokemon IDs
    for id in pokemon_ids:
        # Make an HTTP request to get the Pokemon data
        response = requests.get(api_url + str(id))
        if response.status_code == 200:
            # If the response is successful, parse the JSON data
            data = response.json()

            # Get the Pokemon name and its moves
            name = data['name']
            moves = [move['move']['name'] for move in data['moves']]

            # Write the Pokemon name and moves to the file
            file.write(f"Pokemon: {name}\n")
            file.write("Moves:\n")
            for move in moves:
                file.write(f"- {move}\n")
            file.write("\n")
        else:
            print(f"Failed to fetch data for Pokemon ID {id}")

print("Finished saving Pokemon data to 'pokemon.txt'")
