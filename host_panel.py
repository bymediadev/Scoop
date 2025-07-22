import streamlit as st
from utils.research_utils import generate_guest_profile

st.set_page_config(page_title="Scoop: Podcast Guest Research Tool")
st.title("Scoop by BY Media: A Podcast Guest Research Tool")

# --- Input Fields ---
guest_name = st.text_input("Enter guest name", key="name_input")
guest_url = st.text_input("Enter guest URL (LinkedIn, company website, etc)", key="url_input")

# --- Generate Profile ---
if st.button("Generate Guest Profile", key="generate_btn"):
    with st.spinner("Generating profile..."):
        profile = generate_guest_profile(guest_name, guest_url)

    st.markdown(f"## Guest Research Profile: {guest_name}")

    st.markdown("### 🔹 Bio")
    st.write(profile.get("bio", "No bio available."))

    st.markdown("### 🏢 Company Summary")
    st.write(profile.get("company", "No company summary available."))

    st.markdown("### 🔍 Insight Summary")
    st.write(profile.get("insight", "No insight summary available."))

    for q in profile.get("questions", []):
        st.markdown(f"- {q}")

    if profile.get("error"):
        st.error(profile["error"])
