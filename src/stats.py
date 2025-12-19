# src/stats.py

def probability_movie(df):
    """
    Calculate probability of content being a Movie.
    """
    total = len(df)
    movies = (df["type"] == "movie").sum()
    return movies / total
