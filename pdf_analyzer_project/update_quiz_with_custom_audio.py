#!/usr/bin/env python3
"""
Frissíti a meglévő quiz app-ot saját audio lejátszó használatára
"""

import os
from pathlib import Path

def update_quiz_app_with_custom_audio():
    """
    Frissíti a quiz_app_clean.py fájlt saját audio lejátszó használatára
    """
    
    # Beolvasás
    with open('quiz_app_clean.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Import hozzáadása
    if 'from custom_audio_player import' not in content:
        # Import beszúrása a többi import után
        import_line = 'from custom_audio_player import show_custom_audio_player, replace_spotify_with_custom_player'
        content = content.replace(
            'from topics.idiota_szavak_reversed import IDIOTA_SZAVAK_QUESTIONS',
            'from topics.idiota_szavak_reversed import IDIOTA_SZAVAK_QUESTIONS\nfrom custom_audio_player import show_custom_audio_player, replace_spotify_with_custom_player'
        )
    
    # Spotify embed helyettesítése saját audio lejátszóval
    spotify_section = '''    # Spotify embed if available
    if "spotify_embed" in current_q and current_q["spotify_embed"]:
        
        spotify_url = current_q["spotify_embed"]
        # Clean up the URL and add autoplay with better parameters
        if "?theme=black" in spotify_url:
            spotify_url = spotify_url.split("?theme=black")[0] + "?theme=black&size=small&hide_cover=1&hide_artist=1&hide_title=1&autoplay=1&muted=0"
        else:
            spotify_url = spotify_url + "?autoplay=1&muted=0"
        
        # Add JavaScript for better autoplay support
        st.markdown(f"""
        <script>
        window.addEventListener('load', function() {{
            const iframe = document.querySelector('iframe[src*="spotify"]');
            if (iframe) {{
                iframe.addEventListener('load', function() {{
                    // Try to trigger play
                    iframe.contentWindow.postMessage({{command: 'play'}}, '*');
                }});
            }}
        }});
        </script>
        """, unsafe_allow_html=True)
        
        st.components.v1.iframe(spotify_url, height=80)'''
    
    custom_audio_section = '''    # Saját audio lejátszó megjelenítése
    show_custom_audio_player(current_q)'''
    
    content = content.replace(spotify_section, custom_audio_section)
    
    # Menti a frissített fájlt
    with open('quiz_app_clean.py', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Quiz app frissítve saját audio lejátszóval!")

def create_audio_files_directory():
    """Létrehozza az audio fájlok könyvtárát"""
    audio_dir = Path(__file__).parent / "audio_files"
    audio_dir.mkdir(exist_ok=True)
    
    # .gitkeep fájl létrehozása
    gitkeep_file = audio_dir / ".gitkeep"
    gitkeep_file.touch()
    
    print(f"✅ Audio könyvtár létrehozva: {audio_dir}")

def main():
    """Fő funkció"""
    print("🎵 Quiz App Frissítése Saját Audio Lejátszóval")
    
    # Audio könyvtár létrehozása
    create_audio_files_directory()
    
    # Quiz app frissítése
    update_quiz_app_with_custom_audio()
    
    print("\n📋 Következő lépések:")
    print("1. Telepítsd a szükséges függőségeket: pip install yt-dlp ffmpeg-python")
    print("2. Futtasd a spotify_audio_downloader.py-t az audio fájlok letöltéséhez")
    print("3. Indítsd el a quiz app-ot: streamlit run quiz_app_clean.py")

if __name__ == "__main__":
    main() 