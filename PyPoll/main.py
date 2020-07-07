#import dependencies
import os
import csv

#declare variables
total_votes = []
candidate_list = []
# khan_votes = []
correy_votes = 0
li_votes = 0
tooley_votes = 0
CandidateName = []
candidate_name = str


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
 
#print("Election Results")
#print("----------------------------")

#find total number of votes

#print(f'Total Votes: {VoteTotal}')
print("----------------------------")



CandidateName = list(set(candidate_list))
CandidateName.sort()
print(CandidateName)

# for i in candidate_list:
#     if i == "Khan":
#         khan_votes.append(candidate_list)
# print(khan_votes)

#khan_votes = ((candidate_list.count((CandidateName[2]))/VoteTotal)*100
khan_votes = float(candidate_list.count((CandidateName[1]))/VoteTotal)*100
print (f'(khan votes: {khan_votes}')

correy_votes = float(candidate_list.count((CandidateName[0]))/VoteTotal)*100
print (f'(correy votes: {correy_votes}')

li_votes = float(candidate_list.count((CandidateName[2]))/VoteTotal)*100
print (f'(li votes {li_votes}')

tooley_votes = float(candidate_list.count((CandidateName[3]))/VoteTotal)*100
print (f" (O'Tooley {tooley_votes}")

#find candidate list
#print(candidate_list) <--- total list of candidates