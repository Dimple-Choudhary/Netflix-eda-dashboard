# src/eda.py

class NetflixEDA:
    """
    Encapsulates EDA operations for Netflix dataset.
    """

    def __init__(self, df):
        self.df = df

    def content_type_distribution(self):
        """Returns count of Movies vs TV Shows"""
        return self.df["type"].value_counts()

    def top_countries(self, n=10):
        """Returns top countries producing content"""
        return self.df["country"].value_counts().head(n)
