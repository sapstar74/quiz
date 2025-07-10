#!/usr/bin/env python3
"""
Script to replace specific artist embed links with track embed links for problematic artists.
"""

import re

# Track links for problematic artists (using popular tracks)
TRACK_REPLACEMENTS = {
    "One Direction": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # What Makes You Beautiful
    "Will.i.am": "https://open.spotify.com/embed/track/2RttW7RAu5nOAfq6YFvApB",  # Scream & Shout
    "James Bay": "https://open.spotify.com/embed/track/3UJ3v9zmnToVmxmveJ2QBF",  # Hold Back The River
    "Emelie Sande": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Next To Me
    "Milky Chance": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Stolen Dance
    "Jessie J.": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Price Tag
    "Lilly Allen": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Smile
    "Justin Bieber": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Baby
    "Christina Aguilera": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Beautiful
    "Michael Buble": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Haven't Met You Yet
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
        replacements_made = 0
        
        # For each problematic artist, find their questions and replace the spotify_embed
        for artist, track_link in TRACK_REPLACEMENTS.items():
            # Find the question block for this artist
            # Look for the pattern: "question": "Ki az előadó?", followed by options containing the artist
            pattern = rf'("question": "Ki az előadó?",\s*"options": \[[^\]]*{re.escape(artist)}[^\]]*\],\s*"spotify_embed": ")[^"]*(")'
            
            matches = re.findall(pattern, content, re.DOTALL)
            if matches:
                for match in matches:
                    # Replace the artist embed link with track link
                    old_link_pattern = rf'("question": "Ki az előadó?",\s*"options": \[[^\]]*{re.escape(artist)}[^\]]*\],\s*"spotify_embed": ")[^"]*(")'
                    new_content = rf'\1{track_link}\2'
                    content = re.sub(old_link_pattern, new_content, content, flags=re.DOTALL)
                    replacements_made += 1
                    print(f"  Replaced artist link for {artist} with track link")
        
        # Write back if changes were made
        if content != original_content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  Updated {filename} with {replacements_made} replacements")
        else:
            print(f"  No changes needed in {filename}")
            
    except Exception as e:
        print(f"  Error processing {filename}: {e}")

def main():
    """Main function to fix artist links in question files."""
    print("Replacing specific artist embed links with track embed links...")
    
    # Process the international music question file
    files_to_process = [
        "topics/nemzetkozi_zenekarok.py"
    ]
    
    for filename in files_to_process:
        fix_artist_links_in_file(filename)
    
    print("Artist link replacement completed!")

if __name__ == "__main__":
    main() 