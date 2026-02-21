# 📩 SMS Spam Detection Web App  
### NLP-Based Spam Classification using TF-IDF & Machine Learning

---

## 🚀 Project Overview

This project builds and deploys an end-to-end **SMS Spam Detection system** using Natural Language Processing (NLP) and Machine Learning.

It includes:

- Data preprocessing & label encoding  
- Text vectorization using TF-IDF  
- Model comparison (Naive Bayes vs Logistic Regression)  
- Handling class imbalance  
- Performance evaluation using precision, recall & F1-score  
- Interactive Streamlit web application  

The final output is a deployable web app that allows users to test custom messages in real time.

---

## 📊 Dataset

- **Dataset:** SMS Spam Collection Dataset  
- **Total Messages:** 5572  
- **Ham:** 4825 (~86%)  
- **Spam:** 747 (~14%)  

The dataset is imbalanced, making **spam recall** a critical evaluation metric.

---

## 🧠 Methodology

### 1️⃣ Data Cleaning
- Removed unnecessary columns  
- Renamed columns for clarity  
- Encoded labels:
  - Ham → 0  
  - Spam → 1  

---

### 2️⃣ Text Vectorization

Used **TF-IDF (Term Frequency – Inverse Document Frequency)** to convert text messages into numerical feature vectors.

- Total features extracted: **8672 unique words**

---

### 3️⃣ Train-Test Split

- 80% Training Data  
- 20% Testing Data  
- `random_state=42` for reproducibility  

---

## 🤖 Models Implemented

### 🔹 Multinomial Naive Bayes

- Accuracy: **96.2%**
- Spam Precision: **1.00**
- Spam Recall: **0.72**
- F1-Score (Spam): **0.84**

Confusion Matrix:

|                | Predicted Ham | Predicted Spam |
|---------------|---------------|----------------|
| Actual Ham    | 965           | 0              |
| Actual Spam   | 42            | 108            |

The model is highly precise (no false positives) but misses some spam messages.

---

### 🔹 Logistic Regression (Balanced)

Implemented using:

LogisticRegression(max_iter=1000, class_weight='balanced')

Results:

- Accuracy: **96%**
- Spam Recall: **89%**
- Spam Precision: **~93%**
- Reduced missed spam messages from 41 → 16

Confusion Matrix:

|                | Predicted Ham | Predicted Spam |
|---------------|---------------|----------------|
| Actual Ham    | 955           | 10             |
| Actual Spam   | 16            | 134            |

Balanced Logistic Regression significantly improved recall while maintaining strong precision.

---

## 📈 Model Comparison

| Model | Spam Recall | False Positives |
|--------|------------|----------------|
| Naive Bayes | 72% | 0 |
| Logistic Regression | 73% | 0 |
| **Logistic (Balanced)** | **89%** | 10 |

Balanced Logistic Regression performs best in real-world spam detection scenarios.

---

## 🌐 Streamlit Web Application

An interactive web application was built using **Streamlit** to:

- Accept custom SMS input  
- Compare both models side-by-side  
- Display spam probability scores  
- Visualize predictions in real time  


---

## 🛠️ Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Seaborn  
- Streamlit  
- Joblib  
- Git & GitHub  

---


---

## 🔮 Future Improvements

- Hyperparameter tuning using GridSearchCV  
- Advanced text preprocessing (stemming, lemmatization, n-grams)  
- Cross-validation  
- Deployment on Streamlit Cloud  
- Integration with real SMS APIs  

---

## 🎓 Key Learning Outcomes

- End-to-end NLP pipeline development  
- TF-IDF feature engineering  
- Handling imbalanced classification problems  
- Model comparison & evaluation  
- Building and deploying ML web applications  
- Version control and structured project organization  

---

## 👩‍💻 Author

Built as a hands-on NLP & Machine Learning project focused on real-world spam detection and deployable ML systems. 

