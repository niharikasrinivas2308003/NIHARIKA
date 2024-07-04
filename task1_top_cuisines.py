#LEVEL-1
#Task: Top Cuisines
import pandas as pd
import matplotlib.pyplot as plt
task1 = 'C:\\Users\\nihar\\OneDrive\\Pictures\\Documents\\cognify techno intern\\level 1\\Dataset .csv'  
level = pd.read_csv(task1)
print(level)

# Cleaning the 'Cuisines' column
level['Cuisines'] = level['Cuisines'].str.lower().str.strip()

# Split the cuisines by comma and explode the list to count each cuisine separately
cuisines_exploded = level['Cuisines'].str.split(',').explode().str.strip()

# Count occurrences of each cuisine
cuisine_counts = cuisines_exploded.value_counts()
print(cuisine_counts)

#Determine the top three most common cuisines in the dataset
# Get the top three cuisines
top_three_cuisines = cuisine_counts.head(3)
print(top_three_cuisines)

# primarily we are calculating total number of restaurants
total_restaurants = level.shape[0]
print(total_restaurants)

# Calculate the percentage of restaurants serving each of the top three cuisines
top_three_percentages = (top_three_cuisines / total_restaurants) * 100
print(top_three_percentages)