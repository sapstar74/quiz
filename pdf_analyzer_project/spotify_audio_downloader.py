#!/usr/bin/env python3
"""
Spotify Audio Downloader
Letölti az audio tartalmakat a Spotify linkekből
"""

import os
import requests
import json
import time
from pathlib import Path
from urllib.parse import urlparse, parse_qs
import yt_dlp

class SpotifyAudioDownloader:
    def __init__(self):
        self.audio_dir = Path(__file__).parent / "audio_files"
        self.audio_dir.mkdir(exist_ok=True)
        
    def extract_track_id(self, spotify_url):
        """Kinyeri a track ID-t a Spotify URL-ből"""
        if '/track/' in spotify_url:
            return spotify_url.split('/track/')[1].split('?')[0]
        elif '/artist/' in spotify_url:
            return spotify_url.split('/artist/')[1].split('?')[0]
        return None
    
    def get_track_info(self, track_id):
        """Lekéri a track információit a Spotify API-ból"""
        # Ez egy egyszerű példa - valós implementációban Spotify API kulcs kellene
        try:
            # YouTube keresés a track neve alapján
            search_query = f"spotify track {track_id}"
            return {"track_id": track_id, "search_query": search_query}
        except Exception as e:
            print(f"Hiba a track info lekérésekor: {e}")
            return None
    
    def download_from_youtube(self, search_query, output_filename):
        """Letölti az audio fájlt YouTube-ról"""
        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': str(self.audio_dir / output_filename),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'quiet': True,
                'no_warnings': True,
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([f"ytsearch:{search_query}"])
            
            return True
        except Exception as e:
            print(f"Hiba a YouTube letöltéskor: {e}")
            return False
    
    def download_spotify_track(self, spotify_url, output_filename=None):
        """Letölti egy Spotify track-et"""
        track_id = self.extract_track_id(spotify_url)
        if not track_id:
            print(f"Érvénytelen Spotify URL: {spotify_url}")
            return False
        
        if not output_filename:
            output_filename = f"track_{track_id}.mp3"
        
        track_info = self.get_track_info(track_id)
        if not track_info:
            return False
        
        print(f"Letöltés: {track_info['search_query']}")
        return self.download_from_youtube(track_info['search_query'], output_filename)
    
    def batch_download_questions(self, questions):
        """Több kérdés audio fájljainak letöltése"""
        downloaded_files = []
        
        for i, question in enumerate(questions):
            if 'spotify_embed' not in question or not question['spotify_embed']:
                continue
            
            spotify_url = question['spotify_embed']
            explanation = question.get('explanation', f'track_{i}')
            
            # Fájlnév generálása
            track_id = self.extract_track_id(spotify_url)
            if track_id:
                output_filename = f"track_{track_id}.mp3"
            else:
                output_filename = f"audio_{i}.mp3"
            
            print(f"Letöltés {i+1}/{len(questions)}: {explanation}")
            
            if self.download_spotify_track(spotify_url, output_filename):
                downloaded_files.append({
                    'question_index': i,
                    'filename': output_filename,
                    'explanation': explanation
                })
                print(f"✅ Sikeres: {output_filename}")
            else:
                print(f"❌ Sikertelen: {explanation}")
            
            # Várakozás a következő letöltés előtt
            time.sleep(2)
        
        return downloaded_files

def main():
    """Fő funkció a letöltés teszteléséhez"""
    downloader = SpotifyAudioDownloader()
    
    # Teszt kérdések betöltése
    from topics.magyar_zenekarok import MAGYAR_ZENEKAROK_QUESTIONS
    
    print("🎵 Spotify Audio Downloader")
    print(f"Talált kérdések: {len(MAGYAR_ZENEKAROK_QUESTIONS)}")
    
    # Első 5 kérdés letöltése tesztként
    test_questions = MAGYAR_ZENEKAROK_QUESTIONS[:5]
    
    downloaded = downloader.batch_download_questions(test_questions)
    
    print(f"\n✅ Sikeresen letöltve: {len(downloaded)} fájl")
    for file_info in downloaded:
        print(f"  - {file_info['filename']}: {file_info['explanation']}")

if __name__ == "__main__":
    main() 