import streamlit as st
import joblib

# -------------------------
# Load saved models
# -------------------------
log_model = joblib.load("models/logistic_model.pkl")
nb_model = joblib.load("models/naive_bayes_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

# -------------------------
# Streamlit UI Setup
# -------------------------
st.set_page_config(page_title="SMS Spam Detector", layout="centered")

st.title("SMS Spam Detection Web App")
st.write("Compare Balanced Logistic Regression and Naive Bayes models")

st.markdown("---")

# -------------------------
# User Input
# -------------------------
user_input = st.text_area("Enter your message below:")

# -------------------------
# Prediction Logic
# -------------------------
if st.button("Predict"):

    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        # Transform input using saved vectorizer
        input_vector = vectorizer.transform([user_input])

        # Logistic Regression Prediction
        log_prediction = log_model.predict(input_vector)[0]
        log_probability = log_model.predict_proba(input_vector)[0][1]

        # Naive Bayes Prediction
        nb_prediction = nb_model.predict(input_vector)[0]
        nb_probability = nb_model.predict_proba(input_vector)[0][1]

        st.subheader("🔍 Results")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Balanced Logistic Regression")
            if log_prediction == 1:
                st.error("🚨 Spam")
            else:
                st.success("✅ Ham")
            st.write("Spam Probability:", round(log_probability, 3))

        with col2:
            st.markdown("### Naive Bayes")
            if nb_prediction == 1:
                st.error("🚨 Spam")
            else:
                st.success("✅ Ham")
            st.write("Spam Probability:", round(nb_probability, 3))