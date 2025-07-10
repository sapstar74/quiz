import os
import requests
import time
from PIL import Image, ImageDraw, ImageFont

# Create directory for state seals
SEALS_DIR = 'us_state_seals_images'
os.makedirs(SEALS_DIR, exist_ok=True)

# Dictionary of US states with their abbreviations
US_STATES = [
    {"name": "Alabama", "abbreviation": "AL"},
    {"name": "Alaska", "abbreviation": "AK"},
    {"name": "Arizona", "abbreviation": "AZ"},
    {"name": "Arkansas", "abbreviation": "AR"},
    {"name": "California", "abbreviation": "CA"},
    {"name": "Colorado", "abbreviation": "CO"},
    {"name": "Connecticut", "abbreviation": "CT"},
    {"name": "Delaware", "abbreviation": "DE"},
    {"name": "Florida", "abbreviation": "FL"},
    {"name": "Georgia", "abbreviation": "GA"},
    {"name": "Hawaii", "abbreviation": "HI"},
    {"name": "Idaho", "abbreviation": "ID"},
    {"name": "Illinois", "abbreviation": "IL"},
    {"name": "Indiana", "abbreviation": "IN"},
    {"name": "Iowa", "abbreviation": "IA"},
    {"name": "Kansas", "abbreviation": "KS"},
    {"name": "Kentucky", "abbreviation": "KY"},
    {"name": "Louisiana", "abbreviation": "LA"},
    {"name": "Maine", "abbreviation": "ME"},
    {"name": "Maryland", "abbreviation": "MD"},
    {"name": "Massachusetts", "abbreviation": "MA"},
    {"name": "Michigan", "abbreviation": "MI"},
    {"name": "Minnesota", "abbreviation": "MN"},
    {"name": "Mississippi", "abbreviation": "MS"},
    {"name": "Missouri", "abbreviation": "MO"},
    {"name": "Montana", "abbreviation": "MT"},
    {"name": "Nebraska", "abbreviation": "NE"},
    {"name": "Nevada", "abbreviation": "NV"},
    {"name": "New Hampshire", "abbreviation": "NH"},
    {"name": "New Jersey", "abbreviation": "NJ"},
    {"name": "New Mexico", "abbreviation": "NM"},
    {"name": "New York", "abbreviation": "NY"},
    {"name": "North Carolina", "abbreviation": "NC"},
    {"name": "North Dakota", "abbreviation": "ND"},
    {"name": "Ohio", "abbreviation": "OH"},
    {"name": "Oklahoma", "abbreviation": "OK"},
    {"name": "Oregon", "abbreviation": "OR"},
    {"name": "Pennsylvania", "abbreviation": "PA"},
    {"name": "Rhode Island", "abbreviation": "RI"},
    {"name": "South Carolina", "abbreviation": "SC"},
    {"name": "South Dakota", "abbreviation": "SD"},
    {"name": "Tennessee", "abbreviation": "TN"},
    {"name": "Texas", "abbreviation": "TX"},
    {"name": "Utah", "abbreviation": "UT"},
    {"name": "Vermont", "abbreviation": "VT"},
    {"name": "Virginia", "abbreviation": "VA"},
    {"name": "Washington", "abbreviation": "WA"},
    {"name": "West Virginia", "abbreviation": "WV"},
    {"name": "Wisconsin", "abbreviation": "WI"},
    {"name": "Wyoming", "abbreviation": "WY"},
]

