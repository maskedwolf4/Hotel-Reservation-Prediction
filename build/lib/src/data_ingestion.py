import os
import pandas as pd
from google.cloud import storage
from sklearn.model_selection import train_test_split
from src.custom_exception import CustomException
from src.logger import get_logger
from config.paths_config import *
from utils.common_functions import read_yaml

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self, config):
        self.config =  config["data_ingestion"]
        self.bucket_name = self.config["bucket_name"]
        self.bucket_file_name = self.config["bucket_file_name"]
        self.train_ratio = self.config["train_ratio"]

        os.makedirs(RAW_DIR, exist_ok=True)

        logger.info(f"Data Ingestio Started from {self.bucket_name} of file {self.bucket_file_name}")

    def download_csv_from_gcp(self):
        try:
            client = storage.Client()
            bucket = client.bucket(self.bucket_name)
            blob = bucket.blob(self.bucket_file_name)

            blob.download_to_filename(RAW_FILE_PATH)

            logger.info(f"CSV file succesfully downloaded to {RAW_FILE_PATH}")

        except Exception as e:
            logger.error("Error while loading CSV File")
            raise CustomException("Error while loading CSV File", e)

    def split_data(self):
        try: 
            logger.info("Data Splitting Started")
            data = pd.read_csv(RAW_FILE_PATH)
            train_data, test_data = train_test_split(data, test_size=1-self.train_ratio, random_state=42)

            train_data.to_csv(TRAIN_FILE_PATH)
            test_data.to_csv(TEST_FILE_PATH)

            logger.info(f"Train data saved to {TRAIN_FILE_PATH} and Test data saved to {TEST_FILE_PATH} ")

        except Exception as e:
            logger.error("Error while Splitting Data")
            raise CustomException("Error while Splitting data into Train and Test", e)
        

    def run(self):
        try:
            logger.info("Starting Data Ingestion ....")
            self.download_csv_from_gcp()
            self.split_data()
            logger.info("Data Ingestion Completed.")

        except Exception as e:
            logger.error("Error in Data Ingestion Process ", str(e))
            
        finally:
            logger.info("Data Ingestion Completed")


if __name__=="__main__":

    data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()

