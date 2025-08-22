# House Price Prediction System  

## 📌 Project Overview  
This is a **Machine Learning project** designed to predict house prices based on various features such as **area, number of bedrooms, bathrooms, furnishing status, and proximity to the main road**.  

The dataset used is relatively small, but the challenge arises due to **strong multicollinearity among features**. The objective was to build regression models that can predict housing prices both with **single features** and **multiple features**, and then compare their performance.  

---

## 🎯 Objectives  
- Understand and clean the dataset.  
- Build regression models using:  
  - A **single feature** (e.g., `area`).  
  - **Multiple features** combined.  
- Evaluate the models using performance metrics such as **R² Score, RMSE, and MAE**.  
- Compare and analyze the effectiveness of the models.  

---

## 📂 Dataset  
- File used: `Housing.csv`  
- Features considered:  
  - `area`  
  - `bedrooms`  
  - `bathrooms`  
  - `stories`  
  - `mainroad`  
  - `guestroom`  
  - `basement`  
  - `hotwaterheating`  
  - `airconditioning`  
  - `parking`  
  - `prefarea`  
  - `furnishingstatus`  
- Target column: **price**  

### 🔹 Data Preprocessing  
- Converted categorical **yes/no** columns → Binary (1 = yes, 0 = no).  
- Converted **furnishing status** →  
  - unfurnished = 0  
  - semi-furnished = 1  
  - furnished = 2  
- Checked for missing values → **No missing values found**.  

---

## ⚙️ Methodology  

### 🔹 Models Implemented  
1. **Simple Linear Regression** → Using only `area` as the predictor.  
2. **Multiple Linear Regression** → Using all available features.  

### 🔹 Metrics Used  
- R² Score (Coefficient of Determination)  
- RMSE (Root Mean Squared Error)  
- MAE (Mean Absolute Error)  

---

## 📊 Results  

| Model                       | R² Score | RMSE         | MAE        |
|-----------------------------|----------|--------------|------------|
| Linear Regression (area)    | 0.27     | 1,917,103.70 | 1,474,748.13 |
| Linear Regression (all features) | 0.65     | 1,331,071.41 | 979,679.69   |

✅ **Multiple Linear Regression** (all features) outperformed the single feature model with a significantly higher R² score and lower errors.  

---

## 📈 Visualizations (Recommended Enhancements)  
- Scatter plot: **Actual vs Predicted Prices**  
- Distribution plot: **Residual errors**  
- Feature importance (to analyze which features most influence price)  

---

## 📦 Requirements  

Make sure you have the following installed:  
- Python 3.x  
- pandas  
- numpy  
- scikit-learn  

Install dependencies with:  
```bash
pip install pandas numpy scikit-learn
```

## How to Run
Clone the repository:
git clone https://github.com/your-username/House-Price-Prediction.git
cd House-Price-Prediction
Place the dataset file Housing.csv inside the project directory.

Run the script:
python house_price_prediction.py

## 🙌 Acknowledgment
This project was created as part of my learning in Machine Learning & Regression Models.
Special thanks to the open-source ML community for providing valuable resources and guidance.

## 📝 License
This project is for educational purposes only.
