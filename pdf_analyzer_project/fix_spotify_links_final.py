#!/usr/bin/env python3
"""
Fix the last 10 broken Spotify links in nemzetkozi_zenekarok.py with the correct artist IDs
"""

def fix_spotify_links():
    """Fix the incorrect Spotify links"""
    
    # Read the current file
    with open('topics/nemzetkozi_zenekarok.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Correct Spotify artist IDs for the last 10 broken links
    correct_links = {
        "Zaz": "https://open.spotify.com/embed/artist/1mbgj8ERPs8lWi7t5cYrdy",
        "Emelie Sande": "https://open.spotify.com/embed/artist/7sfgqEdoeBTjd8lQsPT3Cy",
        "Lilly Allen": "https://open.spotify.com/embed/artist/13saZpZnCDWOI9D4IJhp1f",
        "Jessie J.": "https://open.spotify.com/embed/artist/2gsggkzM5R49q6jpPvazou",
        "Megan Trainor": "https://open.spotify.com/embed/artist/6JL8zeS1NmiOftqZTRgdTz",
        "Alanis Morissette": "https://open.spotify.com/embed/artist/6ogn9necmbUdCppmNnGOdi",
        "Will.i.am": "https://open.spotify.com/embed/artist/085pc2PYOi8bGKj0PNjekA",
        "One Direction": "https://open.spotify.com/embed/artist/4AK6F7OLvEQ5QYCBNiQWHq",
        "Maneskin": "https://open.spotify.com/embed/artist/0lAWpj5szCSwM4rUMHYmrr",
        "Milky Chance": "https://open.spotify.com/embed/artist/1hzfo8twXdOegF3xireCYs"
    }
    
    # Replace the links
    lines = content.split('\n')
    fixed_lines = []
    
    for i, line in enumerate(lines):
        # Check if this line contains an explanation for one of the problematic artists
        for artist, correct_link in correct_links.items():
            if f'"explanation": "{artist}' in line:
                # This is the artist's question, fix the link above it
                if i > 0 and '"spotify_embed":' in lines[i-1]:
                    # Replace the spotify_embed line
                    fixed_lines[-1] = f'        "spotify_embed": "{correct_link}",'
                    print(f"Fixed {artist} Spotify link: {correct_link}")
        
        fixed_lines.append(line)
    
    # Write the fixed content back
    with open('topics/nemzetkozi_zenekarok.py', 'w', encoding='utf-8') as f:
        f.write('\n'.join(fixed_lines))
    
    print("✅ Fixed all last problematic Spotify links!")

if __name__ == "__main__":
    fix_spotify_links() 