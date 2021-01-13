#import OS
import os
#import csv
import csv
# create path for csv
budget_csv = os.path.join('Resources', 'budget_data.csv')
text_path="output_Pybank.txt"
totalmonths=[]
profittotal=[]
monthlychange=[]
avg_list=[]
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
    
  
    #Go through list and keep track of profit/loss average
    for i in range(1, len(profittotal)):
        #Create a list for the average change
        monthlychange.append(profittotal[i]-profittotal[i-1])
        #Find Average Change
        avg_list=round(sum(monthlychange)/len(monthlychange),2)
       
    print("Financial Analysis")
    print("---------------------------------------")
    print(f"Total Months: {len(totalmonths)}")
    print(f"Total: ${sum(profittotal)}")
    print(f"Average Change: (${avg_list})")
    print(f"Greatest Increase in Profits: {totalmonths[monthlychange.index(max(monthlychange))+1]} ({max(monthlychange)})")
    print(f"Greatest Decrease in Profits: {totalmonths[monthlychange.index(min(monthlychange))+1]} ({min(monthlychange)})")

    with open(text_path, "w") as file:
        file.write("Financial Analysis\n")
        file.write("---------------------------------------\n")
        file.write(f"Total Months: {len(totalmonths)}\n")
        file.write(f"Total: ${sum(profittotal)}\n")
        file.write(f"Average Change: (${avg_list})\n")
        file.write(f"Greatest Increase in Profits: {totalmonths[monthlychange.index(max(monthlychange))+1]} ({max(monthlychange)})\n")
        file.write(f"Greatest Decrease in Profits: {totalmonths[monthlychange.index(min(monthlychange))+1]} ({min(monthlychange)})\n")