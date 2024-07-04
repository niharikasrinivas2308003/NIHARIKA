# Price_Range vs Onlinedelivery and table booking

import pandas as pd
import re
import seaborn as sns
from collections import Counter
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
# Analyze the text reviews to identify the most common positive and negative keywords.
import pandas as pd
task1 = 'C:\\Users\\nihar\\OneDrive\\Pictures\\Documents\\cognify techno intern\\level3\\Dataset .csv'
level = pd.read_csv(task1)
print(level)
# Analyze if there is a relationship between the price range and the availability of online delivery and table booking.

level['Has Online delivery'] = level['Has Online delivery'].apply(lambda x: 1 if x == 'Yes' else 0)
level['Has Table booking'] = level['Has Table booking'].apply(lambda x: 1 if x == 'Yes' else 0)

# Summarize the availability of online delivery and table booking across different price ranges
price_range_delivery = level.groupby('Price range')['Has Online delivery'].mean()
price_range_booking = level.groupby('Price range')['Has Table booking'].mean()

# Visualize the relationship using bar plots
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.barplot(x=price_range_delivery.index, y=price_range_delivery.values)
plt.xlabel('Price Range')
plt.ylabel('Proportion of Restaurants Offering Online Delivery')
plt.title('Online Delivery vs Price Range')

plt.subplot(1, 2, 2)
sns.barplot(x=price_range_booking.index, y=price_range_booking.values)
plt.xlabel('Price Range')
plt.ylabel('Proportion of Restaurants Offering Table Booking')
plt.title('Table Booking vs Price Range')

plt.tight_layout()
plt.show()

# Determine if higher-priced restaurants are more likely to offer these services.

contingency_table_delivery = pd.crosstab(level['Price range'], level['Has Online delivery'])
contingency_table_booking = pd.crosstab(level['Price range'], level['Has Table booking'])
chi2_delivery, p_delivery, _, _ = chi2_contingency(contingency_table_delivery)
chi2_booking, p_booking, _, _ = chi2_contingency(contingency_table_booking)

print(f"Chi-square test for online delivery: chi2 = {chi2_delivery}, p-value = {p_delivery}")
print(f"Chi-square test for table booking: chi2 = {chi2_booking}, p-value = {p_booking}")