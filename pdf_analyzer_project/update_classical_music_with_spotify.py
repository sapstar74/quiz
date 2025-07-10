#!/usr/bin/env python3
"""
Spotify linkek beépítése a komolyzenei kérdésekbe
"""

import json
from classical_music_questions import CLASSICAL_MUSIC_QUESTIONS

def load_spotify_results():
    """Betölti a Spotify keresési eredményeket"""
    with open('spotify_search_results_final.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def update_classical_music_questions():
    """Frissíti a komolyzenei kérdéseket Spotify linkekkel"""
    
    # Spotify eredmények betöltése
    spotify_results = load_spotify_results()
    
    # Eredmények indexelése question_index alapján
    spotify_dict = {}
    for result in spotify_results:
        spotify_dict[result['question_index']] = result
    
    # Kérdések frissítése
    updated_questions = []
    
    for i, question in enumerate(CLASSICAL_MUSIC_QUESTIONS):
        if i in spotify_dict:
            spotify_data = spotify_dict[i]
            
            # Spotify embed link hozzáadása
            updated_question = question.copy()
            updated_question['spotify_embed'] = spotify_data['spotify_embed']
            updated_question['spotify_confidence'] = spotify_data['confidence']
            updated_question['spotify_found_track'] = spotify_data['found_track']
            updated_question['spotify_found_artist'] = spotify_data['found_artist']
            
            updated_questions.append(updated_question)
        else:
            # Ha nincs Spotify találat, akkor is hozzáadjuk
            updated_question = question.copy()
            updated_question['spotify_embed'] = None
            updated_question['spotify_confidence'] = 'none'
            updated_question['spotify_found_track'] = None
            updated_question['spotify_found_artist'] = None
            
            updated_questions.append(updated_question)
    
    return updated_questions

def save_updated_questions(questions):
    """Menti a frissített kérdéseket"""
    
    # Python kód generálása
    python_code = """#!/usr/bin/env python3
\"\"\"
Komolyzenei kérdések Spotify linkekkel
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
    print("Spotify linkekkel rendelkező kérdések:")
    for i, q in enumerate(CLASSICAL_MUSIC_QUESTIONS):
        if q['spotify_embed']:
            print(f"{i+1}. {q['explanation']} - {q['spotify_confidence']} confidence")
"""
    
    # Fájl mentése
    with open('classical_music_questions_with_spotify.py', 'w', encoding='utf-8') as f:
        f.write(python_code)
    
    print(f"✅ Frissített kérdések mentve: classical_music_questions_with_spotify.py")

def main():
    """Fő függvény"""
    print("🎵 Spotify linkek beépítése a komolyzenei kérdésekbe")
    print("=" * 50)
    
    # Kérdések frissítése
    updated_questions = update_classical_music_questions()
    
    # Statisztikák
    with_spotify = len([q for q in updated_questions if q['spotify_embed']])
    high_confidence = len([q for q in updated_questions if q['spotify_confidence'] == 'high'])
    medium_confidence = len([q for q in updated_questions if q['spotify_confidence'] == 'medium'])
    
    print(f"Összes kérdés: {len(updated_questions)}")
    print(f"Spotify linkkel: {with_spotify}")
    print(f"Magas bizonyosság: {high_confidence}")
    print(f"Közepes bizonyosság: {medium_confidence}")
    
    # Fájl mentése
    save_updated_questions(updated_questions)
    
    return updated_questions

if __name__ == "__main__":
    main() 