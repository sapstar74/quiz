import requests
import os
import time
from PIL import Image
from io import BytesIO
import json
import shutil

# NHL csapatok adatai (ID és név)
NHL_TEAMS = [
    {"id": 1, "name": "New Jersey Devils"},
    {"id": 2, "name": "New York Islanders"},
    {"id": 3, "name": "New York Rangers"},
    {"id": 4, "name": "Philadelphia Flyers"},
    {"id": 5, "name": "Pittsburgh Penguins"},
    {"id": 6, "name": "Boston Bruins"},
    {"id": 7, "name": "Buffalo Sabres"},
    {"id": 8, "name": "Montréal Canadiens"},
    {"id": 9, "name": "Ottawa Senators"},
    {"id": 10, "name": "Toronto Maple Leafs"},
    {"id": 12, "name": "Carolina Hurricanes"},
    {"id": 13, "name": "Florida Panthers"},
    {"id": 14, "name": "Tampa Bay Lightning"},
    {"id": 15, "name": "Washington Capitals"},
    {"id": 16, "name": "Chicago Blackhawks"},
    {"id": 17, "name": "Detroit Red Wings"},
    {"id": 18, "name": "Nashville Predators"},
    {"id": 19, "name": "St. Louis Blues"},
    {"id": 20, "name": "Calgary Flames"},
    {"id": 21, "name": "Colorado Avalanche"},
    {"id": 22, "name": "Edmonton Oilers"},
    {"id": 23, "name": "Vancouver Canucks"},
    {"id": 24, "name": "Anaheim Ducks"},
    {"id": 25, "name": "Dallas Stars"},
    {"id": 26, "name": "Los Angeles Kings"},
    {"id": 28, "name": "San Jose Sharks"},
    {"id": 29, "name": "Columbus Blue Jackets"},
    {"id": 30, "name": "Minnesota Wild"},
    {"id": 52, "name": "Winnipeg Jets"},
    {"id": 53, "name": "Arizona Coyotes"},
    {"id": 54, "name": "Vegas Golden Knights"},
    {"id": 55, "name": "Seattle Kraken"}
]

def get_logo_urls(team_id, team_name):
    """
    Lehetséges URL-ek gyűjteménye az NHL csapatok logóihoz
    """
    # Tisztított név különböző formátumokban
    clean_name = team_name.lower().replace(' ', '-')
    short_name = team_name.split()[-1].lower()  # Utolsó szó (pl. "Devils" a "New Jersey Devils"-ből)
    
    # Lehetséges URL-ek különböző forrásokból (sorrendben próbáljuk)
    urls = [
        # NHL.com hivatalos API logók
        f"https://www.nhl.com/.image/ar_1:1,c_fill,g_auto,h_300,q_auto:best,w_300/MTg5MDEyMDc4MTEyODE5ODgw/team-{team_id}.png",
        f"https://www-league.nhlstatic.com/images/logos/teams-current-primary-light/{team_id}.svg",
        f"https://www-league.nhlstatic.com/images/logos/teams-current-primary-dark/{team_id}.svg",
        f"https://www.nhl.com/site-core/images/team/logo/{team_id}_dark.svg",
        
        # NHL.com alternatív logó formátumok
        f"https://www.nhl.com/site-core/images/team/logo/{team_id}.svg",
        f"https://www.nhl.com/.image/t_share/MTg1MjQxMDY4MTk5MDYxNTY0/{team_id}.png",
        
        # Külső források
        f"https://assets.nhle.com/logos/nhl/svg/{team_id}_light.svg",
        f"https://assets.nhle.com/logos/nhl/svg/{team_id}_dark.svg",
        
        # Más alternatív források
        f"https://cdn.freebiesupply.com/logos/large/2x/nhl-{clean_name}-logo-png-transparent.png",
        f"https://cdn.freebiesupply.com/logos/large/2x/{clean_name}-logo-png-transparent.png",
        f"https://loodibee.com/wp-content/uploads/nhl-{clean_name}-logo.png",
        f"https://1000logos.net/wp-content/uploads/{clean_name}-logo.png",
        f"https://a.espncdn.com/i/teamlogos/nhl/500/{short_name}.png"
    ]
    
    return urls

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
        
        # Ellenőrizzük, hogy tényleg kép-e
        content_type = response.headers.get('Content-Type', '').lower()
        if not ('image/' in content_type) and not ('svg+xml' in content_type):
            print(f"  Nem kép tartalom: {content_type}")
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
                    print(f"  SVG->PNG konvertálás sikertelen")
            except Exception as e:
                print(f"  SVG->PNG konvertálási hiba: {e}")
        
        print(f"  Kép sikeresen mentve: {output_path}")
        return output_path
    
    except Exception as e:
        print(f"  Hiba: {e}")
        return False

