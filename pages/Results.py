import streamlit as st

st.set_page_config(page_title="AI Red Team - Results", page_icon="📊", layout="wide")

st.title("📊 Recon & Attack Plan")

if "target" in st.session_state:
    st.subheader(f"Target: {st.session_state['target']}")

    # 🔹 Recon Checklist
    with st.container():
        st.markdown("### 📝 Recon Checklist")
        st.success("• Run nmap scan")
        st.success("• Enumerate subdomains")
        st.success("• Search Shodan")

    # 🔹 OSINT Queries
    with st.container():
        st.markdown("### 🔍 OSINT Queries")
        target_domain = st.session_state["target"].replace(" ", "")
        st.code(f"Google dork: site:{target_domain} inurl:login", language="bash")
        st.code(f"Shodan query: {target_domain}", language="bash")

    # 🔹 Suggested Attack Vectors
    with st.container():
        st.markdown("### 🛡️ Suggested Attack Vectors")
        attacks = {
            "Credential Stuffing": "T1110",
            "SQL Injection": "T1505",
            "Default Credentials": "T1078"
        }
        for attack, mitre_id in attacks.items():
            st.info(f"• {attack} → MITRE ID: {mitre_id}")

    # 🔹 Card Styling for Dark Mode
    st.markdown(
        """
        <style>
        .stContainer { background-color: #1c1c1c; padding:10px; border-radius:10px; margin-bottom:10px; }
        .stCodeBlock { background-color:#222222; color:white; border-radius:5px; }
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.warning("⚠️ Please enter target first on Home page.")