# Map of multiple potential URLs for each state
SEAL_URL_SOURCES = {
    # Formátum: állam rövidítés -> [url1, url2, url3...]
    # Az első működő URL-t használjuk
    "ALL": [
        # Wikimedia sablonok
        lambda abbr, name: f"https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Seal_of_{name.replace(' ', '_')}.svg/500px-Seal_of_{name.replace(' ', '_')}.svg.png",
        lambda abbr, name: f"https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Seal_of_{abbr}.svg/500px-Seal_of_{abbr}.svg.png",
        lambda abbr, name: f"https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/{name.replace(' ', '_')}_state_seal.svg/500px-{name.replace(' ', '_')}_state_seal.svg.png",
        lambda abbr, name: f"https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/{abbr}_state_seal.svg/500px-{abbr}_state_seal.svg.png",
        
        # Egyéb formátumok
        lambda abbr, name: f"https://www.50states.com/images/redesign/seals/{abbr.lower()}-seal.png",
        lambda abbr, name: f"https://www.50states.com/images/redesign/seals/{name.lower().replace(' ', '-')}-seal.png",
        lambda abbr, name: f"https://state.1keydata.com/state-seal/{abbr.lower()}-seal.png",
        lambda abbr, name: f"https://state.1keydata.com/state-seal/{name.lower().replace(' ', '-')}-seal.png"
    ],
    
    # Egyedi URL-ek államonként
    "AL": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Seal_of_Alabama.svg/500px-Seal_of_Alabama.svg.png",
        "https://www.netstate.com/states/symb/seals/images/al_seal_h.gif"
    ],
    "AK": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/State_Seal_of_Alaska.svg/500px-State_Seal_of_Alaska.svg.png",
        "https://www.netstate.com/states/symb/seals/images/ak_seal_h.gif"
    ],
    "AZ": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Arizona-StateSeal.svg/500px-Arizona-StateSeal.svg.png",
        "https://www.netstate.com/states/symb/seals/images/az_seal_h.gif"
    ],
    "AR": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Seal_of_Arkansas.svg/500px-Seal_of_Arkansas.svg.png", 
        "https://www.netstate.com/states/symb/seals/images/ar_seal_h.gif"
    ],
    "CA": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Seal_of_California.svg/500px-Seal_of_California.svg.png",
        "https://www.netstate.com/states/symb/seals/images/ca_seal_h.gif"
    ],
    "CO": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Seal_of_Colorado.svg/500px-Seal_of_Colorado.svg.png",
        "https://www.netstate.com/states/symb/seals/images/co_seal_h.gif"
    ],
    "CT": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Seal_of_Connecticut.svg/500px-Seal_of_Connecticut.svg.png",
        "https://www.netstate.com/states/symb/seals/images/ct_seal_h.gif"
    ],
    "DE": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Seal_of_Delaware.svg/500px-Seal_of_Delaware.svg.png",
        "https://www.netstate.com/states/symb/seals/images/de_seal_h.gif"
    ],
    "FL": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Seal_of_Florida.svg/500px-Seal_of_Florida.svg.png",
        "https://www.netstate.com/states/symb/seals/images/fl_seal_h.gif"
    ],
    "GA": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Seal_of_Georgia.svg/500px-Seal_of_Georgia.svg.png",
        "https://www.netstate.com/states/symb/seals/images/ga_seal_h.gif"
    ],
    "HI": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Seal_of_the_State_of_Hawaii.svg/500px-Seal_of_the_State_of_Hawaii.svg.png",
        "https://www.netstate.com/states/symb/seals/images/hi_seal_h.gif"
    ],
    "ID": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Seal_of_Idaho.svg/500px-Seal_of_Idaho.svg.png",
        "https://www.netstate.com/states/symb/seals/images/id_seal_h.gif"
    ],
    "IL": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Seal_of_Illinois.svg/500px-Seal_of_Illinois.svg.png",
        "https://www.netstate.com/states/symb/seals/images/il_seal_h.gif"
    ],
    "IN": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Indiana-StateSeal.svg/500px-Indiana-StateSeal.svg.png",
        "https://www.netstate.com/states/symb/seals/images/in_seal_h.gif"
    ],
    "IA": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Iowa-StateSeal.svg/500px-Iowa-StateSeal.svg.png",
        "https://www.netstate.com/states/symb/seals/images/ia_seal_h.gif"
    ],
    "KS": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Seal_of_Kansas.svg/500px-Seal_of_Kansas.svg.png",
        "https://www.netstate.com/states/symb/seals/images/ks_seal_h.gif"
    ],
    "KY": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Seal_of_Kentucky.svg/500px-Seal_of_Kentucky.svg.png",
        "https://www.netstate.com/states/symb/seals/images/ky_seal_h.gif"
    ],
    "LA": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Seal_of_Louisiana.svg/500px-Seal_of_Louisiana.svg.png",
        "https://www.netstate.com/states/symb/seals/images/la_seal_h.gif"
    ],
    "ME": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Seal_of_Maine.svg/500px-Seal_of_Maine.svg.png",
        "https://www.netstate.com/states/symb/seals/images/me_seal_h.gif"
    ],
    "MD": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Seal_of_Maryland_%28obverse%29.png/500px-Seal_of_Maryland_%28obverse%29.png",
        "https://www.netstate.com/states/symb/seals/images/md_seal_h.gif"
    ],
    "MA": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Seal_of_Massachusetts.svg/500px-Seal_of_Massachusetts.svg.png",
        "https://www.netstate.com/states/symb/seals/images/ma_seal_h.gif"
    ],
    "MI": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Seal_of_Michigan.svg/500px-Seal_of_Michigan.svg.png",
        "https://www.netstate.com/states/symb/seals/images/mi_seal_h.gif"
    ],
    "MN": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Seal_of_Minnesota.svg/500px-Seal_of_Minnesota.svg.png",
        "https://www.netstate.com/states/symb/seals/images/mn_seal_h.gif"
    ],
    "MS": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Seal_of_Mississippi_%282014%29.svg/500px-Seal_of_Mississippi_%282014%29.svg.png",
        "https://www.netstate.com/states/symb/seals/images/ms_seal_h.gif"
    ],
    "MO": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Seal_of_Missouri.svg/500px-Seal_of_Missouri.svg.png",
        "https://www.netstate.com/states/symb/seals/images/mo_seal_h.gif"
    ],
    "MT": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Montana_state_seal.png/500px-Montana_state_seal.png",
        "https://www.netstate.com/states/symb/seals/images/mt_seal_h.gif"
    ],
    "NE": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Seal_of_Nebraska.svg/500px-Seal_of_Nebraska.svg.png",
        "https://www.netstate.com/states/symb/seals/images/ne_seal_h.gif"
    ],
    "NV": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Nevada-StateSeal.svg/500px-Nevada-StateSeal.svg.png",
        "https://www.netstate.com/states/symb/seals/images/nv_seal_h.gif"
    ],
    "NH": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Seal_of_New_Hampshire.svg/500px-Seal_of_New_Hampshire.svg.png",
        "https://www.netstate.com/states/symb/seals/images/nh_seal_h.gif"
    ],
    "NJ": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Seal_of_New_Jersey.svg/500px-Seal_of_New_Jersey.svg.png",
        "https://www.netstate.com/states/symb/seals/images/nj_seal_h.gif"
    ],
    "NM": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Great_seal_of_the_state_of_New_Mexico.png/500px-Great_seal_of_the_state_of_New_Mexico.png",
        "https://www.netstate.com/states/symb/seals/images/nm_seal_h.gif"
    ],
    "NY": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Seal_of_New_York.svg/500px-Seal_of_New_York.svg.png",
        "https://www.netstate.com/states/symb/seals/images/ny_seal_h.gif"
    ],
    "NC": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Seal_of_North_Carolina.svg/500px-Seal_of_North_Carolina.svg.png",
        "https://www.netstate.com/states/symb/seals/images/nc_seal_h.gif"
    ],
    "ND": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/NorthDakotaStateSeal.svg/500px-NorthDakotaStateSeal.svg.png",
        "https://www.netstate.com/states/symb/seals/images/nd_seal_h.gif"
    ],
    "OH": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Seal_of_Ohio.svg/500px-Seal_of_Ohio.svg.png",
        "https://www.netstate.com/states/symb/seals/images/oh_seal_h.gif"
    ],
    "OK": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Seal_of_Oklahoma.svg/500px-Seal_of_Oklahoma.svg.png",
        "https://www.netstate.com/states/symb/seals/images/ok_seal_h.gif"
    ],
    "OR": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Seal_of_Oregon.svg/500px-Seal_of_Oregon.svg.png",
        "https://www.netstate.com/states/symb/seals/images/or_seal_h.gif"
    ],
    "PA": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Seal_of_Pennsylvania.svg/500px-Seal_of_Pennsylvania.svg.png",
        "https://www.netstate.com/states/symb/seals/images/pa_seal_h.gif"
    ],
    "RI": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Seal_of_Rhode_Island.svg/500px-Seal_of_Rhode_Island.svg.png",
        "https://www.netstate.com/states/symb/seals/images/ri_seal_h.gif"
    ],
    "SC": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Seal_of_South_Carolina.svg/500px-Seal_of_South_Carolina.svg.png",
        "https://www.netstate.com/states/symb/seals/images/sc_seal_h.gif"
    ],
    "SD": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/SouthDakotaStateSeal.svg/500px-SouthDakotaStateSeal.svg.png",
        "https://www.netstate.com/states/symb/seals/images/sd_seal_h.gif"
    ],
    "TN": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Seal_of_Tennessee.svg/500px-Seal_of_Tennessee.svg.png",
        "https://www.netstate.com/states/symb/seals/images/tn_seal_h.gif"
    ],
    "TX": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Seal_of_Texas.svg/500px-Seal_of_Texas.svg.png",
        "https://www.netstate.com/states/symb/seals/images/tx_seal_h.gif"
    ],
    "UT": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Seal_of_Utah.svg/500px-Seal_of_Utah.svg.png",
        "https://www.netstate.com/states/symb/seals/images/ut_seal_h.gif"
    ],
    "VT": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Seal_of_Vermont.svg/500px-Seal_of_Vermont.svg.png",
        "https://www.netstate.com/states/symb/seals/images/vt_seal_h.gif"
    ],
    "VA": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Seal_of_Virginia.svg/500px-Seal_of_Virginia.svg.png",
        "https://www.netstate.com/states/symb/seals/images/va_seal_h.gif"
    ],
    "WA": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Seal_of_Washington.svg/500px-Seal_of_Washington.svg.png",
        "https://www.netstate.com/states/symb/seals/images/wa_seal_h.gif"
    ],
    "WV": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Seal_of_West_Virginia.svg/500px-Seal_of_West_Virginia.svg.png",
        "https://www.netstate.com/states/symb/seals/images/wv_seal_h.gif"
    ],
    "WI": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Seal_of_Wisconsin.svg/500px-Seal_of_Wisconsin.svg.png",
        "https://www.netstate.com/states/symb/seals/images/wi_seal_h.gif"
    ],
    "WY": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Seal_of_Wyoming.svg/500px-Seal_of_Wyoming.svg.png",
        "https://www.netstate.com/states/symb/seals/images/wy_seal_h.gif"
    ]
}

