# Retail Demand Analysis: Corporación Favorita

## Overview
Explores the Corporación Favorita time series data, focusing particularly on transactions from the Guayas region and pertaining to items belonging to the top three families (GROCERY I,  BEVERAGES, and CLEANING). 

## notebooks
- data_prep.ipynb: begin here to take a look at how the data was loaded and cleaned, and to see the data exploration that led to the choice of features for training the models. Autocorrelation, trend, and seasonality of the dataset were assessed, and an initial attempt at forecasting was done through linear regression.
- Guayas_XGBoost.ipynb: the cleaned dataframe from `data_prep` was imported, further features developed, and then fed to XGBoost variants. The performance of vanilla XGBoost (i.e. done with default parameters) was compared with the best estimator from a randomized search, to determine if tuning hyperparameters would bring improvements to model performance.

## data
- datasets.py: contains links to the data sets

## outputs
- contains relevant plots
- the subfolders `tuned_xgb` and `vanilla_xgb` contain:
    - an aggregated train-prediction-actual plot for all stores and items at once, and
    - ten plots for specific store and item combinations (`_S_{store_id}_I_{item_id}.png`). These are the ten store-item combinations with the most logged days with non-zero sales.

## models
- contains the XGB model with default parameters (XGBVanilla) as well as the best estimator from a randomized search with cross validation (XGBTuned).

### To load the trained model

Using **MLflow**:

```python
import mlflow.sklearn

model = mlflow.sklearn.load_model("models/XGBTuned/artifacts")
y_pred = model.predict(X_test)
```

Or using **plain pickle**:

```python
import pickle

with open("models/XGBTuned/artifacts/model.pkl", "rb") as f:
    model = pickle.load(f)

y_pred = model.predict(X_test)
```

## requirements

see `requirements.txt` from `models/XGBTuned/artifacts` or `models/XGBVanilla/artifacts`