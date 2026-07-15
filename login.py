import streamlit as st
from auth import login_user

def show():

    st.markdown("""
    <style>
    .main{
        background:linear-gradient(135deg,#EAF4FF,#F8FAFC);
    }

    .login-box{
        width:420px;
        margin:auto;
        margin-top:70px;
        background:white;
        padding:40px;
        border-radius:20px;
        box-shadow:0 8px 25px rgba(0,0,0,.12);
    }

    .banner{
        height:90px;
        border-radius:20px;
        background:linear-gradient(135deg,#2563EB,#7C3AED,#06B6D4);
        display:flex;
        justify-content:center;
        align-items:center;
        color:white;
        font-size:34px;
        font-weight:bold;
        margin-bottom:25px;
        box-shadow:0 8px 20px rgba(0,0,0,.15);
    }

    .subtitle{
        text-align:center;
        color:gray;
        margin-bottom:30px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="login-box">', unsafe_allow_html=True)

    st.markdown("""
    <div class="banner">
        🧠 EmoCare AI
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="subtitle">Emotion Detection for Special Children</div>', unsafe_allow_html=True)

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Sign In", use_container_width=True):

        user = login_user(email.strip(), password.strip())

        if user:
            st.session_state["logged_in"] = True
            st.session_state["user_name"] = user[1]
            st.rerun()

        else:
            st.error("❌ Invalid Email or Password")

    st.markdown("<br>", unsafe_allow_html=True)

    st.button("Continue with Google", use_container_width=True)

    st.markdown(
        "<p style='text-align:center;'>Don't have an account? <b>Sign Up</b></p>",
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)