# AI2-Project
Startups Success prediction

# 📊 Startup Success Prediction Using Machine Learning

## 📌 Project Overview
This project leverages machine learning to predict the success of startups based on various features such as funding, milestones, relationships, and more. By analyzing industry trends and company attributes, the model determines whether a startup is likely to succeed (acquired) or fail (closed). The ultimate goal is to assist investors and entrepreneurs in making informed decisions about startup investments.

---

## 📂 Dataset Overview

### **Context**
Startups are new businesses designed to scale and grow rapidly. However, they face significant uncertainty and a high failure rate. Predicting a startup's success can provide valuable insights for stakeholders.

### **Objective**
The objective is to classify startups into two categories: 
- **Acquired (Success)**
- **Closed (Failure)**

### **Key Features in the Dataset**
- `age_first_funding_year`: Time since the first funding.
- `age_last_funding_year`: Time since the last funding.
- `relationships`: Number of key relationships the startup has.
- `funding_rounds`: Number of funding rounds completed.
- `funding_total_usd`: Total funding received in USD.
- `milestones`: Number of significant achievements.
- `state`: Location of the startup.
- `industry_type`: The industry the startup operates in.
- `has_VC`, `has_angel`: Indicates the type of investors.
- `status`: The target variable (`acquired` = success, `closed` = failure).

---

## 🛠️ Feature Engineering

The following preprocessing steps were applied to the dataset:
1. **Data Cleaning**: 
   - Removed irrelevant or redundant columns.
   - Dropped outliers in `avg_participants` using a statistical threshold.
2. **Categorical Encoding**: 
   - Used `LabelEncoder` to convert categorical variables into numeric format.
3. **Feature Selection**: 
   - Retained only relevant features for the model to ensure better performance.

---

## 🤖 Machine Learning Models

### Models Used:
1. **Logistic Regression**:
   - A simple yet effective model for binary classification.
   - Results:
     - Accuracy: `68.64%`
     - Precision: `61.36%`
     - Recall: `34.18%`
     - F1-Score: `43.90%`

2. **Decision Tree Classifier**:
   - A more complex model with higher flexibility.
   - Results:
     - Accuracy: `100%`
     - Precision: `100%`
     - Recall: `100%`
     - F1-Score: `100%`

### Single Example Prediction:
The model predicts whether a hypothetical startup (based on given input features) will succeed or fail. In the provided example, the result was **Failure (Closed)**.

---

## 📈 Results & Insights

- **Logistic Regression**: 
  - Lower accuracy and recall indicate it struggles with the dataset's complexity.
- **Decision Tree**:
  - Achieved perfect metrics, though this might suggest overfitting on the training data.

---

## 💡 Applications

### Real-World Use Cases:
1. **For Investors**:
   - Identify high-potential startups for investment.
2. **For Entrepreneurs**:
   - Assess factors contributing to success and adapt strategies accordingly.
3. **For Analysts**:
   - Provide data-driven insights into startup ecosystems.
