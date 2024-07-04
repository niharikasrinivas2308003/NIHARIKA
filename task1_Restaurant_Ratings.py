#Task: Restaurant Ratings
import pandas as pd
import matplotlib.pyplot as plt
task1 = 'C:\\Users\\nihar\\OneDrive\\Pictures\\Documents\\cognify techno intern\\level 2\\Dataset .csv'  
level = pd.read_csv(task1)

# Analyze the distribution of aggregate ratings and determine the most common rating range.

import matplotlib.pyplot as plt

# Plot the distribution of aggregate ratings
plt.figure(figsize=(10, 6))
n, bins, patches = plt.hist(level['Aggregate rating'].dropna(), bins=20, edgecolor='black', alpha=0.7)
plt.xlabel('Aggregate Rating')
plt.ylabel('Frequency')
plt.title('Distribution of Aggregate Ratings')
plt.grid(True)
plt.show()

# Determine the most common rating range
most_common_bin_start = bins[n.argmax()]
most_common_bin_end = bins[n.argmax() + 1]
print(f'The most common rating range is: {most_common_bin_start} to {most_common_bin_end}')

# Calculate the average number of votes received by restaurants.
average_votes = level['Votes'].mean()
print(f'The average number of votes received by restaurants is: {average_votes}')