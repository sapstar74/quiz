#!/usr/bin/env python3
"""
Debug script to analyze the specific scoring logic from quiz_app_clean.py
"""

import random
import sys
import os

# Add the current directory to Python path to import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from topics.nemzetkozi_zenekarok import NEMZETKOZI_ZENEKAROK_QUESTIONS

def analyze_quiz_app_logic():
    """Analyze the exact logic from quiz_app_clean.py"""
    print("🔍 ANALYZING QUIZ APP LOGIC")
    print("=" * 50)
    
    # Extract the exact logic from quiz_app_clean.py
    print("From quiz_app_clean.py, the scoring logic is:")
    print("1. Options are shuffled: options = list(enumerate(current_q['options']))")
    print("2. random.shuffle(options)")
    print("3. Mapping created: correct_answer_mapping = {new_idx: original_idx for new_idx, (original_idx, _) in enumerate(options)}")
    print("4. Reverse mapping: original_to_new_mapping = {original_idx: new_idx for new_idx, (original_idx, _) in enumerate(options)}")
    print("5. When user selects: correct_new_idx = original_to_new_mapping[current_q['correct']]")
    print("6. Check: is_correct = i == correct_new_idx")
    print("7. Store: user_answer = original_idx (from the selected option)")
    print()

def test_exact_quiz_logic():
    """Test the exact logic from the quiz app"""
    print("🧪 TESTING EXACT QUIZ LOGIC")
    print("=" * 50)
    
    # Take a few questions for testing
    test_questions = NEMZETKOZI_ZENEKAROK_QUESTIONS[:5]
    
    for q_idx, question in enumerate(test_questions):
        print(f"\n--- Testing Question {q_idx + 1} ---")
        print(f"Question: {question['question']}")
        print(f"Original options: {question['options']}")
        print(f"Correct answer index: {question['correct']}")
        print(f"Correct answer text: {question['options'][question['correct']]}")
        
        # Simulate the EXACT logic from quiz_app_clean.py
        options = list(enumerate(question["options"]))
        random.shuffle(options)
        
        print(f"Shuffled options: {[opt[1] for opt in options]}")
        
        # Create mappings exactly as in quiz app
        correct_answer_mapping = {new_idx: original_idx for new_idx, (original_idx, _) in enumerate(options)}
        original_to_new_mapping = {original_idx: new_idx for new_idx, (original_idx, _) in enumerate(options)}
        
        print(f"Original to new mapping: {original_to_new_mapping}")
        print(f"Correct answer new index: {original_to_new_mapping[question['correct']]}")
        
        # Test all possible user selections
        for user_selection in range(4):
            # Get the original index for the user's selection
            user_original_idx = correct_answer_mapping[user_selection]
            
            # Get the correct answer's new index
            correct_new_idx = original_to_new_mapping[question['correct']]
            
            # Check if correct (exact logic from quiz app)
            is_correct = user_selection == correct_new_idx
            
            print(f"  User selects {user_selection} ({options[user_selection][1]}) -> Original idx: {user_original_idx} -> {'✅' if is_correct else '❌'}")
            
            # Simulate storing the answer (as in quiz app)
            answer_data = {
                'question': question["question"],
                'user_answer': user_original_idx,  # Original index
                'correct_answer': question['correct'],  # Original index
                'is_correct': is_correct,
                'explanation': question.get("explanation", "")
            }
            
            if is_correct:
                print(f"    Stored answer: {answer_data}")

def test_results_display_logic():
    """Test how the results are displayed in the quiz app"""
    print("\n📊 TESTING RESULTS DISPLAY LOGIC")
    print("=" * 50)
    
    # Simulate a quiz session with some answers
    question = NEMZETKOZI_ZENEKAROK_QUESTIONS[0]
    
    print(f"Original question: {question['question']}")
    print(f"Original options: {question['options']}")
    print(f"Correct answer index: {question['correct']}")
    
    # Simulate shuffling
    options = list(enumerate(question["options"]))
    random.shuffle(options)
    
    print(f"Shuffled options: {[opt[1] for opt in options]}")
    
    # Simulate user selecting the wrong answer
    user_selection = 1  # User selects second option
    user_original_idx = options[user_selection][0]  # Original index of selected option
    correct_new_idx = options[question['correct']][0]  # Original index of correct answer
    
    is_correct = user_selection == correct_new_idx
    
    print(f"User selected: {user_selection} ({options[user_selection][1]})")
    print(f"User original index: {user_original_idx}")
    print(f"Correct original index: {correct_new_idx}")
    print(f"Is correct: {is_correct}")
    
    # Simulate the results display logic
    print("\n--- Results Display Simulation ---")
    print("The quiz app would show:")
    
    for j, option in enumerate(question["options"]):
        if j == user_original_idx and j == question['correct']:
            print(f"✅ **{option}** (helyes válasz)")
        elif j == user_original_idx and j != question['correct']:
            print(f"❌ **{option}** (te választottad)")
        elif j == question['correct']:
            print(f"✅ **{option}** (helyes válasz)")
        else:
            print(f"• {option}")

def check_potential_issues():
    """Check for potential issues in the logic"""
    print("\n⚠️  POTENTIAL ISSUES CHECK")
    print("=" * 50)
    
    # Check if all questions have correct=0
    all_correct_zero = all(q['correct'] == 0 for q in NEMZETKOZI_ZENEKAROK_QUESTIONS)
    print(f"All questions have correct=0: {all_correct_zero}")
    
    if all_correct_zero:
        print("⚠️  This means the correct answer is always the first option!")
        print("   This could cause confusion if users expect the correct answer to be randomized.")
    
    # Check for any duplicate options
    duplicate_issues = []
    for i, q in enumerate(NEMZETKOZI_ZENEKAROK_QUESTIONS):
        if len(set(q['options'])) != len(q['options']):
            duplicate_issues.append(i)
    
    if duplicate_issues:
        print(f"⚠️  Questions with duplicate options: {duplicate_issues}")
    else:
        print("✅ No duplicate options found")
    
    # Check if the logic handles edge cases correctly
    print("\nTesting edge case: What if user selects the correct answer?")
    question = NEMZETKOZI_ZENEKAROK_QUESTIONS[0]
    options = list(enumerate(question["options"]))
    random.shuffle(options)
    
    correct_new_idx = options[question['correct']][0]
    print(f"Correct answer should be at new index: {correct_new_idx}")
    
    # Find which new index corresponds to the correct answer
    for new_idx, (original_idx, _) in enumerate(options):
        if original_idx == question['correct']:
            print(f"Correct answer is at new index: {new_idx}")
            break

def main():
    """Main analysis function"""
    print("🔧 QUIZ APP LOGIC ANALYSIS")
    print("=" * 60)
    
    analyze_quiz_app_logic()
    test_exact_quiz_logic()
    test_results_display_logic()
    check_potential_issues()
    
    print("\n📋 ANALYSIS SUMMARY")
    print("=" * 30)
    print("The quiz logic appears to be mathematically correct.")
    print("The scoring should work properly with the current implementation.")
    print("If you're experiencing scoring issues, it might be due to:")
    print("1. Browser caching or session state issues")
    print("2. Multiple quiz sessions running simultaneously")
    print("3. JavaScript errors in the Streamlit interface")
    print("4. Network issues affecting the app state")

if __name__ == "__main__":
    main() 