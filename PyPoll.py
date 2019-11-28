
import csv
from  os import path

file_to_load = path.join('Resources','election_results.csv',)
file_to_save = path.join('Analysis', 'election_analysis.txt')

total_votes=0
county_options=list()
candidate_options=list()
counter_counties=dict()
counter_candidates=dict()

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
            #begin tracking the candidate counter, init counter as zero
            counter_candidates[candidate_name]=0
        #histogram of candidates
        counter_candidates[candidate_name]=counter_candidates.get(candidate_name)+1

        
print(total_votes)

print(county_options)
print(counter_counties)

print(candidate_options)
print(counter_candidates)


with open(file_to_save, 'w') as outputFile:
    outputFile.write("Total number of votes cast is "+str(total_votes))
    #outputFile.write('--------------------------\n')
    #outputFile.write('Arapahoe\nDenver\nJefferson')

  



# 3. the percentage of votes each candidate won
# 4. the total number of votes each candidate won
# 5.the winner of the election based on popular vote