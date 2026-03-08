import streamlit as st
import requests

st.title("🧠 AI Exam Anxiety Detector")

text = st.text_area("How do you feel about your exams?")

if st.button("Check Anxiety"):
    if text.strip() == "":
        st.warning("Please enter text")
    else:
        try:
            response = requests.post(
                "https://ai-exam-anxiety-detector01-production.up.railway.app//predict",
                json={"text": text}
            )

            result = response.json()
            level = result["anxiety_level"]

            if level == "Low":
                st.success("Low Anxiety 😊")
            elif level == "Moderate":
                st.warning("Moderate Anxiety 😐")
            else:
                st.error("High Anxiety 😟")

            st.subheader("Helpful Tips")
            st.write("• Take study breaks")
            st.write("• Sleep well")
            st.write("• Practice breathing exercises")

        except:
            st.error("Start FastAPI backend first")