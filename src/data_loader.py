import pandas as pd

def load_csv(path):
    """Load a CSV file safely."""
    return pd.read_csv(path)
