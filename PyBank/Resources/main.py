#PyBank

#Import csv file & output txt file
import os
import csv

budget_data = os.path.join("budget_data.csv")
output_file = os.path.join("Analysis", "budget_analysis.txt")

#Variable
total_months = 0
months_change = []
prev_net = 0
net_change_list = []
net_total = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999]

#Open csv for both reading and writing
with open(budget_data, 'r') as csv_file:
   csv_reader = csv.DictReader(csv_file)


#run loop for month count
   for row in csv_reader:
      total_months = total_months + 1
      net_total = net_total + int(row["Profit/Losses"])

      net_change = int(row["Profit/Losses"]) - (prev_net)
      prev_net = int(row["Profit/Losses"])
      months_change = (row["Date"])
      net_change_list.append(net_change)

#find greatest increase (month incl) and decrease (month incl)
   if net_change > greatest_increase[1]:
         greatest_increase[0] = row["Date"]
         greatest_increase[1] = net_change

   if net_change < greatest_decrease[1]:
         greatest_decrease[0] = row["Date"]
         greatest_decrease[1] = net_change
         
#average of profit/loss changes over the period
avg__net_change = sum(net_change_list)/ len(net_change_list)
    


summary = (
   f"Financual Analysis\n"
   f"-------------------------\n"
   f"Total Months:  {total_months}\n"
   f"Total:  ${net_total}\n"
   f"Average Change: ${avg__net_change}\n"
   f"Greatest Increase in Profits: ${greatest_increase}\n"
   f"Greatest Decrease in Profits: ${greatest_decrease}\n" 
   )

# #Terminal Print
print(summary)

# #Export txt print
with open('budget_analysis.txt', 'w') as new_file:
      
      new_file.write(summary) 

      
      


