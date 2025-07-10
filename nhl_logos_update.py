import requests
import os
import time
from PIL import Image
import json
import shutil

# NHL csapatok adatai ID, név és rövidítés
NHL_TEAMS = [
    {"id": 1, "name": "New Jersey Devils", "abbreviation": "NJD"},
    {"id": 2, "name": "New York Islanders", "abbreviation": "NYI"},
    {"id": 3, "name": "New York Rangers", "abbreviation": "NYR"},
    {"id": 4, "name": "Philadelphia Flyers", "abbreviation": "PHI"},
    {"id": 5, "name": "Pittsburgh Penguins", "abbreviation": "PIT"},
    {"id": 6, "name": "Boston Bruins", "abbreviation": "BOS"},
    {"id": 7, "name": "Buffalo Sabres", "abbreviation": "BUF"},
    {"id": 8, "name": "Montréal Canadiens", "abbreviation": "MTL"},
    {"id": 9, "name": "Ottawa Senators", "abbreviation": "OTT"},
    {"id": 10, "name": "Toronto Maple Leafs", "abbreviation": "TOR"},
    {"id": 12, "name": "Carolina Hurricanes", "abbreviation": "CAR"},
    {"id": 13, "name": "Florida Panthers", "abbreviation": "FLA"},
    {"id": 14, "name": "Tampa Bay Lightning", "abbreviation": "TBL"},
    {"id": 15, "name": "Washington Capitals", "abbreviation": "WSH"},
    {"id": 16, "name": "Chicago Blackhawks", "abbreviation": "CHI"},
    {"id": 17, "name": "Detroit Red Wings", "abbreviation": "DET"},
    {"id": 18, "name": "Nashville Predators", "abbreviation": "NSH"},
    {"id": 19, "name": "St. Louis Blues", "abbreviation": "STL"},
    {"id": 20, "name": "Calgary Flames", "abbreviation": "CGY"},
    {"id": 21, "name": "Colorado Avalanche", "abbreviation": "COL"},
    {"id": 22, "name": "Edmonton Oilers", "abbreviation": "EDM"},
    {"id": 23, "name": "Vancouver Canucks", "abbreviation": "VAN"},
    {"id": 24, "name": "Anaheim Ducks", "abbreviation": "ANA"},
    {"id": 25, "name": "Dallas Stars", "abbreviation": "DAL"},
    {"id": 26, "name": "Los Angeles Kings", "abbreviation": "LAK"},
    {"id": 28, "name": "San Jose Sharks", "abbreviation": "SJS"},
    {"id": 29, "name": "Columbus Blue Jackets", "abbreviation": "CBJ"},
    {"id": 30, "name": "Minnesota Wild", "abbreviation": "MIN"},
    {"id": 52, "name": "Winnipeg Jets", "abbreviation": "WPG"},
    {"id": 53, "name": "Arizona Coyotes", "abbreviation": "ARI"},
    {"id": 54, "name": "Vegas Golden Knights", "abbreviation": "VGK"},
    {"id": 55, "name": "Seattle Kraken", "abbreviation": "SEA"}
]

def get_logo_urls(team_id, team_name, abbreviation):
    """
    Lehetséges URL-ek gyűjteménye az NHL csapatok logóihoz
    """
    return [
        # Az új URL rövidítésekkel
        f"http://assets.nhle.com/logos/nhl/svg/{abbreviation}_dark.svg",
        f"http://assets.nhle.com/logos/nhl/svg/{abbreviation}_light.svg",
        
        # A régi URL formátumok tartalékként
        f"https://www-league.nhlstatic.com/images/logos/teams-current-primary-light/{team_id}.svg",
        f"https://www-league.nhlstatic.com/images/logos/teams-current-primary-dark/{team_id}.svg"
    ]

def save_image_from_url(url, output_path, timeout=10):
    """
    Mentse el a képet az URL-ről a megadott kimeneti útvonalra
    """
    try:
        print(f"Próbálkozás: {url}")
        response = requests.get(url, timeout=timeout)
        
        if response.status_code != 200:
            print(f"  Sikertelen kérés: {response.status_code}")
            return False
        
        # Mentsük a képet
        with open(output_path, 'wb') as f:
            f.write(response.content)
        
        # SVG -> PNG konvertálás, ha szükséges
        if output_path.lower().endswith('.svg'):
            png_path = output_path.replace('.svg', '.png')
            try:
                # Próbáljuk konvertálni az SVG-t
                print(f"  SVG->PNG konvertálási kísérlet...")
                
                # Opcionális módszer: inkscape, ha elérhető
                inkscape_cmd = f"inkscape --export-filename={png_path} {output_path}"
                result = os.system(inkscape_cmd)
                
                if result == 0 and os.path.exists(png_path):
                    print(f"  SVG->PNG konvertálás sikeres: {png_path}")
                    return png_path
                else:
                    print(f"  SVG->PNG konvertálás sikertelen - az eredeti SVG fájl marad")
            except Exception as e:
                print(f"  SVG->PNG konvertálási hiba: {e}")
        
        print(f"  Kép sikeresen mentve: {output_path}")
        return output_path
    
    except Exception as e:
        print(f"  Hiba: {e}")
        return False

