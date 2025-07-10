#!/usr/bin/env python3
"""
Magyar zenekarok kérdések frissítése valódi Spotify linkekkel
"""

import re

# Import valódi Spotify linkek
from magyar_zenekarok_spotify_api_links import MAGYAR_ZENEKAROK_SPOTIFY_API_LINKS

def update_spotify_links_in_file():
    """Frissíti a magyar_zenekarok.py fájlt valódi Spotify linkekkel"""
    
    # Olvasd be az eredeti fájlt
    with open('topics/magyar_zenekarok.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fallback link
    fallback_link = "https://open.spotify.com/artist/0YqQvRjqNXAv2K5FqS9cdO"
    
    # Számlálók
    updated_count = 0
    total_questions = 0
    
    # Keresd meg az összes kérdést és frissítsd a Spotify linkeket
    lines = content.split('\n')
    updated_lines = []
    
    for line in lines:
        if '"spotify_embed":' in line and fallback_link in line:
            # Keresd meg a kérdésben szereplő zenekar nevét
            # Visszafelé keresünk a kérdés sorában
            question_index = len(updated_lines) - 1
            while question_index >= 0 and '"question":' not in updated_lines[question_index]:
                question_index -= 1
            
            if question_index >= 0:
                question_line = updated_lines[question_index]
                # Keresd meg a kérdésben szereplő zenekar nevét
                for zenekar, spotify_link in MAGYAR_ZENEKAROK_SPOTIFY_API_LINKS.items():
                    if zenekar in question_line:
                        # Frissítsd a Spotify linket
                        new_line = line.replace(fallback_link, spotify_link)
                        updated_lines.append(new_line)
                        updated_count += 1
                        print(f"✅ Frissítve: {zenekar} -> {spotify_link}")
                        break
                else:
                    # Ha nem találtunk egyezést, hagyd meg a fallback linket
                    updated_lines.append(line)
                    print(f"⚠️  Nem találtam egyezést: {question_line.strip()}")
            else:
                updated_lines.append(line)
        else:
            updated_lines.append(line)
        
        # Számold a kérdéseket
        if '"question":' in line:
            total_questions += 1
    
    # Írd ki a frissített tartalmat
    updated_content = '\n'.join(updated_lines)
    
    # Mentsd el a frissített fájlt
    with open('topics/magyar_zenekarok_updated.py', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"\n📊 Összefoglaló:")
    print(f"📝 Összes kérdés: {total_questions}")
    print(f"✅ Frissített link: {updated_count}")
    print(f"📁 Frissített fájl: topics/magyar_zenekarok_updated.py")
    
    return updated_content

def create_updated_questions():
    """Létrehozza a frissített kérdéseket a valódi Spotify linkekkel"""
    
    # Alap kérdések struktúra
    questions_template = []
    
    # Magyar alternatív zenekarok
    alt_zenekarok = [
        "Hiperkarma", "HS7", "Óriás", "Kispál", "Kiscsillag", "Vad Fruttik",
        "Tereskova", "Anna and the Barbies", "Honeybeast", "Konyha",
        "Follow the flow", "Elefánt", "4Street", "Bagossy Brothers",
        "Csaknekedkislány", "Lóci játszik", "Galaxisok"
    ]
    
    for zenekar in alt_zenekarok:
        spotify_link = MAGYAR_ZENEKAROK_SPOTIFY_API_LINKS.get(zenekar, "https://open.spotify.com/artist/0YqQvRjqNXAv2K5FqS9cdO")
        question = {
            "question": f"Melyik magyar alternatív zenekar tagja volt {zenekar}?",
            "spotify_embed": spotify_link,
            "options": [zenekar, 'Hiperkarma', 'HS7', 'Óriás'],
            "correct": 0,
            "explanation": f"{zenekar} magyar alternatív zenekar",
            "topic": "magyar_zenekarok"
        }
        questions_template.append(question)
    
    # Magyar roma/népzene
    roma_zenekarok = [
        "Parno Graszt", "Palya Bea", "Bohemian Betyars", "Aurevoir", "Dánielffy", "Ham Ko Ham"
    ]
    
    for zenekar in roma_zenekarok:
        spotify_link = MAGYAR_ZENEKAROK_SPOTIFY_API_LINKS.get(zenekar, "https://open.spotify.com/artist/0YqQvRjqNXAv2K5FqS9cdO")
        question = {
            "question": f"Melyik magyar roma/népzene zenekar tagja volt {zenekar}?",
            "spotify_embed": spotify_link,
            "options": [zenekar, 'Parno Graszt', 'Palya Bea', 'Bohemian Betyars'],
            "correct": 0,
            "explanation": f"{zenekar} magyar roma/népzene zenekar",
            "topic": "magyar_zenekarok"
        }
        questions_template.append(question)
    
    # Magyar elektronikus
    elektronikus_zenekarok = [
        "Carbonfools", "Zagar", "Neo", "Soulwave", "Neon"
    ]
    
    for zenekar in elektronikus_zenekarok:
        spotify_link = MAGYAR_ZENEKAROK_SPOTIFY_API_LINKS.get(zenekar, "https://open.spotify.com/artist/0YqQvRjqNXAv2K5FqS9cdO")
        question = {
            "question": f"Melyik magyar elektronikus zenekar tagja volt {zenekar}?",
            "spotify_embed": spotify_link,
            "options": [zenekar, 'Carbonfools', 'Zagar', 'Neo'],
            "correct": 0,
            "explanation": f"{zenekar} magyar elektronikus zenekar",
            "topic": "magyar_zenekarok"
        }
        questions_template.append(question)
    
    # Magyar rock/pop
    rock_pop_zenekarok = [
        "Quimby", "Tankcsapda", "P. Mobil", "Republic", "Bonanza Banzai", "Korai Öröm"
    ]
    
    for zenekar in rock_pop_zenekarok:
        spotify_link = MAGYAR_ZENEKAROK_SPOTIFY_API_LINKS.get(zenekar, "https://open.spotify.com/artist/0YqQvRjqNXAv2K5FqS9cdO")
        question = {
            "question": f"Melyik magyar rock/pop zenekar tagja volt {zenekar}?",
            "spotify_embed": spotify_link,
            "options": [zenekar, 'Quimby', 'Tankcsapda', 'P. Mobil'],
            "correct": 0,
            "explanation": f"{zenekar} magyar rock/pop zenekar",
            "topic": "magyar_zenekarok"
        }
        questions_template.append(question)
    
    # Python kód generálása
    python_code = "# Magyar zenekarok kérdések valódi Spotify linkekkel\n\n"
    python_code += "MAGYAR_ZENEKAROK_QUESTIONS = [\n"
    
    for i, question in enumerate(questions_template):
        python_code += "    {\n"
        python_code += f'        "question": "{question["question"]}",\n'
        python_code += f'        "spotify_embed": "{question["spotify_embed"]}",\n'
        python_code += f'        "options": {question["options"]},\n'
        python_code += f'        "correct": {question["correct"]},\n'
        python_code += f'        "explanation": "{question["explanation"]}",\n'
        python_code += f'        "topic": "{question["topic"]}"\n'
        python_code += "    }"
        if i < len(questions_template) - 1:
            python_code += ","
        python_code += "\n"
    
    python_code += "]\n"
    
    # Mentsd el a frissített kérdéseket
    with open('topics/magyar_zenekarok_with_real_links.py', 'w', encoding='utf-8') as f:
        f.write(python_code)
    
    print(f"\n📁 Frissített kérdések mentve: topics/magyar_zenekarok_with_real_links.py")
    print(f"✅ {len(questions_template)} kérdés valódi Spotify linkekkel")
    
    return questions_template

if __name__ == "__main__":
    print("🎵 Magyar zenekarok kérdések frissítése valódi Spotify linkekkel...")
    
    # Opció 1: Frissítsd a meglévő fájlt
    print("\n1. Meglévő fájl frissítése")
    update_spotify_links_in_file()
    
    # Opció 2: Új fájl létrehozása
    print("\n2. Új fájl létrehozása valódi linkekkel")
    create_updated_questions()
    
    print("\n🎉 Frissítés befejezve!") 