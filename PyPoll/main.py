
#PYPOLL

#Import csv file & output txt file
import os
import csv

election_data = os.path.join("Resources","election_data.csv")
output_file = os.path.join("Analysis", "election_data.txt")

#variables
total_votes = 0
candidate_list = []
new_candidate = []
candidate_percent_vote = []
candidate_vote_count = {}
winner = []
winning_votes = 0

winner = ""
winning_vote = 0

#Open csv and add header
with open(election_data, 'r') as csv_file:
   csv_reader = csv.reader(csv_file)
   header = next(csv_reader)
   #loop votes
   for row in csv_reader:
      total_votes += 1
      candidate = row[2]
      #if for names
      if candidate not in candidate_list:
         
         candidate_list.append(candidate)
         
         candidate_vote_count[candidate] = 0
      candidate_vote_count[candidate] = candidate_vote_count[candidate] +1

    


summary = (
   f"Election Results\n"
   f"-------------------------\n"
   f"Total Votes:  {total_votes}\n"
   f"-------------------------\n"
   )

#print in text file
with open(output_file, 'w') as new_file:
   new_file.write(summary) 
   print(summary)
   #loop counts and percent
   for candidate in candidate_list:
      votes = candidate_vote_count[candidate]
      candidate_percent_vote = int(votes) / int(total_votes) * 100

      output = f"{candidate}: {candidate_percent_vote:.3f}% ({votes})\n" 
      print(output)
      new_file.write(output)
   #    if votes > winning_votes:
   #       winner = {candidate}

   # output = summary = (
   # f"-------------------------\n"
   # f"Winner: {candidate}\n"
   # f"-------------------------\n"
   # )
   # with open(output, 'w') as new_file:
   #    output.write(output)
   #    print(output)

   # with open('election_data.txt', 'w') as new_file:
      
   #    new_file.write(output) 

      if votes > winning_votes:
           winning_votes = votes
      winner = max(candidate_vote_count, key=candidate_vote_count.get)

      output = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n"
        )
   print(output)
   
   new_file.write(output) 


#   Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------