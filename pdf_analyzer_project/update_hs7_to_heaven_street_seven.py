#!/usr/bin/env python3
"""
HS7 cseréje Heaven Street Seven-re a magyar zenekarok kérdésekben
"""

def update_hs7_to_heaven_street_seven():
    """Cseréli le az HS7-et Heaven Street Seven-re"""
    
    # Olvasd be az eredeti fájlt
    with open('topics/magyar_zenekarok.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Cseréld le az összes HS7-et Heaven Street Seven-re
    updated_content = content.replace("'HS7'", "'Heaven Street Seven'")
    updated_content = updated_content.replace('"HS7"', '"Heaven Street Seven"')
    
    # Különleges esetek kezelése
    updated_content = updated_content.replace(
        '"question": "Melyik magyar alternatív zenekar tagja volt HS7?"',
        '"question": "Melyik magyar alternatív zenekar tagja volt Heaven Street Seven?"'
    )
    updated_content = updated_content.replace(
        '"explanation": "HS7 magyar alternatív zenekar"',
        '"explanation": "Heaven Street Seven magyar alternatív zenekar"'
    )
    
    # Mentsd el a frissített fájlt
    with open('topics/magyar_zenekarok.py', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("✅ HS7 sikeresen lecserélve Heaven Street Seven-re!")
    
    # Ellenőrizzük a változtatásokat
    import re
    hs7_count = len(re.findall(r'HS7', content))
    heaven_street_count = len(re.findall(r'Heaven Street Seven', updated_content))
    
    print(f"🔍 {hs7_count} HS7 találat lecserélve {heaven_street_count} Heaven Street Seven-re")
    
    return updated_content

if __name__ == "__main__":
    print("🎵 HS7 cseréje Heaven Street Seven-re...")
    update_hs7_to_heaven_street_seven()
    print("🎉 Frissítés befejezve!") 