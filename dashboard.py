import streamlit as st

from pages import live_detection
from pages import upload_image
from pages import history
from pages import reports
from pages import settings


def show():

    # ---------------- Sidebar ----------------

    st.sidebar.title("🧠 EmoCare AI")

    st.sidebar.success(f"👤 {st.session_state.get('user_name','Administrator')}")

    if st.sidebar.button("🚪 Logout"):
        st.session_state.clear()
        st.rerun()

    page = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "Live Detection",
            "Upload Image",
            "History",
            "Reports",
            "Settings"
        ]
    )

    # ---------------- Dashboard ----------------

    if page == "Dashboard":

        st.title("🧠 EmoCare AI Dashboard")
        st.write("### AI-Based Emotion Detection for Special Children")

        st.divider()

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("😊 Happy", "45%", "+5%")

        with col2:
            st.metric("😐 Neutral", "25%", "-2%")

        with col3:
            st.metric("😢 Sad", "20%", "-1%")

        with col4:
            st.metric("😡 Angry", "10%", "-2%")

        st.divider()

        c1, c2 = st.columns(2)

        with c1:

            st.subheader("📊 Today's Summary")

            st.info("""
Total Scans : 26

Children Monitored : 12

Highest Emotion : Happy 😊

System Status : Online 🟢
""")

        with c2:

            st.subheader("❤️ Therapist Recommendation")

            st.success("""
✔ Continue positive interaction.

✔ Encourage social activities.

✔ Monitor repeated negative emotions.

✔ Generate reports weekly.
""")

        st.divider()

        st.subheader("📋 Recent Activity")

        st.table({
            "Child": ["Child A", "Child B", "Child C"],
            "Emotion": ["Happy 😊", "Neutral 😐", "Sad 😢"],
            "Confidence": ["96%", "88%", "91%"]
        })

    # ---------------- Other Pages ----------------

    elif page == "Live Detection":
        live_detection.show()

    elif page == "Upload Image":
        upload_image.show()

    elif page == "History":
        history.show()

    elif page == "Reports":
        reports.show()

    elif page == "Settings":
        settings.show()