#!/usr/bin/env python3
"""
Fix the magyar zenekarok questions by adding missing question field and removing duplicates
"""

def fix_magyar_questions():
    """Fix the magyar zenekarok questions structure"""
    
    # Read the current file
    with open('topics/magyar_zenekarok.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split into lines for processing
    lines = content.split('\n')
    fixed_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Look for question blocks that start with "correct" instead of "question"
        if line.strip().startswith('"correct": 0,') and i > 0:
            # Check if this is the start of a new question block
            prev_line = lines[i-1].strip()
            if prev_line == '{':
                # This is the start of a question block, but it's missing the question field
                # Add the question field before the correct field
                fixed_lines.append('    {')
                fixed_lines.append('        "question": "Ki az előadó?",')
                fixed_lines.append('        "spotify_embed": "' + lines[i+1].split('"')[3] + '",')
                fixed_lines.append('        "options": ' + lines[i+2].split('options": ')[1])
                fixed_lines.append('        "correct": 0,')
                fixed_lines.append('        "explanation": "' + lines[i+3].split('"explanation": "')[1].split('",')[0] + '",')
                fixed_lines.append('        "topic": "magyar_zenekarok"')
                fixed_lines.append('    },')
                
                # Skip the next few lines since we've already processed them
                i += 5
                continue
        
        # Skip lines that are part of the broken structure
        if any(skip in line for skip in ['"correct": 0,', '"spotify_embed":', '"options":', '"explanation":', '"topic":']):
            if not any(fixed in line for fixed in ['"question":', 'MAGYAR_ZENEKAROK_QUESTIONS']):
                i += 1
                continue
        
        fixed_lines.append(line)
        i += 1
    
    # Write the fixed content back
    with open('topics/magyar_zenekarok.py', 'w', encoding='utf-8') as f:
        f.write('\n'.join(fixed_lines))
    
    print("✅ Fixed magyar zenekarok questions structure!")

if __name__ == "__main__":
    fix_magyar_questions() 