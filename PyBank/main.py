import csv

total_months = 0
net_total = 0
previous_profit_loss = 0
profit_losses = []
months = []

file_path = ("Resources/budget_data.csv")

with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    next(csvreader)
    
    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])
        
        total_months += 1
        
        net_total += profit_loss
        
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            profit_losses.append(change)
            months.append(date)
        
        previous_profit_loss = profit_loss

average_change = sum(profit_losses) / len(profit_losses)

greatest_increase = max(profit_losses)
greatest_decrease = min(profit_losses)

increase_index = profit_losses.index(greatest_increase)
decrease_index = profit_losses.index(greatest_decrease)
greatest_increase_date = months[increase_index]
greatest_decrease_date = months[decrease_index]

print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

output = (
f"Financial Analysis\n"
    f"---------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})" 


)

output_path = ("analysis/budget_analysis.txt")

with open(output_path, "w") as txtfile:
    txtfile.write(output)
      
