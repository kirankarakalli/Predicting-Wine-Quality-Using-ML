from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation
from src.datascience import logger
from pathlib import Path

STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self) -> None:
        pass
    def initiate_data_transformation(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"),'r') as f:
                status=f.read().split(" ")[-1]
                if status=="True":
                    config=ConfigurationManager()
                    data_validation_config=config.get_data_transformation_config()
                    data_validation=DataTransformation(config=data_validation_config)
                    data_validation.train_test_spliting()

                else:
                    raise Exception("your data is not valid")
                
        except Exception as e:
            print(e)





