import streamlit as st

st.set_page_config(page_title="More About Me | Jingwen Zhang", page_icon="📸")

st.title("More About Me")

st.markdown("""
Welcome! Here's a little more about who I am beyond work and projects.
""")

# --- Personal / Professional Moments
st.subheader("📸 Presenting, Competing, and Connecting")
col1, col2 = st.columns(2)

with col1:
    st.image("assets/me_presenting.jpg", caption="Presenting at Google Competition")
    st.image("assets/me_with_competition_team.jpg", caption="With my competition team")

with col2:
    st.image("assets/me_with_tony_xu.jpg", caption="Meeting Tony Xu at the Berkeley alumni event")
    st.image("assets/alumni_event_day.JPG", caption="UC Berkeley alumni celebration")

# --- Career & Team
st.subheader("👨‍💻 Working with Teams")
st.image("assets/me_with_kone_team.jpg", caption="Me with the KONE Analytics Team")

# --- Nature & Exploration
st.subheader("🌄 Outside of Work")
st.image("assets/me_at_yosemite_top.jpg", caption="Hiking to the top of Yosemite — one of my favorite adventures")

st.subheader("🐶 Meet Lele!")
st.markdown("Lele is my loyal companion and brings me lots of joy every day.")
lele_cols = st.columns(3)
lele_cols[0].image("assets/lele_1.jpg", use_container_width=True)
lele_cols[1].image("assets/lele_3.jpg", use_container_width=True)
lele_cols[2].image("assets/lele_2.jpg", use_container_width=True)

st.markdown("---")
st.markdown("Thanks for taking the time to get to know me a bit more! 😊")
