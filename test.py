
import os
import csv

#set path for file
csvpath = os.path.join ("Resources", "election_data.csv")
outpath = os.path.join ("analysis", "election_data.txt")

total_votes =0
charles_votes =0
diana_votes =0
raymond_votes =0
vote_percentage =0
winning_count =0
winning_percentage =0 
winning_candidate =0
diana_percentage =0

#open and read the csv
with open (csvpath) as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter = ',')

    next(csv_reader)

    for row in csv_reader:

        total_votes +=1
        canidate_name = row[2]


        #print canidates name with final vote count to terminal
        if canidate_name == "Charles Casper Stockham":
            charles_votes +=1
        elif canidate_name == "Diana DeGette":
            diana_votes +=1
        elif canidate_name == "Raymon Anthony Doane":
            raymond_votes +=1 
        else:
            print (f"the name of the canidate {canidate_name} is unknown")
