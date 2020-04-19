# Import CSV and OS for this exercise
import os
import csv

# Define path to CSV file
cereal_csv = os.path.join("..","Resources", "cereal.csv")

with open(cereal_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader,'none')    
    
# Read in rows, Establish names for necessary variables
    for row in csvreader:
        Name = row[0]
        Fiber = float(row[7])
        Sugar = float(row[9])
        Calor = float(row[3])
# Set Criteria for data to share and print to terminal    
        if Fiber >=5:
            
            print(f"{Name} contains: {Fiber} g Fiber {Sugar} g Sugar & {Calor} Calories")
            print("****************************************************************")