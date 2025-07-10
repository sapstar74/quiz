#!/usr/bin/env python3
"""
Nemzetközi zenekarok embed linkek javítása és "Hallgasd meg a zeneművet:" szöveg eltávolítása
"""

import re

def fix_nemzetkozi_embeds():
    """Nemzetközi zenekarok embed linkek javítása"""
    
    with open('topics/nemzetkozi_zenekarok.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex pattern az artist URL-ek kereséséhez
    pattern = r'"spotify_embed":\s*"https://open\.spotify\.com/artist/([^"]+)"'
    
    def replace_embed(match):
        artist_id = match.group(1)
        # Cseréljük le az artist URL-t embed URL-re
        return f'"spotify_embed": "https://open.spotify.com/embed/artist/{artist_id}"'
    
    # Cseréljük le az embed linkeket
    updated_content = re.sub(pattern, replace_embed, content)
    
    # Mentsük el a frissített fájlt
    with open('topics/nemzetkozi_zenekarok.py', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("✅ Nemzetközi zenekarok embed linkek javítva!")

def remove_hallgasd_meg_from_quiz_app():
    """Hallgasd meg a zeneművet szöveg eltávolítása a quiz app-ból"""
    
    with open('quiz_app_clean.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Cseréljük le a "Hallgasd meg a zeneművet:" szöveget üres stringre
    updated_content = content.replace('st.markdown("### 🎵 Hallgasd meg a zeneművet:")', '')
    
    # Mentsük el a frissített fájlt
    with open('quiz_app_clean.py', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("✅ 'Hallgasd meg a zeneművet:' szöveg eltávolítva a quiz app-ból!")

if __name__ == "__main__":
    print("🔧 Nemzetközi zenekarok embed linkek javítása és szöveg tisztítása...")
    
    try:
        fix_nemzetkozi_embeds()
    except FileNotFoundError:
        print("⚠️  Nemzetközi zenekarok fájl nem található")
    
    try:
        remove_hallgasd_meg_from_quiz_app()
    except FileNotFoundError:
        print("⚠️  Quiz app fájl nem található")
    
    print("🎉 Javítások befejezve!") 