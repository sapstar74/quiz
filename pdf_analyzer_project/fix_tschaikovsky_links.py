#!/usr/bin/env python3
"""
Script Csajkovszkij linkek javításához "Tschaikovsky" névvel
"""

import requests
import json
import time

# Spotify API credentials
CLIENT_ID = "b288da1cbde34062aba6724de8531c46"
CLIENT_SECRET = "bd3b3835e63744149f580ebb919cbdd3"

def get_spotify_token():
    """Get Spotify access token"""
    auth_url = "https://accounts.spotify.com/api/token"
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })
    auth_response_data = auth_response.json()
    return auth_response_data['access_token']

def search_tschaikovsky_tracks():
    """Search for Tschaikovsky tracks with correct spelling"""
    token = get_spotify_token()
    headers = {
        'Authorization': f'Bearer {token}'
    }
    
    # Csajkovszkij művek a helyes névvel
    tschaikovsky_pieces = [
        "Tschaikovsky Nutcracker Dance of the Sugar Plum Fairy",
        "Tschaikovsky Nutcracker Waltz of the Flowers",
        "Tschaikovsky Nutcracker March",
        "Tschaikovsky Swan Lake Dance of the Little Swans",
        "Tschaikovsky Piano Concerto No 1",
        "Tschaikovsky Romeo and Juliet Love Theme",
        "Tschaikovsky Symphony No 5",
        "Tschaikovsky Symphony No 6 Pathetique",
        "Tschaikovsky 1812 Overture",
        "Tschaikovsky Sleeping Beauty Waltz"
    ]
    
    results = {}
    
    for piece in tschaikovsky_pieces:
        print(f"🔍 Keresem: {piece}")
        search_url = f"https://api.spotify.com/v1/search?q={piece}&type=track&limit=3"
        response = requests.get(search_url, headers=headers)
        data = response.json()
        
        if data['tracks']['items']:
            track = data['tracks']['items'][0]
            results[piece] = {
                'name': track['name'],
                'artist': track['artists'][0]['name'],
                'id': track['id'],
                'url': f"https://open.spotify.com/embed/track/{track['id']}?theme=black&size=small&hide_cover=1&hide_artist=1&hide_title=1"
            }
            print(f"✅ Találtam: {track['name']} - {track['artists'][0]['name']}")
        else:
            print(f"❌ Nem találtam: {piece}")
        
        time.sleep(0.5)  # Rate limiting
    
    return results

def update_classical_music_questions():
    """Update the classical music questions with new Tschaikovsky links"""
    results = search_tschaikovsky_tracks()
    
    # Create updated questions
    updated_questions = []
    
    # Add Tschaikovsky questions with new links
    tschaikovsky_questions = [
        {
            'question': 'Hallgasd meg ezt a zeneművet és válaszd ki a zeneszerzőjét:',
            'options': ['Beethoven', 'Mozart', 'Csajkovszkij', 'Bach'],
            'correct': 2,
            'explanation': 'Csajkovszkij: Diótörő - Tánc a cukorkák hercegnőjéről',
            'spotify_embed': results.get("Tschaikovsky Nutcracker Dance of the Sugar Plum Fairy", {}).get('url', ''),
            'spotify_confidence': 'high',
            'spotify_found_track': results.get("Tschaikovsky Nutcracker Dance of the Sugar Plum Fairy", {}).get('name', ''),
            'spotify_found_artist': results.get("Tschaikovsky Nutcracker Dance of the Sugar Plum Fairy", {}).get('artist', '')
        },
        {
            'question': 'Hallgasd meg ezt a zeneművet és válaszd ki a zeneszerzőjét:',
            'options': ['Beethoven', 'Mozart', 'Csajkovszkij', 'Bach'],
            'correct': 2,
            'explanation': 'Csajkovszkij: Hattyúk tava - Tánc a kis hattyúkról',
            'spotify_embed': results.get("Tschaikovsky Swan Lake Dance of the Little Swans", {}).get('url', ''),
            'spotify_confidence': 'high',
            'spotify_found_track': results.get("Tschaikovsky Swan Lake Dance of the Little Swans", {}).get('name', ''),
            'spotify_found_artist': results.get("Tschaikovsky Swan Lake Dance of the Little Swans", {}).get('artist', '')
        },
        {
            'question': 'Hallgasd meg ezt a zeneművet és válaszd ki a zeneszerzőjét:',
            'options': ['Beethoven', 'Mozart', 'Csajkovszkij', 'Bach'],
            'correct': 2,
            'explanation': 'Csajkovszkij: 1. Zongoraverseny',
            'spotify_embed': results.get("Tschaikovsky Piano Concerto No 1", {}).get('url', ''),
            'spotify_confidence': 'high',
            'spotify_found_track': results.get("Tschaikovsky Piano Concerto No 1", {}).get('name', ''),
            'spotify_found_artist': results.get("Tschaikovsky Piano Concerto No 1", {}).get('artist', '')
        },
        {
            'question': 'Hallgasd meg ezt a zeneművet és válaszd ki a zeneszerzőjét:',
            'options': ['Beethoven', 'Mozart', 'Csajkovszkij', 'Bach'],
            'correct': 2,
            'explanation': 'Csajkovszkij: Rómeó és Júlia - Love Theme',
            'spotify_embed': results.get("Tschaikovsky Romeo and Juliet Love Theme", {}).get('url', ''),
            'spotify_confidence': 'high',
            'spotify_found_track': results.get("Tschaikovsky Romeo and Juliet Love Theme", {}).get('name', ''),
            'spotify_found_artist': results.get("Tschaikovsky Romeo and Juliet Love Theme", {}).get('artist', '')
        }
    ]
    
    updated_questions.extend(tschaikovsky_questions)
    
    # Save results
    with open('tschaikovsky_search_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    # Save updated questions
    with open('classical_music_questions_tschaikovsky_fixed.py', 'w', encoding='utf-8') as f:
        f.write("#!/usr/bin/env python3\n")
        f.write('"""\n')
        f.write('Classical music questions with corrected Tschaikovsky links\n')
        f.write('"""\n\n')
        f.write('CLASSICAL_MUSIC_QUESTIONS = [\n')
        
        for question in updated_questions:
            f.write('    {\n')
            f.write(f"        'question': '{question['question']}',\n")
            f.write(f"        'options': {question['options']},\n")
            f.write(f"        'correct': {question['correct']},\n")
            f.write(f"        'explanation': '{question['explanation']}',\n")
            f.write(f"        'spotify_embed': '{question['spotify_embed']}',\n")
            f.write(f"        'spotify_confidence': '{question['spotify_confidence']}',\n")
            f.write(f"        'spotify_found_track': '{question['spotify_found_track']}',\n")
            f.write(f"        'spotify_found_artist': '{question['spotify_found_artist']}'\n")
            f.write('    },\n')
        
        f.write(']\n')
    
    print(f"\n✅ Mentettem {len(results)} Tschaikovsky linket")
    print("📁 Fájlok:")
    print("- tschaikovsky_search_results.json")
    print("- classical_music_questions_tschaikovsky_fixed.py")

if __name__ == "__main__":
    print("🎵 Csajkovszkij linkek javítása 'Tschaikovsky' névvel...")
    update_classical_music_questions() 