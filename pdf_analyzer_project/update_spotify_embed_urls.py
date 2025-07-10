#!/usr/bin/env python3
"""
Spotify embed URL-ek frissítése minimalista lejátszóhoz
"""

import json
from classical_music_questions_with_spotify import CLASSICAL_MUSIC_QUESTIONS

def update_spotify_embed_urls():
    """Frissíti a Spotify embed URL-eket minimalista lejátszóhoz"""
    
    updated_questions = []
    
    for question in CLASSICAL_MUSIC_QUESTIONS:
        updated_question = question.copy()
        
        if question.get('spotify_embed'):
            # Alap URL megszerzése
            base_url = question['spotify_embed']
            
            # Paraméterek hozzáadása a minimalista lejátszóhoz
            # theme=black: fekete téma
            # size=small: kis méret
            # hide_cover: borító elrejtése
            # hide_artist: előadó elrejtése
            # hide_title: cím elrejtése
            minimal_url = f"{base_url}?theme=black&size=small&hide_cover=1&hide_artist=1&hide_title=1"
            
            updated_question['spotify_embed'] = minimal_url
        
        updated_questions.append(updated_question)
    
    return updated_questions

def save_minimal_spotify_questions(questions):
    """Menti a minimalista Spotify lejátszós kérdéseket"""
    
    python_code = """#!/usr/bin/env python3
\"\"\"
Komolyzenei kérdések minimalista Spotify lejátszóval
\"\"\"

CLASSICAL_MUSIC_QUESTIONS = [
"""
    
    for question in questions:
        python_code += f"""    {{
        'question': '{question['question']}',
        'options': {question['options']},
        'correct': {question['correct']},
        'explanation': '{question['explanation']}',
        'spotify_embed': {repr(question['spotify_embed'])},
        'spotify_confidence': '{question['spotify_confidence']}',
        'spotify_found_track': {repr(question['spotify_found_track'])},
        'spotify_found_artist': {repr(question['spotify_found_artist'])}
    }},
"""
    
    python_code += """]

if __name__ == "__main__":
    print(f"Komolyzenei kérdések száma: {len(CLASSICAL_MUSIC_QUESTIONS)}")
    print("Minimalista Spotify lejátszóval:")
    for i, q in enumerate(CLASSICAL_MUSIC_QUESTIONS):
        if q['spotify_embed']:
            print(f"{i+1}. {q['explanation']} - {q['spotify_confidence']} confidence")
"""
    
    with open('classical_music_questions_minimal_spotify.py', 'w', encoding='utf-8') as f:
        f.write(python_code)
    
    print(f"✅ Minimalista Spotify lejátszós kérdések mentve: classical_music_questions_minimal_spotify.py")

def main():
    """Fő függvény"""
    print("🎵 Spotify Embed URL-ek frissítése minimalista lejátszóhoz")
    print("=" * 60)
    
    # Kérdések frissítése
    updated_questions = update_spotify_embed_urls()
    
    # Statisztikák
    with_spotify = len([q for q in updated_questions if q['spotify_embed']])
    
    print(f"Összes kérdés: {len(updated_questions)}")
    print(f"Minimalista Spotify lejátszóval: {with_spotify}")
    
    # Példa URL
    if updated_questions and updated_questions[0]['spotify_embed']:
        print(f"\nPélda minimalista URL:")
        print(f"Eredeti: {CLASSICAL_MUSIC_QUESTIONS[0]['spotify_embed']}")
        print(f"Minimalista: {updated_questions[0]['spotify_embed']}")
    
    # Fájl mentése
    save_minimal_spotify_questions(updated_questions)
    
    return updated_questions

if __name__ == "__main__":
    main() 