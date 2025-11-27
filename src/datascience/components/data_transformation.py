import os
from sklearn.model_selection import train_test_split
from src.datascience.entity.config_entity import DataTransformationConfig
from src.datascience import logger
import pandas as pd



class DataTransformation:
    def __init__(self,config:DataTransformationConfig) -> None:
        self.config=config

    def train_test_spliting(self):
        data=pd.read_csv(self.config.data_path)

        train,test=train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir,"train.csv"))
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"))

        logger.info("data transformation is done")
        logger.info(train.shape)
        logger.info(test.shape)
