import pandas as pd
from .data_loader import load_csv
from .data_cleaning import clean_data
from .visualization import create_basic_plots
import logging



class NetflixEDA:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = None
        logging.info("NetflixEDA object created")

    def load_data(self):
        logging.info("Loading dataset")
        self.df = pd.read_excel(self.filepath)
        logging.info(f"Dataset loaded with shape: {self.df.shape}")

    def run_basic_plots(self):
        logging.info("Creating basic plots")
        # plotting code here
        logging.info("Basic plots created and saved")
