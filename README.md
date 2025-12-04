# Predicting-Wine-Quality-Using-ML

## workflows--ML Pipeline


This project builds an end-to-end Machine Learning pipeline to predict the quality of wine based on physicochemical features.
It follows a modular, production-ready architecture that includes:

Data ingestion
Data validation
Data transformation
Model training
Model evaluation
Model deployment (Flask API)



Predicting-Wine-Quality-Using-ML
│
├── app.py
├── main.py
├── model.pkl
├── requirements.txt
│
├── configs/
│   ├── params.yaml
│   ├── schema.yaml
│
├── src/datascience/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   ├── model_evaluation.py
│   │
│   ├── pipelines/
│   ├── utils/
│
├── artifacts/        # Generated outputs
└── README.md


⚙️ How to Run the Project

1. Clone the repository
    git clone https://github.com/kirankarakalli/Predicting-Wine-Quality-Using-ML.git
    cd Predicting-Wine-Quality-Using-ML


2. Create virtual environment
    python -m venv venv
    source venv/Scripts/activate     

3. Install dependencies
    pip install -r requirements.txt

4. Run the ML pipeline
     python main.py

5. Run Flask App
     python app.py


ML Models Used
1. ElasticNet
2. RandomForest Classfier


🛠️ Technologies Used

    Python

    NumPy / Pandas

    Scikit-Learn

    Matplotlib

    Flask

    YAML for configuration

    Logging and exception handling

    Modular ML pipeline design

