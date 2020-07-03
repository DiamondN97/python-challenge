#import dependencies
import os
import csv
values = []
month_count = []


#read csv

datacsv = os.path.join('Resources', 'budget_data.csv')

with open (datacsv, 'r') as datacsv_file:
    csvReader = csv.reader (datacsv_file, delimiter = ',')
    next (csvReader) 
    for row in csvReader:
        Date = row[0]
        Profit = row[1]
        month_count.append(row[0])        
        #count number of months
TotalMonth = len(month_count)

print(TotalMonth)

#find net total of P/L
# profit_total = 0
# month_total += 1
# profit_change = 0

# for row in csvReader:
#     profit_total + int(Profit)
#     month_total 


#find the average of the changes of P/L

#find greatest increase in profits

#find greatest decrease in profits











