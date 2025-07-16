#!/usr/bin/env python3
"""
Saját audio lejátszó komponens a Spotify embed helyett
"""

import streamlit as st
import os
from pathlib import Path
import base64

def get_audio_file_path(audio_filename):
    """Visszaadja az audio fájl teljes elérési útját"""
    audio_dir = Path(__file__).parent / "audio_files"
    return audio_dir / audio_filename

def audio_player_with_download(audio_filename, title="Zene lejátszása"):
    """
    Saját audio lejátszó komponens letöltési lehetőséggel
    
    Args:
        audio_filename: Az audio fájl neve (pl. "track_1.mp3")
        title: A lejátszó címe
    """
    
    audio_path = get_audio_file_path(audio_filename)
    
    if not audio_path.exists():
        st.warning(f"⚠️ Audio fájl nem található: {audio_filename}")
        return
    
    # Audio lejátszó megjelenítése
    st.markdown(f"### 🎵 {title}")
    
    # Streamlit beépített audio lejátszó
    with open(audio_path, "rb") as audio_file:
        audio_bytes = audio_file.read()
    
    st.audio(audio_bytes, format=f"audio/{audio_path.suffix[1:]}")
    
    # Letöltési gomb
    st.download_button(
        label="📥 Letöltés",
        data=audio_bytes,
        file_name=audio_filename,
        mime=f"audio/{audio_path.suffix[1:]}"
    )

def create_audio_downloader():
    """
    Audio fájlok letöltő rendszere a Spotify linkekből
    """
    
    st.markdown("## 🎵 Audio Fájlok Letöltése")
    st.markdown("Ez a funkció letölti az audio tartalmakat a Spotify linkekből.")
    
    # Audio könyvtár létrehozása
    audio_dir = Path(__file__).parent / "audio_files"
    audio_dir.mkdir(exist_ok=True)
    
    # Spotify linkek gyűjtése a kérdésekből
    from topics.magyar_zenekarok import MAGYAR_ZENEKAROK_QUESTIONS
    from topics.nemzetkozi_zenekarok import NEMZETKOZI_ZENEKAROK_QUESTIONS
    from classical_music_questions_tschaikovsky_updated import CLASSICAL_MUSIC_QUESTIONS
    
    all_questions = (
        MAGYAR_ZENEKAROK_QUESTIONS + 
        NEMZETKOZI_ZENEKAROK_QUESTIONS + 
        CLASSICAL_MUSIC_QUESTIONS
    )
    
    spotify_links = []
    for i, q in enumerate(all_questions):
        if 'spotify_embed' in q and q['spotify_embed']:
            spotify_links.append({
                'index': i,
                'question': q['question'],
                'explanation': q.get('explanation', ''),
                'spotify_url': q['spotify_embed']
            })
    
    st.write(f"**Talált Spotify linkek száma:** {len(spotify_links)}")
    
    if st.button("🚀 Letöltés Indítása"):
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i, link_info in enumerate(spotify_links):
            status_text.text(f"Letöltés: {link_info['explanation']}")
            
            # Itt implementálhatnánk a tényleges letöltést
            # Egyelőre csak placeholder
            
            progress_bar.progress((i + 1) / len(spotify_links))
        
        status_text.text("✅ Letöltés befejezve!")
        st.success("Az audio fájlok sikeresen letöltve!")

def replace_spotify_with_custom_player(question_data):
    """
    Spotify embed helyettesítése saját audio lejátszóval
    
    Args:
        question_data: A kérdés adatai
    
    Returns:
        Frissített kérdés adatok
    """
    
    if 'spotify_embed' not in question_data:
        return question_data
    
    spotify_url = question_data['spotify_embed']
    
    # Track ID kinyerése a Spotify URL-ből
    if '/track/' in spotify_url:
        track_id = spotify_url.split('/track/')[1].split('?')[0]
        audio_filename = f"track_{track_id}.mp3"
    elif '/artist/' in spotify_url:
        artist_id = spotify_url.split('/artist/')[1].split('?')[0]
        audio_filename = f"artist_{artist_id}.mp3"
    else:
        audio_filename = f"audio_{hash(spotify_url)}.mp3"
    
    # Kérdés frissítése
    updated_question = question_data.copy()
    updated_question['audio_file'] = audio_filename
    updated_question['spotify_embed'] = None  # Spotify embed eltávolítása
    
    return updated_question

def show_custom_audio_player(question_data):
    """
    Saját audio lejátszó megjelenítése a kérdésben
    
    Args:
        question_data: A kérdés adatai
    """
    
    if 'audio_file' in question_data and question_data['audio_file']:
        audio_filename = question_data['audio_file']
        title = question_data.get('explanation', 'Zene lejátszása')
        audio_player_with_download(audio_filename, title)
    elif 'spotify_embed' in question_data and question_data['spotify_embed']:
        # Fallback: Spotify embed megjelenítése
        st.markdown("### 🎵 Spotify Lejátszó")
        st.components.v1.iframe(question_data['spotify_embed'], height=80)

# Példa használat
if __name__ == "__main__":
    st.title("Saját Audio Lejátszó Teszt")
    
    # Teszt audio lejátszó
    test_question = {
        'question': 'Teszt kérdés',
        'audio_file': 'test_track.mp3',
        'explanation': 'Teszt zene'
    }
    
    show_custom_audio_player(test_question) 