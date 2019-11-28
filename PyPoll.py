
import csv
from  os import path

file_to_load = path.join('Resources','election_results.csv',)
file_to_save = path.join('Analysis', 'election_analysis.txt')

total_votes=0
county_options=list()
candidate_options=list()
counter_counties=dict()
counter_candidates=dict()

winning_candidate=str()
winning_candidate_count=0
winning_candidate_percentage=0

winning_county=str()
winning_county_count=0
winning_county_percentage=0

#outputFile.close() only needed with out WITH statement, combine with open() fection
with open(file_to_load) as election_data_fhand:
# To do: read and analyze the data here
    #Read the file object with CSV function---.reader()
    file_reader=csv.reader(election_data_fhand)

    headers=next(file_reader)
# 1.The total number of votes cast
# 2. A complete list of candidates who received votes

    for row in file_reader:
        total_votes+=1
        
        Ballot_ID=row[0]
        country_name=row[1]
        candidate_name=row[2]

        if country_name not in county_options:
            county_options.append(country_name)
        #histogram of counties
        counter_counties[country_name]=counter_counties.get(country_name,0)+1


        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #counter_candidates[candidate_name]=0
# 4. the total number of votes each candidate won
        #histogram of candidates
        counter_candidates[candidate_name]=counter_candidates.get(candidate_name,0)+1

for county in counter_counties:
    county_votes=counter_counties[county]
    county_percentage = int(county_votes)/int(total_votes)*100
    print(f"{county}:  {county_percentage :.1f}% ({county_votes:,})\n")


# 3. the percentage of votes each candidate won
for candidate in counter_candidates:
    vote_percentage = int(counter_candidates[candidate])/int(total_votes)*100
    print(f"{candidate}: {vote_percentage :.1f}% ({counter_candidates[candidate]:,})\n")
    # decision statement for winner!!
    if winning_candidate_count is None or winning_candidate_count < counter_candidates[candidate]:
        winning_candidate_count=counter_candidates[candidate]
    if winning_candidate_percentage is None or winning_candidate_percentage < vote_percentage:
        winning_candidate_percentage = vote_percentage
        winning_candidate=candidate

# 5.the winner of the election based on popular vote
winning_candidate_summary=(
    f'------------------------\n'
    f'Winner: {winning_candidate}\n'
    f'Winning Vote Count: {winning_candidate_count:,}\n'
    f'Winning Percentage: {winning_candidate_percentage:.1f}%\n'
    f'------------------------\n')
print(winning_candidate_summary)

print(total_votes)

print(county_options)
print(counter_counties)

print(candidate_options)
print(counter_candidates)


with open(file_to_save, 'w') as outputFile:
    outputFile.write("Total number of votes cast is "+str(total_votes))
    #outputFile.write('--------------------------\n')
    #outputFile.write('Arapahoe\nDenver\nJefferson')

  


