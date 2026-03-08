import streamlit as st
import requests

# Page settings
st.set_page_config(page_title="AI Exam Anxiety Detector", page_icon="🧠")

# Title
st.title("🧠 AI Exam Anxiety Detector")
st.write("Analyze your exam stress level using AI")

# Input box
text = st.text_area("✍️ Write how you feel about your exams:")

# Button
if st.button("🔍 Analyze Anxiety"):

    if text.strip() == "":
        st.warning("Please enter some text first.")
    else:
        try:
            response = requests.post(
                "ai-exam-anxiety-detector01-production.up.railway.app/predict",
                json={"text": text}
            )

            result = response.json()
            level = result["anxiety_level"]

            st.subheader("📊 Anxiety Level Result")

            # Display result
            if level == "Low":
                st.success("😊 Low Anxiety")
                st.progress(30)

                st.info("""
                **Tips to stay confident**
                - Keep following your study schedule
                - Revise regularly
                - Maintain good sleep
                """)

            elif level == "Moderate":
                st.warning("😐 Moderate Anxiety")
                st.progress(60)

                st.info("""
                **Tips to reduce stress**
                - Take short study breaks
                - Practice breathing exercises
                - Organize your study plan
                """)

            else:
                st.error("😟 High Anxiety")
                st.progress(90)

                st.info("""
                **Important tips**
                - Take deep breaths
                - Talk to friends or teachers
                - Break study tasks into smaller parts
                """)

        except:
            st.error("⚠ Backend connection failed")

# Footer
st.markdown("---")
st.caption("⚠ This tool is for educational purposes only. It is not a medical diagnosis system.")