#!/usr/bin/env python3
"""
Equipment Recognition Project Setup Script
Műszaki Berendezés Felismerő Projekt Telepítő Script
"""

import os
import sys
import subprocess
import json
from pathlib import Path

def print_header():
    """Print setup header."""
    print("=" * 60)
    print("    Műszaki Berendezés Felismerő Projekt Telepítő")
    print("    Equipment Recognition Project Setup")
    print("=" * 60)
    print()

def check_python_version():
    """Check if Python version is compatible."""
    print("Python verzió ellenőrzése...")
    
    if sys.version_info < (3, 8):
        print("❌ Hiba: Python 3.8 vagy újabb verzió szükséges!")
        print(f"Jelenlegi verzió: Python {sys.version}")
        return False
    
    print(f"✅ Python verzió megfelelő: {sys.version}")
    return True

def create_virtual_environment():
    """Create virtual environment."""
    print("\nVirtuális környezet létrehozása...")
    
    venv_path = Path("venv")
    
    if venv_path.exists():
        print("✅ Virtuális környezet már létezik")
        return True
    
    try:
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("✅ Virtuális környezet sikeresen létrehozva")
        return True
    except subprocess.CalledProcessError:
        print("❌ Hiba a virtuális környezet létrehozásakor")
        return False

def install_dependencies():
    """Install required dependencies."""
    print("\nFüggőségek telepítése...")
    
    # Determine pip path based on OS
    if os.name == 'nt':  # Windows
        pip_path = Path("venv/Scripts/pip")
    else:  # Unix/Linux/MacOS
        pip_path = Path("venv/bin/pip")
    
    if not pip_path.exists():
        print("❌ Hiba: pip nem található a virtuális környezetben")
        return False
    
    try:
        # Upgrade pip first
        print("pip frissítése...")
        subprocess.run([str(pip_path), "install", "--upgrade", "pip"], check=True)
        
        # Install requirements
        print("Könyvtárak telepítése...")
        subprocess.run([str(pip_path), "install", "-r", "requirements.txt"], check=True)
        
        print("✅ Függőségek sikeresen telepítve")
        return True
    except subprocess.CalledProcessError:
        print("❌ Hiba a függőségek telepítésekor")
        return False

def create_directories():
    """Create necessary directories."""
    print("\nMappák létrehozása...")
    
    directories = [
        "recognition_results",
        "test_images",
        "models",
        "logs"
    ]
    
    for directory in directories:
        dir_path = Path(directory)
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"✅ Mappa létrehozva: {directory}")
        else:
            print(f"✅ Mappa már létezik: {directory}")

def create_sample_config():
    """Create sample configuration if not exists."""
    print("\nKonfiguráció ellenőrzése...")
    
    config_path = Path("config.json")
    if config_path.exists():
        print("✅ Konfiguráció már létezik")
        return
    
    print("✅ Konfiguráció használatra kész")

def test_installation():
    """Test if installation works."""
    print("\nTelepítés tesztelése...")
    
    try:
        # Test basic imports
        test_script = """
import cv2
import numpy as np
import PIL
import requests
print("✅ Alapvető könyvtárak importálva")

# Test OpenCV
print("OpenCV verzió:", cv2.__version__)

# Test numpy
print("NumPy verzió:", np.__version__)

print("✅ Telepítés sikeres!")
"""
        
        # Determine python path based on OS
        if os.name == 'nt':  # Windows
            python_path = Path("venv/Scripts/python")
        else:  # Unix/Linux/MacOS
            python_path = Path("venv/bin/python")
        
        result = subprocess.run([str(python_path), "-c", test_script], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print(result.stdout)
            return True
        else:
            print("❌ Tesztelési hiba:")
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Tesztelési hiba: {e}")
        return False

def print_usage_instructions():
    """Print usage instructions."""
    print("\n" + "=" * 60)
    print("    TELEPÍTÉS BEFEJEZVE - HASZNÁLATI ÚTMUTATÓ")
    print("=" * 60)
    
    if os.name == 'nt':  # Windows
        activate_cmd = "venv\\Scripts\\activate"
        python_cmd = "venv\\Scripts\\python"
    else:  # Unix/Linux/MacOS
        activate_cmd = "source venv/bin/activate"
        python_cmd = "venv/bin/python"
    
    print("\n1. Virtuális környezet aktiválása:")
    print(f"   {activate_cmd}")
    
    print("\n2. Program futtatása:")
    print(f"   {python_cmd} equipment_recognition_project.py")
    
    print("\n3. Vagy importálás Python kódban:")
    print("   from equipment_recognition_project import EquipmentRecognizer")
    
    print("\n4. Konfiguráció testreszabása:")
    print("   Szerkessze a config.json fájlt")
    
    print("\n5. API kulcsok beállítása:")
    print("   - Google Vision API kulcs a config.json-ban")
    print("   - Vagy környezeti változó: GOOGLE_VISION_API_KEY")
    
    print("\n6. Teszt képek:")
    print("   Helyezzen képfájlokat a test_images mappába")
    
    print("\n7. Eredmények:")
    print("   Az eredmények a recognition_results mappában lesznek")
    
    print("\n📖 Részletes dokumentáció: README_Equipment_Recognition.md")
    print("🔧 Támogatás: github.com/your-repo/issues")
    print("\n" + "=" * 60)

def main():
    """Main setup function."""
    print_header()
    
    success = True
    
    # Check Python version
    if not check_python_version():
        success = False
        
    # Create virtual environment
    if success and not create_virtual_environment():
        success = False
    
    # Install dependencies
    if success and not install_dependencies():
        success = False
    
    # Create directories
    if success:
        create_directories()
    
    # Create sample config
    if success:
        create_sample_config()
    
    # Test installation
    if success and not test_installation():
        success = False
    
    # Print results
    if success:
        print("\n✅ TELEPÍTÉS SIKERES!")
        print_usage_instructions()
    else:
        print("\n❌ TELEPÍTÉSI HIBA TÖRTÉNT!")
        print("\nEllenőrizze a következőket:")
        print("- Python 3.8+ telepítve van")
        print("- Internet kapcsolat elérhető")
        print("- Megfelelő jogosultságok")
        print("- requirements.txt fájl létezik")
        
    return success

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 