import streamlit as st
import random
import webbrowser

# --- CONFIGURATION ---
st.set_page_config(page_title="EchoBreak", page_icon="🌊", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #4CAF50; color: white; }
    .break-text { font-size: 1.2rem; color: #555; font-style: italic; }
    </style>
    """, unsafe_allow_html=True)

# --- APP HEADER ---
st.title("🌊 EchoBreak")
st.subheader("Escape the echo chamber. Explore the unexplored.")

# --- SIDEBAR: SETTINGS ---
with st.sidebar:
    st.header("Exploration Mode")
    platform = st.radio("Select Platform:", ["YouTube", "Instagram"])
    intensity = st.slider("Anti-Algorithm Intensity", 1, 10, 5)
    st.info("Higher intensity picks keywords further from your typical search history.")

# --- CORE LOGIC ---
keywords = [
    "Permaculture", "Stoicism", "Deep Sea Exploration", "Modular Synthesizers", 
    "Urban Planning", "Microscopy", "Linguistics", "Brutalist Architecture", 
    "Artisan Blacksmithing", "Quantum Computing", "Ancient Navigation"
]

perspectives = {
    "The Skeptic": "critique of",
    "The Artist": "aesthetic and visual",
    "The Scientist": "data and mechanics of",
    "The Historian": "origins and evolution of"
}

# --- MAIN INTERFACE ---
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🎲 Break the Loop")
    st.write("Click below to generate a search query that exists outside your usual bubble.")
    
    selected_perspective = st.selectbox("View the world as:", list(perspectives.keys()))
    
    if st.button("Generate New Horizon"):
        random_topic = random.choice(keywords)
        prefix = perspectives[selected_perspective]
        final_query = f"{prefix} {random_topic}"
        
        st.success(f"**Your Mission:** Explore **{final_query}**")
        
        # Construct Search URLs
        if platform == "YouTube":
            url = f"https://www.youtube.com/results?search_query={final_query.replace(' ', '+')}"
        else:
            url = f"https://www.instagram.com/explore/tags/{random_topic.replace(' ', '')}/"
        
        st.markdown(f"### [Click to Open {platform} 🚀]({url})")
        st.caption("Pro-tip: Don't look at the 'Suggested' sidebar. Stay on mission.")

with col2:
    st.markdown("### 🧘 Daily Deep Dive")
    st.info("The algorithm wants you to scroll. EchoBreak wants you to focus.")
    
    st.write("**Today's Deep Dive Topic:**")
    st.code("The impact of 17th-century cartography on modern borders.")
    
    if st.checkbox("I commit to 10 minutes of reading/watching this."):
        st.balloons()
        st.write("Focus mode activated. See you in 10 minutes.")

# --- FOOTER ---
st.divider()
st.markdown(
    "<div class='break-text'>'The algorithm knows what you liked yesterday. EchoBreak knows you might like something different today.'</div>", 
    unsafe_allow_html=True
)
