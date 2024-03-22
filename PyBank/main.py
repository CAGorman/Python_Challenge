import os
import csv

budget_data_csv = os.path.join("..", "Resources", "budget_data.csv")

with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")