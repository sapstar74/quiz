#!/usr/bin/env python3
"""
Magyar zenekarok Spotify linkjeinek keresése
"""

import requests
import json
import time
import re
from urllib.parse import quote

def search_spotify_artist(artist_name):
    """Spotify API keresés magyar zenekarokra"""
    
    # Magyar zenekarok specifikus keresési feltételek
    search_terms = [
        f"{artist_name} magyar",
        f"{artist_name} hungary",
        f"{artist_name} budapest",
        f"{artist_name} magyarország",
        artist_name
    ]
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    for search_term in search_terms:
        try:
            # Spotify web search
            encoded_term = quote(search_term)
            url = f"https://open.spotify.com/search/{encoded_term}/artists"
            
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                # Extract artist ID from response
                content = response.text
                
                # Look for artist URLs in the page
                artist_patterns = [
                    r'https://open\.spotify\.com/artist/([a-zA-Z0-9]+)',
                    r'/artist/([a-zA-Z0-9]{22})',
                    r'"uri":"spotify:artist:([a-zA-Z0-9]{22})"'
                ]
                
                for pattern in artist_patterns:
                    matches = re.findall(pattern, content)
                    if matches:
                        artist_id = matches[0]
                        return f"https://open.spotify.com/artist/{artist_id}"
            
            time.sleep(1)  # Rate limiting
            
        except Exception as e:
            print(f"❌ Hiba a keresés során ({search_term}): {e}")
            continue
    
    return None

def search_spotify_web_api(artist_name):
    """Spotify Web API keresés"""
    
    # Known Hungarian band mappings
    hungarian_bands = {
        "Hiperkarma": "Hiperkarma",
        "HS7": "HS7",
        "Óriás": "Óriás",
        "Kispál": "Kispál és a Borz",
        "Kiscsillag": "Kiscsillag",
        "Vad Fruttik": "Vad Fruttik",
        "Tereskova": "Tereskova",
        "Anna and the Barbies": "Anna and the Barbies",
        "Honeybeast": "Honeybeast",
        "Konyha": "Konyha",
        "Follow the flow": "Follow the Flow",
        "Elefánt": "Elefánt",
        "4Street": "4Street",
        "Bagossy Brothers": "Bagossy Brothers Company",
        "Csaknekedkislány": "Csaknekedkislány",
        "Lóci játszik": "Lóci játszik",
        "Galaxisok": "Galaxisok",
        "Parno Graszt": "Parno Graszt",
        "Palya Bea": "Bea Palya",
        "Bohemian Betyars": "Bohemian Betyars",
        "Aurevoir": "Aurevoir",
        "Dánielffy": "Dánielffy",
        "Ham Ko Ham": "Ham Ko Ham",
        "Carbonfools": "Carbonfools",
        "Zagar": "Zagar",
        "Neo": "Neo",
        "Soulwave": "Soulwave",
        "Neon": "Neon"
    }
    
    # Try exact name first
    search_name = hungarian_bands.get(artist_name, artist_name)
    
    try:
        # Use Spotify's search endpoint
        encoded_name = quote(search_name)
        url = f"https://open.spotify.com/search/{encoded_name}/artists"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            content = response.text
            
            # Look for artist links
            artist_links = re.findall(r'https://open\.spotify\.com/artist/([a-zA-Z0-9]{22})', content)
            
            if artist_links:
                # Return the first found artist
                return f"https://open.spotify.com/artist/{artist_links[0]}"
        
        # If not found, try with "magyar" suffix
        if "magyar" not in search_name.lower():
            magyar_url = f"https://open.spotify.com/search/{quote(search_name + ' magyar')}/artists"
            response = requests.get(magyar_url, headers=headers, timeout=15)
            
            if response.status_code == 200:
                content = response.text
                artist_links = re.findall(r'https://open\.spotify\.com/artist/([a-zA-Z0-9]{22})', content)
                
                if artist_links:
                    return f"https://open.spotify.com/artist/{artist_links[0]}"
    
    except Exception as e:
        print(f"❌ API hiba ({artist_name}): {e}")
    
    return None

def main():
    print("🎵 Magyar zenekarok Spotify linkjeinek keresése...")
    print("⏳ Ez eltarthat néhány percig...")
    
    # Magyar zenekarok listája
    magyar_zenekarok = [
        "Hiperkarma", "HS7", "Óriás", "Kispál", "Kiscsillag", "Vad Fruttik",
        "Tereskova", "Anna and the Barbies", "Honeybeast", "Konyha",
        "Follow the flow", "Elefánt", "4Street", "Bagossy Brothers",
        "Csaknekedkislány", "Lóci játszik", "Galaxisok", "Parno Graszt",
        "Palya Bea", "Bohemian Betyars", "Aurevoir", "Dánielffy",
        "Ham Ko Ham", "Carbonfools", "Zagar", "Neo", "Soulwave", "Neon"
    ]
    
    results = {}
    success_count = 0
    fallback_count = 0
    
    print(f"🔍 Magyar zenekarok Spotify linkjeinek keresése...")
    print(f"📋 Összesen {len(magyar_zenekarok)} zenekar")
    
    for i, zenekar in enumerate(magyar_zenekarok, 1):
        print(f"[{i}/{len(magyar_zenekarok)}] Keresés: {zenekar}")
        
        # Try improved search
        link = search_spotify_web_api(zenekar)
        
        if link and "0YqQvRjqNXAv2K5FqS9cdO" not in link:
            print(f"✅ {zenekar}: {link}")
            results[zenekar] = link
            success_count += 1
        else:
            # Fallback link
            fallback_link = "https://open.spotify.com/artist/0YqQvRjqNXAv2K5FqS9cdO"
            print(f"❌ {zenekar}: Fallback link")
            results[zenekar] = fallback_link
            fallback_count += 1
        
        time.sleep(2)  # Rate limiting
    
    # Eredmények mentése
    with open('magyar_zenekarok_spotify_links.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    # Python fájl generálása
    python_code = "# Magyar zenekarok Spotify linkjei\n"
    python_code += "MAGYAR_ZENEKAROK_SPOTIFY_LINKS = {\n"
    
    for zenekar, link in results.items():
        python_code += f'    "{zenekar}": "{link}",\n'
    
    python_code += "}\n"
    
    with open('magyar_zenekarok_spotify_links.py', 'w', encoding='utf-8') as f:
        f.write(python_code)
    
    print(f"\n📁 Eredmények mentve: magyar_zenekarok_spotify_links.json")
    print(f"✅ {success_count} valódi link találva")
    print(f"❌ {fallback_count} fallback link")
    print(f"📁 Python fájl létrehozva: magyar_zenekarok_spotify_links.py")
    print("🎉 Keresés befejezve!")
    
    print("\n📊 Összefoglaló:")
    for zenekar, link in results.items():
        status = "✅" if "0YqQvRjqNXAv2K5FqS9cdO" not in link else "❌"
        print(f"{status} {zenekar}: {link}")

if __name__ == "__main__":
    main() 