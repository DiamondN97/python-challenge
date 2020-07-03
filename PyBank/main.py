#import dependencies
import os
import csv
values = []
month_count = []
profit_total = []
profit_sum = 0

#read csv
datacsv = os.path.join('Resources', 'budget_data.csv')

# with open ('Bootcamp/GitLab/python-challenge/PyBank/Resources/budget_data.csv', 'r') as datacsv_file:
with open (datacsv, 'r') as datacsv_file:
    csvReader = csv.reader (datacsv_file, delimiter = ',')
    next (csvReader) 
    for row in csvReader:
        Date = row[0]
        Profit = row[1]
        month_count.append(Date) 
        profit_total.append(Profit)       
        #count number of months
TotalMonth = len(month_count)

print("Financial Analysis")
print("----------------------------")

print(f'Total Months: {TotalMonth}')


#find net total of P/L
# print(profit_total)
# print(Profit)
# this would start at index 1, not 0
for i in range(0, len(profit_total)):
# for i in range(1, 86): 
    # profit_sum = profit_total + profit_total[i]
    # profit_sum is not 0 yet
    # profit_total[i] is a string right now
    profit_sum = profit_sum + int(profit_total[i])

print(f'Total Profit: ${profit_sum}')
# 0 + 867887 = sum
# sum + 984655 = sum
# profit_total = 0
# month_total += 1
# profit_change = 0

# for row in csvReader:
#     profit_total + int(Profit)
#     month_total 


#find the average of the changes of P/L

#find greatest increase in profits

#find greatest decrease in profits











