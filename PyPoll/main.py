#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------


#Import OS
import os
#Import CSV
import csv
#create path for csv
election_csv = os.path.join('Resources', 'election_data.csv')
text_path="output_PyPoll.txt"
#variables
total_votes=0
candidate_name=[]
candidate_list={}
wordcount=[]
Khan = 0
Correy=0
Li=0
O_Tooley=0
#create a with statement
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
#Create Header row
    csv_header = next(csvreader) 
    for row in csvreader:
#The total number of votes cast
       total_votes+=1
#Get candidate name from each row
       candidate_name.append(row[2])
    #The total number of votes each candidate won
    Khan = int(candidate_name.count("Khan"))
    Correy=int(candidate_name.count("Correy"))
    Li=int(candidate_name.count("Li"))
    O_Tooley=int(candidate_name.count("O'Tooley"))
    #Calculate Percentages for each candidate
    K_percent=round((Khan / total_votes)*100,3)
    C_percent= round((Correy/total_votes)*100,3)
    L_percent=round((Li/total_votes)*100,3)
    O_percent=round((O_Tooley/total_votes)*100,3)
#The winner of the election based on popular vote.
    if Khan>Correy>Li>O_Tooley:
        winner="Khan"
    elif Correy>Khan>Li>O_Tooley:
        winner="Correy"
    elif Li>Correy>Khan>O_Tooley:
        winner="Li"
    elif O_Tooley>Li>Correy>Khan:
        winner="O'Tooley"
#Print Results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Khan: {K_percent}% ({Khan})")
print(f"Correy: {C_percent}% ({Correy})")
print(f"Li:{L_percent}% ({Li})")
print(f"O'Tooley: {O_percent}% ({O_Tooley})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#Write results to a text file 
with open(text_path, "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    file.write(f"Khan: {K_percent}% ({Khan})\n")
    file.write(f"Correy: {C_percent}% ({Correy})\n")
    file.write(f"Li:{L_percent}% ({Li})\n")
    file.write(f"O'Tooley: {O_percent}% ({O_Tooley})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