def download_team_logos(output_dir="logos", team_list=None):
    """
    Letölti az NHL csapatok logóit különböző forrásokból
    """
    os.makedirs(output_dir, exist_ok=True)
    print(f"NHL csapatok logóinak letöltése a {output_dir} mappába...")
    
    # Ha nincs megadva csapatlista, használjuk az összes csapatot
    if team_list is None:
        team_list = NHL_TEAMS
    
    # Eredmények tárolására
    successful_downloads = {}
    failed_teams = []
    
    for team in team_list:
        team_id = team["id"]
        team_name = team["name"]
        print(f"\nCsapat: {team_name} (ID: {team_id})")
        
        # Beszerezzük a lehetséges URL-ek listáját
        urls = get_logo_urls(team_id, team_name)
        
        # Próbáljuk meg letölteni a logót a különböző forrásokból
        logo_saved = False
        for url in urls:
            # Határozzuk meg a fájlkiterjesztést az URL alapján
            if url.lower().endswith('.svg'):
                ext = '.svg'
            elif url.lower().endswith('.png'):
                ext = '.png'
            elif url.lower().endswith('.jpg') or url.lower().endswith('.jpeg'):
                ext = '.jpg'
            else:
                ext = '.png'  # Alapértelmezett
            
            # Célútvonal a mentéshez
            file_name = f"{team_id}_{team_name.replace(' ', '_')}{ext}"
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
        
        if not logo_saved:
            print(f"Nem sikerült logót letölteni a {team_name} csapathoz.")
            failed_teams.append(team)
    
    # Összegzés
    print(f"\nÖsszesen {len(successful_downloads)} csapat logóját sikerült letölteni.")
    if failed_teams:
        print(f"{len(failed_teams)} csapathoz nem sikerült logót letölteni:")
        for team in failed_teams:
            print(f"  - {team['name']} (ID: {team['id']})")
    
    # Mentsük az eredményeket egy JSON fájlba a későbbi felhasználáshoz
    result_data = {
        "successful_downloads": {k: os.path.basename(v) for k, v in successful_downloads.items()},
        "failed_teams": [{"id": t["id"], "name": t["name"]} for t in failed_teams]
    }
    
    result_path = os.path.join(output_dir, "download_results.json")
    with open(result_path, 'w') as f:
        json.dump(result_data, f, indent=2)
    
    print(f"Eredmények mentve: {result_path}")
    return successful_downloads

def main():
    output_dir = "nhl_logos"
    
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
    print(f"\nSikeresen letöltött logók ellenőrzése...")
    for team_id, logo_path in logo_paths.items():
        team_name = next((t["name"] for t in NHL_TEAMS if t["id"] == team_id), "Ismeretlen")
        
        try:
            img = Image.open(logo_path)
            width, height = img.size
            print(f"{team_name}: {width}x{height} ({img.format})")
        except Exception as e:
            print(f"{team_name}: Hiba a kép ellenőrzésekor - {str(e)}")
    
    print(f"\nA letöltés befejeződött. A logók a következő mappában találhatók: {output_dir}")
    print(f"Összesen {len(logo_paths)} csapat logóját sikerült letölteni.")

if __name__ == "__main__":
    main() 