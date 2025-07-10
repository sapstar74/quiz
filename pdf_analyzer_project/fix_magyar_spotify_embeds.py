#!/usr/bin/env python3
"""
Magyar zenekarok Spotify linkek konvertálása embed formátumra
"""

def convert_artist_to_embed_url(artist_url):
    """Konvertálja az artist URL-t embed URL-re"""
    if "open.spotify.com/artist/" in artist_url:
        # Cseréljük le az artist-t embed-re
        embed_url = artist_url.replace("/artist/", "/embed/artist/")
        return embed_url
    return artist_url

def update_magyar_zenekarok_embeds():
    """Frissíti a magyar zenekarok fájlt embed linkekkel"""
    
    # Olvasd be az eredeti fájlt
    with open('topics/magyar_zenekarok.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Konvertáljuk az artist linkeket embed linkekre
    updated_content = content.replace(
        'https://open.spotify.com/artist/',
        'https://open.spotify.com/embed/artist/'
    )
    
    # Mentsd el a frissített fájlt
    with open('topics/magyar_zenekarok_embed.py', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("✅ Magyar zenekarok Spotify linkek konvertálva embed formátumra!")
    print("📁 Frissített fájl: topics/magyar_zenekarok_embed.py")
    
    # Ellenőrizzük a konverziót
    import re
    artist_links = re.findall(r'https://open\.spotify\.com/artist/[^"\s]+', content)
    embed_links = re.findall(r'https://open\.spotify\.com/embed/artist/[^"\s]+', updated_content)
    
    print(f"🔗 {len(artist_links)} artist link konvertálva {len(embed_links)} embed linkre")
    
    return updated_content

def test_embed_links():
    """Teszteli az embed linkeket"""
    
    # Néhány példa link tesztelése
    test_links = [
        "https://open.spotify.com/artist/71buZyotrHSZMVkSTcDY8c",  # Kispál
        "https://open.spotify.com/artist/0iVQlLqQwkK3VUvUMp3EIq",  # HS7
        "https://open.spotify.com/artist/7faDICJ6UmmMzTCzT2DyRE",  # Óriás
    ]
    
    print("\n🧪 Embed linkek tesztelése:")
    for link in test_links:
        embed_link = convert_artist_to_embed_url(link)
        print(f"Artist: {link}")
        print(f"Embed:  {embed_link}")
        print()

if __name__ == "__main__":
    print("🎵 Magyar zenekarok Spotify embed linkek konvertálása...")
    
    # Teszteljük a konverziót
    test_embed_links()
    
    # Frissítsük a fájlt
    update_magyar_zenekarok_embeds()
    
    print("\n🎉 Konverzió befejezve!")
    print("💡 Most már az embed linkek működni fognak a quiz app-ban!") 