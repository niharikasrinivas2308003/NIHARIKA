#Task: Price Range Distribution

#Create a histogram or bar chart to visualize the distribution of price ranges among the restaurants.
import pandas as pd
import matplotlib.pyplot as plt
task1 = 'C:\\Users\\nihar\\OneDrive\\Pictures\\Documents\\cognify techno intern\\level 1\\Dataset .csv'   
level = pd.read_csv(task1)

import matplotlib.pyplot as plt

# Calculate counts of each price range category
price_range_counts = level['Price range'].value_counts()

# Plotting
plt.figure(figsize=(8, 6))
price_range_counts.plot(kind='bar', color='skyblue')
plt.title('Distribution of Price Ranges among Restaurants')
plt.xlabel('Price range')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Calculate the percentage of restaurants in each price range category.
percentage_price_range = (level['Price range'].value_counts() / len(level)) * 100
print("Percentage of restaurants in each price range category:")
print(percentage_price_range)


