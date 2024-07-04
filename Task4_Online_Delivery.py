#Task: Online Delivery

# Load the dataset
import pandas as pd
import matplotlib.pyplot as plt
task1 = 'C:\\Users\\nihar\\OneDrive\\Pictures\\Documents\\cognify techno intern\\level 1\\Dataset .csv'   
level = pd.read_csv(task1)
print(level)

# Determine the percentage of restaurants that offer online delivery

online_delivery_counts = level['Has Online delivery'].value_counts()
total_restaurants = len(level)
percentage_online_delivery = (online_delivery_counts['Yes'] / total_restaurants) * 100
print(f"Percentage of restaurants that offer online delivery: {percentage_online_delivery:.2f}%")

# Compare the average ratings of restaurants with and without online delivery

average_rating_with_delivery = level[level['Has Online delivery'] == 'Yes']['Aggregate rating'].mean()
average_rating_without_delivery = level[level['Has Online delivery'] == 'No']['Aggregate rating'].mean()
print(f"Average rating of restaurants with online delivery: {average_rating_with_delivery:.2f}")
print(f"Average rating of restaurants without online delivery: {average_rating_without_delivery:.2f}")



