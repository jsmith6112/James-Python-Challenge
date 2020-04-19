# -*- coding: utf-8 -*-
# Import Modules/Dependencies

import os
import csv
 
# Establish Variables for the upcoming analysis
total_mos = 0
Total_PNL = 0
Profit_incr_Max = 0 
avg_chg = 0
Net_chg_List = []
Profit_Incr_Max = ["", 100]
Profit_Decr_Max = ["", 0.0]
Monthly_Chg=[]
Month_Count=0


# Set Path For File

csvpath= os.path.join('Resources','budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile, delimiter=',')

    print(csv_reader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csv_reader)
    
    #print(f"CSV Header: {csv_header}")
    Previous_row = 0
    
#    print(Previous_row)    
        
 #Calculate Total Number Of Months, Net Amount Of "Profit/Losses" & Set Variables For Rows

    for row in csv_reader:
    #net_amount += int(row[1])
        Profit_incr_Max = int(row[1])
    
        Profit_incr_date = row[0]   

        #Total_PNL += int(row[1]
        ProfitLoss = int(row[1])
        Total_PNL=ProfitLoss + Total_PNL
        print(ProfitLoss)
        Net_chg = ProfitLoss - Previous_row
        Net_chg_List.append(Net_chg)         
        Date = row[0]
        Month_Count += 1
        Previous_row=int(row[1])
        
        if Net_chg < Profit_Decr_Max[1]:
            Profit_Decr_Max[1] = Net_chg
            Profit_Decr_Max[0] = Date
            Net_chg=0
        elif Net_chg > Profit_Incr_Max[1]:
            Profit_Incr_Max[1] = Net_chg
            Profit_Incr_Max[0] = Date
            Net_chg=0                
        #Monthly Calcs for Profit & Loss, Monthly change, etc.
Net_Chgnew = Net_chg_List[1:]
#print(Net_chg_List)        
print(Profit_Incr_Max)  
print(Profit_Decr_Max)          
avg_chg = sum(Net_Chgnew)/(Month_Count-1)

print("*****************************")
print("")
print("*****Financial Analysis*******")
print("")
print(f"Total Months: {Month_Count}")
print(f"The Total Profit is {Total_PNL}")
print(f"Maximum gain occured in {Profit_Incr_Max[0]} and was {Profit_Incr_Max[1]}")
print(f"Maximum loss occured in {Profit_Decr_Max[0]} and was {Profit_Decr_Max[1]}")
print(f"The average change in Profit was {avg_chg} over the entire period")

print("")
print("*****************************")
       
        
#Oupt file to text
output_path = os.path.join('Analysis', 'Pybankoutput.txt')
    
with open (output_path,'w') as newFile:
    newFile.write(("*****************************\n"))    
#    newFile.write(("")
    newFile.write(("*****Financial Analysis*******\n"))
    newFile.write((""))
    newFile.write((f"Total Months: {Month_Count+1}\n"))
    newFile.write((f"The Total Profit is {Total_PNL}\n"))
    newFile.write((f"Maximum gain occured in {Profit_Incr_Max[0]} and was {Profit_Incr_Max[1]}\n"))
    newFile.write((f"Maximum loss occured in {Profit_Decr_Max[0]} and was {Profit_Decr_Max[1]}\n"))
    newFile.write((f"The average change in Profit was {avg_chg} over the entire period\n"))














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