#!/usr/bin/env python3
"""
Find correct Spotify artist IDs for broken links
"""

import requests
import json
from spotify_api_config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

def get_spotify_token():
    """Get Spotify access token using client credentials flow"""
    auth_url = "https://accounts.spotify.com/api/token"
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': SPOTIFY_CLIENT_ID,
        'client_secret': SPOTIFY_CLIENT_SECRET,
    })
    
    if auth_response.status_code == 200:
        return auth_response.json()['access_token']
    else:
        print(f"Error getting token: {auth_response.status_code}")
        return None

def search_artist(artist_name: str, token: str):
    """Search for an artist on Spotify"""
    if not token:
        return None
    
    url = "https://api.spotify.com/v1/search"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    params = {
        'q': artist_name,
        'type': 'artist',
        'limit': 5
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            return data['artists']['items']
        else:
            print(f"Error searching for {artist_name}: {response.status_code}")
            return None
    except Exception as e:
        print(f"Exception searching for {artist_name}: {e}")
        return None

def main():
    print("🔍 Searching for correct Spotify artist IDs...")
    
    # Artists with broken links
    broken_artists = [
        "Zaz",
        "Emeli Sandé",  # Note: Emelie Sande -> Emeli Sandé
        "Lily Allen",   # Note: Lilly Allen -> Lily Allen
        "Jessie J",
        "Meghan Trainor",  # Note: Megan Trainor -> Meghan Trainor
        "Alanis Morissette",
        "will.i.am",    # Note: Will.i.am -> will.i.am
        "One Direction",
        "Måneskin",     # Note: Maneskin -> Måneskin
        "Milky Chance",
        "James Bay",    # This one was wrong
        "Pharrell Williams",  # This one was wrong (Pharrel -> Pharrell)
        "Pitbull"       # This one was wrong (FloRida -> Pitbull)
    ]
    
    token = get_spotify_token()
    if not token:
        print("❌ Could not get Spotify token")
        return
    
    print("✅ Got Spotify token, searching...")
    
    results = {}
    
    for artist_name in broken_artists:
        print(f"\n🔍 Searching for: {artist_name}")
        artists = search_artist(artist_name, token)
        
        if artists and len(artists) > 0:
            print(f"  Found {len(artists)} results:")
            for i, artist in enumerate(artists[:3]):  # Show top 3
                print(f"    {i+1}. {artist['name']} (ID: {artist['id']}) - Popularity: {artist['popularity']}")
            
            # Get the most popular result
            best_match = max(artists, key=lambda x: x['popularity'])
            results[artist_name] = {
                'id': best_match['id'],
                'name': best_match['name'],
                'popularity': best_match['popularity']
            }
            print(f"  ✅ Best match: {best_match['name']} (ID: {best_match['id']})")
        else:
            print(f"  ❌ No results found for {artist_name}")
            results[artist_name] = None
    
    # Print summary
    print("\n" + "="*60)
    print("📋 CORRECT SPOTIFY ARTIST IDs")
    print("="*60)
    
    for artist_name, result in results.items():
        if result:
            print(f"✅ {artist_name}: {result['id']} -> {result['name']} (popularity: {result['popularity']})")
        else:
            print(f"❌ {artist_name}: No match found")

if __name__ == "__main__":
    main() 