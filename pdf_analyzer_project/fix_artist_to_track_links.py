#!/usr/bin/env python3
"""
Script to replace artist embed links with track embed links for problematic artists.
"""

import json
import re

# Track links for problematic artists (using popular tracks)
TRACK_REPLACEMENTS = {
    "One Direction": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # What Makes You Beautiful
    "will.i.am": "https://open.spotify.com/embed/track/2RttW7RAu5nOAfq6YFvApB",  # Scream & Shout
    "James Bay": "https://open.spotify.com/embed/track/3UJ3v9zmnToVmxmveJ2QBF",  # Hold Back The River
    "Emeli Sandé": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Next To Me
    "Milky Chance": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Stolen Dance
    "Jessie J": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Price Tag
    "Lily Allen": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Smile
    "Justin Bieber": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Baby
    "Christina Aguilera": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Beautiful
    "Michael Bublé": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Haven't Met You Yet
    "The Chainsmokers": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Closer
    "Alanis Morissette": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Ironic
    "Meghan Trainor": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # All About That Bass
    "Kylie Minogue": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Can't Get You Out of My Head
    "Imagine Dragons": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Radioactive
    "Adele": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Rolling in the Deep
    "Zaz": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu"  # Je veux
}

def fix_artist_links_in_file(filename):
    """Replace artist embed links with track embed links in a question file."""
    print(f"Processing {filename}...")
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Replace each artist link with track link
        for artist, track_link in TRACK_REPLACEMENTS.items():
            # Pattern to match artist embed links
            pattern = rf'https://open\.spotify\.com/embed/artist/[^"\s]+'
            
            # Find all artist links in the content
            artist_links = re.findall(pattern, content)
            
            for link in artist_links:
                # Check if this link is for the current artist
                if artist.lower() in content.lower():
                    content = content.replace(link, track_link)
                    print(f"  Replaced artist link for {artist} with track link")
        
        # Write back if changes were made
        if content != original_content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  Updated {filename}")
        else:
            print(f"  No changes needed in {filename}")
            
    except Exception as e:
        print(f"  Error processing {filename}: {e}")

def main():
    """Main function to fix artist links in all question files."""
    print("Replacing artist embed links with track embed links...")
    
    # Process both Hungarian and international music question files
    files_to_process = [
        "topics/konnyuzene.py",
        "topics/magyar_zenekarok.py"
    ]
    
    for filename in files_to_process:
        fix_artist_links_in_file(filename)
    
    print("Artist link replacement completed!")

if __name__ == "__main__":
    main() 