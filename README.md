# 📩 SMS Spam Detection using NLP & Machine Learning

## 🚀 Project Overview
This project builds a machine learning model to classify SMS messages as **Spam** or **Ham (Not Spam)** using Natural Language Processing (NLP) techniques.

The goal is to develop an end-to-end text classification pipeline including:
- Data preprocessing
- Text vectorization using TF-IDF
- Model training
- Model evaluation using precision, recall, F1-score
- Visualization using confusion matrix

---

## 📊 Dataset

- **Dataset:** SMS Spam Collection Dataset  
- **Total Messages:** 5572  
- **Ham:** 4825 (~86%)  
- **Spam:** 747 (~14%)  

The dataset is imbalanced, making recall and precision important evaluation metrics beyond simple accuracy.

---

## 🧠 Methodology

### 1️⃣ Data Cleaning
- Removed unnecessary columns
- Renamed columns for clarity
- Encoded labels:
  - Ham → 0
  - Spam → 1

### 2️⃣ Text Vectorization
Used **TF-IDF (Term Frequency – Inverse Document Frequency)** to convert text messages into numerical feature vectors.

- Total extracted features: 8672 unique words

### 3️⃣ Train-Test Split
- 80% Training Data
- 20% Testing Data
- Random state fixed for reproducibility

---

## 🤖 Models Used

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

The model is very precise (no false positives) but misses some spam messages.

---

### 🔹 Logistic Regression
(To be filled after evaluation)

---

## 📈 Evaluation Metrics

Since the dataset is imbalanced, evaluation was done using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

Special focus was placed on **Spam Recall**, as missing spam messages is more critical than falsely flagging ham.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## 🔮 Future Improvements

- Hyperparameter tuning
- Advanced text preprocessing (stemming, lemmatization)
- Class imbalance handling
- Deploying model as a REST API
- Building a web interface for real-time predictions

---

## 📌 Key Learning Outcomes

- End-to-end NLP pipeline implementation
- Text vectorization using TF-IDF
- Handling imbalanced datasets
- Model comparison and evaluation
- Git version control and project structuring

---

## 📎 How to Run the Project

1. Clone the repository
2. Install dependencies:

