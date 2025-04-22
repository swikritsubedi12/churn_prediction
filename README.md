# Customer Churn Prediction 📉

A machine learning classification project to predict whether a customer will churn or not based on various attributes. This project uses real-world customer data and applies multiple machine learning models to determine the best performing model for churn prediction.

## 🚀 Project Overview

Customer churn is a critical metric for businesses, especially in the telecom sector. By predicting potential churners, companies can take proactive actions to retain customers.

This project aims to:
- Explore and analyze customer data
- Engineer relevant features
- Apply and evaluate multiple classification models
- Build the best performing model for deployment

## 🧠 Machine Learning Models Used

- Logistic Regression
- Random Forest Classifier
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- Decision Tree
- XGBoost (if applicable)

## 📁 Project Structure

```
churn_prediction/
│
├── dataset/                  # Raw and cleaned dataset files
├── models/                   # Saved models (if any)
├── notebooks/                # Jupyter notebooks for EDA and model training
├── app/                      # Streamlit app or Flask API for deployment
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── main.py                   # Main script (optional)
```

## 📊 Dataset

- Source: Kaggle
- Features: Gender, Tenure, Monthly Charges, Total Charges, Contract Type, Payment Method, etc.
- Target: `Churn` (Yes/No)

## 🛠️ Features Engineering

- Encoding categorical variables using One-Hot or Label Encoding
- Handling missing values
- Feature scaling with StandardScaler or MinMaxScaler
- Correlation analysis for feature selection

## 📈 Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- ROC-AUC Score

## 💻 Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Streamlit (for deployment)
- VS Code

## ✅ How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/swikritsubedi12/churn_prediction.git
   cd churn_prediction
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the notebook or main script to train and evaluate models:
   ```bash
   jupyter notebook
   ```

5. (Optional) Run the Streamlit app:
   ```bash
   streamlit run app/app.py
   ```

## 📌 Future Improvements

- Hyperparameter tuning using GridSearchCV
- Model explainability using SHAP/LIME
- API or web deployment using Flask or Streamlit Sharing
- Add more models like LightGBM or CatBoost

## 🙋‍♂️ Author

**Swikrit Subedi**  
📧 swikritsubedi12@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/swikrit-subedi-4913a8340)  
💻 [GitHub](https://github.com/swikritsubedi12?tab=repositories)
🔗 [Streamlit](https://churnprediction12.streamlit.app/)
---

> This project is part of my data science portfolio. Feedback and contributions are welcome!
