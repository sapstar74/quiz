"""
🧠 PDF Alapú Advanced Quiz Alkalmazás
Témakörök szerint csoportosított kérdések, választható témakörök és kérdésszám
"""

import streamlit as st
import random
import time
from datetime import datetime

# Page config
st.set_page_config(
    page_title="🧠 Advanced PDF Quiz",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Quiz adatok témakörök szerint csoportosítva
QUIZ_DATA_BY_TOPIC = {
    "földrajz": [
        {
            "question": "Mi a legmagasabb csúcs a Mátrában?",
            "options": ["Kékes", "Dobogó-kő", "Csóványos", "Szilvási-kő"],
            "correct": 0,
            "explanation": "A Kékes 1014 méter magasságával a Mátra és Magyarország legmagasabb csúcsa."
        },
        {
            "question": "Melyik ország fővárosa Taskent?",
            "options": ["Kazahsztán", "Üzbegisztán", "Kirgizisztán", "Tádzsikisztán"],
            "correct": 1,
            "explanation": "Taskent Üzbegisztán fővárosa, pénzneme a som."
        },
        {
            "question": "Melyik a világ leghosszabb folyója?",
            "options": ["Amazonas", "Nílus", "Jangce", "Mississippi"],
            "correct": 1,
            "explanation": "A Nílus 6650 km hosszával a világ leghosszabb folyója."
        },
        {
            "question": "Melyik ország pénzneme a manat?",
            "options": ["Grúzia", "Azerbajdzsán", "Örményország", "Kazahsztán"],
            "correct": 1,
            "explanation": "Azerbajdzsán pénzneme a manat, fővárosa Baku."
        },
        {
            "question": "Mi Bhután fővárosa?",
            "options": ["Thimphu", "Katmandu", "Dhaka", "Vientiane"],
            "correct": 0,
            "explanation": "Bhután fővárosa Thimphu, pénzneme a ngultrum."
        },
        {
            "question": "Melyik hegység csúcsa a Börzsöny legmagasabb pontja?",
            "options": ["Nagy-Kopasz", "Csóványos", "Pilis", "Dobogó-kő"],
            "correct": 1,
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
            "options": ["Peso", "Colón", "Dollár", "Quetzal"],
            "correct": 1,
            "explanation": "Costa Rica pénzneme a Costa Rica-i colón."
        },
        {
            "question": "Melyik az Európa leghosszabb folyója?",
            "options": ["Duna", "Rajna", "Volga", "Dnyeper"],
            "correct": 2,
            "explanation": "A Volga 3530 km hosszával Európa leghosszabb folyója."
        },
        {
            "question": "Mi a Pilis hegység legmagasabb csúcsa?",
            "options": ["Nagy-Kopasz", "Pilis", "Dobogó-kő", "Szánkó-hegy"],
            "correct": 1,
            "explanation": "A Pilis (757 m) a Pilis hegység névadó és legmagasabb csúcsa."
        }
    ],
    "zene": [
        {
            "question": "Ki szerezte a 'Diótörő' balettzenét?",
            "options": ["Beethoven", "Mozart", "Csajkovszkij", "Dvorak"],
            "correct": 2,
            "explanation": "Csajkovszkij szerezte a híres 'Diótörő' balettzenét."
        },
        {
            "question": "Melyik zeneszerző írta a 'Török induló'-t?",
            "options": ["Mozart", "Beethoven", "Chopin", "Liszt"],
            "correct": 0,
            "explanation": "Mozart szerezte a híres 'Török induló'-t."
        },
        {
            "question": "Ki szerezte a 'Háry János' című művet?",
            "options": ["Bartók Béla", "Kodály Zoltán", "Liszt Ferenc", "Erkel Ferenc"],
            "correct": 1,
            "explanation": "Kodály Zoltán szerezte a 'Háry János' című népoperát."
        },
        {
            "question": "Ki szerezte a 'Hattyúk tava' balettzenét?",
            "options": ["Beethoven", "Csajkovszkij", "Ravel", "Stravinsky"],
            "correct": 1,
            "explanation": "Csajkovszkij szerezte a 'Hattyúk tava' című balettet is."
        },
        {
            "question": "Melyik zeneszerző írt 'Magyar rapszódiá'-kat?",
            "options": ["Bartók Béla", "Kodály Zoltán", "Liszt Ferenc", "Chopin"],
            "correct": 2,
            "explanation": "Liszt Ferenc írt 19 Magyar rapszódiát."
        },
        {
            "question": "Ki szerezte a 'Peer Gynt' zenéjét?",
            "options": ["Grieg", "Sibelius", "Nielsen", "Brahms"],
            "correct": 0,
            "explanation": "Edvard Grieg szerezte a 'Peer Gynt' kísérőzenéjét."
        },
        {
            "question": "Ki szerezte a 'Bolero'-t?",
            "options": ["Debussy", "Ravel", "Satie", "Fauré"],
            "correct": 1,
            "explanation": "Maurice Ravel szerezte a híres 'Bolero'-t."
        },
        {
            "question": "Melyik zeneszerző írta a 'Román táncok'-at?",
            "options": ["Liszt Ferenc", "Brahms", "Bartók Béla", "Dvorak"],
            "correct": 2,
            "explanation": "Bartók Béla szerezte a 'Román táncok'-at."
        },
        {
            "question": "Ki szerezte a 'Carmina Burana'-t?",
            "options": ["Carl Orff", "Wagner", "Brahms", "Mahler"],
            "correct": 0,
            "explanation": "Carl Orff szerezte a 'Carmina Burana' kantátát."
        },
        {
            "question": "Ki írta a 'Pisztráng ötös'-t?",
            "options": ["Mozart", "Schubert", "Haydn", "Brahms"],
            "correct": 1,
            "explanation": "Franz Schubert szerezte a 'Pisztráng' ötöst (vonósnégyes + zongora)."
        }
    ],
    "tudósok": [
        {
            "question": "Ki alapította a Vöröskeresztet?",
            "options": ["Albert Schweitzer", "Jean-Henri Dunant", "Kármán Tódor", "Jedlik Ányos"],
            "correct": 1,
            "explanation": "Jean-Henri Dunant alapította a Vöröskeresztet."
        },
        {
            "question": "Melyik magyar tudós volt bencés szerzetes?",
            "options": ["Kármán Tódor", "Csonka János", "Jedlik Ányos", "Bolyai János"],
            "correct": 2,
            "explanation": "Jedlik Ányos bencés szerzetes volt, számos találmánya közül a dinamó az egyik legismertebb."
        },
        {
            "question": "Ki dolgozta ki a Cauchy-eloszlást?",
            "options": ["Gauss", "Cauchy", "Euler", "Newton"],
            "correct": 1,
            "explanation": "Augustin-Louis Cauchy francia matematikus dolgozta ki a róla elnevezett eloszlást."
        },
        {
            "question": "Ki oldotta meg a königsbergi hidak problémáját?",
            "options": ["Newton", "Leibniz", "Euler", "Gauss"],
            "correct": 2,
            "explanation": "Leonhard Euler oldotta meg a königsbergi hidak problémáját, megalapítva a gráfelmélet alapjait."
        },
        {
            "question": "Ki volt Konrad Lorenz?",
            "options": ["Fizikus", "Etológus", "Kémikus", "Matematikus"],
            "correct": 1,
            "explanation": "Konrad Lorenz osztrák etológus (állatviselkedés-kutató) volt, Nobel-díjas."
        },
        {
            "question": "Kármán Tódor melyik tudományterületen alkotott?",
            "options": ["Biológia", "Aerodinamika", "Kémia", "Geológia"],
            "correct": 1,
            "explanation": "Kármán Tódor magyar származású aerodinamikus, a Kármán-örvények felfedezője."
        },
        {
            "question": "Ki volt Albert Schweitzer?",
            "options": ["Fizikus", "Orvos és filozófus", "Kémikus", "Matematikus"],
            "correct": 1,
            "explanation": "Albert Schweitzer német-francia orvos, filozófus és teológus volt, Nobel-békedíjas."
        },
        {
            "question": "Csonka János mivel foglalkozott?",
            "options": ["Csillagászat", "Gépészet", "Botanika", "Geológia"],
            "correct": 1,
            "explanation": "Csonka János magyar gépészmérnök és feltaláló volt."
        },
        {
            "question": "Ki a fotoszintézis kutatásának egyik úttörője?",
            "options": ["Darwin", "Mendel", "Van Helmont", "Pasteur"],
            "correct": 2,
            "explanation": "Jan Baptist van Helmont belga tudós volt az egyik első, aki a fotoszintézist kutatta."
        },
        {
            "question": "Mi a ganglion az orvostudományban?",
            "options": ["Izom", "Idegdúc", "Csont", "Véredény"],
            "correct": 1,
            "explanation": "A ganglion idegdúc, idegsejtek csoportosulása az idegrendszerben."
        }
    ],
    "mitológia": [
        {
            "question": "Ki a görög mitológiában a nap, jóslás, költészet és zene istene?",
            "options": ["Arész", "Apollón", "Hermész", "Héphaisztosz"],
            "correct": 1,
            "explanation": "Apollón a görög mitológiában a nap, jóslás, költészet és zene istene."
        },
        {
            "question": "Ki volt Orpheusz felesége?",
            "options": ["Eurüdiké", "Artemisz", "Aphrodité", "Thetisz"],
            "correct": 0,
            "explanation": "Eurüdiké volt Orpheusz felesége, akit kígyó mart meg."
        },
        {
            "question": "Ki a háború és vérontás istene a görög mitológiában?",
            "options": ["Apollón", "Arész", "Héphaisztosz", "Hermész"],
            "correct": 1,
            "explanation": "Arész a háború és vérontás istene, akit még az istenek sem kedveltek."
        },
        {
            "question": "Ki Akhilleusz anyja?",
            "options": ["Héra", "Aphrodité", "Thetisz", "Artemisz"],
            "correct": 2,
            "explanation": "Thetisz tengeri istennő Akhilleusz anyja, próbálta halhatatlanná tenni fiát."
        },
        {
            "question": "Ki a tűz, kovácsmesterség és technológia istene?",
            "options": ["Apollón", "Arész", "Héphaisztosz", "Hermész"],
            "correct": 2,
            "explanation": "Héphaisztosz a sánta isten, aki gyönyörű fegyvereket kovácsolt."
        },
        {
            "question": "Ki az alvilág révésze?",
            "options": ["Hadész", "Kharón", "Orpheusz", "Hermész"],
            "correct": 1,
            "explanation": "Kharón az alvilág révésze, aki átviszi azokat, akik megfizették az oboloszt."
        },
        {
            "question": "Ki a vadászat, erdők és szűziesség istennője?",
            "options": ["Héra", "Aphrodité", "Artemisz", "Athéné"],
            "correct": 2,
            "explanation": "Artemisz a vadászat, erdők és szűziesség istennője."
        },
        {
            "question": "Ki a szerelem, vágy és szépség istennője?",
            "options": ["Héra", "Aphrodité", "Artemisz", "Athéné"],
            "correct": 1,
            "explanation": "Aphrodité a szerelem, vágy és szépség istennője, a tenger habjaiból született."
        },
        {
            "question": "Mi okozta a trójai háborút?",
            "options": ["Héra bosszúja", "Aphrodité aranyalmája", "Zeus haragja", "Athéné bosszúja"],
            "correct": 1,
            "explanation": "Aphrodité aranyalmája okozta a trójai háborút."
        },
        {
            "question": "Ki lett Athén védőistennője?",
            "options": ["Aphrodité", "Artemisz", "Athéné", "Héra"],
            "correct": 2,
            "explanation": "Athéné, a bölcsesség és hadviselés istennője lett Athén védőistennője."
        }
    ]
}

def get_selected_questions(selected_topics, num_questions):
    """Kiválasztott témakörökből véletlenszerű kérdéseket választ"""
    all_questions = []
    
    for topic in selected_topics:
        if topic in QUIZ_DATA_BY_TOPIC:
            topic_questions = QUIZ_DATA_BY_TOPIC[topic].copy()
            for q in topic_questions:
                q["topic"] = topic
            all_questions.extend(topic_questions)
    
    if len(all_questions) == 0:
        return []
    
    # Ha kevesebb kérdés van, mint amennyit kérnek, adjuk vissza az összeset
    if len(all_questions) <= num_questions:
        return all_questions
    
    # Véletlenszerű kiválasztás
    return random.sample(all_questions, num_questions)

def reset_quiz(selected_topics, num_questions):
    """Quiz újraindítása a kiválasztott beállításokkal"""
    st.session_state.selected_questions = get_selected_questions(selected_topics, num_questions)
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.answers = []
    st.session_state.quiz_completed = False
    st.session_state.start_time = time.time()
    st.session_state.total_questions = len(st.session_state.selected_questions)

def main():
    st.title("🧠 Advanced PDF Quiz Alkalmazás")
    st.markdown("**Témakörök szerint csoportosított kérdések**")
    st.markdown("---")
    
    # Sidebar - Beállítások
    with st.sidebar:
        st.header("⚙️ Quiz Beállítások")
        
        # Témakör választás
        st.subheader("📚 Témakörök")
        available_topics = list(QUIZ_DATA_BY_TOPIC.keys())
        topic_labels = {
            "földrajz": "🌍 Földrajz", 
            "zene": "🎵 Zene",
            "tudósok": "🔬 Tudósok", 
            "mitológia": "🏛️ Mitológia"
        }
        
        selected_topics = []
        for topic in available_topics:
            if st.checkbox(topic_labels[topic], key=f"topic_{topic}"):
                selected_topics.append(topic)
        
        # Kérdések száma
        st.subheader("🔢 Kérdések száma")
        max_available = sum(len(questions) for topic, questions in QUIZ_DATA_BY_TOPIC.items() if topic in selected_topics)
        
        if selected_topics:
            num_questions = st.slider(
                "Kérdések száma:", 
                min_value=1, 
                max_value=min(10, max_available), 
                value=min(5, max_available),
                help=f"Elérhető kérdések: {max_available}"
            )
        else:
            st.warning("⚠️ Válassz legalább egy témakört!")
            num_questions = 1
        
        # Quiz indítás
        if st.button("🚀 Quiz Indítása", type="primary", disabled=len(selected_topics)==0):
            reset_quiz(selected_topics, num_questions)
            st.rerun()
        
        # Témakörök információ
        st.markdown("---")
        st.subheader("📊 Témakör Statisztikák")
        for topic, questions in QUIZ_DATA_BY_TOPIC.items():
            icon = topic_labels[topic].split()[0]
            st.metric(f"{icon} {topic.title()}", f"{len(questions)} kérdés")
    
    # Fő tartalom
    if 'selected_questions' not in st.session_state or len(st.session_state.selected_questions) == 0:
        # Kezdő képernyő
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            st.info("""
            ### 👋 Üdvözöl az Advanced Quiz!
            
            **Új funkciók:**
            - 🎯 **Témakör választás**: Válaszd ki a kedvenc témáidat
            - 🔢 **Rugalmas kérdésszám**: 1-10 kérdés között
            - 📊 **Témakör statisztikák**: Lásd mennyi kérdés van témakörönként
            - 🎨 **Színes kategóriák**: Minden téma más színnel
            
            **Elérhető témakörök:**
            - 🌍 **Földrajz** (10 kérdés): Országok, fővárosok, hegyek, folyók
            - 🎵 **Zene** (10 kérdés): Zeneszerzők, művek, klasszikus zene
            - 🔬 **Tudósok** (10 kérdés): Híres tudósok és felfedezések
            - 🏛️ **Mitológia** (10 kérdés): Görög istenek és hősök
            
            **Kezdéshez válassz témakör(öke)t a bal oldali panelen!**
            """)
    
    elif st.session_state.quiz_completed:
        # Eredmények megjelenítése
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            st.success("🎉 Quiz Befejezve!")
            
            score_percentage = (st.session_state.score / st.session_state.total_questions) * 100
            
            st.metric("Végső Pontszám", f"{st.session_state.score}/{st.session_state.total_questions} ({score_percentage:.0f}%)")
            
            total_time = time.time() - st.session_state.start_time
            st.metric("Teljes idő", f"{total_time:.0f} másodperc")
            
            # Értékelés
            if score_percentage >= 80:
                st.balloons()
                st.success("🌟 Kiváló! Nagyszerű tudás!")
            elif score_percentage >= 60:
                st.info("👍 Jó! Szép munka!")
            else:
                st.warning("📚 Érdemes tanulni még!")
        
        # Részletes eredmények
        st.markdown("---")
        st.header("📝 Részletes Eredmények")
        
        # Témakörök szerinti csoportosítás
        results_by_topic = {}
        for i, (question, answer) in enumerate(zip(st.session_state.selected_questions, st.session_state.answers)):
            topic = question.get("topic", "egyéb")
            if topic not in results_by_topic:
                results_by_topic[topic] = []
            results_by_topic[topic].append((i, question, answer))
        
        for topic, topic_results in results_by_topic.items():
            topic_icon = topic_labels.get(topic, f"📋 {topic}")
            
            with st.expander(f"{topic_icon} - {len(topic_results)} kérdés"):
                for i, question, answer in topic_results:
                    is_correct = answer == question["correct"]
                    
                    st.markdown(f"**{i+1}. {question['question']}** {'✅' if is_correct else '❌'}")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"**Válaszod:** {question['options'][answer]}")
                    with col2:
                        st.write(f"**Helyes válasz:** {question['options'][question['correct']]}")
                    
                    st.info(f"💡 {question['explanation']}")
                    st.markdown("---")
    
    else:
        # Quiz folyamatban
        current_q = st.session_state.selected_questions[st.session_state.current_question]
        topic_icon = topic_labels.get(current_q.get("topic", ""), "📋")
        
        # Progress és info
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Kérdés", f"{st.session_state.current_question + 1}/{st.session_state.total_questions}")
        with col2:
            answered = len(st.session_state.answers)
            st.metric("Pontszám", f"{st.session_state.score}/{answered}")
        with col3:
            if st.session_state.current_question > 0:
                elapsed = time.time() - st.session_state.start_time
                st.metric("Eltelt idő", f"{elapsed:.0f}s")
        
        # Kérdés megjelenítése
        st.markdown(f"### {topic_icon} Kérdés {st.session_state.current_question + 1}")
        st.markdown(f"#### {current_q['question']}")
        
        # Válaszlehetőségek
        selected_option = st.radio(
            "Válaszd ki a helyes választ:",
            options=range(len(current_q['options'])),
            format_func=lambda x: current_q['options'][x],
            key=f"question_{st.session_state.current_question}"
        )
        
        st.markdown("---")
        
        # Válasz küldése gomb
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col2:
            if st.button("📤 Válasz Küldése", type="primary", key="submit_answer"):
                # Válasz mentése
                st.session_state.answers.append(selected_option)
                
                # Pontszám frissítése
                if selected_option == current_q['correct']:
                    st.session_state.score += 1
                
                # Következő kérdés vagy befejezés
                if st.session_state.current_question + 1 < st.session_state.total_questions:
                    st.session_state.current_question += 1
                    st.rerun()
                else:
                    st.session_state.quiz_completed = True
                    st.rerun()
        
        # Előrehaladás jelző
        progress = (st.session_state.current_question + 1) / st.session_state.total_questions
        st.progress(progress)

if __name__ == "__main__":
    main() 