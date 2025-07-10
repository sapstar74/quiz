#!/usr/bin/env python3
"""
Szintaktikai hibák javítása a quiz fájlokban
"""

import re

def fix_foldrajz_syntax():
    """Földrajz fájl szintaktikai hibáinak javítása"""
    
    with open('topics/foldrajz.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Javítsuk ki a hibás formátumot
    # "explanation":\n        "topic": "földrajz", "szöveg" -> "explanation": "szöveg",\n        "topic": "földrajz"
    pattern = r'"explanation":\s*\n\s*"topic": "földrajz",\s*"([^"]+)"'
    
    def fix_explanation(match):
        explanation_text = match.group(1)
        return f'"explanation": "{explanation_text}",\n        "topic": "földrajz"'
    
    updated_content = re.sub(pattern, fix_explanation, content)
    
    # Mentsük el a javított fájlt
    with open('topics/foldrajz.py', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("✅ Földrajz szintaktikai hibák javítva!")

def fix_komolyzene_syntax():
    """Komolyzene fájl szintaktikai hibáinak javítása"""
    
    with open('classical_music_questions_tschaikovsky_updated.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Javítsuk ki a hibás formátumot
    pattern = r'"spotify_found_artist":\s*\n\s*"topic": "komolyzene",\s*([^,]+)'
    
    def fix_spotify_field(match):
        spotify_value = match.group(1)
        return f'"spotify_found_artist": {spotify_value},\n        "topic": "komolyzene"'
    
    updated_content = re.sub(pattern, fix_spotify_field, content)
    
    # Mentsük el a javított fájlt
    with open('classical_music_questions_tschaikovsky_updated.py', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("✅ Komolyzene szintaktikai hibák javítva!")

def fix_other_files_syntax():
    """Többi fájl szintaktikai hibáinak javítása"""
    
    files_to_fix = [
        ('topics/haboru_all_questions.py', 'háborúk'),
        ('topics/kiralyok.py', 'magyar_királyok'),
        ('topics/tudosok.py', 'tudósok'),
        ('topics/mitologia_all_questions.py', 'mitológia'),
        ('topics/allatok_balanced.py', 'állatok'),
        ('topics/dramak.py', 'drámák'),
        ('topics/sport_logok.py', 'sport_logók'),
        ('topics/zaszlok_all_questions.py', 'zászlók')
    ]
    
    for file_path, topic_name in files_to_fix:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Javítsuk ki a hibás formátumot
            pattern = r'"explanation":\s*\n\s*"topic": "' + re.escape(topic_name) + r'",\s*"([^"]+)"'
            
            def fix_explanation(match):
                explanation_text = match.group(1)
                return f'"explanation": "{explanation_text}",\n        "topic": "{topic_name}"'
            
            updated_content = re.sub(pattern, fix_explanation, content)
            
            # Mentsük el a javított fájlt
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            print(f"✅ {file_path} szintaktikai hibák javítva!")
            
        except FileNotFoundError:
            print(f"⚠️  {file_path} nem található")

if __name__ == "__main__":
    print("🔧 Szintaktikai hibák javítása...")
    
    fix_foldrajz_syntax()
    fix_komolyzene_syntax()
    fix_other_files_syntax()
    
    print("🎉 Szintaktikai hibák javítva!") 