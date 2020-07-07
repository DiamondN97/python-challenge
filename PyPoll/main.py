#import dependencies
import os
import csv

#declare variables
total_votes = []
candidate_list = []
CandidateNameList = []
correy_votes = 0
li_votes = 0
tooley_votes = 0
CandidateName = []
candidate_name = str


#read csv

datacsv = os.path.join('Resources', 'election_data.csv')

with open ('Bootcamp/GitLab/python-challenge/PyPoll/Resources/election_data.csv', 'r') as datacsv_file:
#with open (datacsv, 'r') as datacsv_file:  USE THIS IN GITBASH
    csvReader = csv.reader (datacsv_file, delimiter = ',')
    next (csvReader) 
    for row in csvReader:
        total_votes.append(row[0]) 
        candidate_list.append(row[2])
        CandidateNameList.append(row[2])
VoteTotal = len(total_votes)
 
# print("Election Results")
# print("----------------------------")

#find total number of votes

# print(f'Total Votes: {VoteTotal}')
# print("----------------------------")



CandidateName = list(set(candidate_list))
CandidateName.sort()
#print(CandidateName)


khan_votes_pct = round((float(candidate_list.count((CandidateName[1]))/VoteTotal)*100),4)
khan_votes =  candidate_list.count((CandidateName[1]))
# print(f"Khan Votes: {khan_votes_pct}% ({khan_votes})")


correy_votes_pct = round((float(candidate_list.count((CandidateName[0]))/VoteTotal)*100),4)
correy_votes =  candidate_list.count((CandidateName[0]))
# print(f"Correy: {correy_votes_pct}% ({correy_votes})")


li_votes_pct = round((float(candidate_list.count((CandidateName[2]))/VoteTotal)*100),4)
li_votes = candidate_list.count((CandidateName[2]))
# print(f"Li: {li_votes_pct}% ({li_votes})")


tooley_votes_pct = round((float(candidate_list.count((CandidateName[3]))/VoteTotal)*100),4)
tooley_votes = candidate_list.count((CandidateName[3]))

# print(f"O'Tooley: {tooley_votes_pct}% ({tooley_votes})")
# print("----------------------------")


PopularVote = max(set(CandidateNameList), key = CandidateNameList.count)
# print (f"Winner: {PopularVote}")
# print("----------------------------")

print("Election Results")
print("----------------------------")
print(f'Total Votes: {VoteTotal}')
print("----------------------------")
print(f"Khan Votes: {khan_votes_pct}% ({khan_votes})")
print(f"Correy: {correy_votes_pct}% ({correy_votes})")
print(f"Li: {li_votes_pct}% ({li_votes})")
print(f"O'Tooley: {tooley_votes_pct}% ({tooley_votes})")
print("----------------------------")
print (f"Winner: {PopularVote}")
print("----------------------------")


output = open('Bootcamp\GitLab\python-challenge\PyPoll\PyPollOutput.txt', 'w')
print("Election Results", file=output)
print("----------------------------")
print(f'Total Votes: {VoteTotal}', file=output)
print("----------------------------", file=output)
print(f"Khan Votes: {khan_votes_pct}% ({khan_votes})", file=output)
print(f"Correy: {correy_votes_pct}% ({correy_votes})", file=output)
print(f"Li: {li_votes_pct}% ({li_votes})", file=output)
print(f"O'Tooley: {tooley_votes_pct}% ({tooley_votes})", file=output)
print("----------------------------", file=output)
print (f"Winner: {PopularVote}", file=output)
print("----------------------------", file=output)