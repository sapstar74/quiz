#!/usr/bin/env python3
"""
Test all Spotify links in nemzetkozi_zenekarok.py using Spotify API
"""

import requests
import json
import re
from typing import Dict, List, Tuple
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

def test_spotify_artist(artist_id: str, token: str) -> Tuple[bool, str]:
    """Test if a Spotify artist ID is valid"""
    if not token:
        return False, "No token available"
    
    url = f"https://api.spotify.com/v1/artists/{artist_id}"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            artist_data = response.json()
            return True, artist_data['name']
        else:
            return False, f"HTTP {response.status_code}"
    except Exception as e:
        return False, str(e)

def extract_artist_ids_from_file():
    """Extract all Spotify artist IDs from the nemzetkozi_zenekarok.py file"""
    with open('topics/nemzetkozi_zenekarok.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all spotify_embed lines
    pattern = r'"spotify_embed": "https://open\.spotify\.com/embed/artist/([^"]+)"'
    matches = re.findall(pattern, content)
    
    # Also find the corresponding artist names
    lines = content.split('\n')
    artist_data = []
    
    for i, line in enumerate(lines):
        if '"spotify_embed":' in line:
            # Extract artist ID
            match = re.search(r'https://open\.spotify\.com/embed/artist/([^"]+)', line)
            if match:
                artist_id = match.group(1)
                
                # Find the explanation line to get artist name
                artist_name = "Unknown"
                for j in range(i, min(i + 10, len(lines))):
                    if '"explanation":' in lines[j]:
                        # Extract artist name from explanation
                        exp_match = re.search(r'"explanation": "([^"]+)"', lines[j])
                        if exp_match:
                            explanation = exp_match.group(1)
                            # Extract artist name (before the dash)
                            name_match = re.match(r'^([^-]+)', explanation)
                            if name_match:
                                artist_name = name_match.group(1).strip()
                        break
                
                artist_data.append((artist_id, artist_name))
    
    return artist_data

def main():
    print("🎵 Testing Spotify links...")
    
    # Get artist data from file
    artist_data = extract_artist_ids_from_file()
    print(f"Found {len(artist_data)} Spotify links to test")
    
    # Get Spotify token
    token = get_spotify_token()
    if not token:
        print("❌ Could not get Spotify token. Please check your credentials.")
        print("You can still see the artist IDs that need to be tested:")
        for artist_id, artist_name in artist_data:
            print(f"  {artist_name}: {artist_id}")
        return
    
    print("✅ Got Spotify token, testing links...")
    
    # Test each artist
    working_links = []
    broken_links = []
    
    for artist_id, artist_name in artist_data:
        print(f"Testing {artist_name} ({artist_id})...", end=" ")
        is_valid, result = test_spotify_artist(artist_id, token)
        
        if is_valid:
            print(f"✅ {result}")
            working_links.append((artist_name, artist_id, result))
        else:
            print(f"❌ {result}")
            broken_links.append((artist_name, artist_id, result))
    
    # Summary
    print("\n" + "="*50)
    print("📊 SUMMARY")
    print("="*50)
    print(f"✅ Working links: {len(working_links)}")
    print(f"❌ Broken links: {len(broken_links)}")
    
    if broken_links:
        print("\n❌ BROKEN LINKS:")
        for artist_name, artist_id, error in broken_links:
            print(f"  {artist_name}: {artist_id} - {error}")
    
    if working_links:
        print("\n✅ WORKING LINKS:")
        for artist_name, artist_id, spotify_name in working_links:
            print(f"  {artist_name}: {artist_id} -> {spotify_name}")

if __name__ == "__main__":
    main() 