#!/usr/bin/env python3
"""
Zenei kérdések formátumának javítása
A kérdés legyen "Ki az előadó?" és az előadó neve ne szerepeljen a kérdésben
Eltávolítjuk a "Hallgasd meg a zeneművet:" szöveget is
"""

import re

def fix_magyar_zenekarok_questions():
    """Magyar zenekarok kérdések javítása"""
    
    with open('topics/magyar_zenekarok.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex pattern a kérdések kereséséhez
    pattern = r'"question":\s*"([^"]*)"'
    
    def replace_question(match):
        question_text = match.group(1)
        
        # Ha a kérdés tartalmazza az előadó nevét vagy a "Hallgasd meg" szöveget, cseréljük le
        if "tagja volt" in question_text or "Hallgasd meg" in question_text:
            # Kivonjuk az előadó nevét a kérdésből
            # Példa: "Melyik magyar alternatív zenekar tagja volt Hiperkarma?" -> "Ki az előadó?"
            return '"question": "Ki az előadó?"'
        
        return match.group(0)
    
    # Cseréljük le a kérdéseket
    updated_content = re.sub(pattern, replace_question, content)
    
    # Mentsük el a frissített fájlt
    with open('topics/magyar_zenekarok.py', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("✅ Magyar zenekarok kérdések javítva!")

def fix_nemzetkozi_zenekarok_questions():
    """Nemzetközi zenekarok kérdések javítása"""
    
    with open('topics/nemzetkozi_zenekarok.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex pattern a kérdések kereséséhez
    pattern = r'"question":\s*"([^"]*)"'
    
    def replace_question(match):
        question_text = match.group(1)
        
        # Ha a kérdés tartalmazza az előadó nevét vagy a "Hallgasd meg" szöveget, cseréljük le
        if "tagja volt" in question_text or "előadó" in question_text or "Hallgasd meg" in question_text:
            # Kivonjuk az előadó nevét a kérdésből
            return '"question": "Ki az előadó?"'
        
        return match.group(0)
    
    # Cseréljük le a kérdéseket
    updated_content = re.sub(pattern, replace_question, content)
    
    # Mentsük el a frissített fájlt
    with open('topics/nemzetkozi_zenekarok.py', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("✅ Nemzetközi zenekarok kérdések javítva!")

def fix_konnyuzene_questions():
    """Könnyűzene kérdések javítása"""
    
    with open('topics/konnyuzene.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex pattern a kérdések kereséséhez
    pattern = r'"question":\s*"([^"]*)"'
    
    def replace_question(match):
        question_text = match.group(1)
        
        # Ha a kérdés tartalmazza az előadó nevét vagy a "Hallgasd meg" szöveget, cseréljük le
        if "tagja volt" in question_text or "előadó" in question_text or "Hallgasd meg" in question_text:
            # Kivonjuk az előadó nevét a kérdésből
            return '"question": "Ki az előadó?"'
        
        return match.group(0)
    
    # Cseréljük le a kérdéseket
    updated_content = re.sub(pattern, replace_question, content)
    
    # Mentsük el a frissített fájlt
    with open('topics/konnyuzene.py', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("✅ Könnyűzene kérdések javítva!")

def fix_classical_music_questions():
    """Klasszikus zene kérdések javítása"""
    
    with open('classical_music_questions_tschaikovsky_updated.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex pattern a kérdések kereséséhez
    pattern = r'"question":\s*"([^"]*)"'
    
    def replace_question(match):
        question_text = match.group(1)
        
        # Ha a kérdés tartalmazza a zeneszerző nevét vagy a "Hallgasd meg" szöveget, cseréljük le
        if "zeneszerző" in question_text or "composer" in question_text.lower() or "Hallgasd meg" in question_text:
            # Kivonjuk a zeneszerző nevét a kérdésből
            return '"question": "Ki a zeneszerző?"'
        
        return match.group(0)
    
    # Cseréljük le a kérdéseket
    updated_content = re.sub(pattern, replace_question, content)
    
    # Mentsük el a frissített fájlt
    with open('classical_music_questions_tschaikovsky_updated.py', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("✅ Klasszikus zene kérdések javítva!")

if __name__ == "__main__":
    print("🎵 Zenei kérdések formátumának javítása...")
    
    try:
        fix_magyar_zenekarok_questions()
    except FileNotFoundError:
        print("⚠️  Magyar zenekarok fájl nem található")
    
    try:
        fix_nemzetkozi_zenekarok_questions()
    except FileNotFoundError:
        print("⚠️  Nemzetközi zenekarok fájl nem található")
    
    try:
        fix_konnyuzene_questions()
    except FileNotFoundError:
        print("⚠️  Könnyűzene fájl nem található")
    
    try:
        fix_classical_music_questions()
    except FileNotFoundError:
        print("⚠️  Klasszikus zene fájl nem található")
    
    print("🎉 Zenei kérdések formátuma javítva!") 