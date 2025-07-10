#!/usr/bin/env python3
"""
Find and extract Major logók section from PDF
"""

from src.pdf_processor import PDFProcessor
import pathlib

def find_major_logos_section():
    """Find and display the Major logók section"""
    processor = PDFProcessor()
    content = processor.extract_text(pathlib.Path('uploads/Hasznos haszontalanságok 218ec5b77ea680c6958dd6fd30a8c040.pdf'))
    
    lines = content.split('\n')
    major_index = -1
    
    # Find the Major logók section
    for i, line in enumerate(lines):
        if 'Major logók' in line:
            major_index = i
            break
    
    if major_index >= 0:
        print(f'Major logók section found at line {major_index}')
        print('Content around Major logók:')
        print('=' * 50)
        
        # Show context around the section
        start = max(0, major_index - 5)
        end = min(len(lines), major_index + 100)
        
        for i in range(start, end):
            prefix = ">>> " if i == major_index else "    "
            print(f'{prefix}{i}: {lines[i]}')
            
        print('=' * 50)
    else:
        print('Major logók section not found')
        
        # Search for other sport-related terms
        print('\nSearching for other sport-related content...')
        sport_keywords = ['sport', 'team', 'football', 'basketball', 'baseball', 'hockey', 'nfl', 'nba', 'mlb', 'nhl', 'logo', 'major', 'league']
        
        for i, line in enumerate(lines):
            if any(keyword in line.lower() for keyword in sport_keywords):
                print(f'Line {i}: {line}')

if __name__ == "__main__":
    find_major_logos_section() 