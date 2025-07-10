#!/usr/bin/env python3
"""
Idióta szavak kérdések generálása szabad szöveges válaszokkal
"""

# Idióta szavak a PDF 8. oldaláról
IDIOTA_SZAVAK = [
    "Hygge",
    "ikigai", 
    "onsen",
    "appaloosa",
    "aguti",
    "ladino",
    "sinobi-kunoicsi",
    "talkum",
    "merengue",
    "Titty Twister",
    "homo florensis",
    "endoplazmatikus retikulum",
    "marengo csirke",
    "kallisztenix",
    "kamerlengo",
    "guanakó",
    "autókláv",
    "kwanza",
    "CapCut",
    "Unilad",
    "CD Projekt RED",
    "nadír",
    "eseményhorizont",
    "Tankréd lovag",
    "Rasztafári vallás",
    "Plutharkosz",
    "Takla-Makán"
]

# Magyar jelentések (manuálisan összegyűjtve)
MAGYAR_JELENTESEK = {
    "Hygge": "Dán életfelfogás, kellemes, otthonos hangulat",
    "ikigai": "Japán életcél fogalom, az élet értelme",
    "onsen": "Japán termálfürdő",
    "appaloosa": "Amerikai indián lovasfajta, pettyes szőrrel",
    "aguti": "Dél-amerikai rágcsálófaj",
    "ladino": "Spanyol nyelvjárás, sefárd zsidók nyelve",
    "sinobi-kunoicsi": "Nindzsa harcosok",
    "talkum": "Por, amit a bőrre szórnak",
    "merengue": "Dominikai tánc és zenei stílus",
    "Titty Twister": "Fiktív bár a From Dusk Till Dawn filmből",
    "homo florensis": "Kihalt emberfaj, 'hobbit' ember",
    "endoplazmatikus retikulum": "Sejtszervecske, fehérje szintézis",
    "marengo csirke": "Olasz étel, csirke szósszal",
    "kallisztenix": "Görög atléta, ókori sportoló",
    "kamerlengo": "Pápai hivatalnok",
    "guanakó": "Dél-amerikai lámafaj",
    "autókláv": "Nyerség, nyomás alatt működő készülék",
    "kwanza": "Angolai pénznem",
    "CapCut": "Video szerkesztő alkalmazás",
    "Unilad": "Brit média cég",
    "CD Projekt RED": "Lengyel játékfejlesztő cég",
    "nadír": "Az égbolt legalsó pontja",
    "eseményhorizont": "Fekete lyuk határa",
    "Tankréd lovag": "Keresztes lovag, Tasso művéből",
    "Rasztafári vallás": "Jamaicai vallási mozgalom",
    "Plutharkosz": "Görög történetíró",
    "Takla-Makán": "Kína sivataga"
}

def create_idiota_szavak_questions():
    """Idióta szavak kérdések létrehozása szabad szöveges válaszokkal"""
    
    questions = []
    
    for word in IDIOTA_SZAVAK:
        if word in MAGYAR_JELENTESEK:
            question = {
                "question": f"Mit jelent az alábbi idióta szó: **{word}**?",
                "correct_answer": MAGYAR_JELENTESEK[word],
                "explanation": f"A(z) '{word}' jelentése: {MAGYAR_JELENTESEK[word]}",
                "topic": "idiota_szavak",
                "question_type": "text_input"
            }
            questions.append(question)
    
    return questions

def save_questions_to_file():
    """Kérdések mentése fájlba"""
    
    questions = create_idiota_szavak_questions()
    
    # Python fájl generálása
    with open("topics/idiota_szavak.py", "w", encoding="utf-8") as f:
        f.write("# Idióta szavak kérdések szabad szöveges válaszokkal\n\n")
        f.write("IDIOTA_SZAVAK_QUESTIONS = [\n")
        
        for i, q in enumerate(questions):
            f.write(f"    {{\n")
            f.write(f'        "question": """{q["question"]}""",\n')
            f.write(f'        "correct_answer": """{q["correct_answer"]}""",\n')
            f.write(f'        "explanation": """{q["explanation"]}""",\n')
            f.write(f'        "topic": "{q["topic"]}",\n')
            f.write(f'        "question_type": "{q["question_type"]}"\n')
            f.write(f"    }}{',' if i < len(questions)-1 else ''}\n")
        
        f.write("]\n")
    
    print(f"✅ {len(questions)} idióta szó kérdés létrehozva!")
    print(f"📁 Fájl mentve: topics/idiota_szavak.py")
    
    return questions

if __name__ == "__main__":
    questions = save_questions_to_file()
    
    print("\n📋 Első 3 kérdés:")
    for i, q in enumerate(questions[:3]):
        print(f"{i+1}. {q['question']}")
        print(f"   Válasz: {q['correct_answer']}")
        print() 