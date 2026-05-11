import streamlit as st
import numpy as np
import pickle
import pandas as pd
from datetime import timedelta
import os

# ------------------ LOAD MODEL ------------------
model = pickle.load(open("model/model.pkl", "rb"))
scaler = pickle.load(open("model/scaler.pkl", "rb"))

st.title("🏥 PCOS Clinical Decision Support System")

# ------------------ SESSION ------------------
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

# ------------------ SIDEBAR ------------------
menu = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "🔍 Prediction", "📅 Period Tracker", "🧬 Health Monitor", "💬 Consultation"]
)

st.sidebar.write(f"👤 User: {st.session_state.user_name}")
st.sidebar.info("⚠️ Not a medical diagnosis")

# ------------------ HOME ------------------
if menu == "🏠 Home":
    st.header("Welcome")

    name = st.text_input("Enter Your Name")
    if name:
        st.session_state.user_name = name
        st.success(f"Welcome, {name}!")

# ------------------ PREDICTION ------------------
elif menu == "🔍 Prediction":

    st.header(f"PCOS Analysis for {st.session_state.user_name}")

    # ⭐ AGE ADDED
    age = st.number_input("Age", 10, 50)

    height = st.number_input("Height (cm)", 100, 220)
    weight = st.number_input("Weight (kg)", 30, 120)

    height_m = height / 100
    bmi = weight / (height_m ** 2)
    st.write(f"📊 BMI: {bmi:.2f}")

    cycle_len = st.number_input("Cycle Length", 20, 60)
    cycle_type = st.selectbox("Cycle Type", ["Regular", "Irregular"])

    hair = st.selectbox("Hair Growth", ["No", "Yes"])
    skin = st.selectbox("Skin Darkening", ["No", "Yes"])

    # OPTIONAL FSH/LH
    know = st.radio("Do you know your hormone levels (FSH/LH)?", ["No", "Yes"])

    if know == "Yes":
        fsh_lh = st.number_input("Enter FSH/LH Ratio", min_value=0.0)
    else:
        fsh_lh = 1.0

    if st.button("Analyze"):

        cycle_type_val = 1 if cycle_type == "Irregular" else 0
        hair_val = 1 if hair == "Yes" else 0
        skin_val = 1 if skin == "Yes" else 0
        weight_gain = 1 if weight > 65 else 0

        # ✅ FINAL INPUT WITH AGE FIRST
        data = np.array([[
            age,
            cycle_type_val,
            cycle_len,
            bmi,
            weight_gain,
            hair_val,
            skin_val,
            fsh_lh
        ]])

        data = scaler.transform(data)

        pred = model.predict(data)[0]
        prob = model.predict_proba(data)[0][1]

        st.subheader(f"📊 Risk Score: {prob*100:.2f}%")

        if pred == 1:
            st.error("⚠️ High Risk of PCOS")
        else:
            st.success("✅ Low Risk")

        # Save
        save_data = pd.DataFrame([{
            "Name": st.session_state.user_name,
            "Age": age,
            "BMI": bmi,
            "Cycle Length": cycle_len,
            "Risk": prob
        }])

        if os.path.exists("user_data.csv"):
            save_data.to_csv("user_data.csv", mode='a', header=False, index=False)
        else:
            save_data.to_csv("user_data.csv", index=False)

# ------------------ PERIOD TRACKER ------------------
elif menu == "📅 Period Tracker":

    last = st.date_input("Last Period")
    cycle = st.number_input("Cycle Length", 20, 40)

    if st.button("Predict"):
        next_p = last + timedelta(days=cycle)
        ovulation = next_p - timedelta(days=14)

        st.success(f"Next Period: {next_p}")
        st.info(f"🌼 Ovulation: {ovulation}")

# ------------------ HEALTH MONITOR ------------------
elif menu == "🧬 Health Monitor":

    st.header(f"Health Monitor for {st.session_state.user_name}")

    irregular = st.checkbox("Irregular Periods")
    acne = st.checkbox("Acne")
    hair = st.checkbox("Hair Growth")
    weight = st.checkbox("Weight Gain")

    score = 100
    if irregular: score -= 20
    if acne: score -= 15
    if hair: score -= 20
    if weight: score -= 15

    st.progress(score/100)
    st.write(f"💯 Health Score: {score}")

    if st.button("Save Health Data"):

        df = pd.DataFrame([{
            "Name": st.session_state.user_name,
            "Health Score": score
        }])

        if os.path.exists("health.csv"):
            df.to_csv("health.csv", mode='a', header=False, index=False)
        else:
            df.to_csv("health.csv", index=False)

        st.success("Saved!")

    if os.path.exists("health.csv"):
        df = pd.read_csv("health.csv")
        user_df = df[df["Name"] == st.session_state.user_name]

        if not user_df.empty and "Health Score" in user_df.columns:
            st.line_chart(user_df["Health Score"])

# ------------------ CONSULTATION ------------------
elif menu == "💬 Consultation":

    st.header("Consultation")

    issue = st.selectbox("Select Issue",
                         ["Irregular periods", "Weight gain", "Hair growth"])

    if issue == "Irregular periods":
        st.write("Consult doctor if persistent")
    elif issue == "Weight gain":
        st.write("Exercise + diet")
    elif issue == "Hair growth":
        st.write("Hormonal imbalance possible") 