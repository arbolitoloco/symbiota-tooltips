# Creates multiple JSON files with all the data in the CSV file
# The API endpoints will be defined by the `path` column in the CSV file
# JSON will be nested if the column contains a `/`
# author: Laura Rocha Prado
# date: 2022-01-04

import os, csv, json
# ***** Configure generator ******
version = "1_0" # Version of the generator
inputFilename = "pages.csv" # Name of the input file to be converted to json
inputfile = os.path.abspath(os.path.join("data", inputFilename))

def process(header, value, record):
    key, other = header.partition('/')[::2]
    if other:
        process(other, value, record.setdefault(key, {}))
    else:
        record[key] = value

# # Read the CSV and add data to a dictionary
with open(inputfile) as csvFile:
  csvReader = csv.DictReader(csvFile)
  data = {}
  for row in csvReader:
      structure = os.path.join("api", "v"+version, row['path']) # Path to the structure (api/v1/), add last endpoint to CSV in column 'path'
      outputFileName = row['id']+'.json' # Name of the output file (pick desired column from CSV)
      outputfile = os.path.abspath(os.path.join(structure, outputFileName))
      os.makedirs(os.path.dirname(outputfile), exist_ok=True)
      groupBy = 'data' # Root-level node for JSON file
      # # Processes the CSV to nest the JSON data based on headings that include a '/'
      data[row['id']] = record = {}
      for header, value in row.items():
            process(header, value, record)
      root = {}
      root[groupBy] = record
      # # Write data to JSON file
      with open(outputfile, "w") as jsonFile:
            jsonFile.write(json.dumps(root, indent=4, ensure_ascii=False))      
            print("Created JSON files and folders to: " + outputfile)