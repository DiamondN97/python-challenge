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
#with open (datacsv, 'r') as datacsv_file:
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

# print(profit_total) <-- this is the list of each profit value

#find net total of P/L

for i in range(0, len(profit_total)):

    profit_sum = profit_sum + int(profit_total[i])

print(f'Total Profit: ${profit_sum}')


#find the average of the changes of P/L

# values=[int(i) for i in values] 
# for i in range(0, len(values)-1):

profit_change = [float(profit_total[i+1]) - float(profit_total[i]) for i in range(len(profit_total)-1)]

average_change = (round(sum(profit_change) / len(profit_change), 2))
print(f'Average Change: ${average_change}')


#find greatest increase in profits
for i in range(0, len(profit_change)):
    if profit_change > 
    profit_max = max(profit_change)
#print(profit_max)
print(f'Greatest Increase in Profits: : (${profit_max})')


#find greatest decrease in profits
for i in range(0, len(profit_change)):
    profit_min = min(profit_change)
print(f'Greatest Decrease in Profits: : (${profit_min})')
    

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



 

# for i in range(0,len(month_count)):
#     profit_max_month = [(month_count, profit_max)]
# print (profit_max_month)












