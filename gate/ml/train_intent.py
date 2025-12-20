import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("data/gate_logs.csv")

X = df[['visit_time', 'frequency_7d']]
y = df['intent']

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "intent_model.pkl")
