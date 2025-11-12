# Solar Dashboard Development Notes

## How to Run

1. Create and activate your Python environment:
  
   python -m venv venv
   
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   pip install -r requirements.txt

3. Install Streamlit if not in requirements:

pip install streamlit pandas matplotlib seaborn


3. Run the app:

streamlit run app/main.py


4. Use the file uploader widget to upload your CSV files.

Folder Structure

app/: Main Streamlit app and utility functions.

scripts/: Development notes and documentation.

data/: Place your CSV files here for local testing (ignored in git).


Git Branching

Work done on dashboard-dev branch.

Single commit with message: "feat: basic Streamlit UI"


## 4. Update `.gitignore`

Add:

data/


## 5. Make One Commit and Push

bash

git add app/main.py app/utils.py scripts/README.md .gitignore

git commit -m "feat: basic Streamlit UI with file uploader, country filter, GHI boxplot, and top regions table"

git push origin dashboard-dev


6. Deployment (Optional, if you want)

Push code to GitHub.

Go to Streamlit Community Cloud

Link your repo and branch dashboard-dev.

Deploy and test your app.


Summary

Created dashboard-dev branch.

Setup folder structure.

Implemented Streamlit app using file uploader.

Interactive widgets: multi-select country filter.

Visualizations: boxplot and top regions table.

Git hygiene: one clean commit, data folder ignored.

Documented usage in scripts/README.md.
