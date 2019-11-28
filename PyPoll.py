
import csv
from  os import path

file_to_load = path.join('Resources','election_results.csv',)
file_to_save = path.join('Analysis', 'election_analysis.txt')

#outputFile.close() only needed with out WITH statement, combine with open() fection
with open(file_to_load) as election_data_fhand:
# To do: read and analyze the data here
    #Read the file object with CSV function---.reader()
    file_reader=csv.reader(election_data_fhand)

    headers=next(file_reader)
    print(headers)
    #for row in file_reader:
        #print(row)



#with open(file_to_save, 'w') as outputFile:
    #outputFile.write('Counties in the Election\n')
    #outputFile.write('--------------------------\n')
    #outputFile.write('Arapahoe\nDenver\nJefferson')

    #print(outputFile)



# 1.The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. the percentage of votes each candidate won
# 4. the total number of votes each candidate won
# 5.the winner of the election based on popular vote