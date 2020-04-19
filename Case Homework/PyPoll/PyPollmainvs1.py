# -*- coding: utf-8 -*-
# Import Modules/Dependencies

import os
import csv
 
Votes_Cast=0
Correy_Count=0




# Set Path For File


csvpath= os.path.join('Resources','election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
 #   csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
  
  #  PNL=0

    # Read each row of data after the header
    for row in csvreader:
        Candidate = row[2]
        County = row[1]
        Votes_Cast = Votes_Cast + 1
        if Candidate == "Correy":
            Correy_Count = Correy_Count + 1
        elif Candidate =="Khan":
            Khan_Count = Khan_Count +1
        elif Candidate =="Li":
            Li_Count = Li_Count+1
        else OT_Count = OT Count +1
        
        
print(Correy_Count)


print("*****************************")
print("")
print(f"Total Votes: {Votes_Cast}")
print(f"Votes for Correy: {Correy_Count}")
print(f"Insert count")

print("")
print("*****************************")

        

    















'''
# Open & Read CSV File
    # CSV Reader Specifies Delimiter & Variable That Holds Contents

 
   # Read The Header Row First (Skip This Step If There Is No Header)
    # Calculate Total Number Of Months, Net Amount Of "Profit/Losses" & Set Variables For Rows
    # Read Each Row Of Data After The Header
    for row in csvreader:
        # Calculate Total Number Of Months Included In Dataset
        # Calculate Net Amount Of "Profit/Losses" Over The Entire Period
        # Calculate Change From Current Month To Previous Month
        # Calculate The Greatest Increase
        # Calculate The Greatest Decrease
    # Calculate The Average & The DateEditor

        # Print Analysis
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")
# Specify File To Write To
# Open File Using "Write" Mode. Specify The Variable To Hold The Contents
# Write New Data
    .write(f"Financial Analysis\n")
   .write(f"---------------------------\n")
    .write(f"Total Months: {total_months}\n")
    .write(f"Total: ${net_amount}\n")
    .write(f"Average Change: ${average_change}\n")
    pwrite(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
   .write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")
        
        
This is a temporary script file.
'''