import pandas as pd

# Read the CSV file
df = pd.read_csv('data/winemag-data-130k-v2.csv.zip', compression='zip')

# Group by country and calculate the number of reviews and average points
summary = df.groupby('country').agg(
    num_reviews=('country', 'size'),
    avg_points=('points', 'mean')
).reset_index()

# Write the summary to a new CSV file
summary.to_csv('data/reviews-per-country.csv', index=False)

print("Summary data has been written to 'data/reviews-per-country.csv'")

