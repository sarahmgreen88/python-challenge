#import OS
import os 
#import csv
import csv
#create path for csv 
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')
#create a with statement 
with open(budget_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    print(csvreader)
#create header row 
#write code to read each row of data after the header 
#Your task is to create a Python script that analyzes the records to calculate each of the following:

#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in losses (date and amount) over the entire period
#Export a text file with the results