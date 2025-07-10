# Könnyűzene Spotify linkek javítása
# Frissíti a konnyuzene.py fájlt valódi Spotify linkekkel

from topics.konnyuzene_spotify import SPOTIFY_LINKS
from topics.konnyuzene import POP_MUSIC_QUESTIONS

def fix_konnyuzene_spotify_links():
    """
    Frissíti a könnyűzene kérdéseket valódi Spotify linkekkel
    """
    updated_questions = []
    
    for question in POP_MUSIC_QUESTIONS:
        # Keresés a helyes válasz alapján
        correct_answer = question['options'][question['correct']]
        
        # Spotify link keresése
        spotify_link = SPOTIFY_LINKS.get(correct_answer, "https://open.spotify.com/embed/playlist/37i9dQZF1DX5Vy6DFOcx00")
        
        # Ha artist link van, átalakítjuk embed linkké
        if "/artist/" in spotify_link:
            # Artist linket playlist linkké alakítjuk
            spotify_link = "https://open.spotify.com/embed/artist/" + spotify_link.split("/artist/")[1]
        
        # Kérdés frissítése
        updated_question = question.copy()
        updated_question['spotify_embed'] = spotify_link
        
        updated_questions.append(updated_question)
    
    return updated_questions

def save_fixed_questions(questions):
    """
    Elmenti a javított kérdéseket
    """
    with open('topics/konnyuzene_fixed.py', 'w', encoding='utf-8') as f:
        f.write("# Könnyűzene kérdések a PDF 13. oldala alapján - Javított Spotify linkekkel\n\n")
        f.write("POP_MUSIC_QUESTIONS = [\n")
        
        for question in questions:
            f.write("    {\n")
            f.write(f'        "question": "{question["question"]}",\n')
            f.write(f'        "spotify_embed": "{question["spotify_embed"]}",\n')
            f.write(f'        "options": {question["options"]},\n')
            f.write(f'        "correct": {question["correct"]},\n')
            f.write(f'        "explanation": "{question["explanation"]}",\n')
            f.write(f'        "topic": "{question["topic"]}"\n')
            f.write("    },\n")
        
        f.write("]\n\n")
        f.write(f'# Összesen: {len(questions)} kérdés\n')
        f.write(f'print(f"Könnyűzene kérdések száma: {len(questions)}")\n')

def main():
    """
    Fő függvény
    """
    print("🎵 Könnyűzene Spotify Linkek Javítása")
    print("=" * 40)
    
    # Kérdések frissítése
    updated_questions = fix_konnyuzene_spotify_links()
    
    # Eredmények mentése
    save_fixed_questions(updated_questions)
    
    print(f"✅ Javított kérdések mentve: topics/konnyuzene_fixed.py")
    print(f"📊 Összesen {len(updated_questions)} kérdés frissítve")
    
    # Néhány példa megjelenítése
    print("\n📋 Példák a javított linkekről:")
    for i, question in enumerate(updated_questions[:5]):
        correct_answer = question['options'][question['correct']]
        print(f"{i+1}. {correct_answer}")
        print(f"   Link: {question['spotify_embed']}")
        print()

if __name__ == "__main__":
    main() 