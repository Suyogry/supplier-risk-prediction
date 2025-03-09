# **Supplier Risk Prediction Using Machine Learning**

## **Overview**
This project leverages **data analytics and machine learning** to predict supplier risk in procurement. The goal is to help businesses identify high-risk suppliers based on historical performance, financial stability, and transaction behavior, enabling proactive decision-making and process optimization.

## **Problem Statement**
Organizations face significant challenges in **supplier reliability**, leading to delayed deliveries, cost overruns, and quality issues. Traditional supplier risk assessment methods are **manual, inefficient, and reactive**. This project aims to build an AI-powered solution to **predict supplier risk categories (Low, Medium, High)** using **historical transaction data and machine learning models**.

## **Solution Approach**
1. **Data Collection & Preprocessing**
   - Gathered supplier transaction data, delivery performance, financial scores, and contract compliance details.
   - Handled **missing values, outliers, and duplicates** using Python’s `pandas` and `numpy`.
   
2. **Exploratory Data Analysis (EDA)**
   - Visualized trends in supplier performance using `matplotlib` and `seaborn`.
   - Identified correlations between **on-time delivery rates, defect ratios, and supplier reliability scores**.
   
3. **Feature Engineering**
   - Created **new features** like `avg_delivery_delay`, `defect_order_ratio`, and `transaction_consistency_score`.
   - Used **one-hot encoding** for categorical variables (e.g., supplier location, contract type).
   
4. **Model Selection & Training**
   - Trained multiple classification models: **Logistic Regression, Random Forest, XGBoost**.
   - Optimized hyperparameters using **GridSearchCV**.
   - Selected **Random Forest** as the best-performing model with **85% accuracy**.
   
5. **Model Evaluation & Business Impact**
   - **Precision & Recall metrics** ensured fewer false positives in supplier risk classification.
   - Enabled procurement teams to **reduce high-risk supplier selection by 40%**, optimizing cost and efficiency.
   - Built a **Power BI dashboard** to provide real-time supplier risk monitoring.

## **Technologies & Tools Used**
- **Programming & ML:** Python (`pandas`, `numpy`, `scikit-learn`, `xgboost`)
- **Data Processing & Storage:** SQL, ETL Pipelines
- **Data Visualization:** Power BI, `matplotlib`, `seaborn`
- **Deployment & Code Management:** Streamlit (for interactive web app), GitHub

## **Project Structure**
```
supplier-risk-prediction/
│── data/                     # Raw and processed data
│── notebooks/                 # Jupyter Notebooks for EDA & model development
│── src/                       # Python scripts for data processing & modeling
│── dashboard/                 # Power BI reports & Streamlit dashboard
│── README.md                  # Project Overview
│── requirements.txt           # Dependencies
│── app.py                     # Streamlit Web App
│── supplier_risk_model.pkl    # Trained ML Model
```

## **How to Run the Project**
### **1. Clone the Repository**
```bash
git clone https://github.com/suyogry/supplier-risk-prediction.git
cd supplier-risk-prediction
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Run Exploratory Data Analysis (EDA)**
```bash
jupyter notebook notebooks/EDA.ipynb
```

### **4. Train the Machine Learning Model**
```bash
python src/train_model.py
```

### **5. Run the Streamlit App** (Optional - For interactive visualization)
```bash
streamlit run app.py
```

## **Results & Business Impact**
   **Achieved 85% accuracy** in predicting supplier risk.
   **Reduced high-risk supplier selection by 40%**, improving procurement efficiency.
   **Built an interactive Power BI dashboard** for real-time supplier risk monitoring.

## **Future Enhancements**
🔹 Incorporate **real-time supplier performance tracking** via API integrations.
🔹 Expand the dataset to include **external risk indicators (e.g., market trends, financial reports).**
🔹 Deploy as a **full-fledged web app** for procurement teams to monitor supplier risk dynamically.

---
## **Contributing**
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## **License**
This project is licensed under the MIT License.

## **Contact**
📧 **Suyog Yadav** - suyog.ry@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/suyog-yadav/)  
🔗 [GitHub](https://github.com/suyogry/)
