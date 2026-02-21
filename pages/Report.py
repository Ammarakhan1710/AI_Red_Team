import streamlit as st

st.set_page_config(page_title="AI Red Team - Report", page_icon="📝", layout="wide")

st.title("📝 Report Generator")

# 🔹 Upload Findings File
uploaded_file = st.file_uploader("📂 Upload Findings File", type=["txt", "csv"])

if uploaded_file:
    content = uploaded_file.read().decode("utf-8")
    
    st.subheader("📄 Findings Preview")
    st.text(content)
    
    # 🔹 Save in session state for multiple targets
    if "reports" not in st.session_state:
        st.session_state["reports"] = []
    st.session_state["reports"].append(content)
    
    # 🔹 Download Report Button
    report_text = f"AI Red Team Report\n\n{content}\n\nGenerated with ❤️ using Streamlit"
    st.download_button(
        label="⬇️ Download Report",
        data=report_text,
        file_name="pentest_report.txt",
        mime="text/plain"
    )

# 🔹 Previous Reports History
if "reports" in st.session_state and st.session_state["reports"]:
    st.subheader("📚 Previous Reports")
    for i, r in enumerate(st.session_state["reports"], 1):
        st.info(f"Report {i} preview:")
        st.text(r)

# 🔹 Dark Mode CSS
st.markdown(
    """
    <style>
    .stContainer { background-color: #1c1c1c; padding:10px; border-radius:10px; margin-bottom:10px; }
    .stTextArea>div>textarea { background-color:#222222; color:white; border-radius:5px; }
    .stButton>button { background-color:#1f77b4; color:white; border-radius:10px; height:40px; width:200px; }
    </style>
    """,
    unsafe_allow_html=True
)