#the data we need to retrieve.
import csv
from  os import path

file_to_load = path.join('Resources','election_results.csv',)
with open(file_to_load) as election_data_fhand:
    print(election_data_fhand)
#Using WIth_AS the output: <_io.TextIOWrapper name='Resources/election_results.csv' mode='r' encoding='cp1252'>


file_to_save = path.join('Analysis', 'election_analysis.txt')
outputFile=open(file_to_save, 'w').write('hello world')
#right now, this new created text is empty.



# 1.The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. the percentage of votes each candidate won
# 4. the total number of votes each candidate won
# 5.the winner of the election based on popular vote