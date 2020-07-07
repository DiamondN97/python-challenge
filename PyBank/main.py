#import dependencies
import os
import csv


month_count = []
profit_total = []
profit_sum = 0
profit_delta = []
average_change = 0



#read csv
datacsv = os.path.join('Resources', 'budget_data.csv')

with open ('Bootcamp/GitLab/python-challenge/PyBank/Resources/budget_data.csv', 'r') as datacsv_file:
#with open (datacsv, 'r') as datacsv_file: USE THIS IN GITBASH
    csvReader = csv.reader (datacsv_file, delimiter = ',')
    next (csvReader) 
    for row in csvReader:
        Date = row[0]
        Profit = row[1]
        month_count.append(Date) 
        profit_total.append(Profit)  
        #count number of months
TotalMonth = len(month_count)


# print("Financial Analysis")
# print("----------------------------")

# print(f'Total Months: {TotalMonth}')

# print(profit_total) <-- this is the list of each profit value

#find net total of P/L

for i in range(0, len(profit_total)):

    profit_sum = profit_sum + int(profit_total[i])

#print(f'Total Profit: ${profit_sum}')


#find the average of the changes of P/L

# values=[int(i) for i in values] 
# for i in range(0, len(values)-1):

profit_change = [float(profit_total[i+1]) - float(profit_total[i]) for i in range(len(profit_total)-1)]

average_change = (round(sum(profit_change) / len(profit_change), 2))
#print(f'Average Change: ${average_change}')


#find greatest increase in profits
# for i in range(0, len(profit_change))
profit_max = max(profit_change)
maxIndex = (profit_change.index(profit_max)+1)


maxMonth = month_count[maxIndex]

#print(f'Greatest Increase in Profits: : {maxMonth} (${profit_max})')


#find greatest decrease in profits
profit_min = min(profit_change)
minIndex = (profit_change.index(profit_min)+1)


minMonth = month_count[minIndex]

print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {TotalMonth}')
print(f'Total Profit: ${profit_sum}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: : {maxMonth} (${profit_max})')
print(f'Greatest Increase in Profits: : {minMonth} (${profit_min})')


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# # output = r'C:\Users\diamo\Bootcamp\GitLab\python-challenge\PyBank\PyBankOutput.txt'
# with open('Bootcamp\GitLab\python-challenge\PyBank', 'w') as output:
# #outputFile = output.txt

#     output.write("Financial Analysis")
#     output.write("----------------------------")
#     output.write(f'Total Months: {TotalMonth}')
#     output.write(f'Total Profit: ${profit_sum}')
#     output.write(f'Average Change: ${average_change}')
#     output.write(f'Greatest Increase in Profits: : {maxMonth} (${profit_max})')
#     output.write(f'Greatest Increase in Profits: : {minMonth} (${profit_min})')












