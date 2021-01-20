#Import python libraries
import pathlib
import csv

#Connect python and data
records_csv = pathlib.Path('/Users/nataligracia/git/python_packages/PyBank/Resources/PyBank_Resources_budget_data.csv')

#Tell python how to read data
with open (records_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    months = 1
    total_funds = 0
    before_profitlosses = 0

    start = next(csvreader)
    before_profitlosses = int(start[1])
    total_funds += before_profitlosses
    difference = []
    month_year = []

#Loop through data
    for row in csvreader:
        #Total months
        months += 1
        month_year.append(row[0])

        #Funds Total
        profit_losses = int(row[1])
        total_funds += profit_losses

        #Average Change
        change = profit_losses - before_profitlosses
        difference.append(change)
        before_profitlosses = profit_losses
        average = format(sum(difference)/(months -1),'.2f')

        #Greatest Profit
        greatest_profit = max(difference)
        greatestprofit_month = difference.index(greatest_profit)
        greatestprofit_monthyear = month_year[greatestprofit_month]

        #Greatest Loss
        greatest_loss = min(difference)
        greatestloss_month = difference.index(greatest_loss)
        greatestloss_monthyear = month_year[greatestloss_month]


    #Export script text to file with the results
    budget_summary = pathlib.Path('/Users/nataligracia/git/python_packages/PyBank/analysis/budget_summary.txt')

    #Formatting summary table for number of months, total funds, average change, greatest profit, and least profit in terminaal and text file
    with open(budget_summary,'w') as resultsfile:
        csvwriter = csv.writer(resultsfile)
        budget_summary = (
        f"\n\nFinancial Analysis\n"
        f"-----------------------------\n"
        f"Total Months: {months}\n"
        f"Total: ${format(total_funds,',d')}\n"
        f"Average Change: ${average} \n"
        f"Greatest Increase in Profits: {greatestprofit_monthyear} (${format(greatest_profit,',d')})\n"
        f"Greatest Decrease in Profits: {greatestloss_monthyear} (${format(greatest_loss,',d')})\n")
        print(budget_summary)
        resultsfile.write(budget_summary)