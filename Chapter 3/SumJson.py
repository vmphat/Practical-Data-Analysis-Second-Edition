import json
import csv
from collections import defaultdict
from pprint import pprint

# Define a dictionary to store the type of Pokemon
#   and the number of Pokemon of that type
typePokemon = defaultdict(int)

# Open the JSON file and load the data
with open("pokemon.json") as f:
    data = json.loads(f.read())

    # Fill the dictionary with sum of Pokemon of each type
    for line in data:
        typePokemon[line["type"]] += 1

# Open a CSV file to write the results
with open("sumPokemon.csv", "w") as a:
    w = csv.writer(a)

    # Write the header of the CSV file
    w.writerow(["type", "amount"])

    # Sort the dictionary by the number of Pokemon
    # Write the result (type, number of Pokemon) to the CSV file
    for key, value in sorted(
        typePokemon.items(), key=lambda x: x[1]
    ):
        w.writerow([str(key).strip(), str(value).strip()])

    # Use "pretty print" to display the dictionary
    pprint(typePokemon)
