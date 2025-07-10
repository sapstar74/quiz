"""
Demo script for PDF Analyzer
Creates a simple test PDF and demonstrates functionality
"""

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from pathlib import Path
import tempfile

def create_demo_pdf():
    """Create a simple demo PDF for testing"""
    
    # Create demo directory
    demo_dir = Path("demo_files")
    demo_dir.mkdir(exist_ok=True)
    
    # Create PDF
    pdf_path = demo_dir / "demo_document.pdf"
    
    c = canvas.Canvas(str(pdf_path), pagesize=letter)
    
    # Page 1
    c.drawString(100, 750, "PDF Elemző Demo Dokumentum")
    c.drawString(100, 720, "=" * 40)
    c.drawString(100, 680, "Ez egy teszt dokumentum a PDF Elemző alkalmazás számára.")
    c.drawString(100, 650, "")
    c.drawString(100, 620, "Főbb pontok:")
    c.drawString(120, 590, "• Automatikus szöveg kinyerés")
    c.drawString(120, 560, "• Intelligens keresési funkciók")
    c.drawString(120, 530, "• AI-alapú chat (fejlesztés alatt)")
    c.drawString(120, 500, "• Statisztikai elemzések")
    c.drawString(100, 450, "")
    c.drawString(100, 420, "Technológiák:")
    c.drawString(120, 390, "- Streamlit webes felület")
    c.drawString(120, 360, "- PyPDF2 és pdfplumber könyvtárak")
    c.drawString(120, 330, "- Python backend")
    
    # Page 2
    c.showPage()
    c.drawString(100, 750, "Második oldal - További információk")
    c.drawString(100, 720, "=" * 40)
    c.drawString(100, 680, "Ez a második oldal további tesztadatokat tartalmaz.")
    c.drawString(100, 650, "")
    c.drawString(100, 620, "Keresési tesztek:")
    c.drawString(120, 590, "1. Keress rá a 'technológiák' szóra")
    c.drawString(120, 560, "2. Próbáld ki a 'AI' keresést")
    c.drawString(120, 530, "3. Nézd meg a statisztikákat")
    c.drawString(100, 480, "")
    c.drawString(100, 450, "Jövőbeli funkciók:")
    c.drawString(120, 420, "• OpenAI GPT integráció")
    c.drawString(120, 390, "• Fejlett szemantikai keresés")
    c.drawString(120, 360, "• Automatikus összefoglaló")
    c.drawString(120, 330, "• Exportálási lehetőségek")
    
    c.save()
    
    return pdf_path

def test_pdf_processor():
    """Test the PDF processor with demo file"""
    from src.pdf_processor import PDFProcessor
    
    # Create demo PDF
    pdf_path = create_demo_pdf()
    print(f"✅ Demo PDF létrehozva: {pdf_path}")
    
    # Test processor
    processor = PDFProcessor()
    
    # Extract text
    print("\n🔍 Szöveg kinyerése...")
    text = processor.extract_text(pdf_path)
    print(f"Kinyert szöveg hossza: {len(text)} karakter")
    print(f"Első 200 karakter: {text[:200]}...")
    
    # Get document info
    print("\n📊 Dokumentum információ...")
    info = processor.get_document_info(pdf_path)
    for key, value in info.items():
        print(f"{key}: {value}")
    
    # Search test
    print("\n🔍 Keresési teszt...")
    matches = processor.search_in_document(pdf_path, "technológiák")
    print(f"Találatok 'technológiák' szóra: {len(matches)}")
    for match in matches:
        print(f"  - Oldal {match['page']}, Sor {match['line']}: {match['text'][:50]}...")

if __name__ == "__main__":
    print("🧠 PDF Elemző Demo")
    print("=" * 30)
    
    try:
        test_pdf_processor()
        print("\n✅ Demo sikeresen lefutott!")
        print("\n🌐 Streamlit alkalmazás: http://localhost:8504")
        print("📄 Demo PDF: demo_files/demo_document.pdf")
        
    except Exception as e:
        print(f"\n❌ Hiba: {e}")
        print("\nAz alkalmazás még fejlesztés alatt áll.") 