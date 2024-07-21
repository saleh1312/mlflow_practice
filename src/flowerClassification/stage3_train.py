#!/usr/bin/env python
# coding: utf-8




import numpy as np
import pandas as pd
import json
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import mlflow
import numpy as np





with open('assets/feature_store/pca_data.json', 'r') as f:
    combined = json.load(f)
    
metadata = combined['metadata']
print(metadata["description"])
data = combined['data']


df = pd.DataFrame(data)
df.head()





x= df.drop(columns=["target"])
y= df["target"]





X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)





X_train.shape





from flowerClassification.config import config
import flowerClassification.utils as utils





current_branch = utils.get_current_branch()
current_branch

head_commit = utils.get_current_commit_id()
head_commit





config






log_reg = LogisticRegression(C = config.logistic_regression.C)
dec_tree = DecisionTreeClassifier(max_depth = config.desition_tree.max_depth )

# Predict and evaluate the models
models = {
    'Logistic Regression': log_reg,
    'Decision Tree': dec_tree
}





mlflow.set_experiment("flowerClassification")


scores={
    
}

for model_name, model in models.items():
    model.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred, output_dict=True)
    accuracy = report['accuracy']
    f1_score = report['weighted avg']["f1-score"]
    
    scores={
        **scores,
        f"{model_name}_accuracy":accuracy,
        f"{model_name}_f1_score":f1_score
    }
    
    print(report)    
    print(f"Model: {model_name}")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))
    print("-" * 60)






params = {
    "pca_comps" : config.prep.pca_comps_count,
    "lr_C":config.logistic_regression.C,
    "desition_tree_max_depth":config.desition_tree.max_depth
}





scores





current_branch,head_commit





with mlflow.start_run(run_name="koko",tags={"branch":current_branch , 'commit_id':head_commit}) as run:
    mlflow.log_params(params)
    mlflow.log_metrics(scores)







