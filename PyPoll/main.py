
#PYPOLL

#Import csv file & output txt file
import os
import csv

election_data = os.path.join("election_data.csv")
output_file = os.path.join("Analysis", "election_data.txt")


#variables
total_votes = 0
candidate_list = []
new_candidate = []
candidate_percent_vote = []
candidate_vote_count = 0

winner = []
winning_vote = 0

#Open csv and add header
with open(election_data, 'r') as csv_file:
   csv_reader = csv.DictReader(csv_file)

#loop votes
   for row in csv_reader:
      total_votes += 1
      candidate_list = row["Candidate"]
#if for names
      if new_candidate not in candidate_list:
         
         candidate_list.append(new_candidate)
         
         candidate_vote_count[new_candidate] += 1


#loop counts and percent
   for candidate in candidate_list:
       candidate_vote_count = {candidate} + 1
       candidate_percent_vote = int(candidate_vote_count) / int(total_votes) * 100

#winner
   {candidate} == max(candidate_vote_count)       


summary = (
   f"Election Results\n"
   f"-------------------------\n"
   f"Total Votes:  {net_total}\n"
   f"-------------------------\n"
   f"Winner": {candidate}"
   )

#print in terminal
print(summary)

#print in text file
with open('new_election_data.txt', 'w') as new_file:
      new_file.write(summary) 



  