#!/usr/bin/env python3
"""
Debug script a quiz kérdések és értékelés ellenőrzéséhez
"""

from topics.foldrajz import FOLDRAJZ_QUESTIONS
from classical_music_questions_tschaikovsky_updated import CLASSICAL_MUSIC_QUESTIONS as ZENEK_QUESTIONS
from topics.tudosok import TUDOSOK_QUESTIONS
from topics.mitologia_all_questions import MITOLOGIA_QUESTIONS_ALL
from topics.haboru_all_questions import HABORU_QUESTIONS_ALL
from topics.kiralyok import KIRALYOK_QUESTIONS
from topics.allatok_balanced import ALLATOK_QUESTIONS_BALANCED
from topics.dramak import DRAMAK_QUESTIONS
from topics.sport_logok import SPORT_LOGOK_QUESTIONS
from topics.zaszlok_all_questions import ZASZLOK_QUESTIONS_ALL
from topics.magyar_zenekarok import MAGYAR_ZENEKAROK_QUESTIONS
from topics.nemzetkozi_zenekarok import NEMZETKOZI_ZENEKAROK_QUESTIONS
from topics.idiota_szavak_reversed import IDIOTA_SZAVAK_QUESTIONS

# Quiz adatok témakörök szerint csoportosítva
QUIZ_DATA_BY_TOPIC = {
    "földrajz": FOLDRAJZ_QUESTIONS,
    "komolyzene": ZENEK_QUESTIONS,
    "magyar_zenekarok": MAGYAR_ZENEKAROK_QUESTIONS,
    "nemzetkozi_zenekarok": NEMZETKOZI_ZENEKAROK_QUESTIONS,
    "háborúk": HABORU_QUESTIONS_ALL,
    "magyar_királyok": KIRALYOK_QUESTIONS,
    "tudósok": TUDOSOK_QUESTIONS,
    "mitológia": MITOLOGIA_QUESTIONS_ALL,
    "állatok": ALLATOK_QUESTIONS_BALANCED,
    "drámák": DRAMAK_QUESTIONS,
    "sport_logók": SPORT_LOGOK_QUESTIONS,
    "zászlók": ZASZLOK_QUESTIONS_ALL,
    "idióta_szavak": IDIOTA_SZAVAK_QUESTIONS,
}

def check_question_structure():
    """Ellenőrzi a kérdések struktúráját"""
    
    print("🔍 Quiz kérdések struktúra ellenőrzése...")
    print("=" * 60)
    
    for topic, questions in QUIZ_DATA_BY_TOPIC.items():
        print(f"\n📚 Témakör: {topic}")
        print(f"   Kérdések száma: {len(questions)}")
        
        if questions:
            # Ellenőrizzük az első kérdés struktúráját
            first_q = questions[0]
            print(f"   Első kérdés mezői: {list(first_q.keys())}")
            
            # Ellenőrizzük a kötelező mezőket
            required_fields = ["question", "options", "correct", "explanation", "topic"]
            missing_fields = []
            
            for field in required_fields:
                if field not in first_q:
                    missing_fields.append(field)
            
            if missing_fields:
                print(f"   ⚠️  Hiányzó mezők: {missing_fields}")
            else:
                print(f"   ✅ Minden kötelező mező megtalálható")
            
            # Ellenőrizzük a correct mező értékét
            correct_idx = first_q["correct"]
            options_count = len(first_q["options"])
            
            if isinstance(correct_idx, int) and 0 <= correct_idx < options_count:
                print(f"   ✅ Correct index helyes: {correct_idx} (0-{options_count-1} tartományban)")
            else:
                print(f"   ❌ Correct index hibás: {correct_idx} (0-{options_count-1} tartományban kellene lennie)")
            
            # Ellenőrizzük a válaszlehetőségeket
            print(f"   Válaszlehetőségek száma: {options_count}")
            for i, option in enumerate(first_q["options"]):
                marker = "✅" if i == correct_idx else "  "
                print(f"   {marker} {i}: {option}")

def simulate_quiz_scoring():
    """Szimulál egy quiz-t az értékelés teszteléséhez"""
    
    print("\n🎯 Quiz értékelés szimuláció...")
    print("=" * 60)
    
    # Válasszunk ki egy témakört teszteléshez
    test_topic = "magyar_zenekarok"
    questions = QUIZ_DATA_BY_TOPIC[test_topic]
    
    print(f"📚 Teszt témakör: {test_topic}")
    print(f"   Kérdések száma: {len(questions)}")
    
    # Válasszunk ki 5 véletlenszerű kérdést
    import random
    test_questions = random.sample(questions, min(5, len(questions)))
    
    print(f"\n🧪 Tesztelés 5 kérdéssel:")
    
    score = 0
    total_questions = len(test_questions)
    
    for i, q in enumerate(test_questions):
        print(f"\n   Kérdés {i+1}: {q['question']}")
        print(f"   Válaszlehetőségek:")
        
        for j, option in enumerate(q["options"]):
            marker = "✅" if j == q["correct"] else "  "
            print(f"   {marker} {j}: {option}")
        
        # Szimuláljunk egy helyes választ
        user_answer = q["correct"]  # Mindig helyes válasz
        is_correct = user_answer == q["correct"]
        
        if is_correct:
            score += 1
            print(f"   ✅ Helyes válasz! Pontszám: {score}/{i+1}")
        else:
            print(f"   ❌ Hibás válasz! Pontszám: {score}/{i+1}")
    
    percentage = (score / total_questions) * 100
    print(f"\n🎉 Végső eredmény: {score}/{total_questions} ({percentage:.1f}%)")
    
    if percentage >= 90:
        print("🏆 Kiváló teljesítmény!")
    elif percentage >= 80:
        print("🎯 Nagyon jó!")
    elif percentage >= 70:
        print("👍 Jó teljesítmény!")
    elif percentage >= 60:
        print("⚠️ Átlagos teljesítmény")
    else:
        print("📚 Még gyakorolni kell!")

def check_specific_issues():
    """Ellenőrzi specifikus problémákat"""
    
    print("\n🔧 Specifikus problémák ellenőrzése...")
    print("=" * 60)
    
    # Ellenőrizzük, hogy minden kérdésnek van-e correct mezője
    for topic, questions in QUIZ_DATA_BY_TOPIC.items():
        print(f"\n📚 {topic}:")
        
        for i, q in enumerate(questions):
            if "correct" not in q:
                print(f"   ❌ Kérdés {i+1}: Nincs 'correct' mező")
            elif not isinstance(q["correct"], int):
                print(f"   ❌ Kérdés {i+1}: 'correct' nem szám: {q['correct']}")
            elif q["correct"] < 0 or q["correct"] >= len(q["options"]):
                print(f"   ❌ Kérdés {i+1}: 'correct' index kívül esik a tartományon: {q['correct']} (0-{len(q['options'])-1})")

if __name__ == "__main__":
    check_question_structure()
    simulate_quiz_scoring()
    check_specific_issues()
    
    print("\n🎉 Debug ellenőrzés befejezve!") 