# 🧠 ML-Based House Construction Cost Predictor

This project predicts house construction cost using a machine learning regression model in Python. Users can input area, number of floors, material type, and extra features to get a cost estimate.

## 📁 Files Included

- `house_cost.csv`: Dataset
- `model_train.py`: Trains the ML model
- `predict_cost.py`: Predicts construction cost
- `house_cost_model.pkl`: Saved model
- `README.md`: Project overview

## 🔧 How to Run

1. Train the model:
```bash
python model_train.py


2.Predict construction cost:

python predict_cost.py

3.🎯 Features Used for Prediction

    Area (sq.ft)

    Number of Floors

    Material Type (Normal/Premium)

    Paint (Yes/No)

    Woodwork (Yes/No)

    Tiles (Yes/No)



4.Sample output

📏 Enter area: 520
🏢 Floors: 2
🏗️ Material: normal
🎨 Paint: 1
🪵 Woodwork: 1
🧱 Tiles: 1

💰 Estimated House Cost: ₹2,080,000
