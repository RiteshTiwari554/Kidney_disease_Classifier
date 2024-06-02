# Kidney_disease_Classifier

# Kidney-Disease-Classification-MLflow-DVC


## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/RiteshTiwari554/Kidney_disease_Classifier
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n cnncls python=3.8 -y
```

```bash
conda activate cnncls
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```






## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

##### cmd
- mlflow ui

### DVC Cmd

```bash
dvc init
dvc repro
dvc dag
```

## About MLflow & DVC

#### MLflow

1. Its Production Grade
2. Trace all of your expriements
3. Logging & taging your model

#### DVC

1. Its very lite weight for POC only
2. lite weight expriements tracker
3. It can perform Orchestration (Creating Pipelines)

   

<!-- import dagshub
dagshub.init(repo_owner='RiteshTiwari554', repo_name='Kidney_disease_Classifier', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1) -->
<!-- g -->