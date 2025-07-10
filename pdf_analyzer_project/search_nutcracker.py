#!/usr/bin/env python3
"""
Script más Diótörő linkek kereséséhez
"""

import requests
import json

# Spotify API credentials
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"

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

def search_nutcracker_tracks():
    """Search for different Nutcracker tracks"""
    token = get_spotify_token()
    headers = {
        'Authorization': f'Bearer {token}'
    }
    
    # Different Nutcracker search terms
    search_terms = [
        "Tchaikovsky Nutcracker Waltz of the Flowers",
        "Tchaikovsky Nutcracker Dance of the Sugar Plum Fairy", 
        "Tchaikovsky Nutcracker March",
        "Tchaikovsky Nutcracker Russian Dance",
        "Tchaikovsky Nutcracker Chinese Dance",
        "Tchaikovsky Nutcracker Arabian Dance",
        "Tchaikovsky Nutcracker Dance of the Reed Flutes"
    ]
    
    results = {}
    
    for term in search_terms:
        search_url = f"https://api.spotify.com/v1/search?q={term}&type=track&limit=5"
        response = requests.get(search_url, headers=headers)
        data = response.json()
        
        if data['tracks']['items']:
            track = data['tracks']['items'][0]
            results[term] = {
                'name': track['name'],
                'artist': track['artists'][0]['name'],
                'id': track['id'],
                'url': f"https://open.spotify.com/embed/track/{track['id']}"
            }
    
    return results

if __name__ == "__main__":
    print("🔍 Keresek Diótörő linkeket...")
    results = search_nutcracker_tracks()
    
    print("\n🎵 Talált Diótörő linkek:")
    for term, track in results.items():
        print(f"\n{term}:")
        print(f"  Név: {track['name']}")
        print(f"  Előadó: {track['artist']}")
        print(f"  Link: {track['url']}") 