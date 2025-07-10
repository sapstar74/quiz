# Műszaki Berendezés Felismerő Projekt

Ez a projekt különböző képfelismerő technológiákat használ műszaki berendezések automatikus azonosítására ipari környezetben.

## Főbb funkciók

- **Képbetöltés és előfeldolgozás**: Különböző formátumú képek kezelése
- **Objektum detektálás**: OpenCV és haladó AI modellek használata
- **Berendezés osztályozás**: Műszaki berendezések kategorizálása
- **Eredmény vizualizálás**: Bounding box-ok és címkék megjelenítése
- **Jelentés generálás**: Részletes JSON jelentések készítése

## Támogatott berendezés kategóriák

### Elektromos berendezések
- Transzformátorok
- Generátorok
- Motorok
- Kapcsolótáblák
- Kapcsolók
- Relék

### Mechanikai berendezések
- Szivattyúk
- Kompresszorok
- Szelepek
- Csapágyak
- Fogaskerekek
- Turbinák

### Műszerezés
- Mérőműszerek
- Szenzorok
- Mérők
- Jeladók
- Vezérlők

### Csővezetékek
- Csövek
- Idomok
- Karimák
- Könyökök
- Elágazások
- Szűkítők

### HVAC berendezések
- Ventilátorok
- Légcsatornák
- Csillapítók
- Szűrők
- Hőcserélők

## Telepítés

1. **Projekt klónozása vagy letöltése**
```bash
git clone <repository_url>
cd equipment_recognition_project
```

2. **Python környezet beállítása**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Függőségek telepítése**
```bash
pip install -r requirements.txt
```

## Használat

### Alapvető használat

```bash
python equipment_recognition_project.py
```

A program bekéri a kép elérési útját és opcionálisan a Google Vision API kulcsot.

### Programozási interfész

```python
from equipment_recognition_project import EquipmentRecognizer

# Felismerő létrehozása
recognizer = EquipmentRecognizer()

# Kép feldolgozása
result = recognizer.process_image("path/to/image.jpg")

if result:
    print(f"Talált objektumok: {len(result['objects'])}")
    print(f"Eredmény kép: {result['result_image']}")
    print(f"Jelentés: {result['report']}")
```

## API integráció

### Google Vision API

1. Google Cloud Console-ban hozzon létre projektet
2. Vision API engedélyezése
3. API kulcs generálása
4. Kulcs megadása a programban

```python
api_key = "your_google_vision_api_key"
result = recognizer.process_image("image.jpg", api_key)
```

### Egyéb támogatott API-k

- **AWS Rekognition**: Amazon képfelismerő szolgáltatás
- **Azure Computer Vision**: Microsoft képfelismerő API
- **Roboflow**: Egyedi modellek betanítására

## Haladó funkciók

### YOLO modellek használata

```python
# YOLOv8 modell betöltése
from ultralytics import YOLO

model = YOLO('yolov8n.pt')
results = model('image.jpg')
```

### Egyedi modellek betanítása

1. **Adatkészlet előkészítése**
   - Képek gyűjtése
   - Annotáció (bounding box-ok)
   - Adatok felosztása (train/val/test)

2. **Modell betanítása**
```python
from ultralytics import YOLO

model = YOLO('yolov8n.pt')
model.train(data='dataset.yaml', epochs=100)
```

3. **Modell használata**
```python
model = YOLO('best.pt')
results = model('new_image.jpg')
```

## Eredmények struktúrája

### Objektum adatok
```json
{
  "id": 0,
  "equipment_type": "pump",
  "category": "mechanical",
  "confidence": 0.85,
  "bbox": [x, y, width, height],
  "area": 15000,
  "aspect_ratio": 1.2
}
```

### Jelentés struktúra
```json
{
  "timestamp": "2024-01-15T10:30:00",
  "input_image": "equipment.jpg",
  "total_objects": 5,
  "objects": [...],
  "summary": {
    "mechanical": 3,
    "electrical": 2
  }
}
```

## Hibaelhárítás

### Gyakori problémák

1. **OpenCV telepítési hiba**
```bash
pip install opencv-python-headless
```

2. **GPU támogatás TensorFlow-hoz**
```bash
pip install tensorflow-gpu
```

3. **Memória problémák nagy képeknél**
```python
# Kép átméretezése
image = cv2.resize(image, (800, 600))
```

## Teljesítmény optimalizálás

### CPU optimalizálás
- Képméret csökkentése
- Batch feldolgozás
- Multithreading használata

### GPU gyorsítás
```python
import torch
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
```

### Memória kezelés
```python
# Memória tisztítása
import gc
gc.collect()
```

## Bővítési lehetőségek

1. **Webcam támogatás**
2. **Valós idejű videó feldolgozás**
3. **Adatbázis integráció**
4. **Web interfész**
5. **Mobile alkalmazás**
6. **IoT szenzorok integrálása**

## Példák

### Gyári berendezések felismerése
- Szalagok
- Robotok
- Munkagépek

### Építőipari berendezések
- Daruk
- Exkavátorok
- Betonkeverők

### Közművek
- Villamos berendezések
- Vízi létesítmények
- Gázellátó rendszerek

## Licenc

MIT License - részletek a LICENSE fájlban.

## Támogatás

Problémák esetén kérjük nyisson issue-t a GitHub repository-ban vagy írjon emailt a support@example.com címre.

## Közreműködés

Pull request-ek és fejlesztési javaslatok szívesen fogadottak!

## Verziónapló

### v1.0.0
- Alapvető objektum detektálás
- OpenCV integráció
- Google Vision API támogatás
- Jelentés generálás

### Tervezett fejlesztések
- YOLOv8 integráció
- Egyedi modellek támogatása
- Web interfész
- Mobil alkalmazás 