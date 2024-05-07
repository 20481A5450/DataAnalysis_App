import streamlit as st
import pandas as pd

st.title("Data Analysis App")

allowed_extensions = ["csv", "xls", "xlsx"]
uploaded_files = st.file_uploader("Upload CSV, Excel, or XLSX files", type=allowed_extensions,accept_multiple_files=True)

if uploaded_files is not None:
    for uploaded_file in uploaded_files:
        if uploaded_file.name.endswith(".csv"):
            data = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".xls") or uploaded_file.name.endswith(".xlsx"):
            data = pd.read_excel(uploaded_file)
        else:
            st.error(f"Unsupported file format for {uploaded_file.name}. Please upload CSV, Excel, or XLSX files.")
            continue  # Skip to the next iteration if format is not supported

    # Process the data for each file (e.g., display filename and descriptive statistics)
    st.write(f"File: {uploaded_file.name}")
    st.write(data.describe())
    # ... (more data analysis logic per file)
    st.success("All uploaded files analyzed!")
else:
    st.info("Please upload one or more CSV, Excel, or XLSX files.")
