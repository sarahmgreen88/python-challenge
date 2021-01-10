#import OS
import os
#import csv
import csv
# create path for csv
budget_csv = os.path.join('Resources', 'budget_data.csv')
totalmonths=[]
profittotal=[]
greatestinc=[]
greatestdec=[]
    
# create a with statement
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
# create header row
    csv_header = next(csvreader)   
# write code to read each row of data after the header
    for row in csvreader:
        # The total number of months included in the dataset
        totalmonths.append(row[0])
        # The net total amount of "Profit/Losses" over the entire period
        profittotal.append(int(row[1]))
print("Financial Analysis")
print("---------------------------------------")
print(f"Total Months: {len(totalmonths)}")
print(f"Total: ${sum(profittotal)}")



# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period
# Export a text file with the results