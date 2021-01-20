#Import python libraries
import pathlib
import csv

#Connect python and data
records_csv = pathlib.Path('/Users/nataligracia/git/python_packages/PyBank/Resources/PyBank_Resources_budget_data.csv')

#Tell python how to read data
with open (records_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    months = 0
    total_budget = 0

#Loop through data
    for row in csvreader:
        months += 1
    print(months)

    for row in csvreader:
        profit_losses = row[1]
        total_budget = sum(profit_losses)
    print(total_budget)

    #profit_losses = row[1]
    #total_profitlosses = 0

    #record_month = row[0]
    #if record_month in total_months
    #   total_months[record_month] += 1
    #else:
    #   total_months[record_month] = 1
    #print(total_month)

    #Export script text to file with the results
    budget_summary = pathlib.Path('/Users/nataligracia/git/python_packages/PyBank/analysis/budget_summary.txt')

    #Formatting summary table for total count, candidate breakdowns, and the winner in terminaal and text file
    with open(budget_summary,'w') as resultsfile:
        csvwriter = csv.writer(resultsfile)
        budget_summary = (
        f"\n\nFinancial Analysis\n"
        f"-----------------------------\n"
        f"Total Months: {months}\n")
        #f"Total: {total_budget}\n"
        #f"Average Change: \n"
        #f"Greatest Increase in Profits: \n"
        #f"Greatest Decrease in Profits: \n"
        print(budget_summary, end="")
        resultsfile.write(budget_summary)

#Total # of months
#total_months = sum(date)
#print(total_months)

#Net Total $ "Profit/Losses"
#total_balance = total_balance + int
#Average Change in $ "Profit/Losses"
#Greatest Increase in Profits (Date and Amount)
#Greatest Decrease in Losses (Date and Amount)


#The total number of months included in the dataset


#The net total amount of "Profit/Losses" over the entire period


#The average of the changes in "Profit/Losses" over the entire period


#The greatest increase in profits (date and amount) over the entire period


#The greatest decrease in losses (date and amount) over the entire period


#Financial Analysis
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.