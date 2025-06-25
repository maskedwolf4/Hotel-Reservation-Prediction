from src.data_ingestion import DataIngestion
from src.data_preprocessing import Data_Preprocessing
from src.model_training import ModelTraining
from utils.common_functions import read_yaml
from config.paths_config import *


if __name__=="__main__":

    # DATA INGESTION
    data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()

    # DATA PREPROCESSING
    processor = Data_Preprocessing(TRAIN_FILE_PATH, TEST_FILE_PATH, PROCESSED_DIR, CONFIG_PATH)
    processor.process()

    # MODEL TRAINING
    trainer = ModelTraining(PROCESSED_TRAIN_DATA,PROCESSED_TEST_DATA,MODEL_OUTPUT_PATH)
    trainer.run()
