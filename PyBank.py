import os
import csv

#read in the csv file and store the header row 
with open('budget_data.csv', 'r') as f:
    reader = csv.reader(f) 
    header = next(reader) 

    # store the data in a list of dictionaries
    # each dictionary represents a row 
    data = [row for row in reader]
#print(data)

# this will calculate the total number of months
total_months = len(data)
#print(total_months)  

#The net total amount of "Profit/Losses" over the entire period
net_total = sum(int(row[1]) for row in data)
#print(net_total)

#The changes in "Profit/Losses" over the entire period
changes = [int(data[i+1][1]) - int(data[i][1]) for i in range(total_months - 1)]
#print(changes)
#print(len(changes))


#then the average of those changes
average_change = round(sum(changes) / len(changes), 2)
#print(average_change)

#The greatest increase in profits (date and amount) over the entire period
greatest_increase = max(changes)
#print(greatest_increase)
greatest_increase_month = data[changes.index(greatest_increase) + 1][0]
#print(greatest_increase_month)


#The greatest decrease in profits (date and amount) over the entire period
greatest_decrease = min(changes)
#print(greatest_decrease )
greatest_decrease_month = data[changes.index(greatest_decrease) + 1][0]
#print(greatest_decrease_month)

#print to the ternimal
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${net_total}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')

#export the results to a text file 

with open("financial_analysis.txt" , "w") as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write(f'Total Months: {total_months}\n')
    f.write(f'Total: ${net_total}\n')
    f.write(f'Average Change: ${average_change}\n')
    f.write(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n')
    f.write(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n')




