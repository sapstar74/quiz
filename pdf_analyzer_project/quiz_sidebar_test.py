import streamlit as st
import random

# Custom CSS to make sidebar more visible
st.markdown("""
<style>
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
        border-right: 3px solid #ff4b4b;
    }
    .sidebar .sidebar-content .block-container {
        padding: 1rem;
    }
    .sidebar .sidebar-content h1, .sidebar .sidebar-content h2, .sidebar .sidebar-content h3 {
        color: #ff4b4b;
        font-weight: bold;
    }
    .sidebar .sidebar-content .stButton > button {
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        font-size: 1.2em;
        padding: 1rem;
        border-radius: 10px;
    }
    .sidebar .sidebar-content .stButton > button:hover {
        background-color: #ff3333;
    }
</style>
""", unsafe_allow_html=True)

# Page config
st.set_page_config(
    page_title="Quiz Sidebar Test",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Session state
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False

# Simple questions
questions = {
    "földrajz": [
        {"question": "Mi Magyarország fővárosa?", "options": ["Budapest", "Debrecen", "Szeged", "Miskolc"], "correct": 0},
        {"question": "Melyik a legnagyobb kontinens?", "options": ["Európa", "Ázsia", "Afrika", "Amerika"], "correct": 1}
    ],
    "történelem": [
        {"question": "Mikor kezdődött az első világháború?", "options": ["1914", "1915", "1916", "1917"], "correct": 0},
        {"question": "Ki volt Magyarország első királya?", "options": ["Szent István", "Szent László", "Kálmán", "Béla"], "correct": 0}
    ]
}

# Main title
st.title("🧠 Quiz Sidebar Test")

# Sidebar with very visible elements
with st.sidebar:
    st.markdown("# ⚙️ BEÁLLÍTÁSOK")
    st.markdown("---")
    
    st.markdown("## 📚 TÉMAKÖRÖK")
    st.markdown("**Válaszd ki a témaköröket:**")
    
    available_topics = list(questions.keys())
    selected_topics = st.multiselect(
        "Témakörök:",
        available_topics,
        default=available_topics,
        help="Válaszd ki a témaköröket"
    )
    
    st.markdown("## 📊 KÉRDÉSEK")
    num_questions = st.slider(
        "Kérdések száma:",
        min_value=1,
        max_value=10,
        value=3,
        step=1
    )
    
    st.markdown("---")
    st.markdown("## 🚀 QUIZ INDÍTÁSA")
    
    if st.button("🎯 INDÍTSD EL!", type="primary", use_container_width=True):
        if not selected_topics:
            st.error("❌ Válassz ki témaköröket!")
        else:
            st.session_state.quiz_started = True
            st.rerun()
    
    # Debug info
    st.markdown("---")
    st.markdown("## 🔍 DEBUG")
    st.write(f"**Quiz indítva:** {st.session_state.quiz_started}")
    st.write(f"**Kiválasztott témák:** {selected_topics}")
    st.write(f"**Kérdések száma:** {num_questions}")

# Main content
if not st.session_state.quiz_started:
    st.markdown("""
    ## Üdvözöllek! 🎯
    
    ### A sidebar a bal oldalon található ⬅️
    
    **Lépések:**
    1. Nézd meg a bal oldali menüt
    2. Válaszd ki a témaköröket
    3. Állítsd be a kérdések számát
    4. Kattints az "INDÍTSD EL!" gombra
    
    ### Elérhető témakörök:
    - 🌍 **Földrajz**: Országok, városok
    - 📚 **Történelem**: Történelmi események
    """)
    
    # Statistics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Összes kérdés", sum(len(q) for q in questions.values()))
    with col2:
        st.metric("Témakörök", len(questions))
    with col3:
        st.metric("Kiválasztott", len(selected_topics))

else:
    st.success("🎉 Quiz elindítva!")
    st.info("A sidebar most már működik!")
    
    if st.button("🔄 Vissza a főoldalra"):
        st.session_state.quiz_started = False
        st.rerun() 