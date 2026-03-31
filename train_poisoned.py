import pandas as pd
import mlflow
import mlflow.sklearn

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

mlflow.set_tracking_uri("sqlite:///mlflow.db")

mlflow.set_experiment("iris_poisoning")

def train(dataset, poison_level):

    df = pd.read_csv(dataset)

    X = df.iloc[:,:4]

    y = df.iloc[:,4]

    X_train,X_test,y_train,y_test = train_test_split(
        X,y,test_size=0.2,random_state=42
    )

    model = RandomForestClassifier()

    model.fit(X_train,y_train)

    preds = model.predict(X_test)

    acc = accuracy_score(y_test,preds)

    prec = precision_score(
    y_test,
    preds,
    average='macro',
    zero_division=0
)

    rec = recall_score(
    y_test,
    preds,
    average='macro',
    zero_division=0
)

    f1 = f1_score(
        y_test,preds,average='macro'
    )

    mlflow.start_run()

    mlflow.log_param("poison_level",poison_level)

    mlflow.log_metric("accuracy",acc)

    mlflow.log_metric("precision",prec)

    mlflow.log_metric("recall",rec)

    mlflow.log_metric("f1",f1)

    mlflow.sklearn.log_model(model,"model")

    mlflow.end_run()

train("iris.csv",0)

train("iris_5.csv",5)

train("iris_10.csv",10)

train("iris_50.csv",50)
