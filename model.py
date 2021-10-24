import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression


def predict_salary(list1):
    df = pd.read_csv(r"F:\ML_projects\demo_deployment\salary.csv")
    df.head()

    df['experience'].fillna(df['experience'].mean(), inplace=True)
    df['test_score'].fillna(df['test_score'].mean(), inplace = True)

    X = df.iloc[ : , 1:-1]
    y = df.iloc[ : ,-1]

    model = LinearRegression()
    model.fit(X, y)

    predicted_salary = model.predict([list1])

    return predicted_salary
    