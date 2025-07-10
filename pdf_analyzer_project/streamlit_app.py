"""
🧠 PDF Elemző és Chat Alkalmazás
Töltsd fel PDF dokumentumot és beszélgess vele AI segítségével!
"""

import streamlit as st
import os
import sys
from pathlib import Path

# Add src to path
current_dir = Path(__file__).parent
src_dir = current_dir / "src"
sys.path.insert(0, str(src_dir))

# Page config
st.set_page_config(
    page_title="🧠 PDF Elemző és Chat",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main title
st.title("🧠 PDF Elemző és Chat Alkalmazás")
st.markdown("---")

# Initialize session state
if 'pdf_processed' not in st.session_state:
    st.session_state.pdf_processed = False
if 'document_content' not in st.session_state:
    st.session_state.document_content = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Sidebar - File Upload
with st.sidebar:
    st.header("📄 PDF Feltöltés")
    
    uploaded_file = st.file_uploader(
        "Válassz PDF dokumentumot",
        type=['pdf'],
        help="Tölts fel egy PDF fájlt az elemzéshez"
    )
    
    if uploaded_file is not None:
        # Save uploaded file
        upload_dir = Path("uploads")
        upload_dir.mkdir(exist_ok=True)
        
        file_path = upload_dir / uploaded_file.name
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getvalue())
        
        st.success(f"✅ Feltöltve: {uploaded_file.name}")
        
        # Process PDF button
        if st.button("🔍 PDF Feldolgozása", type="primary"):
            with st.spinner("PDF feldolgozása folyamatban..."):
                try:
                    # Simple PDF processing for now
                    import PyPDF2
                    
                    content = ""
                    with open(file_path, 'rb') as file:
                        pdf_reader = PyPDF2.PdfReader(file)
                        for page in pdf_reader.pages:
                            content += page.extract_text() + "\\n"
                    
                    st.session_state.document_content = content
                    st.session_state.pdf_processed = True
                    st.session_state.current_file = uploaded_file.name
                    
                    st.success("✅ PDF sikeresen feldolgozva!")
                    
                except Exception as e:
                    st.error(f"Hiba a feldolgozás során: {e}")
    
    # Clear session button
    if st.button("🗑️ Törlés"):
        st.session_state.pdf_processed = False
        st.session_state.document_content = None
        st.session_state.chat_history = []
        st.rerun()

# Main content area
if not st.session_state.pdf_processed:
    # Welcome screen
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.info("""
        ### 👋 Üdvözöl a PDF Elemző!
        
        **Amit tudsz csinálni:**
        - 📄 **PDF feltöltés** a bal oldali panelen
        - 🤖 **AI Chat** a dokumentum tartalmával (hamarosan)
        - 📊 **Automatikus elemzés** és összefoglaló
        - 🔍 **Intelligens keresés** a szövegben
        - 📈 **Statisztikák** és vizualizációk
        
        **Kezdd el:** Tölts fel egy PDF-et a bal oldalon!
        """)

else:
    # Document processed - show analysis
    st.success(f"📄 **Betöltött dokumentum:** {st.session_state.current_file}")
    
    # Tabs for different functions
    tab1, tab2, tab3 = st.tabs([
        "📄 Tartalom", 
        "🔍 Keresés", 
        "📈 Statisztikák"
    ])
    
    with tab1:
        st.header("📄 Dokumentum Tartalom")
        
        # Show first part of content
        content = st.session_state.document_content
        preview_length = 1000
        
        if len(content) > preview_length:
            st.text_area(
                "Előnézet (első 1000 karakter):", 
                content[:preview_length] + "...",
                height=400
            )
            st.info(f"Teljes tartalom: {len(content)} karakter")
        else:
            st.text_area("Teljes tartalom:", content, height=400)
    
    with tab2:
        st.header("🔍 Dokumentum Keresés")
        
        search_term = st.text_input("Keresés a dokumentumban:")
        
        if search_term:
            try:
                content = st.session_state.document_content
                if search_term.lower() in content.lower():
                    # Find and highlight matches
                    lines = content.split('\\n')
                    matches = []
                    for i, line in enumerate(lines):
                        if search_term.lower() in line.lower():
                            matches.append(f"**{i+1}. sor:** {line}")
                    
                    st.success(f"✅ {len(matches)} találat")
                    for match in matches[:10]:  # Show first 10 matches
                        st.write(match)
                else:
                    st.warning("❌ Nincs találat")
            except Exception as e:
                st.error(f"Keresési hiba: {e}")
    
    with tab3:
        st.header("📈 Dokumentum Statisztikák")
        
        if st.session_state.document_content:
            content = st.session_state.document_content
            
            # Basic stats
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("📄 Karakterek", len(content))
            
            with col2:
                word_count = len(content.split())
                st.metric("🔤 Szavak", word_count)
            
            with col3:
                line_count = len(content.split('\\n'))
                st.metric("📝 Sorok", line_count)
            
            with col4:
                avg_words_per_line = word_count / max(line_count, 1)
                st.metric("📊 Átlag szó/sor", f"{avg_words_per_line:.1f}")

# Footer
st.markdown("---")
st.markdown("### 🛠️ Készítette: AI PDF Elemző v1.0")
st.markdown("*Tölts fel egy PDF-et és fedezd fel a dokumentumelemzés lehetőségeit!*") 