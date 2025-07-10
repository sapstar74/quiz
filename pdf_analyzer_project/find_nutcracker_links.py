#!/usr/bin/env python3
"""
Script más Diótörő linkek kereséséhez
"""

# Javított Diótörő linkek - a legnépszerűbb részek
NUTCRACKER_LINKS = {
    "Dance of the Sugar Plum Fairy": "https://open.spotify.com/embed/track/0Qe9CUxDFvQi64Tt2EmrM6",
    "Waltz of the Flowers": "https://open.spotify.com/embed/track/4VRRbrw7ai2mztUrXrAvfd", 
    "March": "https://open.spotify.com/embed/track/2Y8j8X4dF8mJp0MX39J4U8",
    "Russian Dance (Trepak)": "https://open.spotify.com/embed/track/6QN6jwnUVuTqvTRxXyF0Ro",
    "Chinese Dance": "https://open.spotify.com/embed/track/62dD6AMgEvZq5OCHAZ7d9a",
    "Arabian Dance": "https://open.spotify.com/embed/track/2Sbb5o2R6zci4L0xEQhsvK",
    "Dance of the Reed Flutes": "https://open.spotify.com/embed/track/6jZj45D2jdR6fMEb58TlSc"
}

print("🎵 Diótörő linkek:")
for dance, link in NUTCRACKER_LINKS.items():
    print(f"- {dance}: {link}")

# Javaslat: használjuk a "Waltz of the Flowers" linket, mert az is nagyon ismert
print("\n💡 Javaslat: Waltz of the Flowers link használata") 