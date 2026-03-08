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
        with st.spinner("Analyzing your anxiety level..."):

            try:
                response = requests.post(
                    "https://ai-exam-anxiety-detector01-production.up.railway.app/predict",
                    json={"text": text},
                    timeout=10
                )

                if response.status_code == 200:
                    result = response.json()
                    level = result.get("anxiety_level", "Unknown")

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

                    elif level == "High":
                        st.error("😟 High Anxiety")
                        st.progress(90)

                        st.info("""
**Important tips**
- Take deep breaths
- Talk to friends or teachers
- Break study tasks into smaller parts
""")

                    else:
                        st.error("⚠ Unexpected response from AI model.")

                else:
                    st.error(f"⚠ Backend error: {response.status_code}")

            except requests.exceptions.ConnectionError:
                st.error("⚠ Cannot connect to backend server.")

            except requests.exceptions.Timeout:
                st.error("⚠ Server is taking too long to respond.")

            except Exception as e:
                st.error(f"⚠ Backend connection failed: {e}")

# Footer
st.markdown("---")
st.caption("⚠ This tool is for educational purposes only. It is not a medical diagnosis system.")