def create_text_image(text, size=(200, 200), bg_color=(240, 240, 240), text_color=(0, 0, 0)):
    """Create a text image as a placeholder."""
    img = Image.new('RGB', size, color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # Use default font
    font = ImageFont.load_default()
    
    # Draw text centered
    text_lines = text.split('\n')
    y_position = size[1] // 2 - 10 * len(text_lines)
    
    for line in text_lines:
        # Approximate center position
        x_position = size[0] // 2 - 5 * len(line)  
        draw.text((x_position, y_position), line, font=font, fill=text_color)
        y_position += 20  # Move down for next line
    
    return img

def download_image(url, output_path, timeout=10):
    """Download an image from URL to the given path."""
    try:
        print(f"Downloading from {url}")
        response = requests.get(url, timeout=timeout)
        
        if response.status_code == 200:
            with open(output_path, 'wb') as f:
                f.write(response.content)
            print(f"Successfully downloaded to {output_path}")
            return True
        else:
            print(f"Failed with status code {response.status_code}")
            return False
    except Exception as e:
        print(f"Error downloading: {e}")
        return False

def download_state_seal(state_name, state_abbr):
    """Try to download a state seal from various sources."""
    output_path = os.path.join(SEALS_DIR, f"{state_abbr}.png")
    
    # If image already exists, skip download
    if os.path.exists(output_path):
        print(f"Skipping {state_name}, image already exists")
        return True
    
    success = False
    
    # Try state-specific URLs first
    if state_abbr in SEAL_URL_SOURCES:
        for url in SEAL_URL_SOURCES[state_abbr]:
            if download_image(url, output_path):
                success = True
                break
    
    # If no success yet, try general URL templates
    if not success:
        for url_template in SEAL_URL_SOURCES["ALL"]:
            try:
                url = url_template(state_abbr, state_name)
                if download_image(url, output_path):
                    success = True
                    break
            except Exception as e:
                print(f"Error creating URL: {e}")
    
    # If still no success, create a placeholder
    if not success:
        try:
            print(f"Creating placeholder for {state_name}")
            placeholder = create_text_image(f"Seal of\n{state_name}")
            placeholder.save(output_path)
            print(f"Created placeholder for {state_name}")
            success = True
        except Exception as e:
            print(f"Error creating placeholder: {e}")
    
    return success

def main():
    """Download all state seals."""
    print(f"Downloading state seals to directory: {SEALS_DIR}")
    
    success_count = 0
    for state in US_STATES:
        print(f"\nProcessing {state['name']} ({state['abbreviation']})...")
        if download_state_seal(state['name'], state['abbreviation']):
            success_count += 1
        
        # Add delay to avoid overwhelming servers
        time.sleep(0.5)
    
    print(f"\nDownload complete. Successfully processed {success_count} of {len(US_STATES)} states.")
    print(f"Images saved to {os.path.abspath(SEALS_DIR)}")

if __name__ == "__main__":
    main() 