#!/usr/bin/env python3
"""
Fix the scoring issue in magyar zenekarok quiz by correcting the correct answer indices
"""

import re

def fix_magyar_quiz_scoring():
    """Fix the correct answer indices in magyar zenekarok questions"""
    
    # Read the current file
    with open('topics/magyar_zenekarok.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split into lines for processing
    lines = content.split('\n')
    fixed_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        fixed_lines.append(line)
        
        # Look for question blocks
        if '"question": "Ki az előadó?"' in line:
            # Find the options and explanation
            options_line = None
            explanation_line = None
            correct_line = None
            
            # Look ahead for the options, correct, and explanation
            j = i + 1
            while j < len(lines) and not lines[j].strip().startswith('{'):
                if '"options":' in lines[j]:
                    options_line = lines[j]
                elif '"correct":' in lines[j]:
                    correct_line = lines[j]
                elif '"explanation":' in lines[j]:
                    explanation_line = lines[j]
                j += 1
            
            # Extract the correct answer from explanation
            if explanation_line:
                # Extract the band name from explanation (format: "BandName magyar...")
                match = re.search(r'"explanation": "([^"]+)', explanation_line)
                if match:
                    explanation_text = match.group(1)
                    # The correct answer is the first word before "magyar"
                    correct_answer = explanation_text.split(' magyar')[0].strip()
                    
                    # Find this answer in the options
                    if options_line:
                        # Extract options from the line
                        options_match = re.search(r'"options": \[(.*?)\]', options_line)
                        if options_match:
                            options_text = options_match.group(1)
                            # Parse options (handle quotes and commas)
                            options = []
                            current_option = ""
                            in_quotes = False
                            for char in options_text:
                                if char == "'" and (not current_option or current_option[-1] != '\\'):
                                    in_quotes = not in_quotes
                                elif char == ',' and not in_quotes:
                                    options.append(current_option.strip().strip("'"))
                                    current_option = ""
                                else:
                                    current_option += char
                            if current_option.strip():
                                options.append(current_option.strip().strip("'"))
                            
                            # Find the correct answer index
                            correct_index = None
                            for idx, option in enumerate(options):
                                if option == correct_answer:
                                    correct_index = idx
                                    break
                            
                            # Update the correct line
                            if correct_index is not None and correct_line:
                                # Replace the correct line in the next iteration
                                fixed_lines[-1] = f'        "correct": {correct_index},'
                                print(f"Fixed: {correct_answer} -> index {correct_index}")
        
        i += 1
    
    # Write the fixed content back
    with open('topics/magyar_zenekarok.py', 'w', encoding='utf-8') as f:
        f.write('\n'.join(fixed_lines))
    
    print("✅ Fixed magyar zenekarok quiz scoring!")

if __name__ == "__main__":
    fix_magyar_quiz_scoring() 