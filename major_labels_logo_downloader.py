"""
🎵 Major Record Labels Logo Downloader
Letölti a nagyobb zenei kiadók logóit
"""

import requests
import os
import json
from pathlib import Path
import time
from urllib.parse import urljoin, urlparse
import streamlit as st
from PIL import Image
import io

# Major zenei kiadók adatai
MAJOR_LABELS = {
    "universal_music_group": {
        "name": "Universal Music Group",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Universal_Music_Group_Logo.svg/320px-Universal_Music_Group_Logo.svg.png",
        "website": "https://www.universalmusic.com/",
        "founded": "1934",
        "headquarters": "Santa Monica, California, USA"
    },
    "sony_music": {
        "name": "Sony Music Entertainment",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Sony_Music_Entertainment_Logo.svg/320px-Sony_Music_Entertainment_Logo.svg.png",
        "website": "https://www.sonymusic.com/",
        "founded": "1929",
        "headquarters": "New York City, USA"
    },
    "warner_music": {
        "name": "Warner Music Group",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Warner_Music_Group_2013_logo.svg/320px-Warner_Music_Group_2013_logo.svg.png",
        "website": "https://www.wmg.com/",
        "founded": "1958",
        "headquarters": "New York City, USA"
    },
    "emi": {
        "name": "EMI Records",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/EMI_Records_Logo.svg/320px-EMI_Records_Logo.svg.png",
        "website": "https://www.emimusic.com/",
        "founded": "1931",
        "headquarters": "London, UK"
    },
    "capitol_records": {
        "name": "Capitol Records",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Capitol_Records_Logo.svg/320px-Capitol_Records_Logo.svg.png",
        "website": "https://www.capitolrecords.com/",
        "founded": "1942",
        "headquarters": "Hollywood, California, USA"
    },
    "columbia_records": {
        "name": "Columbia Records",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Columbia_Records_Logo.svg/320px-Columbia_Records_Logo.svg.png",
        "website": "https://www.columbiarecords.com/",
        "founded": "1887",
        "headquarters": "New York City, USA"
    },
    "atlantic_records": {
        "name": "Atlantic Records",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Atlantic_Records_Logo.svg/320px-Atlantic_Records_Logo.svg.png",
        "website": "https://www.atlanticrecords.com/",
        "founded": "1947",
        "headquarters": "New York City, USA"
    },
    "republic_records": {
        "name": "Republic Records",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Republic_Records_Logo.svg/320px-Republic_Records_Logo.svg.png",
        "website": "https://www.republicrecords.com/",
        "founded": "1995",
        "headquarters": "New York City, USA"
    },
    "def_jam": {
        "name": "Def Jam Recordings",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Def_Jam_Recordings_Logo.svg/320px-Def_Jam_Recordings_Logo.svg.png",
        "website": "https://www.defjam.com/",
        "founded": "1984",
        "headquarters": "New York City, USA"
    },
    "interscope": {
        "name": "Interscope Records",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Interscope_Records_Logo.svg/320px-Interscope_Records_Logo.svg.png",
        "website": "https://www.interscope.com/",
        "founded": "1990",
        "headquarters": "Santa Monica, California, USA"
    }
}

def download_logo(url, filename, output_dir="major_labels_logos"):
    """Letölt egy logót"""
    try:
        # Könyvtár létrehozása
        os.makedirs(output_dir, exist_ok=True)
        
        # Headers a letöltéshez
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Fájl mentése
        file_path = os.path.join(output_dir, filename)
        with open(file_path, 'wb') as f:
            f.write(response.content)
        
        print(f"✅ Letöltve: {filename}")
        return file_path
        
    except Exception as e:
        print(f"❌ Hiba a letöltés során {filename}: {e}")
        return None

def download_all_major_labels(output_dir="major_labels_logos"):
    """Letölti az összes major label logót"""
    print("🎵 Major Record Labels Logo Downloader")
    print("=" * 50)
    
    results = {
        "success": [],
        "failed": [],
        "total": len(MAJOR_LABELS)
    }
    
    for label_id, label_info in MAJOR_LABELS.items():
        print(f"\n📥 Letöltés: {label_info['name']}")
        
        # Fájlnév generálás
        filename = f"{label_id}_{label_info['name'].replace(' ', '_').replace('.', '')}.png"
        
        # Logó letöltése
        file_path = download_logo(label_info['logo_url'], filename, output_dir)
        
        if file_path:
            results["success"].append({
                "label_id": label_id,
                "name": label_info['name'],
                "file_path": file_path
            })
        else:
            results["failed"].append({
                "label_id": label_id,
                "name": label_info['name'],
                "url": label_info['logo_url']
            })
        
        # Kis szünet a túl gyors kérések elkerülésére
        time.sleep(1)
    
    # Eredmények mentése
    results_file = os.path.join(output_dir, "download_results.json")
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    # Összefoglaló
    print(f"\n" + "=" * 50)
    print(f"📊 ÖSSZEFOGLALÓ:")
    print(f"✅ Sikeres letöltések: {len(results['success'])}")
    print(f"❌ Sikertelen letöltések: {len(results['failed'])}")
    print(f"📁 Mentés helye: {output_dir}")
    
    if results['failed']:
        print(f"\n❌ Sikertelen letöltések:")
        for failed in results['failed']:
            print(f"  - {failed['name']}")
    
    return results

