import pandas as pd

# Load the CSV files
ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')

# Merge ratings and movie titles
merged = pd.merge(ratings, movies, on='MovieID')

# Calculate average ratings per movie
movie_ratings = merged.groupby('Title')['Rating'].mean()

# Count number of ratings per movie
rating_counts = merged.groupby('Title')['Rating'].count()

# Filter movies with at least 3 ratings
filtered = movie_ratings[rating_counts >= 3]

# Show top-rated movies
print("Top-rated movies (with at least 3 ratings):")
print(filtered.sort_values(ascending=False))