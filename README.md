# 🚗 Car Price Prediction Model

A beginner-friendly machine learning project that predicts the selling price of a used car using Python, Pandas, Scikit-learn, and Streamlit.

## Project Introduction

This project demonstrates a simple end-to-end machine learning workflow:
- Load and clean the dataset
- Train a regression model
- Evaluate model performance
- Build a Streamlit web app for real-time predictions

## Features

- Clean and simple notebook workflow
- Beginner-friendly code comments
- Random Forest Regressor model
- Easy-to-use Streamlit interface
- Prediction output in Lakhs

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

## Dataset Description

The dataset contains information about used cars such as:
- Car name
- Year
- Selling price
- Present price
- Kilometers driven
- Fuel type
- Seller type
- Transmission
- Number of owners

## Project Workflow

1. Load the dataset
2. Clean the data
3. Create the Car Age feature
4. Train a Random Forest Regressor model
5. Evaluate the model
6. Save the trained model as model.pkl
7. Use Streamlit to make predictions

## Model Used

- Random Forest Regressor

## Evaluation Metrics

The model is evaluated using:
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

## How to Run the Project

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the notebook

Open Car_Price_Prediction.ipynb in VS Code and run the cells step by step.

### 3. Run the Streamlit app

```bash
streamlit run app.py
```

## Folder Structure

```text
Car-Price-Prediction/
│
├── Car_Price_Prediction.ipynb
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
├── screenshots/
└── dataset/
    └── car data.csv
```

## Future Improvements

- Add more features for better prediction
- Try other beginner-friendly models
- Improve the Streamlit design
- Add input validation and better error handling

## Screenshots

Add screenshots of the app interface in the screenshots folder for better presentation.
