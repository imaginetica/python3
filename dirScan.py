import os
import random
import string
import argparse

def rename_pdf_files(root_folder, search_string, replacement_string):
    
    # Loop through items in the root folder
    for item in os.listdir(root_folder):
        item_path = os.path.join(root_folder, item)
        
        # If the item is a directory, recursively search it
        if os.path.isdir(item_path):
            rename_pdf_files(item_path, search_string, replacement_string)
        
        # If the item is a file with ".pdf" extension and contains the search string in its name
        elif item.lower().endswith(".pdf") and search_string in item:
            # Create the new filename by replacing the search string with the replacement string
            new_item = item.replace(search_string, replacement_string)
            new_item_path = os.path.join(root_folder, new_item)
            
            # Check if a file with the new name already exists
            counter = 1                                             # This will occur on subsequent runs if "old" files aren't moved or pruned.
            while os.path.exists(new_item_path):
                base, ext = os.path.splitext(new_item)
                new_item = f"{base}_OLD{counter}{ext}"              # Append "OLD" before the extension
                new_item_path = os.path.join(root_folder, new_item)
                counter += 1
            
            os.rename(item_path, new_item_path)
            print(f"Renamed: {item} -> {new_item}")

def create_test_directory(path, depth=3, num_folders=5, num_files=10):
    os.makedirs(path, exist_ok=True)
    
    for _ in range(num_folders):
        folder_name = ''.join(random.choices(string.ascii_lowercase, k=5))
        folder_path = os.path.join(path, folder_name)
        os.makedirs(folder_path)
        
        for _ in range(num_files):
            file_name = ''.join(random.choices(string.ascii_lowercase, k=8))
            file_extension = random.choice([".pdf", ".txt"])
            file_path = os.path.join(folder_path, file_name + file_extension)
            
            with open(file_path, "w") as f:
                f.write("Test content")

# # Replace 'test_directory_path' with the desired path for the test directory
# test_directory_path = '/path/to/test_directory'
# path_to_search = '/path/to/search'
# search_string = "_OCR_221117"  # Specified search string
# replacement_string = ""        # Specified replacement string

# rename_pdf_files(test_directory_path, search_string, replacement_string)

def main():
    parser = argparse.ArgumentParser(description="Test Application")
    parser.add_argument("path", help="Path for test directory")
    parser.add_argument("search_string", help="Search string for renaming PDF files")
    parser.add_argument("replacement_string", help="Replacement string for renaming PDF files")

    args = parser.parse_args()

    test_directory_path = args.path
    search_string = args.search_string
    replacement_string = args.replacement_string

    # Create the test directory
    create_test_directory(test_directory_path)

    # Rename PDF files in the test directory
    rename_pdf_files(test_directory_path, search_string, replacement_string)

if __name__ == "__main__":
    main()