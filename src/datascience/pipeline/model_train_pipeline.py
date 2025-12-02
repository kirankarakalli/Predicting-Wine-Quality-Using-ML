from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_train import model_train


STAGE_NAME = "Model Training stage"

class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def initiate_model_training(self):
        config=ConfigurationManager()
        model_trainer_config=config.get_model_trainer_config()
        model_trainer=model_train(model_trainer_config) 
        model_trainer.train_model()
    