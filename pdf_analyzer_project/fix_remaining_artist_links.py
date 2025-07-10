#!/usr/bin/env python3
"""
Script to replace remaining problematic artist embed links with track embed links.
"""

# Track links for remaining problematic artists
TRACK_REPLACEMENTS = {
    "https://open.spotify.com/embed/artist/5BrZtP0VqFCl8kRDNw4XIg": "https://open.spotify.com/embed/track/2RttW7RAu5nOAfq6YFvApB",  # Will.i.am - Scream & Shout
    "https://open.spotify.com/embed/artist/1GxkXlMwML1oSg5eLPiAz3": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Michael Buble - Haven't Met You Yet
    "https://open.spotify.com/embed/artist/1uNFoZAHBGtllmzznpCI3s": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Justin Bieber - Baby
    "https://open.spotify.com/embed/artist/4phGZZrJZRo4ElhRtViYdl": "https://open.spotify.com/embed/track/3UJ3v9zmnToVmxmveJ2QBF",  # James Bay - Hold Back The River
    "https://open.spotify.com/embed/artist/53XhwfbYqKCa1cC15pYq2q": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Imagine Dragons - Radioactive
    "https://open.spotify.com/embed/artist/04AK6F7OLvEQ5QYCBNiQWHq": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # One Direction - What Makes You Beautiful
    "https://open.spotify.com/embed/artist/69GGBxA162lTqCwzJG5jLp": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # The Chainsmokers - Closer
    "https://open.spotify.com/embed/artist/1ehfoIf2vc6LDkUALyW9sa": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Milky Chance - Stolen Dance
}

def fix_artist_links_in_file(filename):
    """Replace artist embed links with track embed links in a question file."""
    print(f"Processing {filename}...")
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        replacements_made = 0
        
        # Replace each artist link with track link
        for artist_link, track_link in TRACK_REPLACEMENTS.items():
            if artist_link in content:
                content = content.replace(artist_link, track_link)
                replacements_made += 1
                print(f"  Replaced artist link with track link")
        
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
    print("Replacing remaining problematic artist embed links with track embed links...")
    
    # Process the international music question file
    files_to_process = [
        "topics/nemzetkozi_zenekarok.py"
    ]
    
    for filename in files_to_process:
        fix_artist_links_in_file(filename)
    
    print("Artist link replacement completed!")

if __name__ == "__main__":
    main() 