#!/usr/bin/env python3
"""
Heaven Street Seven keresése Spotify-on
"""

from spotify_api_config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET
import requests
import base64

def get_spotify_access_token():
    """Spotify access token beszerzése"""
    auth_url = "https://accounts.spotify.com/api/token"
    auth_header = base64.b64encode(f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}".encode()).decode()
    
    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    data = {"grant_type": "client_credentials"}
    
    try:
        response = requests.post(auth_url, headers=headers, data=data)
        response.raise_for_status()
        token_data = response.json()
        return token_data["access_token"]
    except Exception as e:
        print(f"❌ Hiba az access token beszerzésekor: {e}")
        return None

def search_heaven_street_seven():
    """Heaven Street Seven keresése"""
    
    access_token = get_spotify_access_token()
    if not access_token:
        print("❌ Nem sikerült access token-t beszerezni")
        return None
    
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    # Különböző keresési variációk
    search_queries = [
        "Heaven Street Seven",
        "Heaven Street Seven magyar",
        "Heaven Street Seven hungary",
        "Heaven Street Seven budapest"
    ]
    
    for query in search_queries:
        print(f"🔍 Keresés: {query}")
        
        params = {
            "q": query,
            "type": "artist",
            "market": "HU",
            "limit": 5
        }
        
        try:
            response = requests.get("https://api.spotify.com/v1/search", headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            
            if data["artists"]["items"]:
                print(f"✅ Találatok a '{query}' keresésre:")
                for i, artist in enumerate(data["artists"]["items"][:3]):
                    print(f"  {i+1}. {artist['name']} (Popularity: {artist['popularity']})")
                    print(f"     ID: {artist['id']}")
                    print(f"     URL: https://open.spotify.com/artist/{artist['id']}")
                    print(f"     Embed: https://open.spotify.com/embed/artist/{artist['id']}")
                    print()
                
                # Ha találtunk Heaven Street Seven-t, adjuk vissza
                for artist in data["artists"]["items"]:
                    if "heaven street seven" in artist['name'].lower():
                        return {
                            "name": artist['name'],
                            "id": artist['id'],
                            "popularity": artist['popularity'],
                            "url": f"https://open.spotify.com/artist/{artist['id']}",
                            "embed_url": f"https://open.spotify.com/embed/artist/{artist['id']}"
                        }
            else:
                print(f"❌ Nincs találat a '{query}' keresésre")
                
        except Exception as e:
            print(f"❌ Hiba a keresés során: {e}")
    
    return None

def update_magyar_zenekarok_with_new_link():
    """Frissíti a magyar zenekarok fájlt az új Heaven Street Seven linkkel"""
    
    # Keresd meg a Heaven Street Seven-t
    heaven_street_seven = search_heaven_street_seven()
    
    if not heaven_street_seven:
        print("❌ Nem találtam Heaven Street Seven-t Spotify-on")
        return
    
    print(f"✅ Heaven Street Seven találva: {heaven_street_seven['name']}")
    print(f"🔗 Embed URL: {heaven_street_seven['embed_url']}")
    
    # Olvasd be a fájlt
    with open('topics/magyar_zenekarok.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Cseréld le a régi HS7 linket az új Heaven Street Seven linkre
    old_link = "https://open.spotify.com/embed/artist/0iVQlLqQwkK3VUvUMp3EIq"
    new_link = heaven_street_seven['embed_url']
    
    updated_content = content.replace(old_link, new_link)
    
    # Mentsd el a frissített fájlt
    with open('topics/magyar_zenekarok.py', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"✅ Magyar zenekarok fájl frissítve az új Heaven Street Seven linkkel!")
    print(f"🔄 Régi link: {old_link}")
    print(f"🆕 Új link: {new_link}")

if __name__ == "__main__":
    print("🎵 Heaven Street Seven keresése Spotify-on...")
    update_magyar_zenekarok_with_new_link()
    print("🎉 Keresés befejezve!") 