import streamlit as st
import login
import dashboard

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if st.session_state["logged_in"]:
    dashboard.show()
else:
    login.show()