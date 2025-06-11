from joblib import load
import streamlit as st

model=load("Student_Performance_predictor")

st.title("Student Exam Marks Predictor")
st.subheader("Enter the below details")

hours_studied=st.number_input("Enter total hours studied",min_value=0)
previous_score=st.number_input("Enter previous exam marks",min_value=0,max_value=100)
hours_slept=st.number_input("Enter total hours slept the day before exam ",min_value=0,max_value=24)
previous_papers=st.number_input("Enter number of previoud question papers practiced",min_value=0)

if hours_studied and previous_papers and previous_score and hours_slept:
    if st.button("Predict Score"):
        score=model.predict([[hours_studied,previous_score,hours_slept,previous_papers]])
        if score>100:
            score =100
        st.write(f"Expected Score:   {score}")