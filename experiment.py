import dagshub
dagshub.init(repo_owner='RiteshTiwari554', repo_name='Kidney_disease_Classifier', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)