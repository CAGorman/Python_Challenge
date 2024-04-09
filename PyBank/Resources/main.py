#PyBank

#Import csv file & output txt file
import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")
output_file = os.path.join("Analysis", "budget_analysis.txt")

# Variables
total_months = 0
net_total = 0
prev_net = 0
net_change_list = []
greatest_increase_day = ""
greatest_decrease_day = ""

# Open the CSV file
with open(budget_data, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row

    # Loop through rows in the CSV file
    for row in reader:
        
        dates = row[0]
        change = int(row[1]) - prev_net

        total_months += 1
        net_total += int(row[1]) 
        
        # Calculate net change
        net_change = int(row[1]) - prev_net
        net_change_list.append(net_change)
        
        prev_net = int(row[1])

# Calculate greatest increase in profits
greatest_increase = max(net_change_list)
greatest_increase_index = net_change_list.index(greatest_increase)
greatest_increase_day = dates


# Calculate greatest decrease in profits
greatest_decrease = min(net_change_list)
greatest_decrease_index = net_change_list.index(greatest_decrease)
greatest_decrease_day = dates

avg_change = sum(net_change_list) / len(net_change_list)
formatted_avg_change = "{:.2f}".format(avg_change)


# Format the output
summary = (
    f"Financial Analysis\n"
    f"-------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${formatted_avg_change}\n"
    f"Greatest Increase in Profits: {greatest_increase_day} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_day} (${greatest_decrease})\n"
)

# Print the summary
print(summary)

# Export summary to a text file
with open('budget_analysis.txt', 'w') as new_file:
    new_file.write(summary)
      
  


