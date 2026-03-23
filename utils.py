import hashlib
import logging

logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def get_file_hash(file_path):
    hasher = hashlib.md5()
    
    with open(file_path, 'rb') as f:
        data = f.read()
        hasher.update(data)
    
    return hasher.hexdigest()


def find_duplicates(files):
    seen_hashes = {}
    duplicates = []

    for file in files:
        file_hash = get_file_hash(file)
        
        if file_hash in seen_hashes:
            duplicates.append(file)
        else:
            seen_hashes[file_hash] = file

    return duplicates


import os
import shutil

def move_duplicates(duplicates, base_folder):
    dup_folder = os.path.join(base_folder, "Duplicates")
    
    os.makedirs(dup_folder, exist_ok=True)
    
    for file in duplicates:
        try:
            file_name = os.path.basename(file)
            new_path = os.path.join(dup_folder, file_name)
            
            shutil.move(file, new_path)

            logging.info(f"Duplicate moved: {file} → {new_path}")
        
        except Exception as e:
            logging.error(f"Error moving duplicate {file}: {e}")



import matplotlib.pyplot as plt
from collections import Counter

def plot_file_distribution(files):
    categories = []

    for file in files:
        ext = file.split('.')[-1].lower()
        
        if ext in ['jpg', 'jpeg', 'png']:
            categories.append('Images')
        elif ext in ['pdf', 'txt', 'docx']:
            categories.append('Documents')
        elif ext in ['mp3', 'wav']:
            categories.append('Audio')
        elif ext in ['mp4', 'mkv']:
            categories.append('Videos')
        else:
            categories.append('Others')

    count = Counter(categories)

    plt.bar(count.keys(), count.values())
    plt.title("File Distribution")
    plt.xlabel("Categories")
    plt.ylabel("Number of Files")
    plt.show()


import os

def cleanup_suggestions(files):
    large_files = []
    old_files = []

    for file in files:
        size = os.path.getsize(file)

        # Large file > 5MB
        if size > 5 * 1024 * 1024:
            large_files.append(file)

    print("\nCleanup Suggestions:")
    print(f"Large files (>5MB): {len(large_files)}")

    for f in large_files[:5]:
        print(f"  {f}")