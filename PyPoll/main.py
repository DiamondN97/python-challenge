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
 
print("Election Results")
print("----------------------------")

#find total number of votes

print(f'Total Votes: {VoteTotal}')
print("----------------------------")



CandidateName = list(set(candidate_list))
CandidateName.sort()
#print(CandidateName)

# for i in candidate_list:
#     if i == "Khan":
#         khan_votes.append(candidate_list)
# print(khan_votes)

#khan_votes = ((candidate_list.count((CandidateName[2]))/VoteTotal)*100
khan_votes_pct = round((float(candidate_list.count((CandidateName[1]))/VoteTotal)*100),4)
khan_votes =  candidate_list.count((CandidateName[1]))
print(f"Khan Votes: {khan_votes_pct}% ({khan_votes})")


correy_votes_pct = round((float(candidate_list.count((CandidateName[0]))/VoteTotal)*100),4)
correy_votes =  candidate_list.count((CandidateName[0]))
print(f"Correy: {correy_votes_pct}% ({correy_votes})")


li_votes_pct = round((float(candidate_list.count((CandidateName[2]))/VoteTotal)*100),4)
li_votes = candidate_list.count((CandidateName[2]))
print(f"Li: {li_votes_pct}% ({li_votes})")


tooley_votes_pct = round((float(candidate_list.count((CandidateName[3]))/VoteTotal)*100),4)
tooley_votes = candidate_list.count((CandidateName[3]))

print(f"O'Tooley: {tooley_votes_pct}% ({tooley_votes})")
print("----------------------------")

# def popular_vote(candidate_list):
#     counter = 0
#     votes = candidate_list[0]
#     for i in candidate_list:
#         popularVotes = candidate_list.count(i)
#         if(popularVotes > counter):
#             counter = popularVotes
#             CommonVotes = i 
#     return CommonVotes
# print(popular_vote(candidate_list))

# popular_vote = {}
# for i in candidate_list:
#     popular_vote[i] = popular_vote.get(i, 0) + 1
# WinnerList = popular_vote.keys()
# # WinnerList.sort()
# for CandidateName in WinnerList:
   
#     print (f'Winner: {CandidateName, popular_vote[CandidateName]}')
#find candidate list
#print(candidate_list) <--- total list of candidates

  