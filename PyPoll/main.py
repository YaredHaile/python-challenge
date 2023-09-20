import csv

# Define the file path to your election data CSV file
file_path = 'election_data.csv'

# Initialize variables to store data
total_votes = 0
candidate_votes = {}
winner = ""
winner_votes = 0

# Read the CSV file and perform the analysis
with open('Resources/election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row if it exists
    header = next(csvreader, None)
    
    for row in csvreader:
        # Count the total number of votes
        total_votes += 1
        
        # Get the candidate name from the row
        candidate = row[2]
        
        # If the candidate is not in the dictionary, add them
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 1
        else:
            # Increment the candidate's vote count
            candidate_votes[candidate] += 1

# Determine the winner based on popular vote
for candidate, votes in candidate_votes.items():
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Calculate and display the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Save the results to a text file
with open("analysis/election_results.txt", "w") as text_file:
    text_file.write("Election Results\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write("-------------------------\n")

    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        text_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    text_file.write("-------------------------\n")
    text_file.write(f"Winner: {winner}\n")
    text_file.write("-------------------------\n")
