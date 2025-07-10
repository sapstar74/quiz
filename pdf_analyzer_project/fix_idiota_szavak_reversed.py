#!/usr/bin/env python3
"""
Idióta szavak kérdések megfordítása
A jelentés lesz a kérdés, az idióta szó lesz a válasz
"""

from topics.idiota_szavak import IDIOTA_SZAVAK_QUESTIONS

def reverse_idiota_szavak_questions():
    """
    Megfordítja az idióta szavak kérdések struktúráját
    """
    reversed_questions = []
    
    for question in IDIOTA_SZAVAK_QUESTIONS:
        # Kivonjuk az idióta szót a kérdésből
        original_question = question["question"]
        # A kérdés formátuma: "Mit jelent az alábbi idióta szó: **szó**?"
        # Kivonjuk a szót a ** ** között
        if "**" in original_question:
            # Megkeressük a szót a ** ** között
            start = original_question.find("**") + 2
            end = original_question.find("**", start)
            if start > 1 and end > start:
                idiota_szo = original_question[start:end]
            else:
                # Fallback ha nem találjuk a ** jeleket
                idiota_szo = "ismeretlen"
        else:
            idiota_szo = "ismeretlen"
        
        # Új kérdés: a jelentés lesz a kérdés
        new_question = f"**{question['correct_answer']}** - melyik idióta szóra gondolok?"
        
        # Új válasz: az idióta szó
        new_answer = idiota_szo
        
        # Új magyarázat
        new_explanation = f"A(z) '{idiota_szo}' jelentése: {question['correct_answer']}"
        
        reversed_question = {
            "question": new_question,
            "correct_answer": new_answer,
            "explanation": new_explanation,
            "topic": "idiota_szavak",
            "question_type": "text_input"
        }
        
        reversed_questions.append(reversed_question)
    
    return reversed_questions

def save_reversed_questions():
    """
    Elmenti a megfordított kérdéseket
    """
    reversed_questions = reverse_idiota_szavak_questions()
    
    with open("topics/idiota_szavak_reversed.py", "w", encoding="utf-8") as f:
        f.write("# Idióta szavak kérdések megfordítva (jelentés -> szó)\n\n")
        f.write("IDIOTA_SZAVAK_QUESTIONS = [\n")
        
        for i, q in enumerate(reversed_questions):
            f.write(f"    {{\n")
            f.write(f'        "question": """{q["question"]}""",\n')
            f.write(f'        "correct_answer": """{q["correct_answer"]}""",\n')
            f.write(f'        "explanation": """{q["explanation"]}""",\n')
            f.write(f'        "topic": "{q["topic"]}",\n')
            f.write(f'        "question_type": "{q["question_type"]}"\n')
            f.write(f"    }}{',' if i < len(reversed_questions)-1 else ''}\n")
        
        f.write("]\n")
    
    print(f"✅ {len(reversed_questions)} megfordított idióta szó kérdés létrehozva!")
    print(f"📁 Fájl mentve: topics/idiota_szavak_reversed.py")
    
    return reversed_questions

if __name__ == "__main__":
    questions = save_reversed_questions()
    
    print("\n📋 Első 3 megfordított kérdés:")
    for i, q in enumerate(questions[:3]):
        print(f"{i+1}. {q['question']}")
        print(f"   Válasz: {q['correct_answer']}")
        print() 