import csv

with open("pokemon.csv") as f:
    # Skip the first line of the file
    next(f)

    # Create a csv reader object
    data = csv.reader(f)

    # Print each row
    for line in data:
        print(" id: {0} , typeTwo: {1}, name:  {2}, type: {3}"
              .format(line[0], line[1], line[2], line[3]))
