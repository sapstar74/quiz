#!/usr/bin/env python3
"""
Main entry point for the Quiz App
"""

import sys
import os

# Add the pdf_analyzer_project directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'pdf_analyzer_project'))

# Import and run the quiz app
from quiz_app_clean import main

if __name__ == "__main__":
    main() 