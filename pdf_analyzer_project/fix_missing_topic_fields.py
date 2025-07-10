#!/usr/bin/env python3
"""
Hiányzó topic mezők hozzáadása a quiz kérdésekhez
"""

def fix_foldrajz_questions():
    """Földrajz kérdések javítása"""
    
    with open('topics/foldrajz.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Hozzáadjuk a topic mezőt minden kérdéshez
    updated_content = content.replace(
        '"explanation":',
        '"explanation":\n        "topic": "földrajz",'
    )
    
    # Mentsük el a frissített fájlt
    with open('topics/foldrajz.py', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("✅ Földrajz kérdések javítva!")

def fix_komolyzene_questions():
    """Komolyzene kérdések javítása"""
    
    with open('classical_music_questions_tschaikovsky_updated.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Hozzáadjuk a topic mezőt minden kérdéshez
    updated_content = content.replace(
        '"spotify_found_artist":',
        '"spotify_found_artist":\n        "topic": "komolyzene",'
    )
    
    # Mentsük el a frissített fájlt
    with open('classical_music_questions_tschaikovsky_updated.py', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("✅ Komolyzene kérdések javítva!")

def fix_haboru_questions():
    """Háborúk kérdések javítása"""
    
    with open('topics/haboru_all_questions.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Hozzáadjuk a topic mezőt minden kérdéshez
    updated_content = content.replace(
        '"explanation":',
        '"explanation":\n        "topic": "háborúk",'
    )
    
    # Mentsük el a frissített fájlt
    with open('topics/haboru_all_questions.py', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("✅ Háborúk kérdések javítva!")

def fix_kiralyok_questions():
    """Királyok kérdések javítása"""
    
    with open('topics/kiralyok.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Hozzáadjuk a topic mezőt minden kérdéshez
    updated_content = content.replace(
        '"explanation":',
        '"explanation":\n        "topic": "magyar_királyok",'
    )
    
    # Mentsük el a frissített fájlt
    with open('topics/kiralyok.py', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("✅ Királyok kérdések javítva!")

def fix_tudosok_questions():
    """Tudósok kérdések javítása"""
    
    with open('topics/tudosok.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Hozzáadjuk a topic mezőt minden kérdéshez
    updated_content = content.replace(
        '"explanation":',
        '"explanation":\n        "topic": "tudósok",'
    )
    
    # Mentsük el a frissített fájlt
    with open('topics/tudosok.py', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("✅ Tudósok kérdések javítva!")

def fix_mitologia_questions():
    """Mitológia kérdések javítása"""
    
    with open('topics/mitologia_all_questions.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Hozzáadjuk a topic mezőt minden kérdéshez
    updated_content = content.replace(
        '"explanation":',
        '"explanation":\n        "topic": "mitológia",'
    )
    
    # Mentsük el a frissített fájlt
    with open('topics/mitologia_all_questions.py', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("✅ Mitológia kérdések javítva!")

def fix_allatok_questions():
    """Állatok kérdések javítása"""
    
    with open('topics/allatok_balanced.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Hozzáadjuk a topic mezőt minden kérdéshez
    updated_content = content.replace(
        '"explanation":',
        '"explanation":\n        "topic": "állatok",'
    )
    
    # Mentsük el a frissített fájlt
    with open('topics/allatok_balanced.py', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("✅ Állatok kérdések javítva!")

def fix_dramak_questions():
    """Drámák kérdések javítása"""
    
    with open('topics/dramak.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Hozzáadjuk a topic mezőt minden kérdéshez
    updated_content = content.replace(
        '"explanation":',
        '"explanation":\n        "topic": "drámák",'
    )
    
    # Mentsük el a frissített fájlt
    with open('topics/dramak.py', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("✅ Drámák kérdések javítva!")

def fix_sport_logok_questions():
    """Sport logók kérdések javítása"""
    
    with open('topics/sport_logok.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Hozzáadjuk a topic mezőt minden kérdéshez
    updated_content = content.replace(
        '"explanation":',
        '"explanation":\n        "topic": "sport_logók",'
    )
    
    # Mentsük el a frissített fájlt
    with open('topics/sport_logok.py', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("✅ Sport logók kérdések javítva!")

def fix_zaszlok_questions():
    """Zászlók kérdések javítása"""
    
    with open('topics/zaszlok_all_questions.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Hozzáadjuk a topic mezőt minden kérdéshez
    updated_content = content.replace(
        '"explanation":',
        '"explanation":\n        "topic": "zászlók",'
    )
    
    # Mentsük el a frissített fájlt
    with open('topics/zaszlok_all_questions.py', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("✅ Zászlók kérdések javítva!")

if __name__ == "__main__":
    print("🔧 Hiányzó topic mezők hozzáadása...")
    
    try:
        fix_foldrajz_questions()
    except FileNotFoundError:
        print("⚠️  Földrajz fájl nem található")
    
    try:
        fix_komolyzene_questions()
    except FileNotFoundError:
        print("⚠️  Komolyzene fájl nem található")
    
    try:
        fix_haboru_questions()
    except FileNotFoundError:
        print("⚠️  Háborúk fájl nem található")
    
    try:
        fix_kiralyok_questions()
    except FileNotFoundError:
        print("⚠️  Királyok fájl nem található")
    
    try:
        fix_tudosok_questions()
    except FileNotFoundError:
        print("⚠️  Tudósok fájl nem található")
    
    try:
        fix_mitologia_questions()
    except FileNotFoundError:
        print("⚠️  Mitológia fájl nem található")
    
    try:
        fix_allatok_questions()
    except FileNotFoundError:
        print("⚠️  Állatok fájl nem található")
    
    try:
        fix_dramak_questions()
    except FileNotFoundError:
        print("⚠️  Drámák fájl nem található")
    
    try:
        fix_sport_logok_questions()
    except FileNotFoundError:
        print("⚠️  Sport logók fájl nem található")
    
    try:
        fix_zaszlok_questions()
    except FileNotFoundError:
        print("⚠️  Zászlók fájl nem található")
    
    print("🎉 Topic mezők hozzáadva!") 