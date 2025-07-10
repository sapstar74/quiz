import streamlit as st
import random

st.set_page_config(page_title="Egyszerű Quiz", page_icon="🧠")

# Session state inicializálása
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0

# Egyszerű kérdések
questions = [
    {
        "question": "Mi Magyarország fővárosa?",
        "options": ["Budapest", "Debrecen", "Szeged", "Miskolc"],
        "correct": 0
    },
    {
        "question": "Melyik a világ leghosszabb folyója?",
        "options": ["Amazonas", "Nílus", "Jangce", "Mississippi"],
        "correct": 1
    },
    {
        "question": "Ki írta a Romeo és Júliát?",
        "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
        "correct": 0
    }
]

st.title("🧠 Egyszerű Quiz Alkalmazás")

# Sidebar
st.sidebar.header("Beállítások")
num_questions = st.sidebar.slider("Kérdések száma", 1, len(questions), 3)

if st.sidebar.button("🚀 Quiz Indítása"):
    st.session_state.quiz_started = True
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.quiz_questions = random.sample(questions, num_questions)
    st.rerun()

if st.session_state.quiz_started:
    if st.session_state.current_question < len(st.session_state.quiz_questions):
        q = st.session_state.quiz_questions[st.session_state.current_question]
        
        st.subheader(f"Kérdés {st.session_state.current_question + 1}/{len(st.session_state.quiz_questions)}")
        st.write(f"**{q['question']}**")
        
        for i, option in enumerate(q['options']):
            if st.button(f"{chr(65+i)}. {option}", key=f"q{st.session_state.current_question}_opt{i}"):
                if i == q['correct']:
                    st.success("✅ Helyes válasz!")
                    st.session_state.score += 1
                else:
                    st.error(f"❌ Helytelen! A helyes válasz: {chr(65+q['correct'])}. {q['options'][q['correct']]}")
                
                st.session_state.current_question += 1
                if st.session_state.current_question < len(st.session_state.quiz_questions):
                    st.rerun()
                else:
                    st.rerun()
    else:
        st.success("🏆 Quiz befejezve!")
        st.write(f"Eredmény: {st.session_state.score}/{len(st.session_state.quiz_questions)}")
        
        if st.button("🔄 Új Quiz"):
            st.session_state.quiz_started = False
            st.rerun()
else:
    st.write("Válaszd ki a kérdések számát és indítsd el a quiz-t!") 