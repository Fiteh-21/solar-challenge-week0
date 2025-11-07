# solar-challenge-week0
A data science project for solar energy analysis
 ## ⚙ Objective
 To ensure every contributor can replicate the same Python environment for development,
 testing, and collaboration.
 ## 🚀 Environment Setup Instructions
 ### 1 Clone the Repository
 git clone https://github.com/Fiteh-21/solar-challenge-week0.git
 cd solar-challenge-week0
 ### 2 Create and Activate Virtual Environment
 For Windows CMD:
 - python -m venv venv
 - venv\Scripts\activate
 
 For macOS/Linux:
 - python3 -m venv venv
 - source venv/bin/activate
 ### 3 Install Dependencies
 pip install -r requirements.txt
 ### 4 Verify Python and Pip
 python --version
 
 pip --version
 ### 5 Run Tests (Optional)
 python -m unittest
 ## 📁Suggested Folder Structure
.vscode/
   -  settings.json
    
.github/
   -  workflows/
       -  unittest.yml
        
 .gitignore
 
requirements.txt

README.md

 src/
 
 notebooks/
   -  __init__.py
   -  README.md
    
 tests/
   -  __init__.py
    
 scripts/
   -  __init__.py
   -  README.md
 ## 🔁 Continuous Integration (CI)
 A basic GitHub Actions workflow file (`.github/workflows/ci.yml`) is included to
 automatically verify your environment setup. It runs the following commands:
 
 python --version
 
 pip install -r requirements.txt
 ## 🧩 Notes
 - Use Python 3.10 or later.
 - Always activate the virtual environment before running Python commands.
 - Keep requirements.txt updated whenever new packages are installed.
 - Commit messages should follow a clear structure (e.g., init: add .gitignore, chore: venv
 setup, ci: add GitHub Actions workflow).
 - After approval, merge your setup-task branch into main via Pull Request.
 ##
 **Author**: Fiteh Tesfaye
 
 **Date**: November 7, 2025
