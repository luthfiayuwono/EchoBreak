import streamlit as st
import random

# --- MOBILE-FIRST CONFIG ---
st.set_page_config(
    page_title="EchoBreak", 
    page_icon="🌊", 
    layout="centered"  # Centers content for narrow screens
)

# --- MOBILE UI STYLING ---
st.markdown("""
    <style>
    /* Remove unnecessary padding on mobile */
    .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    
    /* Make buttons huge and thumb-friendly */
    .stButton>button {
        width: 100%;
        height: 80px;
        font-size: 1.5rem !important;
        border-radius: 15px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        margin-top: 10px;
    }
    
    /* Style the platform selector to look like tabs */
    .stRadio div[role="radiogroup"] {
        flex-direction: row;
        justify-content: space-around;
    }
    
    /* Center text for that app feel */
    .main-header { text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1 class='main-header'>🌊 EchoBreak</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; opacity: 0.8;'>Anti-Algorithm Layer</p>", unsafe_allow_html=True)

# --- PLATFORM PICKER ---
# Using a horizontal radio layout for a "tab" feel on mobile
platform = st.radio("Target App:", ["YouTube", "Instagram"], horizontal=True)

st.divider()

# --- CONTENT GENERATOR ---
keywords = ["Liminal Spaces", "Biohacking", "Found Footage", "Solarpunk", "Theremin Music", "Permaculture"]
perspectives = {
    "🧠 The Scientist": "mechanics of",
    "🎨 The Artist": "aesthetic of",
    "📜 The Historian": "history of",
    "🔮 The Futurist": "future of"
}

st.write("### 1. Choose your lens")
viewpoint = st.selectbox("", list(perspectives.keys()))

st.write("### 2. Break the cycle")
if st.button("🚀 GENERATE EXPLORATION"):
    topic = random.choice(keywords)
    prefix = perspectives[viewpoint]
    query = f"{prefix} {topic}"
    
    # Visual Feedback for Mobile
    st.info(f"Seeking: **{query}**")
    
    if platform == "YouTube":
        url = f"https://m.youtube.com/results?search_query={query.replace(' ', '+')}"
    else:
        url = f"https://www.instagram.com/explore/tags/{topic.replace(' ', '')}/"
    
    # Use a big link button for mobile tapping
    st.markdown(f"""
        <a href="{url}" target="_blank">
            <div style="background-color:#FF4B4B; color:white; padding:20px; text-align:center; border-radius:15px; font-weight:bold; text-decoration:none; font-size:1.2rem;">
                OPEN {platform.upper()} NOW
            </div>
        </a>
    """, unsafe_allow_html=True)

# --- DAILY CHALLENGE ---
st.divider()
with st.expander("🎯 Today's Focus Challenge"):
    st.write("Watch one video over 15 minutes long without checking your notifications.")
    if st.button("Challenge Accepted"):
        st.balloons()
