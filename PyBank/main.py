import csv

# Variables
total_months = 0
net_total = 0
differnce = []
dates = []

# Load the CSV file
file_path = 'C:/Users/Jrp01/OneDrive/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv'
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    next(reader) 
    
    # Process the first row for previous profit
    first_row = next(reader)
    previous_profit = int(first_row[1])
    total_months = 1
    net_total = previous_profit
    
    # Loop through the rest of the rows
    for row in reader:
        date = row[0]
        profit = int(row[1])
        
        # Increment total months
        total_months += 1
        
        # Calculate net total amount of "Profit/Losses"
        net_total += profit
        
        # Calculate changes in "Profit/Losses" and track dates
        change = profit - previous_profit
        differnce.append(change)
        dates.append(date)
        
        # Update previous_profit
        previous_profit = profit

# Calculate average change
average_change = sum(differnce) / len(differnce)

# Greatest increase and decrease in profits
greatest_increase = max(differnce)
greatest_increase_date = dates[differnce.index(greatest_increase)]
greatest_decrease = min(differnce)
greatest_decrease_date = dates[differnce.index(greatest_decrease)]

# Display results
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"
)

# Display results to console
print(output)

# Export results to a text file
output_file = r'C:/Users/Jrp01/OneDrive/Documents/GitHub/python-challenge/PyBank/analysis/financial_analysis.txt'
with open(output_file, mode='w') as file:
    file.write(output)