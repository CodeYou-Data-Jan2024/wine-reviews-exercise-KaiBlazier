import pandas as pd

# Load the CSV file
df = pd.read_csv('data/winemag-data-130k-v2.csv.zip', compression='zip')

# Group by country, count reviews, and calculate average points
summary = df.groupby('country').agg(
    num_reviews=('country', 'size'),
    avg_points=('points', 'mean')).reset_index()

# Save the summary to a new CSV file
summary.to_csv('data/reviews-per-country.csv', index=False)

print("The summary data has been saved to 'data/reviews-per-country.csv'")
