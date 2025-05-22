# 🎬 Movie Ratings Analyzer

A beginner-friendly Python data analytics project that analyzes movie ratings by merging datasets and computing average scores.

## 🔍 What It Does

- Loads movie and user rating data from CSV files
- Merges both datasets using MovieID
- Calculates average rating per movie
- Filters out movies with fewer than 3 ratings (to avoid bias)
- Displays the top-rated movies

## 📁 Files Included

- movie_analyzer.py → Python script
- ratings.csv → Sample ratings data (UserID, MovieID, Rating)
- movies.csv → Sample movie titles (MovieID, Title)
- README.md → This file

## 🛠️ Tools Used

- Python 3
- pandas

## ▶️ How to Run

1. Make sure you have Python and pandas installed
2. Place the ratings.csv and movies.csv files in the same folder
3. Run the script:
4. python movie_analyzer.py
5. ## 📊 Sample Output

Top-rated movies with at least 3 ratings:
Inception        4.67
The Dark Knight  4.50
The Matrix       4.33
## ✨ Notes

- You can replace the sample CSV files with real data from sources like MovieLens.
- The project uses basic data cleaning and merging — good for beginners in data analytics.

---

Made by Debosmita Sen