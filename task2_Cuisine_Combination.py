# Task: Cuisine Combination
import pandas as pd
import matplotlib.pyplot as plt
task1 = 'C:\\Users\\nihar\\OneDrive\\Pictures\\Documents\\cognify techno intern\\level 2\\Dataset .csv'  
level = pd.read_csv(task1)
#Identify the most common combinations of cuisines in the dataset

cuisine_combinations = level['Cuisines'].str.split(', ')
cuisine_combinations = cuisine_combinations.apply(lambda x: tuple(sorted(x)) if isinstance(x, list) else x)
cuisine_comb_counts = cuisine_combinations.value_counts()
print(cuisine_comb_counts.head(10))

# Step 3: Determine if Certain Cuisine Combinations Tend to Have Higher Ratings

level['cuisine_combination'] = cuisine_combinations
cuisine_rating = level.groupby('cuisine_combination')['Aggregate rating'].mean()
print(cuisine_rating.sort_values(ascending=False).head(10))



