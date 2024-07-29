
import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Define a function to make predictions
def predict(CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary):
    # Create a dataframe with all features
    df = pd.DataFrame([[CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary]],
                      columns=['CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary'])

    # Encode Gender
    df['Gender'] = df['Gender'].map({'Female': 0, 'Male': 1})
    df['HasCrCard'] = df['HasCrCard'].map({'No': 0, 'Yes': 1})
    df['IsActiveMember'] = df['IsActiveMember'].map({'No': 0, 'Yes': 1})
    # Apply ColumnTransformer and StandardScaler
    df = ct.transform(df)
    df = sc.transform(df)
    prediction = rf.predict_proba(df)[:, 1]
    return prediction

# Load the saved model and transformers
rf = pickle.load(open('model.pkl', 'rb'))
sc = pickle.load(open('scaler.pkl', 'rb'))
ct = pickle.load(open('encoder.pkl', 'rb'))

#background image
page_bg_img="""
<style>
[data-testid="stAppViewContainer"]{
# background-image: url("https://plus.unsplash.com/premium_vector-1683133474032-d9de48e9199c?q=80&w=1880&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D.jpg");
background-color: #e5e5f7;
opacity: 0.8;
background-image:  linear-gradient(#b2a3e2 2px, transparent 2px), linear-gradient(90deg, #b2a3e2 2px, transparent 2px), linear-gradient(#b2a3e2 1px, transparent 1px), linear-gradient(90deg, #b2a3e2 1px, #e5e5f7 1px);
background-size: 50px 50px, 50px 50px, 10px 10px, 10px 10px;
background-position: -2px -2px, -2px -2px, -1px -1px, -1px -1px;
# background-size:cover;
# height:100%;
# position:absolute;
# width:100%;
}
.css-1dp5vir, .css-1j77c0c, .css-1cpxqw2, .css-1djfy51 {
  font-size: 20px;
  font-weight: bold;
  color: #000000;
}
.css-1cpxqw2, .css-1djfy51 {
  margin-bottom: 10px;
}
</style>   
"""
st.markdown(page_bg_img, unsafe_allow_html=True)



# title
title_style = """
<style>
.title {
    font-size: 50px;
    font-weight: bold;
    color: #4B0082;
    text-align: center;
    margin-bottom: 20px;
}
.message {
    font-size: 20px;
    font-weight: normal;
    color: #000000;
    text-align: center;
    margin-bottom: 20px;
}
</style>
"""
st.markdown(title_style, unsafe_allow_html=True)
st.markdown("<div class='title'>CHURN PREDICTION APP</div>", unsafe_allow_html=True)
st.markdown("<div class='message'>[✒✒✒✒Please fill the below options ✒✒✒✒]</div>", unsafe_allow_html=True)


#selectboxes
st.markdown("<h3 style='font-size:20px;'>GEOGRAPHY</h3>", unsafe_allow_html=True)
Geography = st.selectbox("", ['France', 'Spain', 'Germany'], key="Geography")

st.markdown("<h3 style='font-size:20px;'>GENDER</h3>", unsafe_allow_html=True)
Gender = st.selectbox("", ['Female', 'Male'], key="Gender")

st.markdown("<h3 style='font-size:20px;'>AGE</h3>", unsafe_allow_html=True)
Age = st.text_input("", key="Age", placeholder="Please fill")


st.markdown("<h3 style='font-size:20px;'>CREDIT SCORE</h3>", unsafe_allow_html=True)
CreditScore = st.number_input("", key="CreditScore", placeholder="Please fill")

st.markdown("<h3 style='font-size:20px;'>TENURE</h3>", unsafe_allow_html=True)
Tenure = st.text_input("", key="Tenure", placeholder="Please fill")

st.markdown("<h3 style='font-size:20px;'>BANK BALANCE</h3>", unsafe_allow_html=True)
Balance = st.text_input("", key="Balance", placeholder="Please fill")

st.markdown("<h3 style='font-size:20px;'>NUMBER OF PRODUCTS </h3>", unsafe_allow_html=True)
NumOfProducts = st.text_input("", key="NumOfProducts", placeholder="Please fill")

st.markdown("<h3 style='font-size:20px;'>CREDIT CARD AVAILABILITY (YES/NO) </h3>", unsafe_allow_html=True)
HasCrCard = st.selectbox("", ['No', 'Yes'], key="HasCrCard")

st.markdown("<h3 style='font-size:20px;'>ACTIVE MEMBER (YES/NO) </h3>", unsafe_allow_html=True)
IsActiveMember = st.selectbox("", ['No', 'Yes'], key="IsActiveMember")

st.markdown("<h3 style='font-size:20px;'>ESTIMATED SALARY </h3>", unsafe_allow_html=True)
EstimatedSalary = st.text_input("", key="EstimatedSalary", placeholder="Please fill")


# Create a button to make a prediction
st.markdown("<div class='message'>(For prediction click [Predict] below)</div>", unsafe_allow_html=True)
if st.button("Predict"):
    CreditScore = float(CreditScore)
    Age = float(Age)
    Tenure = float(Tenure)
    Balance = float(Balance)
    NumOfProducts = float(NumOfProducts)
    EstimatedSalary = float(EstimatedSalary)
    prediction = predict(CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary)
    st.write("**🔳 Probability of Customer Leaving:** ", prediction[0])
    if prediction > 0.5:
        st.write("**🔳 Customer will likely leave**")
    else:
        st.write("**🔳 Customer will likely stay**")

#javascropt code for selectboxes
clear_input_script = """
<script>
document.addEventListener("DOMContentLoaded", function() {
    var inputs = document.getElementsByTagName("input");
    for (var i = 0; i < inputs.length; i++) {
        inputs[i].addEventListener("focus", function(event) {
            if (this.value == "Please fill") {
                this.value = "";
            }
        });
    }
});
</script>
"""
st.components.v1.html(clear_input_script)

