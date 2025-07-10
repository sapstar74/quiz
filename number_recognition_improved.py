#!/usr/bin/env python3
"""
Javított szám felismerő szkript
Használat: python number_recognition_improved.py <kép_fájl>

Ez a javított verzió jobban kezeli a kapcsolódó számjegyeket.
"""

import sys
import cv2
import numpy as np
import pytesseract
from PIL import Image
import argparse
import os
import re

def preprocess_image(image_path):
    """
    Előfeldolgozza a képet a jobb OCR eredmény érdekében
    """
    # Kép betöltése
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Nem sikerült betölteni a képet: {image_path}")
    
    # Szürkeárnyalatosra konvertálás
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Kép átméretezése (nagyobb kép = jobb OCR)
    height, width = gray.shape
    if height < 100:
        scale_factor = 100 / height
        new_width = int(width * scale_factor)
        gray = cv2.resize(gray, (new_width, 100), interpolation=cv2.INTER_CUBIC)
    
    # Kontraszt javítása
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    enhanced = clahe.apply(gray)
    
    # Zajszűrés
    denoised = cv2.medianBlur(enhanced, 3)
    
    # Binarizálás (fekete-fehér)
    _, binary = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Morfológiai művelet - bezárás a számjegyek összekapcsolásához
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 1))
    cleaned = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    
    return cleaned, gray, img

def extract_numbers_multiple_configs(image):
    """
    Többféle Tesseract konfigurációval próbálkozik
    """
    configs = [
        '--oem 3 --psm 8 -c tessedit_char_whitelist=0123456789',  # Egy szó
        '--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789',  # Egy sor
        '--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789',  # Szövegblokk
        '--oem 3 --psm 13 -c tessedit_char_whitelist=0123456789', # Nyers sor
        '--oem 3 --psm 10 -c tessedit_char_whitelist=0123456789'  # Egy karakter
    ]
    
    all_results = []
    raw_texts = []
    
    for config in configs:
        try:
            text = pytesseract.image_to_string(image, config=config)
            raw_texts.append(text.strip())
            
            # Számok kinyerése - folytonos számjegyek csoportosítása
            numbers = re.findall(r'\d+', text.strip())
            all_results.extend(numbers)
        except:
            continue
    
    # Deduplikálás hossz szerint rendezve (hosszabb számok előnyben)
    unique_numbers = list(set(all_results))
    unique_numbers.sort(key=len, reverse=True)
    
    return unique_numbers, raw_texts

def find_number_regions(image):
    """
    Megtalálja a számokat tartalmazó régiókat
    """
    # Kontúrok keresése
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Régió kandidátusok
    regions = []
    
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 50:  # Minimális terület
            x, y, w, h = cv2.boundingRect(contour)
            
            # Méret ellenőrzése
            if w > 10 and h > 10:
                regions.append((x, y, w, h, area))
    
    # Rendezés balról jobbra
    regions.sort(key=lambda r: r[0])
    
    return regions

def extract_numbers_regional(image):
    """
    Régió alapú számfelismerés
    """
    regions = find_number_regions(image)
    numbers = []
    
    for x, y, w, h, area in regions:
        # ROI kivágása
        roi = image[y:y+h, x:x+w]
        
        # ROI méretének növelése ha szükséges
        if roi.shape[0] < 30 or roi.shape[1] < 30:
            roi = cv2.resize(roi, (max(30, roi.shape[1]*2), max(30, roi.shape[0]*2)), 
                           interpolation=cv2.INTER_CUBIC)
        
        # OCR a ROI-n
        config = '--oem 3 --psm 8 -c tessedit_char_whitelist=0123456789'
        try:
            text = pytesseract.image_to_string(roi, config=config)
            found_numbers = re.findall(r'\d+', text.strip())
            numbers.extend(found_numbers)
        except:
            continue
    
    return numbers

def recognize_numbers(image_path, debug=False):
    """
    Fő függvény a számok felismerésére
    """
    try:
        # Kép előfeldolgozása
        processed_img, gray_img, original_img = preprocess_image(image_path)
        
        # Debug képek mentése ha szükséges
        if debug:
            cv2.imwrite('debug_gray.png', gray_img)
            cv2.imwrite('debug_processed.png', processed_img)
            print("Debug képek mentve: debug_gray.png, debug_processed.png")
        
        # Többféle módszer használata
        numbers_multi, raw_texts = extract_numbers_multiple_configs(processed_img)
        numbers_regional = extract_numbers_regional(processed_img)
        
        # Eredmények kombinálása
        all_numbers = numbers_multi + numbers_regional
        
        # Deduplikálás és rendezés
        unique_numbers = []
        seen = set()
        
        # Először a hosszabb számok
        for num in sorted(all_numbers, key=len, reverse=True):
            if num not in seen and len(num) > 0:
                unique_numbers.append(num)
                seen.add(num)
        
        return {
            'numbers': unique_numbers,
            'multi_config_numbers': numbers_multi,
            'regional_numbers': numbers_regional,
            'raw_texts': raw_texts
        }
        
    except Exception as e:
        return {'error': str(e)}

def main():
    parser = argparse.ArgumentParser(description='Javított számok felismerése képeken')
    parser.add_argument('image_path', help='A feldolgozandó kép útvonala')
    parser.add_argument('--debug', action='store_true', help='Debug információk és képek mentése')
    parser.add_argument('--verbose', action='store_true', help='Részletes kimenet')
    
    args = parser.parse_args()
    
    # Kép létezésének ellenőrzése
    if not os.path.exists(args.image_path):
        print(f"Hiba: A kép nem található: {args.image_path}")
        sys.exit(1)
    
    # Számok felismerése
    result = recognize_numbers(args.image_path, debug=args.debug)
    
    if 'error' in result:
        print(f"Hiba: {result['error']}")
        sys.exit(1)
    
    # Eredmények kiírása
    print(f"Kép: {args.image_path}")
    print("-" * 50)
    
    if args.verbose:
        print(f"Többféle konfiguráció: {result['multi_config_numbers']}")
        print(f"Régió alapú: {result['regional_numbers']}")
        if args.debug:
            print("Nyers szövegek:")
            for i, text in enumerate(result['raw_texts']):
                print(f"  Config {i+1}: '{text}'")
        print("-" * 50)
    
    # Fő eredmény
    if result['numbers']:
        print(f"Felismert számok: {', '.join(result['numbers'])}")
        
        # Legnagyobb szám kiírása (gyakran ez a főszám)
        if result['numbers']:
            main_number = max(result['numbers'], key=len)
            print(f"Főszám (leghosszabb): {main_number}")
    else:
        print("Nem sikerült számokat felismerni a képen.")

if __name__ == "__main__":
    main() 