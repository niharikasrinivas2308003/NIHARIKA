#Task: Restaurant Reviews
import pandas as pd
import re
import seaborn as sns
from collections import Counter
import matplotlib.pyplot as plt
# Analyze the text reviews to identify the most common positive and negative keywords.
import pandas as pd
task1 = 'C:\\Users\\nihar\\OneDrive\\Pictures\\Documents\\cognify techno intern\\level3\\Dataset .csv'
level = pd.read_csv(task1)
print(level)

def clean_text(text):
    text = re.sub(r'[^\w\s]', '', text).lower()
    return text
level['cleaned_review'] = level['Rating text'].apply(clean_text)
def get_keywords(texts):
    all_words = ' '.join(texts).split()
    return Counter(all_words).most_common(10)
positive_reviews = level[level['Aggregate rating'] >= 4]['cleaned_review']
negative_reviews = level[level['Aggregate rating'] <= 2]['cleaned_review']

positive_keywords = get_keywords(positive_reviews)
negative_keywords = get_keywords(negative_reviews)
print("Positive Keywords:", positive_keywords)
print("Negative Keywords:", negative_keywords)

# Average Review Length
level['review_length'] = level['cleaned_review'].apply(lambda x: len(x.split()))
average_length = level['review_length'].mean()
print("Average Review Length:", average_length)
# Relationship Between Review Length and Rating
plt.scatter(level['Aggregate rating'], level['review_length'])
plt.xlabel('Rating')
plt.ylabel('Review Length')
plt.title('Review Length vs Rating')
plt.show()

