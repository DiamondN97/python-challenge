#import dependencies
import os
import csv

#declare variables
total_votes = []
candidate_list = []
khan_votes = 0
correy_votes = 0
li_votes = 0
tooley_votes = 0



#read csv

datacsv = os.path.join('Resources', 'election_data.csv')

with open ('Bootcamp/GitLab/python-challenge/PyPoll/Resources/election_data.csv', 'r') as datacsv_file:
#with open (datacsv, 'r') as datacsv_file:
    csvReader = csv.reader (datacsv_file, delimiter = ',')
    next (csvReader) 
    for row in csvReader:
        total_votes.append(row[0]) 
        candidate_list.append(row[2])
VoteTotal = len(total_votes)
 
print("Election Results")
print("----------------------------")

#find total number of votes

print(f'Total Votes: {VoteTotal}')
print("----------------------------")

#find candidate list
#print(candidate_list) <--- total list of candidates