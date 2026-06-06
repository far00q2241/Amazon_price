# Product Prediction App

## Project Overview

This project uses Machine Learning to predict product outcomes based on customer ratings, review counts, product popularity, and category information.

The model is deployed using Streamlit, allowing users to enter product details and receive predictions instantly.

## Features Used

* Rating
* Review Count
* Product Name Frequency
* Category Electronics

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit

## Project Structure

```text
Product-Prediction-App/
│
├── app.py
├── product_model.pkl
├── requirements.txt
└── README.md
```

## Streamlit Application

The application allows users to:

* Enter product information
* Predict product performance
* View results instantly through a web interface

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/product-prediction-app.git
cd product-prediction-app
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Input Features

| Feature              | Description                          |
| -------------------- | ------------------------------------ |
| Rating               | Product rating (0–5)                 |
| Review_Count         | Number of product reviews            |
| freq_Product_Name    | Frequency of product name occurrence |
| Category_Electronics | Electronics category indicator (0/1) |

## Example Input

* Rating = 4.5
* Review Count = 5000
* Product Name Frequency = 1
* Category Electronics = No

## Future Improvements

* Hyperparameter tuning
* More product features
* Interactive visualizations
* Model comparison

## Author

Farooq Khan

Machine Learning Enthusiast | Data Science
