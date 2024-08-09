import csv

# Initialize variables
total_votes = 0
candidate_votes = {}

# Load the CSV 
file_path = 'C:/Users/Jrp01/OneDrive/Documents/GitHub/python-challenge/PyPoll/Resources/election_data.csv'  
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    next(reader)  
    
    # Tally the votes
    for row in reader:
        total_votes += 1
        candidate = row[2]
        
        # If the candidate is already in the dictionary, increment the vote count
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Determine the winner and prepare the results
output = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)

# Calculate percentages and determine the winner
winner = None
max_votes = 0

# Run through the candidates and their votes
for candidate, votes in candidate_votes.items():
    vote_percentage = (votes / total_votes) * 100
    output += f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
    
    # Determine the winner 
    if votes > max_votes:
        max_votes = votes
        winner = candidate

output += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

# Print the results 
print(output)

# Export results to a text file
output_file = r'C:/Users/Jrp01/OneDrive/Documents/GitHub/python-challenge/PyPoll/analysis/financial_analysis.txt'
with open(output_file, mode='w') as file:
    file.write(output)