"""
Műszaki berendezés felismerő projekt
Equipment Recognition Project

Ez a projekt különböző képfelismerő technológiákat használ műszaki berendezések azonosítására.
"""

import cv2
import numpy as np
import requests
import base64
import json
import os
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
from datetime import datetime
import logging

# Logging beállítása
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class EquipmentRecognizer:
    """Műszaki berendezések felismerésére szolgáló osztály."""
    
    def __init__(self):
        self.supported_formats = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
        self.results_dir = "recognition_results"
        os.makedirs(self.results_dir, exist_ok=True)
        
        # Előre definiált műszaki berendezés kategóriák
        self.equipment_categories = {
            'electrical': ['transformer', 'generator', 'motor', 'panel', 'switch', 'relay'],
            'mechanical': ['pump', 'compressor', 'valve', 'bearing', 'gear', 'turbine'],
            'instrumentation': ['gauge', 'sensor', 'meter', 'transmitter', 'controller'],
            'piping': ['pipe', 'fitting', 'flange', 'elbow', 'tee', 'reducer'],
            'hvac': ['fan', 'duct', 'damper', 'filter', 'coil', 'unit']
        }
    
    def load_image(self, image_path):
        """Kép betöltése és előfeldolgozása."""
        try:
            if not os.path.exists(image_path):
                raise FileNotFoundError(f"A kép nem található: {image_path}")
            
            # OpenCV-vel betöltés
            image_cv = cv2.imread(image_path)
            if image_cv is None:
                raise ValueError("Nem sikerült betölteni a képet")
            
            # PIL-lel is betöltés
            image_pil = Image.open(image_path)
            
            logger.info(f"Kép sikeresen betöltve: {image_path}")
            logger.info(f"Kép mérete: {image_cv.shape}")
            
            return image_cv, image_pil
            
        except Exception as e:
            logger.error(f"Hiba a kép betöltésekor: {str(e)}")
            return None, None
    
    def preprocess_image(self, image):
        """Kép előfeldolgozása a felismerés előtt."""
        try:
            # Szürkeárnyalatos konverzió
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Kontraszt javítása
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
            enhanced = clahe.apply(gray)
            
            # Élek detektálása
            edges = cv2.Canny(enhanced, 50, 150)
            
            # Zajcsökkentés
            denoised = cv2.bilateralFilter(image, 9, 75, 75)
            
            return {
                'original': image,
                'gray': gray,
                'enhanced': enhanced,
                'edges': edges,
                'denoised': denoised
            }
            
        except Exception as e:
            logger.error(f"Hiba az előfeldolgozáskor: {str(e)}")
            return None
    
    def detect_objects_opencv(self, image):
        """Objektum detektálás OpenCV-vel (alapvető megközelítés)."""
        try:
            # Kontúrok keresése
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            objects = []
            for i, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if area > 1000:  # Kis objektumok kiszűrése
                    x, y, w, h = cv2.boundingRect(contour)
                    
                    # Alapvető jellemzők kinyerése
                    aspect_ratio = float(w) / h
                    extent = float(area) / (w * h)
                    solidity = float(area) / cv2.contourArea(cv2.convexHull(contour))
                    
                    objects.append({
                        'id': i,
                        'bbox': (x, y, w, h),
                        'area': area,
                        'aspect_ratio': aspect_ratio,
                        'extent': extent,
                        'solidity': solidity,
                        'confidence': 0.5  # Alapértelmezett
                    })
            
            logger.info(f"OpenCV detektálás: {len(objects)} objektum találva")
            return objects
            
        except Exception as e:
            logger.error(f"Hiba az OpenCV detektáláskor: {str(e)}")
            return []
    
    def classify_equipment_basic(self, objects, image):
        """Alapvető berendezés osztályozás jellemzők alapján."""
        try:
            classified_objects = []
            
            for obj in objects:
                # Alapvető osztályozási logika
                aspect_ratio = obj['aspect_ratio']
                area = obj['area']
                solidity = obj['solidity']
                
                # Egyszerű szabályalapú osztályozás
                if aspect_ratio > 3:
                    equipment_type = 'pipe'
                    category = 'piping'
                elif aspect_ratio < 0.3:
                    equipment_type = 'pipe'
                    category = 'piping'
                elif 0.8 <= aspect_ratio <= 1.2:
                    if area > 10000:
                        equipment_type = 'tank'
                        category = 'mechanical'
                    else:
                        equipment_type = 'valve'
                        category = 'mechanical'
                elif solidity > 0.9:
                    equipment_type = 'panel'
                    category = 'electrical'
                else:
                    equipment_type = 'unknown'
                    category = 'unknown'
                
                classified_objects.append({
                    **obj,
                    'equipment_type': equipment_type,
                    'category': category,
                    'classification_method': 'basic_rules'
                })
            
            return classified_objects
            
        except Exception as e:
            logger.error(f"Hiba az osztályozáskor: {str(e)}")
            return objects
    
    def google_vision_api_detect(self, image_path, api_key):
        """Google Vision API használata objektum detektáláshoz."""
        try:
            if not api_key:
                logger.warning("Google Vision API kulcs nem található")
                return []
            
            # Kép base64 enkódolása
            with open(image_path, "rb") as image_file:
                image_content = base64.b64encode(image_file.read()).decode()
            
            # API hívás
            url = f"https://vision.googleapis.com/v1/images:annotate?key={api_key}"
            
            payload = {
                "requests": [{
                    "image": {"content": image_content},
                    "features": [
                        {"type": "OBJECT_LOCALIZATION", "maxResults": 50},
                        {"type": "LABEL_DETECTION", "maxResults": 50}
                    ]
                }]
            }
            
            response = requests.post(url, json=payload)
            
            if response.status_code == 200:
                result = response.json()
                objects = []
                
                # Objektum lokalizáció eredményei
                if 'localizedObjectAnnotations' in result['responses'][0]:
                    for obj in result['responses'][0]['localizedObjectAnnotations']:
                        objects.append({
                            'name': obj['name'],
                            'confidence': obj['score'],
                            'bbox': obj['boundingPoly']['normalizedVertices'],
                            'source': 'google_vision'
                        })
                
                logger.info(f"Google Vision API: {len(objects)} objektum detektálva")
                return objects
            else:
                logger.error(f"Google Vision API hiba: {response.status_code}")
                return []
                
        except Exception as e:
            logger.error(f"Hiba a Google Vision API híváskor: {str(e)}")
            return []
    
    def visualize_results(self, image, objects, output_path):
        """Eredmények vizualizálása."""
        try:
            result_image = image.copy()
            
            for obj in objects:
                # Bounding box rajzolása
                if 'bbox' in obj and len(obj['bbox']) == 4:
                    x, y, w, h = obj['bbox']
                    cv2.rectangle(result_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    
                    # Label hozzáadása
                    label = f"{obj.get('equipment_type', 'unknown')} ({obj.get('confidence', 0):.2f})"
                    cv2.putText(result_image, label, (x, y - 10), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            
            # Eredmény mentése
            cv2.imwrite(output_path, result_image)
            logger.info(f"Eredmény kép mentve: {output_path}")
            
            return result_image
            
        except Exception as e:
            logger.error(f"Hiba a vizualizáláskor: {str(e)}")
            return image
    
    def generate_report(self, objects, image_path, output_path):
        """Részletes jelentés generálása."""
        try:
            report = {
                'timestamp': datetime.now().isoformat(),
                'input_image': image_path,
                'total_objects': len(objects),
                'objects': objects,
                'summary': {}
            }
            
            # Összefoglaló statisztikák
            categories = {}
            for obj in objects:
                category = obj.get('category', 'unknown')
                if category in categories:
                    categories[category] += 1
                else:
                    categories[category] = 1
            
            report['summary'] = categories
            
            # JSON fájlba mentés
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            
            logger.info(f"Jelentés mentve: {output_path}")
            return report
            
        except Exception as e:
            logger.error(f"Hiba a jelentés generáláskor: {str(e)}")
            return None
    
    def process_image(self, image_path, api_key=None):
        """Teljes képfeldolgozási pipeline."""
        try:
            logger.info(f"Kép feldolgozása elkezdődött: {image_path}")
            
            # Kép betöltése
            image_cv, image_pil = self.load_image(image_path)
            if image_cv is None:
                return None
            
            # Előfeldolgozás
            processed = self.preprocess_image(image_cv)
            if processed is None:
                return None
            
            # Objektum detektálás OpenCV-vel
            objects_cv = self.detect_objects_opencv(image_cv)
            
            # Berendezés osztályozás
            classified_objects = self.classify_equipment_basic(objects_cv, image_cv)
            
            # Google Vision API (ha van API kulcs)
            objects_gv = []
            if api_key:
                objects_gv = self.google_vision_api_detect(image_path, api_key)
            
            # Eredmények kombinálása
            all_objects = classified_objects + objects_gv
            
            # Fájlnév generálása
            base_name = os.path.splitext(os.path.basename(image_path))[0]
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            # Eredmény vizualizálása
            result_image_path = os.path.join(self.results_dir, f"{base_name}_result_{timestamp}.jpg")
            self.visualize_results(image_cv, classified_objects, result_image_path)
            
            # Jelentés generálása
            report_path = os.path.join(self.results_dir, f"{base_name}_report_{timestamp}.json")
            report = self.generate_report(all_objects, image_path, report_path)
            
            logger.info("Képfeldolgozás befejezve")
            
            return {
                'objects': all_objects,
                'result_image': result_image_path,
                'report': report_path,
                'summary': report['summary'] if report else {}
            }
            
        except Exception as e:
            logger.error(f"Hiba a képfeldolgozáskor: {str(e)}")
            return None


def main():
    """Főprogram - használati példa."""
    
    # Equipment recognizer létrehozása
    recognizer = EquipmentRecognizer()
    
    print("=== Műszaki Berendezés Felismerő ===")
    print("Támogatott formátumok:", recognizer.supported_formats)
    print("Eredmények mappája:", recognizer.results_dir)
    print()
    
    # Használati példa
    image_path = input("Adja meg a kép elérési útját (vagy nyomjon Entert a kilépéshez): ").strip()
    
    if not image_path:
        print("Kilépés...")
        return
    
    if not os.path.exists(image_path):
        print(f"A fájl nem található: {image_path}")
        return
    
    # Google Vision API kulcs (opcionális)
    api_key = input("Google Vision API kulcs (opcionális, Enter = kihagyás): ").strip()
    if not api_key:
        api_key = None
    
    # Képfeldolgozás
    print("\nKépfeldolgozás folyamatban...")
    result = recognizer.process_image(image_path, api_key)
    
    if result:
        print("\n=== Eredmények ===")
        print(f"Talált objektumok száma: {len(result['objects'])}")
        print(f"Eredmény kép: {result['result_image']}")
        print(f"Jelentés: {result['report']}")
        print("\nKategóriák szerint:")
        for category, count in result['summary'].items():
            print(f"  {category}: {count} db")
    else:
        print("Hiba történt a feldolgozás során.")


if __name__ == "__main__":
    main() 