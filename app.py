import streamlit as st

# ⚡ Page Config
st.set_page_config(
    page_title="AI Red Team Assistant",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "AI Red Team Assistant - Hackathon Prototype\nAuthor: Ammara Khan"
    }
)

# 🔹 Sidebar Branding
st.sidebar.title("🛡️ AI Red Team Assistant")
st.sidebar.markdown(
    """
    **Navigation**  
    - 🏠 Home  
    - 📊 Results  
    - 📝 Report
    """
)
st.sidebar.markdown("---")

# 🔹 Home Page
st.title("🛡️ AI Red Team Assistant")
st.write("Enter a target below to generate Recon checklist, OSINT queries, and MITRE-mapped attack vectors.")

# 🔹 Target Input
target = st.text_input("Enter Target (e.g., example.com)")

if st.button("Generate Plan", key="gen_plan"):
    if target:
        st.session_state["target"] = target
        st.success("✅ Plan generated! Go to Results page from sidebar.")
    else:
        st.warning("⚠️ Please enter a target first.")

# 🔹 Dark Mode Styling (Custom CSS)
st.markdown(
     """
    <style>
    body { background-color: #0e1117; color: #f0f0f0; }
    .stButton>button { background-color:#1f77b4; color:white; border-radius:10px; height:40px; width:200px; }
    .stTextInput>div>div>input { background-color:#1c1c1c; color:white; border-radius:5px; }
    .stSidebar { background-color:#111318; color:white; }
    h1 { color: #1f77b4 !important; }
    </style>
    """,
    unsafe_allow_html=True
)