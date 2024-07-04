# Task: Restaurant Chains

import pandas as pd
# Load the CSV file
task1 = 'C:\\Users\\nihar\\OneDrive\\Pictures\\Documents\\cognify techno intern\\level 2\\Dataset .csv'
level = pd.read_csv(task1)
print(level)

# Identify if there are any restaurant chains present in the dataset.

restaurant_name_col = 'Restaurant Name'
rating_col = 'Aggregate rating'
votes_col = 'Votes'

chains = level[restaurant_name_col].unique()
print(f"Unique restaurant chains: {chains}")

#Analyze the ratings and popularity of different restaurant chains.

# Analyze ratings
average_ratings = level.groupby(restaurant_name_col)[rating_col].mean().sort_values(ascending=False)
print("Average Ratings per Chain:")
print(average_ratings)

# Analyze popularity (based on number of votes)
popularity_votes = level.groupby(restaurant_name_col)[votes_col].sum().sort_values(ascending=False)
print("Popularity based on Votes per Chain:")
print(popularity_votes)







    