def create_labels_info_file(output_dir="major_labels_logos"):
    """Létrehoz egy információs fájlt a kiadókról"""
    info_file = os.path.join(output_dir, "labels_info.json")
    with open(info_file, 'w', encoding='utf-8') as f:
        json.dump(MAJOR_LABELS, f, indent=2, ensure_ascii=False)
    print(f"📄 Információs fájl mentve: {info_file}")

def streamlit_app():
    """Streamlit alkalmazás a logo letöltéshez"""
    st.set_page_config(
        page_title="🎵 Major Labels Logo Downloader",
        page_icon="🎵",
        layout="wide"
    )
    
    st.title("🎵 Major Record Labels Logo Downloader")
    st.markdown("**Letölti a nagyobb zenei kiadók logóit**")
    st.markdown("---")
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Beállítások")
        
        output_dir = st.text_input(
            "Kimeneti mappa:", 
            value="major_labels_logos",
            help="A mappa neve, ahová a logók mentésre kerülnek"
        )
        
        st.markdown("---")
        st.subheader("📊 Elérhető Kiadók")
        st.metric("Összes kiadó", len(MAJOR_LABELS))
        
        # Letöltés gomb
        if st.button("📥 Összes Logó Letöltése", type="primary"):
            with st.spinner("Logók letöltése folyamatban..."):
                results = download_all_major_labels(output_dir)
                create_labels_info_file(output_dir)
                
                st.success(f"✅ Kész! {len(results['success'])}/{results['total']} logó letöltve")
                
                if results['failed']:
                    st.warning(f"⚠️ {len(results['failed'])} logó letöltése sikertelen")
    
    # Fő tartalom - Kiadók listája
    st.header("🏢 Major Record Labels")
    
    # Kiadók megjelenítése
    cols = st.columns(2)
    
    for i, (label_id, label_info) in enumerate(MAJOR_LABELS.items()):
        col = cols[i % 2]
        
        with col:
            with st.expander(f"🎵 {label_info['name']}"):
                st.write(f"**Alapítva:** {label_info['founded']}")
                st.write(f"**Székhely:** {label_info['headquarters']}")
                st.write(f"**Website:** {label_info['website']}")
                
                # Logó URL megjelenítése
                st.write(f"**Logó URL:** {label_info['logo_url']}")
                
                # Egyedi letöltés gomb
                if st.button(f"📥 {label_info['name']} logó letöltése", key=f"download_{label_id}"):
                    filename = f"{label_id}_{label_info['name'].replace(' ', '_').replace('.', '')}.png"
                    with st.spinner(f"{label_info['name']} logó letöltése..."):
                        file_path = download_logo(label_info['logo_url'], filename, output_dir)
                        if file_path:
                            st.success(f"✅ {label_info['name']} logó letöltve!")
                        else:
                            st.error(f"❌ Hiba a {label_info['name']} logó letöltése során")
    
    # Információs szekció
    st.markdown("---")
    st.header("ℹ️ Információ")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Mit csinál ez az alkalmazás?")
        st.write("""
        - Letölti a major zenei kiadók logóit
        - PNG formátumban menti a fájlokat
        - Információkat szolgáltat a kiadókról
        - JSON fájlban menti a metaadatokat
        """)
    
    with col2:
        st.subheader("📁 Kimeneti fájlok")
        st.write("""
        - `{label_id}_{name}.png` - Logó fájlok
        - `download_results.json` - Letöltési eredmények
        - `labels_info.json` - Kiadók információi
        """)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "streamlit":
        streamlit_app()
    else:
        # Konzol verzió
        print("🎵 Major Record Labels Logo Downloader")
        print("=" * 50)
        
        output_dir = input("Kimeneti mappa neve (Enter = 'major_labels_logos'): ").strip()
        if not output_dir:
            output_dir = "major_labels_logos"
        
        results = download_all_major_labels(output_dir)
        create_labels_info_file(output_dir)
        
        print(f"\n🎉 Befejezve! Ellenőrizd a '{output_dir}' mappát.") 