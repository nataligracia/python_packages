import pathlib
import csv

#Connect python and data
records_csv = pathlib.Path('/Users/nataligracia/git/python_packages/PyBank/Resources/PyBank_Resources_budget_data.csv')

#Tell python how to read data
with open (records_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvfile)

#Labels
total_months = {}

#Loop through data
for row in csvreader:

    record_month = row[0]
    if record_month in total_months
        total_months[record_month] += 1
    else:
        total_months[record_month] = 1
print(total_month)

#Total # of months
#total_months = sum(date)
#print(total_months)

#Net Total $ "Profit/Losses"
#total_balance = total_balance + int
#Average Change in $ "Profit/Losses"
#Greatest Increase in Profits (Date and Amount)
#Greatest Decrease in Losses (Date and Amount)
