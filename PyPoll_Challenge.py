
import csv
from  os import path
#path to load and save files
file_to_load = path.join('Resources','election_results.csv',)
file_to_save = path.join('Analysis', 'election_analysis.txt')
#initial and make lists as well as dictionaries
total_votes=0
county_options=list()
candidate_options=list()
counter_counties=dict()
counter_candidates=dict()

winning_candidate=str()
winning_candidate_count=0
winning_candidate_percentage=0

winning_county=''
winning_county_count=0
winning_county_percentage=0


# Open the election results and read the file.
#we dont need to close() when use with statemment
with open(file_to_load) as election_data_fhand:
    #Read the file object with CSV function---.reader()
    file_reader=csv.reader(election_data_fhand)

    headers=next(file_reader)
    # 1.The total number of votes cast

    for row in file_reader:
        total_votes+=1
        
        Ballot_ID=row[0]
        country_name=row[1]
        candidate_name=row[2]

        # A complete list of countries where votes
        if country_name not in county_options:
            county_options.append(country_name)
        #histogram of counties
        counter_counties[country_name]=counter_counties.get(country_name,0)+1

        # A complete list of people who received votes
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            counter_candidates[candidate_name]=0
        # the total number of votes each candidate won
        counter_candidates[candidate_name]+=1

#write down and save the results on result text file
with open(file_to_save, 'w') as outputFile:
    election_results=(
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total votes: {total_votes:,}\n"
    f"--------------------------\n"
    f"\nCounty Votes:\n")
    print(election_results, end='')
    #save to text file 
    outputFile.write(election_results)

    # Make loop for retrieving information in county's dictionary.
    for county in counter_counties:
        county_votes=counter_counties[county]
        county_percentage = float(county_votes)/float(total_votes)*100
        county_votes_summary=(f"{county}:  {county_percentage :.1f}% ({county_votes:,})\n")
        
        print(county_votes_summary)
        outputFile.write(county_votes_summary)
        # Determine winning by desicion statment (comparing and logical).
        if (county_votes > winning_county_count) and (county_percentage > winning_county_percentage):
            winning_county_count=county_votes
            winning_county_percentage=county_percentage
            winning_county=county
    #skip out of loop, print out and save them into ouput text file
    winning_county_summary=(
        f"\n-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
    print(winning_county_summary)
    outputFile.write(winning_county_summary)


    # Make loop for retrieving information in candidate's dictionary
    for candidate in counter_candidates:
        vote_percentage = float(counter_candidates[candidate])/float(total_votes)*100
        candidate_votes_summary=(f"{candidate}: {vote_percentage :.1f}% ({counter_candidates[candidate]:,})\n")
        
        print(candidate_votes_summary)
        outputFile.write(candidate_votes_summary)

        # decision statement for winner
        if  winning_candidate_count < counter_candidates[candidate] and winning_candidate_percentage < vote_percentage:
            winning_candidate_count=counter_candidates[candidate]
            winning_candidate_percentage = vote_percentage
            winning_candidate=candidate
    #skip out of loop, print out and save them into ouput text file
    winning_candidate_summary=(
        f'-------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_candidate_count:,}\n'
        f'Winning Percentage: {winning_candidate_percentage:.1f}%\n'
        f'------------------------\n')
    print(winning_candidate_summary)
    outputFile.write(winning_candidate_summary)

