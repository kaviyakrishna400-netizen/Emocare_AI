import streamlit as st
import sqlite3
import pandas as pd

DB_NAME = "emocare.db"

def show():

    st.title("📜 Emotion History")

    conn = sqlite3.connect(DB_NAME)

    query = """
    SELECT
        date,
        time,
        emotion,
        ROUND(confidence,2) AS Confidence
    FROM history
    ORDER BY id DESC
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    if df.empty:
        st.info("No emotion records found.")
    else:
        st.dataframe(df, use_container_width=True)