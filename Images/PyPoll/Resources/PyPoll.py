import csv
import os
#read the csv file and store the data in a list of dictionaries
votes = []
csvpath = os.path.join ("Resources", "election_data.csv")
with open(csvpath) as csv_file: 
    reader = csv.DictReader(csv_file)
    for row in reader:
        votes.append(row)
#print(votes)

#The total number of votes cast
total_votes = len(votes)
#print(total_votes)

#A complete list of candidates who received votes

candidates = []
for vote in votes:
    candidate = vote["Candidate"]
    if candidate not in candidates:
        candidates.append(candidate)
#print(candidates)

# calculate number of votes for each candidate
candidate_vote = {}
for candidate in candidates:
    candidate_vote[candidate] = 0
for vote in votes:
    candidate_vote[vote['Candidate']] += 1
#print(candidate_vote)

#The percentage of votes each candidate won
percent_vote = {}
for candidate in candidates:
    percent_vote[candidate] =  round((100 * candidate_vote[candidate] / total_votes),3)
#print(percent_vote)

#The winner of the election based on popular vote
winner = max(candidate_vote, key= candidate_vote.get)
#print(winner)

#analysis to terminal
print('Election Results')
print("-------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------")
for candidate in candidates:
    print(f'{candidate}: {percent_vote [candidate]} ({candidate_vote[candidate]})')
print("-------------------------")  
print(f'Winner: {winner}')
print("-------------------------")  

#export to a text file
with open("election_results.txt", "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f'Total Votes: {total_votes}\n')
    txtfile.write("-------------------------\n")
    for candidate in candidates:
        txtfile.write(f'{candidate}: {percent_vote [candidate]} ({candidate_vote[candidate]})\n')
    txtfile.write("-------------------------\n") 
    txtfile.write(f'Winner: {winner}\n')
    txtfile.write("-------------------------\n")  







