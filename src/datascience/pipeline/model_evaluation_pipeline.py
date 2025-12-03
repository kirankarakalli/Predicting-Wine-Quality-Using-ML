
from src.datascience.components.model_evaluation import ModelEvaluation
from src.datascience.config.configuration import ConfigurationManager


STAGE_NAME = "MODEL_EVAL_STAGE"

class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass
    def initiate_model_eval(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()