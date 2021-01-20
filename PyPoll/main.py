#Import python ibraries
import pathlib
import csv

#Connect python to data
votes_csv = pathlib.Path('/Users/nataligracia/git/python_packages/PyPoll/Resources/PyPoll_Resources_election_data.csv')

#Tell python how to read csv
with open(votes_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)

    votes_cast = {}

#Start searching data
    for row in csvreader:
        vote_candidate = row[2]
        
        #Get candidate's unique names
        if vote_candidate in votes_cast:
            votes_cast[vote_candidate] += 1
        else: votes_cast[vote_candidate] = 1

    #Get candidate votes cast counts
    vote_totals = (list(votes_cast.values()))

    #Get vote total
    vote_summary = sum(vote_totals)

    #Summary table
    winner = list(votes_cast.keys())[0]
    summary_table = {}
    for vote_candidate in votes_cast.keys():
        if votes_cast[vote_candidate] > votes_cast[winner]:
            winner = vote_candidate
        summary_table[vote_candidate] = {'votes_cast': format(votes_cast[vote_candidate],',d'),'vote_percentage': format((votes_cast[vote_candidate]/vote_summary)*100,".3f")}
        if vote_candidate == winner:
            summary_table[vote_candidate]["is_winner"] = True
        else: summary_table[vote_candidate]["is_winner"] = False
    

    #Export script text to file with the results
    ballot_results = pathlib.Path('/Users/nataligracia/git/python_packages/PyPoll/analysis/ballot_results.txt')

    #Formatting summary table for total count, candidate breakdowns, and the winner in terminaal and text file
    with open(ballot_results,'w') as resultsfile:
        ballot_results = (
        f"\n\nElection Results\n"
        f"-----------------------------\n"
        f"Total Votes: {format(vote_summary, ',d')}\n"
        f"-----------------------------\n")
        print(ballot_results, end="")
        resultsfile.write(ballot_results)

        for vote_candidate in summary_table.keys():
            candidate_count = f"{vote_candidate}: {summary_table[vote_candidate]['vote_percentage']}% ({summary_table[vote_candidate]['votes_cast']})\n"
            print(candidate_count, end= "")
            resultsfile.write(candidate_count)

        result = (
        f"-----------------------------\n"
        f"Winner: {winner}\n"
        f"-----------------------------\n")
        print(result)
        resultsfile.write(result)