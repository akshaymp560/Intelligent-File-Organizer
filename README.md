# Intelligent Python File Organizer

An intelligent file management system that automatically organizes files using rule-based logic, keyword-based classification, and machine learning.

## 🚀 Features
- Rule-based file categorization
- Keyword-based smart categorization
- Machine learning classification (Naive Bayes)
- Duplicate file detection and handling
- Time-based organization (Recent / Old)
- Cleanup suggestions (large files)
- Logging system
- Visualization using Matplotlib
- GUI interface using Tkinter

## 🛠️ Tech Stack
- Python
- Scikit-learn
- NumPy
- Matplotlib
- Tkinter

##  Project Structure
Intelligent_File_Organizer/
│
├── data/
│   └── files.csv              # Dataset storing file metadata and classification records
│
├── logs/
│   └── app.log                # Application runtime logs and activity history
│
├── test_folder/               # Sample directory used for testing file organization
│
├── main.py                    # Entry point — initializes and runs the application
├── organizer.py               # Core logic for scanning, sorting, and moving files
├── ml_model.py                # ML model for intelligent file classification
├── utils.py                   # Shared utility/helper functions
├── config.py                  # App-wide configuration and settings
├── gui.py                     # Graphical User Interface (built with Tkinter/PyQt)
│
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation

## ▶️ How to Run

Prerequisites
Make sure you have the following installed before running the project:

Python 3.8+
Git (configured with your GitHub account)
Required dependencies


1. Clone the Repository
git clone https://github.com/your-username/Intelligent_File_Organizer.git
cd Intelligent_File_Organizer

2. Install Dependencies
bashpip install -r requirements.txt

3. Run the Application