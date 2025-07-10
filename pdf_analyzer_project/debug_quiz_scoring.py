#!/usr/bin/env python3
"""
Debug script to check question structure and scoring logic for international bands quiz
"""

import random
import sys
import os

# Add the current directory to Python path to import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from topics.nemzetkozi_zenekarok import NEMZETKOZI_ZENEKAROK_QUESTIONS

def validate_question_structure():
    """Validate the structure of all questions in the international bands file"""
    print("🔍 VALIDATING QUESTION STRUCTURE")
    print("=" * 50)
    
    issues = []
    total_questions = len(NEMZETKOZI_ZENEKAROK_QUESTIONS)
    
    for i, question in enumerate(NEMZETKOZI_ZENEKAROK_QUESTIONS):
        # Check required fields
        required_fields = ["question", "options", "correct", "explanation", "topic"]
        for field in required_fields:
            if field not in question:
                issues.append(f"Question {i+1}: Missing required field '{field}'")
        
        # Check options structure
        if "options" in question:
            options = question["options"]
            if not isinstance(options, list):
                issues.append(f"Question {i+1}: 'options' is not a list")
            elif len(options) != 4:
                issues.append(f"Question {i+1}: Expected 4 options, got {len(options)}")
            else:
                # Check for duplicate options
                if len(set(options)) != len(options):
                    issues.append(f"Question {i+1}: Duplicate options found")
        
        # Check correct answer index
        if "correct" in question and "options" in question:
            correct_idx = question["correct"]
            options_count = len(question["options"])
            if not isinstance(correct_idx, int):
                issues.append(f"Question {i+1}: 'correct' is not an integer")
            elif correct_idx < 0 or correct_idx >= options_count:
                issues.append(f"Question {i+1}: 'correct' index {correct_idx} out of range (0-{options_count-1})")
        
        # Check Spotify embed
        if "spotify_embed" not in question:
            issues.append(f"Question {i+1}: Missing 'spotify_embed' field")
        elif not question["spotify_embed"].startswith("https://open.spotify.com/embed/"):
            issues.append(f"Question {i+1}: Invalid Spotify embed URL format")
    
    # Summary
    print(f"Total questions: {total_questions}")
    if issues:
        print(f"❌ Found {len(issues)} issues:")
        for issue in issues:
            print(f"  - {issue}")
        return False
    else:
        print("✅ All questions have valid structure!")
        return True

def simulate_quiz_scoring():
    """Simulate the quiz scoring logic to check if it works correctly"""
    print("\n🎯 SIMULATING QUIZ SCORING")
    print("=" * 50)
    
    # Take a sample of questions for testing
    sample_questions = random.sample(NEMZETKOZI_ZENEKAROK_QUESTIONS, min(10, len(NEMZETKOZI_ZENEKAROK_QUESTIONS)))
    
    total_score = 0
    total_questions = len(sample_questions)
    
    for i, question in enumerate(sample_questions):
        print(f"\n--- Question {i+1} ---")
        print(f"Question: {question['question']}")
        print(f"Original options: {question['options']}")
        print(f"Correct answer index: {question['correct']}")
        print(f"Correct answer text: {question['options'][question['correct']]}")
        
        # Simulate the shuffling logic from quiz_app_clean.py
        options = list(enumerate(question["options"]))
        random.shuffle(options)
        
        print(f"Shuffled options: {[opt[1] for opt in options]}")
        
        # Create mappings like in the quiz app
        correct_answer_mapping = {new_idx: original_idx for new_idx, (original_idx, _) in enumerate(options)}
        original_to_new_mapping = {original_idx: new_idx for new_idx, (original_idx, _) in enumerate(options)}
        
        print(f"Original to new mapping: {original_to_new_mapping}")
        print(f"Correct answer new index: {original_to_new_mapping[question['correct']]}")
        
        # Simulate user selecting the correct answer
        correct_new_idx = original_to_new_mapping[question['correct']]
        user_selection = correct_new_idx
        
        # Check if answer is correct (same logic as in quiz app)
        is_correct = user_selection == correct_new_idx
        
        if is_correct:
            total_score += 1
            print("✅ Correct answer!")
        else:
            print("❌ Wrong answer!")
        
        # Store answer like in quiz app
        answer_data = {
            'question': question["question"],
            'user_answer': question['correct'],  # Original index
            'correct_answer': question['correct'],  # Original index
            'is_correct': is_correct,
            'explanation': question.get("explanation", "")
        }
        
        print(f"Stored answer data: {answer_data}")
    
    # Final results
    percentage = (total_score / total_questions) * 100
    print(f"\n📊 SIMULATION RESULTS")
    print(f"Total questions: {total_questions}")
    print(f"Correct answers: {total_score}")
    print(f"Percentage: {percentage:.1f}%")
    
    if total_score == total_questions:
        print("✅ All answers were correctly scored!")
        return True
    else:
        print("❌ Some answers were incorrectly scored!")
        return False

def test_answer_mapping_edge_cases():
    """Test edge cases in answer mapping"""
    print("\n🧪 TESTING EDGE CASES")
    print("=" * 50)
    
    # Test with a specific question
    question = NEMZETKOZI_ZENEKAROK_QUESTIONS[0]
    print(f"Testing with question: {question['question']}")
    print(f"Original options: {question['options']}")
    print(f"Correct index: {question['correct']}")
    
    # Test multiple shuffles to see if mapping is consistent
    for test_round in range(5):
        print(f"\n--- Test Round {test_round + 1} ---")
        
        options = list(enumerate(question["options"]))
        random.shuffle(options)
        
        shuffled_options = [opt[1] for opt in options]
        original_to_new_mapping = {original_idx: new_idx for new_idx, (original_idx, _) in enumerate(options)}
        
        print(f"Shuffled: {shuffled_options}")
        print(f"Mapping: {original_to_new_mapping}")
        
        # Test all possible user selections
        for user_selection in range(4):
            correct_new_idx = original_to_new_mapping[question['correct']]
            is_correct = user_selection == correct_new_idx
            
            print(f"  User selects {user_selection} ({shuffled_options[user_selection]}): {'✅' if is_correct else '❌'}")

def main():
    """Main debug function"""
    print("🔧 INTERNATIONAL BANDS QUIZ DEBUG")
    print("=" * 60)
    
    # Validate question structure
    structure_valid = validate_question_structure()
    
    # Simulate quiz scoring
    scoring_valid = simulate_quiz_scoring()
    
    # Test edge cases
    test_answer_mapping_edge_cases()
    
    # Final summary
    print("\n📋 FINAL SUMMARY")
    print("=" * 30)
    print(f"Question structure: {'✅ Valid' if structure_valid else '❌ Invalid'}")
    print(f"Scoring logic: {'✅ Valid' if scoring_valid else '❌ Invalid'}")
    
    if structure_valid and scoring_valid:
        print("\n🎉 All tests passed! The quiz should work correctly.")
    else:
        print("\n⚠️  Issues found. Please review the problems above.")

if __name__ == "__main__":
    main() 