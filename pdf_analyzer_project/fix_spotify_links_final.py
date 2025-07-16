#!/usr/bin/env python3
"""
Script to fix duplicate Spotify links in Hungarian bands questions.
"""

import re

# Read the current file
with open('topics/magyar_zenekarok.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace duplicate Spotify links with unique ones
replacements = [
    # Soulwave
    ('"spotify_embed": "https://open.spotify.com/embed/artist/5hBCfYFEDK8otrksMYuzoL",\n        "options": [\n            "Soulwave",', 
     '"spotify_embed": "https://open.spotify.com/embed/artist/4hQQE3GUQeBAOFwTJ5aede",\n        "options": [\n            "Soulwave",'),
    
    # Neon
    ('"spotify_embed": "https://open.spotify.com/embed/artist/5hBCfYFEDK8otrksMYuzoL",\n        "options": [\n            "Neon",', 
     '"spotify_embed": "https://open.spotify.com/embed/artist/3zhmiYvMt6ScobjEnbVB4I",\n        "options": [\n            "Neon",'),
    
    # Quimby
    ('"spotify_embed": "https://open.spotify.com/embed/artist/5hBCfYFEDK8otrksMYuzoL",\n        "options": [\n            "Quimby",', 
     '"spotify_embed": "https://open.spotify.com/embed/artist/54N9jnigs5yhiMGY7rVu1K",\n        "options": [\n            "Quimby",'),
    
    # Tankcsapda
    ('"spotify_embed": "https://open.spotify.com/embed/artist/5hBCfYFEDK8otrksMYuzoL",\n        "options": [\n            "Tankcsapda",', 
     '"spotify_embed": "https://open.spotify.com/embed/artist/2ezYPSKWBfnFTobN9puCow",\n        "options": [\n            "Tankcsapda",'),
    
    # P. Mobil
    ('"spotify_embed": "https://open.spotify.com/embed/artist/5hBCfYFEDK8otrksMYuzoL",\n        "options": [\n            "P. Mobil",', 
     '"spotify_embed": "https://open.spotify.com/embed/artist/51BZWZTWqI7GjrgHw3Wvuw",\n        "options": [\n            "P. Mobil",'),
    
    # Republic
    ('"spotify_embed": "https://open.spotify.com/embed/artist/5hBCfYFEDK8otrksMYuzoL",\n        "options": [\n            "Republic",', 
     '"spotify_embed": "https://open.spotify.com/embed/artist/4imSxhDqtkiuKUamV1AL2l",\n        "options": [\n            "Republic",'),
    
    # Bonanza Banzai
    ('"spotify_embed": "https://open.spotify.com/embed/artist/5hBCfYFEDK8otrksMYuzoL",\n        "options": [\n            "Bonanza Banzai",', 
     '"spotify_embed": "https://open.spotify.com/embed/artist/4BcSup56aUUtG55MkrsHDx",\n        "options": [\n            "Bonanza Banzai",'),
    
    # Korai Öröm
    ('"spotify_embed": "https://open.spotify.com/embed/artist/5hBCfYFEDK8otrksMYuzoL",\n        "options": [\n            "Korai Öröm",', 
     '"spotify_embed": "https://open.spotify.com/embed/artist/7KRmqRSdAGjiSDns2qsdQ8",\n        "options": [\n            "Korai Öröm",'),
]

# Apply replacements
for old, new in replacements:
    content = content.replace(old, new)

# Write back to file
with open('topics/magyar_zenekarok.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Spotify linkek javítva!")
print("Minden kérdés most egyedi Spotify linket használ.") 