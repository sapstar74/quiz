"""
🧠 PDF Alapú Quiz Alkalmazás
Teljes verzió az összes kérdéssel
"""

import streamlit as st
import random
import time
from datetime import datetime
import os
from pathlib import Path

# Page config
st.set_page_config(
    page_title="🧠 PDF Quiz Alkalmazás",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Session state inicializálása
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
if 'quiz_finished' not in st.session_state:
    st.session_state.quiz_finished = False
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'answers' not in st.session_state:
    st.session_state.answers = []
if 'quiz_questions' not in st.session_state:
    st.session_state.quiz_questions = []

# Quiz adatok témakörök szerint csoportosítva
QUIZ_DATA_BY_TOPIC = {
    "földrajz": [
        {
            "question": "Mi a legmagasabb csúcs a Mátrában?",
            "options": ["Kékes", "Dobogó-kő", "Csóványos", "Szilvási-kő"],
            "correct": 0,
            "explanation": "A Kékes 1014 méter magasságával a Mátra legmagasabb csúcsa."
        },
        {
            "question": "Melyik ország fővárosa Taskent?",
            "options": ["Kazahsztán", "Üzbegisztán", "Kirgizisztán", "Tádzsikisztán"],
            "correct": 1,
            "explanation": "Taskent Üzbegisztán fővárosa."
        },
        {
            "question": "Melyik a világ leghosszabb folyója?",
            "options": ["Amazonas", "Nílus", "Jangce", "Mississippi"],
            "correct": 1,
            "explanation": "A Nílus 6650 km hosszával a világ leghosszabb folyója."
        },
        {
            "question": "Mi Bhután fővárosa?",
            "options": ["Thimphu", "Katmandu", "Dhaka", "Vientiane"],
            "correct": 0,
            "explanation": "Bhután fővárosa Thimphu, pénzneme a ngultrum."
        },
        {
            "question": "Melyik hegység csúcsa a Börzsöny legmagasabb pontja?",
            "options": ["Nagy-Kopasz", "Pilis", "Dobogó-kő", "Csóványos"],
            "correct": 3,
            "explanation": "A Csóványos (938 m) a Börzsöny hegység legmagasabb csúcsa."
        },
        {
            "question": "Melyik kontinensen található a Kilimandzsáró?",
            "options": ["Ázsia", "Dél-Amerika", "Afrika", "Ausztrália"],
            "correct": 2,
            "explanation": "A Kilimandzsáró (5895 m) Afrika legmagasabb hegycsúcsa."
        },
        {
            "question": "Mi Costa Rica pénzneme?",
            "options": ["Peso", "Dollár", "Quetzal", "Colón"],
            "correct": 3,
            "explanation": "Costa Rica pénzneme a Costa Rica-i colón."
        },
        {
            "question": "Melyik az Európa leghosszabb folyója?",
            "options": ["Volga", "Duna", "Rajna", "Dnyeper"],
            "correct": 0,
            "explanation": "A Volga 3530 km hosszával Európa leghosszabb folyója."
        },
        {
            "question": "Mi a Pilis hegység legmagasabb csúcsa?",
            "options": ["Nagy-Kopasz", "Dobogó-kő", "Szánkó-hegy", "Pilis"],
            "correct": 3,
            "explanation": "A Pilis (757 m) a Pilis hegység névadó és legmagasabb csúcsa."
        },
        {
            "question": "Melyik ország pénzneme a manat?",
            "options": ["Grúzia", "Örményország", "Azerbajdzsán", "Kazahsztán"],
            "correct": 2,
            "explanation": "Azerbajdzsán pénzneme a manat, fővárosa Baku."
        }
    ],
    
    "háborúk": [
        {
            "question": "Melyik háború zajlott 1914-1918 között? (Antant vs. Központi hatalmak)",
            "options": ["I. világháború", "II. világháború", "Koreai háború", "Vietnámi háború"],
            "correct": 0,
            "explanation": "I. világháború (1914-1918): Antant vs. Központi hatalmak"
        },
        {
            "question": "Melyik háború zajlott 1337-1453 között? (Anglia vs Franciaország)",
            "options": ["Százéves háború", "Világháború", "Polgárháború", "Függetlenségi háború"],
            "correct": 0,
            "explanation": "Százéves háború (1337-1453): Anglia vs Franciaország"
        },
        {
            "question": "Melyik háború zajlott 1454-1466 között? (Porosz Konföderáció, Lengyel Királyság vs Teuton Lovagrend)",
            "options": ["Tizenhárom éves háború", "Világháború", "Polgárháború", "Függetlenségi háború"],
            "correct": 0,
            "explanation": "Tizenhárom éves háború (1454-1466): Porosz Konföderáció, Lengyel Királyság vs Teuton Lovagrend"
        },
        {
            "question": "Melyik háború zajlott 1618-1648 között? (Katolikus Habsburgok, Spanyolország vs Protestáns államok, Franciaország, Svédország)",
            "options": ["Harmincéves háború", "Világháború", "Polgárháború", "Függetlenségi háború"],
            "correct": 0,
            "explanation": "Harmincéves háború (1618-1648): Katolikus Habsburgok, Spanyolország vs Protestáns államok, Franciaország, Svédország"
        },
        {
            "question": "Melyik háború zajlott 1701-1714 között? (Franciaország, Spanyolország vs Ausztria, Nagy-Britannia, Hollandia)",
            "options": ["Spanyol örökösödési háború", "Világháború", "Polgárháború", "Függetlenségi háború"],
            "correct": 0,
            "explanation": "Spanyol örökösödési háború (1701-1714): Franciaország, Spanyolország vs Ausztria, Nagy-Britannia, Hollandia"
        },
        {
            "question": "Melyik háború zajlott 1740-1748 között? (Ausztria vs Poroszország, Franciaország, Spanyolország)",
            "options": ["Osztrák örökösödési háború", "Világháború", "Polgárháború", "Függetlenségi háború"],
            "correct": 0,
            "explanation": "Osztrák örökösödési háború (1740-1748): Ausztria vs Poroszország, Franciaország, Spanyolország"
        },
        {
            "question": "Melyik háború zajlott 1756-1763 között? (Nagy-Britannia, Poroszország vs Franciaország, Ausztria, Oroszország)",
            "options": ["Hétéves háború", "Világháború", "Polgárháború", "Függetlenségi háború"],
            "correct": 0,
            "explanation": "Hétéves háború (1756-1763): Nagy-Britannia, Poroszország vs Franciaország, Ausztria, Oroszország"
        },
        {
            "question": "Melyik háború zajlott 1803-1815 között? (Napóleoni Franciaország vs Európai szövetséges hatalmak)",
            "options": ["Napóleoni háborúk", "Világháború", "Polgárháború", "Függetlenségi háború"],
            "correct": 0,
            "explanation": "Napóleoni háborúk (1803-1815): Napóleoni Franciaország vs Európai szövetséges hatalmak"
        },
        {
            "question": "Melyik háború zajlott 1808-1809 között? (Svédország vs Orosz Birodalom)",
            "options": ["Finn háború", "Világháború", "Polgárháború", "Függetlenségi háború"],
            "correct": 0,
            "explanation": "Finn háború (1808-1809): Svédország vs Orosz Birodalom"
        },
        {
            "question": "Melyik háború zajlott 1821-1829 között? (Görög felkelők vs Oszmán Birodalom)",
            "options": ["Görög függetlenségi háború", "Világháború", "Polgárháború", "Függetlenségi háború"],
            "correct": 0,
            "explanation": "Görög függetlenségi háború (1821-1829): Görög felkelők vs Oszmán Birodalom"
        },
        {
            "question": "Melyik háború zajlott 1853-1856 között? (Oroszország vs Oszmán Birodalom, Egyesült Királyság, Franciaország, Szardínia)",
            "options": ["Krími háború", "Világháború", "Polgárháború", "Függetlenségi háború"],
            "correct": 0,
            "explanation": "Krími háború (1853-1856): Oroszország vs Oszmán Birodalom, Egyesült Királyság, Franciaország, Szardínia"
        },
        {
            "question": "Melyik háború zajlott 1912-1913 között? (Balkán Liga vs Oszmán Birodalom)",
            "options": ["Első Balkán-háború", "Világháború", "Polgárháború", "Függetlenségi háború"],
            "correct": 0,
            "explanation": "Első Balkán-háború (1912-1913): Balkán Liga vs Oszmán Birodalom"
        },
        {
            "question": "Melyik háború zajlott 1913 között? (Bulgária vs volt szövetségesei)",
            "options": ["Második Balkán-háború", "Világháború", "Polgárháború", "Függetlenségi háború"],
            "correct": 0,
            "explanation": "Második Balkán-háború (1913): Bulgária vs volt szövetségesei"
        },
        {
            "question": "Melyik háború zajlott 1936-1939 között? (Köztársaságiak vs Franco tábornok nemzeti erői)",
            "options": ["Spanyol polgárháború", "Világháború", "Polgárháború", "Függetlenségi háború"],
            "correct": 0,
            "explanation": "Spanyol polgárháború (1936-1939): Köztársaságiak vs Franco tábornok nemzeti erői"
        },
        {
            "question": "Melyik háború zajlott 1939-1945 között? (Tengelyhatalmak vs Szövetségesek)",
            "options": ["Második világháború", "Világháború", "Polgárháború", "Függetlenségi háború"],
            "correct": 0,
            "explanation": "Második világháború (1939-1945): Tengelyhatalmak vs Szövetségesek"
        },
        {
            "question": "Melyik háború zajlott 1375-1378 között? (Pápai Állam vs. Firenze, Milánó, Siena)",
            "options": ["Nyolc Szent háborúja", "Világháború", "Polgárháború", "Függetlenségi háború"],
            "correct": 0,
            "explanation": "Nyolc Szent háborúja (1375-1378): Pápai Állam vs. Firenze, Milánó, Siena"
        },
        {
            "question": "Melyik háború zajlott 1455-1485/87 között? (Lancaster-ház vs. York-ház)",
            "options": ["Rózsák háborúja", "Világháború", "Polgárháború", "Függetlenségi háború"],
            "correct": 0,
            "explanation": "Rózsák háborúja (1455-1485/87): Lancaster-ház vs. York-ház"
        },
        {
            "question": "Melyik háború zajlott 15. század között? (Magyar Királyság vs. Oszmán Birodalom)",
            "options": ["Oszmán–magyar háborúk", "Világháború", "Polgárháború", "Függetlenségi háború"],
            "correct": 0,
            "explanation": "Oszmán–magyar háborúk (15. század): Magyar Királyság vs. Oszmán Birodalom"
        },
        {
            "question": "Melyik háború zajlott 1990-1991 között? (Irak vs. Nemzetközi koalíció)",
            "options": ["Öbölháború", "Világháború", "Polgárháború", "Függetlenségi háború"],
            "correct": 0,
            "explanation": "Öbölháború (1990-1991): Irak vs. Nemzetközi koalíció"
        }
    ],
    
    "irodalom": [
        {
            "question": "Ki írta a Romeo és Júliát?",
            "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
            "correct": 0,
            "explanation": "A Romeo és Júliát William Shakespeare írta."
        },
        {
            "question": "Melyik évben íródott a Romeo és Júlia?",
            "options": ["1595", "1596", "1597", "1598"],
            "correct": 1,
            "explanation": "A Romeo és Júlia 1596-ban íródott."
        },
        {
            "question": "Hol játszódik a Romeo és Júlia cselekménye?",
            "options": ["London", "Verona", "Róma", "Velence"],
            "correct": 1,
            "explanation": "A Romeo és Júlia cselekménye Veronában játszódik."
        },
        {
            "question": "Ki a főhős a Romeo és Júliában?",
            "options": ["Romeo", "Júlia", "Mindkettő", "Senki"],
            "correct": 2,
            "explanation": "A Romeo és Júlia főhősei Romeo és Júlia."
        }
    ],
    
    "zene": [
        {
            "question": "Ki írta a Hatodik szimfóniát?",
            "options": ["Beethoven", "Mozart", "Bach", "Tchaikovsky"],
            "correct": 3,
            "explanation": "A Hatodik szimfóniát Tchaikovsky írta."
        },
        {
            "question": "Melyik évben íródott a Hatodik szimfónia?",
            "options": ["1891", "1892", "1893", "1894"],
            "correct": 2,
            "explanation": "A Hatodik szimfónia 1893-ban íródott."
        },
        {
            "question": "Mi a Hatodik szimfónia alcíme?",
            "options": ["Patetikus", "Tragikus", "Melankolikus", "Szenvedélyes"],
            "correct": 0,
            "explanation": "A Hatodik szimfónia alcíme 'Patetikus'."
        },
        {
            "question": "Melyik zeneszerző írta a 9. szimfóniát?",
            "options": ["Beethoven", "Mozart", "Bach", "Tchaikovsky"],
            "correct": 0,
            "explanation": "A 9. szimfóniát Beethoven írta."
        }
    ]
}

def shuffle_options(question):
    """Keveri meg a válaszlehetőségeket"""
    options = question["options"].copy()
    correct_answer = options[question["correct"]]
    
    # Keverjük meg az opciókat
    random.shuffle(options)
    
    # Keressük meg az új helyét a helyes válasznak
    new_correct = options.index(correct_answer)
    
    return {
        "question": question["question"],
        "options": options,
        "correct": new_correct,
        "explanation": question["explanation"]
    }

def get_questions_for_topics(selected_topics, num_questions=10):
    """Kiválasztott témakörökből kérdéseket ad vissza"""
    all_questions = []
    
    for topic in selected_topics:
        if topic in QUIZ_DATA_BY_TOPIC:
            all_questions.extend(QUIZ_DATA_BY_TOPIC[topic])
    
    # Keverjük meg az összes kérdést
    random.shuffle(all_questions)
    
    # Visszaadjuk a kért számú kérdést
    return all_questions[:num_questions]

def display_welcome():
    """Kezdő képernyő megjelenítése"""
    st.markdown("""
    ## Üdvözöllek a PDF Alapú Quiz Alkalmazásban! 🎯
    
    ### Hogyan működik?
    1. **Válaszd ki a témaköröket** a bal oldali menüben
    2. **Állítsd be a kérdések számát** (5-20 között)
    3. **Indítsd el a quiz-t** a "Quiz Indítása" gombra kattintva
    4. **Válaszolj a kérdésekre** és nézd meg az eredményeidet!
    
    ### Elérhető témakörök:
    - 🌍 **Földrajz**: Országok, városok, természeti adottságok
    - ⚔️ **Háborúk**: Történelmi konfliktusok és csaták
    - 📚 **Irodalom**: Könyvek, szerzők, művek
    - 🎵 **Zene**: Zeneszerzők, művek, stílusok
    
    ---
    """)
    
    # Statisztikák megjelenítése
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Összes kérdés", sum(len(questions) for questions in QUIZ_DATA_BY_TOPIC.values()))
    
    with col2:
        st.metric("Témakörök", len(QUIZ_DATA_BY_TOPIC))
    
    with col3:
        st.metric("Földrajzi kérdések", len(QUIZ_DATA_BY_TOPIC.get("földrajz", [])))
    
    with col4:
        st.metric("Háborús kérdések", len(QUIZ_DATA_BY_TOPIC.get("háborúk", [])))

def display_quiz():
    """Quiz képernyő megjelenítése"""
    questions = st.session_state.quiz_questions
    current_q = st.session_state.current_question
    
    if current_q >= len(questions):
        st.session_state.quiz_finished = True
        st.rerun()
        return
    
    question = questions[current_q]
    shuffled_question = shuffle_options(question)
    
    # Progress bar
    progress = (current_q + 1) / len(questions)
    st.progress(progress)
    st.caption(f"Kérdés {current_q + 1} / {len(questions)}")
    
    # Kérdés megjelenítése
    st.subheader(f"❓ {shuffled_question['question']}")
    
    # Válaszlehetőségek
    if 'selected_answer' not in st.session_state:
        st.session_state.selected_answer = None
    
    for i, option in enumerate(shuffled_question['options']):
        if st.button(f"{chr(65+i)}. {option}", key=f"option_{i}", use_container_width=True):
            st.session_state.selected_answer = i
            st.session_state.answers.append(i)
            
            # Eredmény ellenőrzése
            if i == shuffled_question['correct']:
                st.session_state.score += 1
                st.success("✅ Helyes válasz!")
            else:
                st.error(f"❌ Helytelen válasz! A helyes válasz: {chr(65+shuffled_question['correct'])}. {shuffled_question['options'][shuffled_question['correct']]}")
            
            # Magyarázat megjelenítése
            st.info(f"💡 **Magyarázat:** {shuffled_question['explanation']}")
            
            # Következő kérdés gomb
            if st.button("⏭️ Következő kérdés", key="next"):
                st.session_state.current_question += 1
                st.session_state.selected_answer = None
                st.rerun()
            break

def display_results():
    """Eredmények megjelenítése"""
    questions = st.session_state.quiz_questions
    score = st.session_state.score
    total = len(questions)
    percentage = (score / total) * 100
    
    st.title("🏆 Quiz Eredmények")
    st.markdown("---")
    
    # Eredmények megjelenítése
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Helyes válaszok", f"{score}/{total}")
    
    with col2:
        st.metric("Százalék", f"{percentage:.1f}%")
    
    with col3:
        if percentage >= 90:
            grade = "A+"
            emoji = "🌟"
        elif percentage >= 80:
            grade = "A"
            emoji = "⭐"
        elif percentage >= 70:
            grade = "B"
            emoji = "👍"
        elif percentage >= 60:
            grade = "C"
            emoji = "😊"
        elif percentage >= 50:
            grade = "D"
            emoji = "😐"
        else:
            grade = "F"
            emoji = "😔"
        
        st.metric("Osztályzat", f"{grade} {emoji}")
    
    # Részletes eredmények
    st.subheader("📊 Részletes eredmények")
    
    for i, (question, user_answer) in enumerate(zip(questions, st.session_state.answers)):
        shuffled_question = shuffle_options(question)
        correct = user_answer == shuffled_question['correct']
        
        with st.expander(f"Kérdés {i+1}: {question['question']}"):
            st.write(f"**Válaszod:** {chr(65+user_answer)}. {shuffled_question['options'][user_answer]}")
            st.write(f"**Helyes válasz:** {chr(65+shuffled_question['correct'])}. {shuffled_question['options'][shuffled_question['correct']]}")
            st.write(f"**Magyarázat:** {question['explanation']}")
            
            if correct:
                st.success("✅ Helyes válasz!")
            else:
                st.error("❌ Helytelen válasz!")
    
    # Új quiz indítása
    st.markdown("---")
    if st.button("🔄 Új Quiz", type="primary"):
        st.session_state.quiz_started = False
        st.session_state.quiz_finished = False
        st.rerun()

def main():
    st.title("🧠 PDF Alapú Quiz Alkalmazás")
    st.markdown("---")
    
    # Sidebar - témakörök kiválasztása
    st.sidebar.header("📚 Témakörök")
    
    available_topics = list(QUIZ_DATA_BY_TOPIC.keys())
    selected_topics = st.sidebar.multiselect(
        "Válaszd ki a témaköröket:",
        available_topics,
        default=available_topics[:2]  # Alapértelmezetten az első két témakör
    )
    
    # Kérdések számának beállítása
    num_questions = st.sidebar.slider(
        "Kérdések száma:",
        min_value=5,
        max_value=20,
        value=10,
        step=1
    )
    
    # Quiz indítása
    if st.sidebar.button("🚀 Quiz Indítása", type="primary"):
        if not selected_topics:
            st.error("Kérlek válassz ki legalább egy témakört!")
            return
        
        # Kérdések lekérése
        questions = get_questions_for_topics(selected_topics, num_questions)
        
        if len(questions) < num_questions:
            st.warning(f"Csak {len(questions)} kérdés áll rendelkezésre a kiválasztott témakörökből.")
        
        # Quiz indítása
        st.session_state.quiz_questions = questions
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.answers = []
        st.session_state.quiz_started = True
        st.session_state.quiz_finished = False
        st.rerun()
    
    # Quiz megjelenítése
    if st.session_state.get('quiz_started', False) and not st.session_state.get('quiz_finished', False):
        display_quiz()
    
    # Eredmények megjelenítése
    elif st.session_state.get('quiz_finished', False):
        display_results()
    
    # Kezdő képernyő
    else:
        display_welcome()

if __name__ == "__main__":
    main() 