import logging
from src.netflix_eda import NetflixEDA

# Logging configuration (do this ONCE)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

if __name__ == "__main__":
    logging.info("Starting Netflix EDA pipeline")

    eda = NetflixEDA("data/netflix_cleaned.xlsx")
    eda.run_basic_plots()

    logging.info("Netflix EDA pipeline completed successfully")
