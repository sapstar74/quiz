import streamlit as st
import random

# Page config
st.set_page_config(
    page_title="Teljes Quiz Alkalmazás",
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

# Teljes kérdésadatbázis
questions = {
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
        },
        {
            "question": "Mi Üzbegisztán fővárosa?",
            "options": ["Taskent", "Biskek", "Dusanbe", "Tbiliszi"],
            "correct": 0,
            "explanation": "Üzbegisztán fővárosa Taskent, pénzneme a som."
        },
        {
            "question": "Mi Kirgizisztán fővárosa?",
            "options": ["Taskent", "Biskek", "Asztana", "Jereván"],
            "correct": 1,
            "explanation": "Kirgizisztán fővárosa Biskek, pénzneme a som."
        },
        {
            "question": "Mi Tádzsikisztán fővárosa?",
            "options": ["Biskek", "Dusanbe", "Taskent", "Baku"],
            "correct": 1,
            "explanation": "Tádzsikisztán fővárosa Dusanbe, pénzneme a somoni."
        },
        {
            "question": "Mi Grúzia fővárosa?",
            "options": ["Baku", "Jereván", "Tbiliszi", "Asztana"],
            "correct": 2,
            "explanation": "Grúzia fővárosa Tbiliszi, pénzneme a lari."
        },
        {
            "question": "Mi Örményország fővárosa?",
            "options": ["Tbiliszi", "Jereván", "Baku", "Biskek"],
            "correct": 1,
            "explanation": "Örményország fővárosa Jereván, pénzneme a dram."
        },
        {
            "question": "Mi Kazahsztán fővárosa?",
            "options": ["Almati", "Asztana", "Taskent", "Biskek"],
            "correct": 1,
            "explanation": "Kazahsztán fővárosa Asztana (ma Nur-Sultan), pénzneme a tenge."
        },
        {
            "question": "Mi Laosz fővárosa?",
            "options": ["Vientiane", "Phnom Penh", "Bangkok", "Hanoi"],
            "correct": 0,
            "explanation": "Laosz fővárosa Vientiane, pénzneme a kip."
        },
        {
            "question": "Mi Brunei fővárosa?",
            "options": ["Bandar Seri Begawan", "Kuala Lumpur", "Jakarta", "Manila"],
            "correct": 0,
            "explanation": "Brunei fővárosa Bandar Seri Begawan, pénzneme a dollár."
        },
        {
            "question": "Mi Costa Rica fővárosa?",
            "options": ["Guatemala City", "San José", "Managua", "Tegucigalpa"],
            "correct": 1,
            "explanation": "Costa Rica fővárosa San José, pénzneme a colón."
        },
        {
            "question": "Mi Honduras fővárosa?",
            "options": ["San José", "Managua", "Tegucigalpa", "Panamaváros"],
            "correct": 2,
            "explanation": "Honduras fővárosa Tegucigalpa, pénzneme a lempira."
        },
        {
            "question": "Mi Nicaragua fővárosa?",
            "options": ["Tegucigalpa", "Managua", "San José", "Belmopan"],
            "correct": 1,
            "explanation": "Nicaragua fővárosa Managua, pénzneme a córdoba."
        },
        {
            "question": "Mi Belize fővárosa?",
            "options": ["Belize City", "Belmopan", "San Salvador", "Guatemala City"],
            "correct": 1,
            "explanation": "Belize fővárosa Belmopan, pénzneme a belize-i dollár."
        },
        {
            "question": "Mi Fidzsi-szigetek fővárosa?",
            "options": ["Suva", "Nuku'alofa", "Apia", "Port Vila"],
            "correct": 0,
            "explanation": "Fidzsi-szigetek fővárosa Suva, pénzneme a fidzsi dollár."
        },
        {
            "question": "Mi Ausztrália fővárosa?",
            "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
            "correct": 2,
            "explanation": "Ausztrália fővárosa Canberra, nem Sydney vagy Melbourne."
        },
        {
            "question": "Mi Új-Zéland fővárosa?",
            "options": ["Auckland", "Wellington", "Christchurch", "Hamilton"],
            "correct": 1,
            "explanation": "Új-Zéland fővárosa Wellington, a legnagyobb város Auckland."
        },
        {
            "question": "Mi Pápua Új-Guinea fővárosa?",
            "options": ["Port Moresby", "Lae", "Mount Hagen", "Madang"],
            "correct": 0,
            "explanation": "Pápua Új-Guinea fővárosa Port Moresby, pénzneme a kina."
        },
        {
            "question": "Mi Samoa fővárosa?",
            "options": ["Apia", "Fagamalo", "Salelologa", "Asau"],
            "correct": 0,
            "explanation": "Samoa fővárosa Apia, pénzneme a tala."
        },
        {
            "question": "Mi Tonga fővárosa?",
            "options": ["Nuku'alofa", "Neiafu", "Pangai", "Hihifo"],
            "correct": 0,
            "explanation": "Tonga fővárosa Nuku'alofa, pénzneme a pa'anga."
        },
        {
            "question": "Mi Vanuatu fővárosa?",
            "options": ["Port Vila", "Luganville", "Isangel", "Lakatoro"],
            "correct": 0,
            "explanation": "Vanuatu fővárosa Port Vila, pénzneme a vatu."
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

st.title("🧠 Teljes Quiz Alkalmazás")

# Sidebar - Beállítások
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
    max_value=50,
    value=10,
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
    ## Üdvözöllek a Teljes Quiz Alkalmazásban! 🎯
    
    ### Hogyan működik:
    1. **Válaszd ki a témaköröket** a bal oldali menüben
    2. **Állítsd be a kérdések számát** (1-50 között)
    3. **Indítsd el a quiz-t** a gombra kattintva
    4. **Válaszolj a kérdésekre**
    
    ### Elérhető témakörök:
    - 🌍 **Földrajz**: Országok, városok, természeti adottságok (30 kérdés)
    - ⚔️ **Háborúk**: Történelmi konfliktusok és csaták (20 kérdés)
    - 📚 **Irodalom**: Könyvek, szerzők, művek (4 kérdés)
    - 🎵 **Zene**: Zeneszerzők, művek, stílusok (4 kérdés)
    """)
    
    # Statisztikák
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Összes kérdés", sum(len(q) for q in questions.values()))
    with col2:
        st.metric("Témakörök", len(questions))
    with col3:
        st.metric("Földrajzi kérdések", len(questions["földrajz"]))
    with col4:
        st.metric("Háborús kérdések", len(questions["háborúk"]))

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