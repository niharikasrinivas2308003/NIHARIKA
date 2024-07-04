# Votes Analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Analyze the text reviews to identify the most common positive and negative keywords.
import pandas as pd
task1 = 'C:\\Users\\nihar\\OneDrive\\Pictures\\Documents\\cognify techno intern\\level3\\Dataset .csv'
level = pd.read_csv(task1)
print(level)
# Identify the restaurants with the highest and lowest number of votes.
most_votes = level.loc[level['Votes'].idxmax()]
least_votes = level.loc[level['Votes'].idxmin()]
print("Restaurant with the highest number of votes:")
print(most_votes[['Restaurant Name', 'Votes']])
print("\nRestaurant with the lowest number of votes:")
print(least_votes[['Restaurant Name', 'Votes']])

# Analyze if there is a correlation between the number of votes and the rating of a restaurant.

plt.figure(figsize=(10, 6))
sns.regplot(x='Votes', y='Aggregate rating', data=level)
plt.xlabel('Number of Votes')
plt.ylabel('Rating')
plt.title('Correlation Between Number of Votes and Rating')
plt.show()
correlation = level[['Votes', 'Aggregate rating']].corr().iloc[0, 1]
print(f"Correlation coefficient between number of votes and rating: {correlation}")