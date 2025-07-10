#!/usr/bin/env python3
"""
Script az összes Csajkovszkij link frissítéséhez a javított fájlban
"""

import json

# Betöltjük az új Tschaikovsky linkeket
with open('tschaikovsky_search_results.json', 'r', encoding='utf-8') as f:
    tschaikovsky_links = json.load(f)

# Betöltjük a jelenlegi kérdéseket
with open('classical_music_questions_fixed.py', 'r', encoding='utf-8') as f:
    current_content = f.read()

# Új Tschaikovsky linkek
new_links = {
    "Diótörő - Tánc a cukorkák hercegnőjéről": tschaikovsky_links["Tschaikovsky Nutcracker Dance of the Sugar Plum Fairy"]["url"],
    "Hattyúk tava - Tánc a kis hattyúkról": tschaikovsky_links["Tschaikovsky Swan Lake Dance of the Little Swans"]["url"],
    "1. Zongoraverseny": tschaikovsky_links["Tschaikovsky Piano Concerto No 1"]["url"],
    "Rómeó és Júlia - Love Theme": tschaikovsky_links["Tschaikovsky Romeo and Juliet Love Theme"]["url"]
}

# Új track információk
new_track_info = {
    "Diótörő - Tánc a cukorkák hercegnőjéről": {
        "track": tschaikovsky_links["Tschaikovsky Nutcracker Dance of the Sugar Plum Fairy"]["name"],
        "artist": tschaikovsky_links["Tschaikovsky Nutcracker Dance of the Sugar Plum Fairy"]["artist"]
    },
    "Hattyúk tava - Tánc a kis hattyúkról": {
        "track": tschaikovsky_links["Tschaikovsky Swan Lake Dance of the Little Swans"]["name"],
        "artist": tschaikovsky_links["Tschaikovsky Swan Lake Dance of the Little Swans"]["artist"]
    },
    "1. Zongoraverseny": {
        "track": tschaikovsky_links["Tschaikovsky Piano Concerto No 1"]["name"],
        "artist": tschaikovsky_links["Tschaikovsky Piano Concerto No 1"]["artist"]
    },
    "Rómeó és Júlia - Love Theme": {
        "track": tschaikovsky_links["Tschaikovsky Romeo and Juliet Love Theme"]["name"],
        "artist": tschaikovsky_links["Tschaikovsky Romeo and Juliet Love Theme"]["artist"]
    }
}

# Frissítjük a linkeket
updated_content = current_content

for explanation, new_url in new_links.items():
    # Keresünk egy sort, ami tartalmazza az explanation-t
    lines = updated_content.split('\n')
    for i, line in enumerate(lines):
        if f"'explanation': '{explanation}'" in line:
            # Frissítjük a spotify_embed sort
            for j in range(i, min(i+10, len(lines))):
                if "'spotify_embed':" in lines[j]:
                    lines[j] = f"        'spotify_embed': '{new_url}',"
                    break
            
            # Frissítjük a track információkat
            for j in range(i, min(i+15, len(lines))):
                if "'spotify_found_track':" in lines[j]:
                    lines[j] = f"        'spotify_found_track': '{new_track_info[explanation]['track']}',"
                    break
                elif "'spotify_found_artist':" in lines[j]:
                    lines[j] = f"        'spotify_found_artist': '{new_track_info[explanation]['artist']}'"
                    break
    
    updated_content = '\n'.join(lines)

# Mentjük a frissített fájlt
with open('classical_music_questions_tschaikovsky_updated.py', 'w', encoding='utf-8') as f:
    f.write(updated_content)

print("✅ Frissítettem az összes Csajkovszkij linket!")
print("📁 Új fájl: classical_music_questions_tschaikovsky_updated.py")

# Ellenőrizzük a változásokat
print("\n🔄 Változások:")
for explanation, new_url in new_links.items():
    print(f"- {explanation}: {new_url}") 