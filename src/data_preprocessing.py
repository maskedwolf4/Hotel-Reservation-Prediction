import os
import pandas as pd
import numpy as np
from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import *
from utils.common_functions import read_yaml,load_data
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE

logger = get_logger(__name__)

class Data_Preprocessing:

    def __init__(self, train_path, test_path, processed_dir, config_path):
        self.train_path = train_path
        self.test_path = test_path
        self.processed_dir = processed_dir
        self.config_path = read_yaml(config_path)

        if not os.path.exists(self.processed_dir):
            os.makedirs(self.processed_dir)

    def preprocess_data(self, df):
        try:
            logger.info("Startting Preprocessing Data...")

            logger.info("Dropping Columns")
            df.drop(columns=['Unnamed: 0', 'Booking_ID'],inplace=True)
            df.drop_duplicates(inplace=True)

            cat_cols = self.config_path["data_preprocessing"]["categorical_columns"]
            num_cols = self.config_path["data_preprocessing"]["numerical_columns"]

            logger.info("Label Encoding...")
            le =  LabelEncoder()
            mappings = {}
            for col in cat_cols:
                df[col] = le.fit_transform(df[col])
                mappings[col] = {label : code for label,code in zip(le.classes_, le.transform(le.classes_))}

            logger.info("Label Encodings are...")
            for col,label in mappings.items():
                logger.info(f"{col}:{label}")


            logger.info("Handling Skewness...")
            skewness_threshlod = self.config_path["data_preprocessing"]["skewness_threshold"]

            skewness = df[num_cols].apply(lambda x:x.skew())

            for column in skewness[skewness>skewness_threshlod].index:
                df[column] = np.log1p(df[column])

            return df
        
        except Exception as e:
            logger.error("Error in Data Preprocessing!! ",e)
            raise CustomException("Error is Data Preprocessing ",e)
        
    def balance_data(self, df):
        try: 
            logger.info("Balancing the data")
            X = df.drop(columns='booking_status')
            y =  df["booking_status"]
            smote = SMOTE(random_state=42)
            X_res , y_res = smote.fit_resample(X,y)
            balanced_df = pd.DataFrame(X_res , columns=X.columns)
            balanced_df["booking_status"] = y_res

            logger.info("Balanced the dataset")
            return balanced_df
        
        except Exception as e:
            logger.error("Error in Balancing Data!!",e)
            raise CustomException("Error in Balancing Data!!",e)
                
    def feature_engineering(self, df):
        try: 
            logger.info("Starting Feature Selection")
            X = df.drop(columns='booking_status')
            y =  df["booking_status"]

            model = RandomForestClassifier(random_state=42)
            model.fit(X,y)
            feature_importance = model.feature_importances_
            feature_importance_df = pd.DataFrame({
                                'feature':X.columns,
                                'importance':feature_importance
                            })
            
            top_features = feature_importance_df.sort_values(by="importance",ascending=False)
            num_features_to_select = self.config_path["data_preprocessing"]["num_of_features"]

            top_features_to_select = top_features["feature"].head(num_features_to_select).values
            logger.info(f"Features Selected: {top_features_to_select}")

            top_features_df = df[top_features_to_select.tolist() + ["booking_status"]]

            return top_features_df
        
        except Exception as e:
            logger.error("Error in Selecting Features!!",e)
            raise CustomException("Error in Selecting Features!!",e)
        


    def save_data(self,df,file_path):
        try:
            logger.info("Saving the preprocessed data ...")
            df.to_csv(file_path, index=False)
            logger.info("Saved the preprocessed data")
        except Exception as e:
            logger.error("Error in saving data!!",e)
            raise CustomException("Error in saving data!!",e)
        

    def process(self):
        try:
            logger.info("Running The Preprocessing Pipelne...")
            train_data = load_data(self.train_path)
            test_data = load_data(self.test_path)

            train_data = self.preprocess_data(train_data)
            test_data = self.preprocess_data(test_data)

            train_data = self.balance_data(train_data)
            test_data = self.balance_data(test_data)

            train_data = self.feature_engineering(train_data)
            test_data = test_data[train_data.columns]

            self.save_data(train_data, PROCESSED_TRAIN_DATA)
            self.save_data(train_data, PROCESSED_TEST_DATA)

            logger.info("Preprocessed and Saved Data Successfully")
        except Exception as e:
            logger.error("Error during Preprocessing Pipeline!!",e)
            raise CustomException("Error while Preprocessing Pipeline!!",e)
        

if __name__=="__main__":
    processor = Data_Preprocessing(TRAIN_FILE_PATH, TEST_FILE_PATH, PROCESSED_DIR, CONFIG_PATH)
    processor.process()
        






