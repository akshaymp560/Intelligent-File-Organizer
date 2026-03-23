import os
import shutil
import logging
from config import FILE_CATEGORIES, KEYWORD_CATEGORIES
from ml_model import train_model, predict_category

# Smart keyword-based categorization
def smart_categorize(file_name):
    file_name = file_name.lower()

    for category, keywords in KEYWORD_CATEGORIES.items():
        for word in keywords:
            if word in file_name:
                return category
    
    return None


#  Load ML model once
model, vectorizer = train_model()


#  Main categorization logic (Hybrid)
def categorize_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    file_name = os.path.basename(file_path)

    # 1️ Smart keyword-based
    smart_category = smart_categorize(file_name)
    if smart_category:
        return smart_category

    # 2️ Rule-based (extension)
    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category

    # 3️ ML fallback
    return predict_category(model, vectorizer, file_name)


#  Move file safely
def move_file(file_path, base_folder):
    try:
        category = categorize_file(file_path)
        time_category = categorize_by_time(file_path)
        category = os.path.join(category, time_category)
        
        target_folder = os.path.join(base_folder, category)
        os.makedirs(target_folder, exist_ok=True)
        
        file_name = os.path.basename(file_path)
        new_path = os.path.join(target_folder, file_name)
        
        shutil.move(file_path, new_path)

        logging.info(f"Moved: {file_path} → {new_path}")
    
    except Exception as e:
        logging.error(f"Error moving file {file_path}: {e}")


#  OOP Wrapper Class
class FileOrganizer:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def scan_files(self):   # ✅ MUST be inside class
        files = []

        skip_folders = ["Images", "Documents", "Audio", "Videos",
                        "Projects", "Personal", "Finance",
                        "Duplicates"]

        for root, dirs, filenames in os.walk(self.folder_path):
            dirs[:] = [d for d in dirs if d not in skip_folders]

            for file in filenames:
                files.append(os.path.join(root, file))

        return files

    def organize_files(self):
        files = self.scan_files()
        for file in files:
            move_file(file, self.folder_path)

    def handle_duplicates(self):
        from utils import find_duplicates, move_duplicates

        files = self.scan_files()
        duplicates = find_duplicates(files)

        print("Duplicate files:")
        for d in duplicates:
            print(d)

        move_duplicates(duplicates, self.folder_path)

    def suggest_cleanup(self):
        from utils import cleanup_suggestions

        files = self.scan_files()
        cleanup_suggestions(files)

    def visualize(self):
        from utils import plot_file_distribution

        files = self.scan_files()
        plot_file_distribution(files)