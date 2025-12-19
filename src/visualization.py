import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_basic_plots(df, output_dir="assets"):
    """
    Create and save basic EDA plots.
    """

    os.makedirs(output_dir, exist_ok=True)

    # 1️⃣ Content Type Count
    plt.figure(figsize=(6,4))
    sns.countplot(data=df, x="type")
    plt.title("Content Type Distribution")
    plt.savefig(f"{output_dir}/content_type.png")
    plt.close()

    # 2️⃣ Rating Distribution
    plt.figure(figsize=(10,5))
    sns.countplot(data=df, y="rating", order=df["rating"].value_counts().index)
    plt.title("Rating Distribution")
    plt.savefig(f"{output_dir}/ratings.png")
    plt.close()

    print("✔ Basic plots created")
