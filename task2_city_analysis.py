#task2 city analysis
#Reading the dataset
import pandas as pd
import matplotlib.pyplot as plt
task1 = 'C:\\Users\\nihar\\OneDrive\\Pictures\\Documents\\cognify techno intern\\level 1\\Dataset .csv'    
level = pd.read_csv(task1)

 #Identify city with the highest number of restaurants
city_with_most_restaurants = level['City'].value_counts().idxmax()
print(f"City with the highest number of restaurants: {city_with_most_restaurants}")

# Calculate average rating for restaurants in each city
average_ratings_by_city = level.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False)
print("\nAverage ratings for restaurants in each city:")
print(average_ratings_by_city)

#Determine city with the highest average rating
average_ratings_by_city = df.groupby('City')['Aggregate Rating'].mean().sort_values(ascending=False)
city_with_highest_average_rating = average_ratings_by_city.idxmax()
highest_average_rating = average_ratings_by_city.max()
print(f"City with the highest average rating: {city_with_highest_average_rating}")
print(f"Highest average rating: {highest_average_rating}")

