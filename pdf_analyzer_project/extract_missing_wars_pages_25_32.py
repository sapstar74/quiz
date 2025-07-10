#!/usr/bin/env python3
"""
A PDF 25-32. oldalai között lévő háborúk kinyerése és hozzáadása a kvízhez
"""

import json
from pathlib import Path

def get_missing_wars_from_pages_25_32():
    """A PDF 25-32. oldalairól hiányzó háborúk"""
    
    missing_wars = [
        # 17. század háborúk (folytatás)
        {
            "years": "1672-1678",
            "name": "Francia–holland háború",
            "parties": "Franciaország vs. Holland Köztársaság, Spanyolország, Német-római Birodalom"
        },
        {
            "years": "1683-1699",
            "name": "Nagy török háború",
            "parties": "Szent Liga (Német-római Birodalom, Lengyelország, Velence, Oroszország) vs. Oszmán Birodalom"
        },
        {
            "years": "1688-1697",
            "name": "Augsburgi Liga háborúja",
            "parties": "Franciaország vs. Augsburgi Liga (Anglia, Hollandia, Német-római Birodalom)"
        },
        {
            "years": "1667-1668",
            "name": "Devolúciós háború",
            "parties": "Franciaország vs. Spanyolország"
        },
        {
            "years": "1652-1654",
            "name": "Első angol-holland háború",
            "parties": "Angol Commonwealth vs. Holland Köztársaság"
        },
        {
            "years": "1665-1667",
            "name": "Második angol-holland háború",
            "parties": "Anglia vs. Holland Köztársaság"
        },
        {
            "years": "1672-1674",
            "name": "Harmadik angol-holland háború",
            "parties": "Anglia, Franciaország vs. Holland Köztársaság"
        },
        {
            "years": "1620-1621",
            "name": "Lengyel–török háború",
            "parties": "Lengyel-Litván Unió & Kozákok vs. Oszmán Birodalom"
        },
        {
            "years": "1676-1681",
            "name": "Lengyel–török háború",
            "parties": "Lengyel-Litván Unió vs. Oszmán Birodalom"
        },
        {
            "years": "1611-1613",
            "name": "Kalmari háború",
            "parties": "Dánia-Norvégia vs. Svédország"
        },
        
        # 18. század háborúk
        {
            "years": "1700-1721",
            "name": "Nagy északi háború",
            "parties": "Svédország vs. Oroszország, Dánia-Norvégia, Szász-Lengyelország"
        },
        {
            "years": "1733-1735",
            "name": "Lengyel örökösödési háború",
            "parties": "Leszczyński Stanisław támogatói (Franciaország) vs. II. Ágost támogatói (Oroszország, Ausztria)"
        },
        {
            "years": "1735-1739",
            "name": "Orosz–török háború",
            "parties": "Orosz Birodalom vs. Oszmán Birodalom"
        },
        {
            "years": "1739-1748",
            "name": "Jenkins füle háborúja",
            "parties": "Nagy-Britannia vs. Spanyolország (Osztrák örökösödési háború része)"
        },
        {
            "years": "1768-1774",
            "name": "Orosz–török háború",
            "parties": "Orosz Birodalom vs. Oszmán Birodalom"
        },
        {
            "years": "1778-1779",
            "name": "Bajor örökösödési háború",
            "parties": "Poroszország, Szászország vs. Habsburg Monarchia"
        },
        {
            "years": "1788-1790",
            "name": "Orosz–svéd háború",
            "parties": "Orosz Birodalom vs. Svédország"
        },
        {
            "years": "1787-1792",
            "name": "Orosz–török háború",
            "parties": "Orosz Birodalom, Ausztria vs. Oszmán Birodalom"
        },
        {
            "years": "1792-1797",
            "name": "Első koalíciós háború",
            "parties": "Francia Köztársaság vs. Első koalíció (Ausztria, Poroszország, Nagy-Britannia)"
        },
        
        # 19. század háborúk
        {
            "years": "1848-1849",
            "name": "Szardíniai–osztrák háború",
            "parties": "Szardínia-Piemont vs. Osztrák Birodalom"
        },
        {
            "years": "1859",
            "name": "Francia–osztrák háború",
            "parties": "Franciaország, Szardínia-Piemont vs. Osztrák Birodalom"
        },
        {
            "years": "1864",
            "name": "Dán–porosz háború",
            "parties": "Poroszország & Ausztria vs. Dánia"
        },
        {
            "years": "1866",
            "name": "Porosz–osztrák háború",
            "parties": "Poroszország & Olaszország vs. Osztrák Birodalom"
        },
        {
            "years": "1870-1871",
            "name": "Porosz–francia háború",
            "parties": "Poroszország & Északnémet Szövetség vs. Franciaország"
        },
        {
            "years": "1877-1878",
            "name": "Orosz–török háború",
            "parties": "Orosz Birodalom vs. Oszmán Birodalom"
        },
        
        # 20. század háborúk
        {
            "years": "1918-1921",
            "name": "Orosz polgárháború",
            "parties": "Vörös Hadsereg vs. Fehér Hadsereg"
        },
        {
            "years": "1919-1921",
            "name": "Ír függetlenségi háború",
            "parties": "Ír Köztársasági Hadsereg (IRA) vs. Brit erők"
        },
        {
            "years": "1919-1921",
            "name": "Lengyel–szovjet háború",
            "parties": "Lengyelország vs. Szovjet-Oroszország"
        },
        {
            "years": "1946-1949",
            "name": "Görög polgárháború",
            "parties": "Görög Kormányhadsereg vs. Kommunista gerillák"
        },
        {
            "years": "1991-2001",
            "name": "Délszláv háborúk",
            "parties": "Jugoszlávia utódállamai (Szlovénia, Horvátország, Bosznia, Szerbia, Montenegró)"
        },
        {
            "years": "1991",
            "name": "Szlovén függetlenségi háború",
            "parties": "Szlovén Területvédelem vs. Jugoszláv Néphadsereg"
        },
        {
            "years": "1991-1995",
            "name": "Horvát függetlenségi háború",
            "parties": "Horvátország vs. Jugoszláv Néphadsereg, Szerb milíciák"
        },
        {
            "years": "1992-1995",
            "name": "Boszniai háború",
            "parties": "Boszniai kormányerők vs. Boszniai szerbek, Boszniai horvátok"
        },
        {
            "years": "1998-1999",
            "name": "Koszovói háború",
            "parties": "Koszovói Felszabadítási Hadsereg vs. Szerbia"
        }
    ]
    
    return missing_wars

