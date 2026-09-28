import streamlit as st
import re

st.set_page_config(page_title="JobShield Odisha", page_icon="🛡️")
st.title("🛡️ JobShield Odisha")
st.write("Fake job alert detector for Odisha")

msg = st.text_area("Job message yahan paste karo:", height=150)

if st.button("Check karo"):
    if not msg:
        st.warning("Pehle message likho")
    else:
        score = 0
        reasons = []
        m = msg.lower()
        keywords = ["registration fee", "pay now", "urgent hiring", "work from home", "no interview", "telegram", "whatsapp only", "advance payment", "processing fee", "job guarantee"]
        for k in keywords:
            if k in m:
                score += 20
                reasons.append(f"⚠️ '{k}' mila")
        if re.search(r'\d{10}', msg):
            score += 10
            reasons.append("⚠️ Phone number mila")
        if "http" in m or "t.me" in m:
            score += 10
            reasons.append("⚠️ Link mila")
        score = min(score, 100)
        if score >= 50:
            st.error(f"🚨 HIGH RISK: {score}% fake lag raha hai")
        elif score >= 20:
            st.warning(f"⚠️ MEDIUM RISK: {score}%")
        else:
            st.success(f"✅ LOW RISK: {score}%")
        if reasons:
            st.write("Karan:")
            for r in reasons:
                st.write(r)

st.markdown("---")
st.caption("Cyber safety ke liye banaya gaya | Odisha")
