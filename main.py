from organizer import FileOrganizer

folder = "test_folder"

organizer = FileOrganizer(folder)

organizer.organize_files()
organizer.handle_duplicates()
organizer.visualize()
organizer.suggest_cleanup()
print("Process completed ")