import numpy as np
import pandas as pd
import streamlit as st

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Streamlit caching
@st.cache_data
def load_data():
    """This function returns the preprocessed data"""
    kentang = pd.read_csv('data/heart_data.csv')
    kentang.dropna(inplace=True)  # Ensure no NaN values
    kentang.drop(['index'], axis=1, inplace=True)
    kentang.drop(['id'], axis=1, inplace=True)
    kentang['age'] = kentang['age'] // 365
    # All features for prediction
    X_pred = kentang[['age', 'gender', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active']]
    # Selected features for visualization
    X_vis = kentang[['age', 'gender', 'cholesterol', 'gluc', 'smoke', 'alco', 'active']]
    y = kentang['cardio']
    return kentang, X_pred.values, X_vis.values, y.values  # Ensure X_pred, X_vis, and y are numpy arrays

@st.cache_data
def train_model(X, y):
    model = MLPClassifier(activation='tanh', hidden_layer_sizes=(100,), solver='adam')
    model.fit(X, y)
    score = model.score(X, y)
    return model, score

def predict(X, y, feature):
    model, score = train_model(X, y)
    prediction = model.predict(np.array(feature).reshape(1, -1))
    return prediction, score