def generate_war_questions(wars):
    """Generál kvíz kérdéseket a háborúkból"""
    questions = []
    
    for war in wars:
        # Kérdés létrehozása
        question = f"Melyik háború zajlott {war['years']} között? ({war['parties']})"
        
        # Válaszlehetőségek generálása
        options = [war['name']]
        
        # További opciók hozzáadása (általános háborúk)
        general_wars = ["Világháború", "Polgárháború", "Függetlenségi háború", "Örökösödési háború"]
        for general_war in general_wars:
            if general_war not in war['name'] and len(options) < 4:
                options.append(general_war)
        
        # Ha kevesebb mint 4 opció van, töltse ki
        while len(options) < 4:
            options.append(f"Egyéb háború {len(options) + 1}")
        
        # Csak az első 4 opciót tartjuk meg
        options = options[:4]
        
        questions.append({
            "question": question,
            "options": options,
            "correct": 0,
            "explanation": f"{war['name']} ({war['years']}): {war['parties']}"
        })
    
    return questions

def add_wars_to_quiz(wars, quiz_file_path):
    """Hozzáadja a háborúkat a kvízhez"""
    
    # Jelenlegi kvíz beolvasása
    with open(quiz_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Háborúk szekció keresése - a legutolsó ], előtt szúrjuk be
    war_section_start = content.find('"háborúk": [')
    if war_section_start == -1:
        print("Háborúk szekció nem található a kvízben!")
        return False
    
    # Háborúk szekció vége keresése - a megfelelő záró ] keresése
    bracket_count = 0
    war_section_end = war_section_start + len('"háborúk": [')
    
    while war_section_end < len(content):
        if content[war_section_end] == '[':
            bracket_count += 1
        elif content[war_section_end] == ']':
            if bracket_count == 0:
                break
            bracket_count -= 1
        war_section_end += 1
    
    if war_section_end >= len(content):
        print("Háborúk szekció vége nem található!")
        return False
    
    # Új háborúk formázása
    new_wars_json = []
    for war in wars:
        war_json = f'''        {{
            "question": "{war['question']}",
            "options": {json.dumps(war['options'], ensure_ascii=False)},
            "correct": {war['correct']},
            "explanation": "{war['explanation']}"
        }}'''
        new_wars_json.append(war_json)
    
    # Új háborúk beszúrása
    new_wars_text = ',\n' + ',\n'.join(new_wars_json)
    
    # Tartalom frissítése
    new_content = (
        content[:war_section_end] + 
        new_wars_text + 
        content[war_section_end:]
    )
    
    # Fájl mentése
    with open(quiz_file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def main():
    """Fő függvény"""
    quiz_path = "quiz_app.py"
    
    print("A PDF 25-32. oldalairól hiányzó háborúk kinyerése...")
    missing_wars = get_missing_wars_from_pages_25_32()
    
    print(f"Hiányzó háborúk száma: {len(missing_wars)}")
    
    if missing_wars:
        print("Első 5 hiányzó háború:")
        for i, war in enumerate(missing_wars[:5]):
            print(f"{i+1}. {war['name']} ({war['years']})")
        
        print("\nKvíz kérdések generálása...")
        questions = generate_war_questions(missing_wars)
        
        print("\nHáborúk hozzáadása a kvízhez...")
        if add_wars_to_quiz(questions, quiz_path):
            print("✅ Sikeresen hozzáadtam az összes hiányzó háborút a kvízhez!")
            print(f"Összesen {len(questions)} új háborús kérdés lett hozzáadva.")
        else:
            print("❌ Hiba történt a kvíz frissítésekor!")
    else:
        print("❌ Nem találtam hiányzó háborúkat!")

if __name__ == "__main__":
    main() 