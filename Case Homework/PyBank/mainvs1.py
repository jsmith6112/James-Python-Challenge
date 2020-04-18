# -*- coding: utf-8 -*-
# Import Modules/Dependencies

import os
import csv
import pandas as pd

# Variables
#total_mos = 
# total_pnl
#Profit_incr_Max 
#Profit_incr_date
#Monthly_Chg
#Month_Count
#Profit_Decrease_Max
#Profit_Decrease_date
#Total

# Set Path For File


csvpath= os.path.join('Resources','budget_data.csv')


budgetdata_pd = pd.read_csv(csvpath)

print(budgetdata_pd)

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