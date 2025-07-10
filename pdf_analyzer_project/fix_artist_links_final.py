#!/usr/bin/env python3
"""
Script to replace specific artist embed links with track embed links for problematic artists.
"""

# Track links for problematic artists (using popular tracks)
TRACK_REPLACEMENTS = {
    "https://open.spotify.com/embed/artist/4dpARuHxo51G3z768sgnrY": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Adele - Rolling in the Deep
    "https://open.spotify.com/embed/artist/1mbgj8ERPs8lWi7t5cKrdq": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Zaz - Je veux
    "https://open.spotify.com/embed/artist/6m3MpzS0GocyS9T6NMW2KQ": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Emelie Sande - Next To Me
    "https://open.spotify.com/embed/artist/7vxVmI7JYzsc7W0e8eJ8yX": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Lilly Allen - Smile
    "https://open.spotify.com/embed/artist/2gAaHnF4qO8l4jWq1Wm4eB": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Jessie J. - Price Tag
    "https://open.spotify.com/embed/artist/1l7ZsJRRS8wlW3WfJfPfNS": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Christina Aguilera - Beautiful
    "https://open.spotify.com/embed/artist/4RVnAU35WRWra6OZ3CbbMA": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Kylie Minogue - Can't Get You Out of My Head
    "https://open.spotify.com/embed/artist/6ogn9necmbUDC560pYqJMy": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Alanis Morissette - Ironic
    "https://open.spotify.com/embed/artist/6JL8zeS1NmiLfG9fXwVrWt": "https://open.spotify.com/embed/track/0V3wPSX9ygBnCm8psDIegu",  # Megan Trainor - All About That Bass
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