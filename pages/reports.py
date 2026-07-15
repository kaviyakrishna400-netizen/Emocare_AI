import streamlit as st
import sqlite3
import pandas as pd

DB_NAME = "emocare.db"

def show():

    st.title("📊 Emotion Reports")

    conn = sqlite3.connect(DB_NAME)

    df = pd.read_sql_query(
        "SELECT * FROM history",
        conn
    )

    conn.close()

    if df.empty:
        st.warning("No emotion records available.")
        return

    st.subheader("Overall Statistics")

    col1, col2, col3 = st.columns(3)

    total = len(df)

    common = df["emotion"].mode()[0]

    avg = round(df["confidence"].mean(), 2)

    col1.metric("Total Detections", total)
    col2.metric("Most Common Emotion", common)
    col3.metric("Average Confidence", f"{avg}%")

    st.divider()

    st.subheader("Emotion Distribution")

    chart = df["emotion"].value_counts()

    st.bar_chart(chart)

    st.divider()

    st.subheader("Detailed Report")

    st.dataframe(df, use_container_width=True)