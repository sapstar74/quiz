#!/usr/bin/env python3
"""
Fix flag image paths in the flag questions
"""

import os

def fix_flag_paths():
    # Read the current flag questions file
    with open('topics/zaszlok_all_questions.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the incorrect path with the correct one
    # Change from '../world_flags_project/data/flags/' to 'world_flags_project/data/flags/'
    fixed_content = content.replace('../world_flags_project/data/flags/', 'world_flags_project/data/flags/')
    
    # Write the fixed content back
    with open('topics/zaszlok_all_questions.py', 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print("Flag paths have been fixed!")

if __name__ == "__main__":
    fix_flag_paths() 