def create_text_image(text, output_path, width=200, height=200, bg_color=(240, 240, 240), text_color=(0, 0, 0)):
    """
    Egyszerű szöveges kép létrehozása ha nem sikerül letölteni
    """
    from PIL import Image, ImageDraw, ImageFont
    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    try:
        # Alapértelmezett font
        font = ImageFont.load_default()
        
        # Kirajzoljuk a szöveget középre
        text_width = draw.textlength(text, font=font) if hasattr(draw, 'textlength') else font.getlength(text) if hasattr(font, 'getlength') else len(text) * 8
        text_height = font.getbbox(text)[3] if hasattr(font, 'getbbox') else 15
        
        x_position = (width - text_width) // 2
        y_position = (height - text_height) // 2
        
        # Háttér a szöveg alatt
        draw.rectangle([x_position - 10, y_position - 10, x_position + text_width + 10, y_position + text_height + 10], fill=(200, 200, 240))
        
        # Szöveg
        draw.text((x_position, y_position), text, fill=text_color, font=font)
    except Exception as e:
        print(f"Hiba a szöveg kirajzolásakor: {str(e)}")
    
    img.save(output_path)
    return output_path

def download_team_logos(output_dir="nhl_logos_new"):
    """
    Letölti az NHL csapatok logóit
    """
    os.makedirs(output_dir, exist_ok=True)
    print(f"NHL csapatok logóinak letöltése a {output_dir} mappába...")
    
    successful_downloads = {}
    failed_teams = []
    
    for team in NHL_TEAMS:
        team_id = team["id"]
        team_name = team["name"]
        abbreviation = team["abbreviation"]
        
        print(f"\nCsapat: {team_name} (ID: {team_id}, Rövidítés: {abbreviation})")
        
        # Beszerezzük a lehetséges URL-ek listáját
        urls = get_logo_urls(team_id, team_name, abbreviation)
        
        # Próbáljuk meg letölteni a logót a különböző forrásokból
        logo_saved = False
        for url in urls:
            # Határozzuk meg a fájlkiterjesztést az URL alapján
            if url.lower().endswith('.svg'):
                ext = '.svg'
            elif url.lower().endswith('.png'):
                ext = '.png'
            else:
                ext = '.png'  # Alapértelmezett
            
            # Célútvonal a mentéshez
            file_name = f"{team_id}_{abbreviation}_{team_name.replace(' ', '_')}{ext}"
            output_path = os.path.join(output_dir, file_name)
            
            # Kísérlet a letöltésre
            result = save_image_from_url(url, output_path)
            if result:
                if isinstance(result, str) and result.endswith('.png'):
                    # Ha SVG->PNG konvertálás történt, frissítsük az elérési utat
                    successful_downloads[team_id] = result
                else:
                    successful_downloads[team_id] = output_path
                logo_saved = True
                break
            
            # Várjunk egy kicsit a következő próbálkozás előtt
            time.sleep(0.5)
        
        # Ha nem sikerült letölteni, készítsünk helyettesítő képet
        if not logo_saved:
            print(f"Nem sikerült logót letölteni a {team_name} csapathoz. Helyettesítő kép készítése...")
            placeholder_path = os.path.join(output_dir, f"{team_id}_{abbreviation}_placeholder.png")
            create_text_image(f"{team_name}\n({abbreviation})", placeholder_path)
            successful_downloads[team_id] = placeholder_path
            failed_teams.append(team)
    
    # Összegzés
    print(f"\nÖsszesen {len(successful_downloads)} csapat logója sikeresen letöltve vagy helyettesítve.")
    if failed_teams:
        print(f"{len(failed_teams)} csapathoz nem sikerült valódi logót letölteni:")
        for team in failed_teams:
            print(f"  - {team['name']} ({team['abbreviation']})")
    
    # Mentsük az eredményeket egy JSON fájlba
    result_data = {
        "successful_downloads": {
            str(k): {
                "path": os.path.basename(v),
                "team_name": next((t["name"] for t in NHL_TEAMS if t["id"] == k), "Unknown"),
                "abbreviation": next((t["abbreviation"] for t in NHL_TEAMS if t["id"] == k), "")
            } for k, v in successful_downloads.items()
        },
        "failed_teams": [{"id": t["id"], "name": t["name"], "abbreviation": t["abbreviation"]} for t in failed_teams]
    }
    
    result_path = os.path.join(output_dir, "download_results.json")
    with open(result_path, 'w', encoding='utf-8') as f:
        json.dump(result_data, f, indent=2)
    
    print(f"Eredmények mentve: {result_path}")
    return successful_downloads

def check_downloaded_images(logo_paths):
    """
    Ellenőrizzük a letöltött képeket, méretüket és formátumukat
    """
    print(f"\nSikeresen letöltött logók ellenőrzése...")
    
    for team_id, logo_path in logo_paths.items():
        team = next((t for t in NHL_TEAMS if t["id"] == team_id), None)
        if not team:
            continue
            
        team_name = team["name"]
        abbreviation = team["abbreviation"]
        
        try:
            with Image.open(logo_path) as img:
                width, height = img.size
                format_name = img.format
                print(f"{team_name} ({abbreviation}): {width}x{height} {format_name}")
        except Exception as e:
            print(f"{team_name} ({abbreviation}): Hiba a kép ellenőrzésekor - {str(e)}")

def main():
    output_dir = "nhl_logos_new"
    
    # Ellenőrizzük, hogy létezik-e már a mappa és van-e benne tartalom
    if os.path.exists(output_dir) and os.listdir(output_dir):
        print(f"A(z) {output_dir} mappa már létezik és tartalmaz fájlokat.")
        overwrite = input("Felülírjuk a meglévő mappát? (i/n): ").lower() == 'i'
        if overwrite:
            # Töröljük a meglévő mappát és tartalmát
            shutil.rmtree(output_dir)
        else:
            print("Letöltés megszakítva.")
            return
    
    # Letöltjük a logókat
    logo_paths = download_team_logos(output_dir)
    
    # Ellenőrizzük a letöltött képeket
    check_downloaded_images(logo_paths)
    
    print(f"\nA letöltés befejeződött. A logók a következő mappában találhatók: {output_dir}")
    print(f"Összesen {len(logo_paths)} csapat logóját sikerült letölteni.")

if __name__ == "__main__":
    main() 