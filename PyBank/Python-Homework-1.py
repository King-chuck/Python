# Import pathlib and csv livbrary
from pathlib import Path
import csv

# set file path
budget_data_csvpath = Path("C:\\Users\\hecto\\OneDrive\\Desktop\\Rutgers\\Class-Work\\02-Homework\\02-Python\\Instructions\\PyBank\\Resources\\budget_data.csv")

#set output text file
text_path = "output.txt"

# data variables
total_months= 0
total_revenue = 0
previous_revenue = 0
revenue_change = 0
revenue_change_list = []
month_of_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999]

# Read budget_data.csv file
with open('budget_data.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)

# loop for total months
for row in csvreader:

    #total months
        total_months = total_months + 1

# total revenue over entire period
total_revenue = total_revenue + int(row["Profit/losses"])

# Calc average change in revenue between months over period
revenue_change = float(row["profit/losses"])- previous_revenue
previous_revenue = float (row["profit/losses"])
revenue_change_list = revenue_change_list + [revenue_change]
month_of_change = month_of_change + [row["date"]]

# greatest increase 
if (revenue_change > greatest_increase[1]):
    greatest_increase[1] = revenue_change
    greatest_increase[0] = row["date"]

# greatest decrease
if (revenue_change < greatest_decrease[1]):
    greatest_decrease[0] = row["date"]
    greatest_increase[1] = revenue_change
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)


#print results
output = (
        f"Total Months:  {total_months}\n")
(f"Total Revenue: {total_revenue}\n"
f"Average Revenue Change: ${revenue_avg}\n"
f"Greatest increase in Revenue: {greatest_increase[0]} ${greatest_increase[1]}\n"
f"Greatest decrease in Revenue: {greatest_decrease[0]} ${greatest_decrease[1]}\n")

print ("Financial Analysis")


#text to path
with open(text_path, "w") as txt_file:
    txt_file.write(output)
    



    



