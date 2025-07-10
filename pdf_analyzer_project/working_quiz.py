import streamlit as st
import random

# Page config
st.set_page_config(
    page_title="Működő Quiz",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Session state inicializálása
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0

# Kérdések
questions = {
    "földrajz": [
        {
            "question": "Mi Magyarország fővárosa?",
            "options": ["Budapest", "Debrecen", "Szeged", "Miskolc"],
            "correct": 0,
            "explanation": "Budapest Magyarország fővárosa."
        },
        {
            "question": "Melyik a világ leghosszabb folyója?",
            "options": ["Amazonas", "Nílus", "Jangce", "Mississippi"],
            "correct": 1,
            "explanation": "A Nílus a világ leghosszabb folyója."
        }
    ],
    "háborúk": [
        {
            "question": "Mikor zajlott az I. világháború?",
            "options": ["1914-1918", "1939-1945", "1912-1913", "1918-1920"],
            "correct": 0,
            "explanation": "Az I. világháború 1914-1918 között zajlott."
        },
        {
            "question": "Mikor zajlott a Tizenhárom éves háború?",
            "options": ["1454-1466", "1466-1478", "1478-1490", "1490-1502"],
            "correct": 0,
            "explanation": "A Tizenhárom éves háború 1454-1466 között zajlott."
        }
    ],
    "irodalom": [
        {
            "question": "Ki írta a Romeo és Júliát?",
            "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
            "correct": 0,
            "explanation": "A Romeo és Júliát William Shakespeare írta."
        }
    ]
}

st.title("🧠 Működő Quiz Alkalmazás")

# Sidebar - ez most biztosan megjelenik
st.sidebar.title("⚙️ Beállítások")

# Témakörök kiválasztása
st.sidebar.subheader("📚 Témakörök")
available_topics = list(questions.keys())
selected_topics = st.sidebar.multiselect(
    "Válaszd ki a témaköröket:",
    available_topics,
    default=available_topics[:2]
)

# Kérdések száma
st.sidebar.subheader("📊 Kérdések")
num_questions = st.sidebar.slider(
    "Kérdések száma:",
    min_value=1,
    max_value=10,
    value=5,
    step=1
)

# Quiz indítása gomb
st.sidebar.markdown("---")
if st.sidebar.button("🚀 Quiz Indítása", type="primary", use_container_width=True):
    if not selected_topics:
        st.sidebar.error("Kérlek válassz ki legalább egy témakört!")
    else:
        # Összes kérdés összegyűjtése
        all_questions = []
        for topic in selected_topics:
            all_questions.extend(questions[topic])
        
        # Véletlenszerű kiválasztás
        if len(all_questions) < num_questions:
            st.sidebar.warning(f"Csak {len(all_questions)} kérdés áll rendelkezésre.")
            quiz_questions = all_questions
        else:
            quiz_questions = random.sample(all_questions, num_questions)
        
        # Quiz indítása
        st.session_state.quiz_started = True
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.quiz_questions = quiz_questions
        st.rerun()

# Fő tartalom
if not st.session_state.quiz_started:
    st.markdown("""
    ## Üdvözöllek! 🎯
    
    ### Hogyan működik:
    1. **Válaszd ki a témaköröket** a bal oldali menüben
    2. **Állítsd be a kérdések számát**
    3. **Indítsd el a quiz-t** a gombra kattintva
    4. **Válaszolj a kérdésekre**
    
    ### Elérhető témakörök:
    - 🌍 **Földrajz**: Országok, városok
    - ⚔️ **Háborúk**: Történelmi konfliktusok
    - 📚 **Irodalom**: Könyvek, szerzők
    """)
    
    # Statisztikák
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Összes kérdés", sum(len(q) for q in questions.values()))
    with col2:
        st.metric("Témakörök", len(questions))
    with col3:
        st.metric("Földrajzi kérdések", len(questions["földrajz"]))

else:
    # Quiz megjelenítése
    if st.session_state.current_question < len(st.session_state.quiz_questions):
        question = st.session_state.quiz_questions[st.session_state.current_question]
        
        # Progress
        progress = (st.session_state.current_question + 1) / len(st.session_state.quiz_questions)
        st.progress(progress)
        st.caption(f"Kérdés {st.session_state.current_question + 1} / {len(st.session_state.quiz_questions)}")
        
        # Kérdés
        st.subheader(f"❓ {question['question']}")
        
        # Válaszlehetőségek
        for i, option in enumerate(question['options']):
            if st.button(f"{chr(65+i)}. {option}", key=f"q{st.session_state.current_question}_opt{i}", use_container_width=True):
                if i == question['correct']:
                    st.success("✅ Helyes válasz!")
                    st.session_state.score += 1
                else:
                    st.error(f"❌ Helytelen! A helyes válasz: {chr(65+question['correct'])}. {question['options'][question['correct']]}")
                
                # Magyarázat
                st.info(f"💡 **Magyarázat:** {question['explanation']}")
                
                # Következő kérdés
                st.session_state.current_question += 1
                if st.session_state.current_question < len(st.session_state.quiz_questions):
                    st.rerun()
                else:
                    st.rerun()
    else:
        # Eredmények
        st.success("🏆 Quiz befejezve!")
        score = st.session_state.score
        total = len(st.session_state.quiz_questions)
        percentage = (score / total) * 100
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Helyes válaszok", f"{score}/{total}")
        with col2:
            st.metric("Százalék", f"{percentage:.1f}%")
        with col3:
            if percentage >= 80:
                grade = "A"
                emoji = "🌟"
            elif percentage >= 60:
                grade = "B"
                emoji = "👍"
            else:
                grade = "C"
                emoji = "😊"
            st.metric("Osztályzat", f"{grade} {emoji}")
        
        # Új quiz gomb
        if st.button("🔄 Új Quiz", type="primary"):
            st.session_state.quiz_started = False
            st.rerun()

# Debug információk a sidebar alján
st.sidebar.markdown("---")
st.sidebar.caption("Debug info:")
st.sidebar.write(f"Quiz indítva: {st.session_state.quiz_started}")
if st.session_state.quiz_started:
    st.sidebar.write(f"Kérdés: {st.session_state.current_question}")
    st.sidebar.write(f"Pontszám: {st.session_state.score}") 