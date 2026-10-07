import streamlit as st

st.title("☁️ Cloud Computing Demo")

st.write("Welcome to my Streamlit Cloud Application!")

st.header("Cloud Platforms")

platform = st.selectbox(
    "Choose a platform",
    ["Streamlit", "Vercel", "Netlify"]
)

if platform == "Streamlit":
    st.success("Streamlit is used for Python and AI/ML applications.")

elif platform == "Vercel":
    st.success("Vercel is used for modern web application deployment.")

else:
    st.success("Netlify is used for website hosting and deployment.")

st.subheader("Deployment Status")

if st.button("Check Status"):
    st.success("✅ Application is running successfully!")