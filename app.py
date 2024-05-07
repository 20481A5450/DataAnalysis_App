import streamlit as st
import pandas as pd
from langchain_community.llms import Ollama
from pandasai import SmartDataframe

llm = Ollama(model="mistral")

st.title("Data Analysis App")
# st.balloons()

allowed_extensions = ["csv", "xls", "xlsx"]
uploaded_files = st.file_uploader("Upload CSV or XLSX files", type=allowed_extensions, accept_multiple_files=True)

if uploaded_files is not None:
    # st.info("File upload successful. Analyzing uploaded files...")
    for uploaded_file in uploaded_files:
        if uploaded_file.name.endswith(".csv"):
            data = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".xls") or uploaded_file.name.endswith(".xlsx"):
            data = pd.read_excel(uploaded_file)
        else:
            st.error(f"Unsupported file format for {uploaded_file.name}. Please upload CSV or XLSX files.")
            continue  # Skip to the next iteration if format is not supported

        st.write(f"**{uploaded_file.name}** has been uploaded.")
        st.write(data.head(2))
        df = SmartDataframe(data,config={"llm": llm})
    prompt = st.text_input("Enter your prompt")

    if st.button("Generate"):
        if prompt:
            with st.spinner("Generating response..."):
                st.write(df.chat(prompt))
        else:
            st.warning("Please enter a prompt.")

    # st.success("All uploaded files analyzed!")
else:
    st.info("Please upload one or more CSV, Excel, or XLSX files.")
