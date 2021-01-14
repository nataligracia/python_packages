#Set python package with library
import pathlib
import csv

#Connect python to data
votes_csv = pathlib.Path('Resources/PyPoll_Resources_election_data.csv')

#Tell Python how to read csv
with open(votes_csv) as count_data
    csvreader = csv.DictReader()

    for row in 
