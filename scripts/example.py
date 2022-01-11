# Creates one single JSON file with all the data in the CSV file
# The API endpoint will be manually defined by the user
# author: Laura Rocha Prado
# date: 2022-01-04

import os, csv, json
# ***** Configure generator ******
version = "1_0" # Version of the generator
groupBy = "root" # Endpoint and group name
structure = os.path.join("api", "v"+version, groupBy) # Path to the structure (api/v1/lands)

inputFilename = "Brazil_indigenous_lands.csv" # Name of the input file to be converted to json
outputFilename = "index.json" # Name of the output file, do not change

inputfile = os.path.abspath(os.path.join("data", inputFilename))
outputfile = os.path.abspath(os.path.join(structure, outputFilename))

os.makedirs(os.path.dirname(outputfile), exist_ok=True)

# # Read the CSV and add data to a dictionary
with open(inputfile) as csvFile:
  csvReader = csv.DictReader(csvFile)

  # Add data to a root node
  root = {}
  root[groupBy] = [row for row in csvReader]

  # # Write data to JSON file
  with open(outputfile, "w") as jsonFile:
    jsonFile.write(json.dumps(root, indent=4))
  print("Created JSON files and folders to: " + outputfile)