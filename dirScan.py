import os

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
            if not os.path.exists(new_item_path):
                # Rename the file
                os.rename(item_path, new_item_path)
                # Print a message to indicate the renaming
                print(f"Renamed: {item} -> {new_item}")
            else:
                print(f"Skipping: {new_item} already exists")

# Replace 'path_to_search' with the root path where you want to start the search
path_to_search = '/path/to/search'
search_string = "_OCR_221117"  # Specified search string
replacement_string = ""         # Specified replacement string
rename_pdf_files(path_to_search, search_string, replacement_string)




# import os

# def search_files_with_substring(folder_path, substring):
#     found_files = []

#     for item in os.listdir(folder_path):
#         item_path = os.path.join(folder_path, item)

#         if os.path.isfile(item_path) and substring in item:
#             found_files.append(item_path)
        
#         if os.path.isdir(item_path):
#             found_files.extend(search_files_with_substring(item_path, substring))

#     return found_files

# def get_total_size(files):
#     total_size = 0
#     for file_path in files:
#         total_size += os.path.getsize(file_path)
#     return total_size
    
# # Replace 'path_to_start_folder' with the actual path where you want to start the search
# start_folder = 'path_to_start_folder'
# substring_to_search = '_OCR_221117'

# result_files = search_files_with_substring(".", substring_to_search)

# if result_files:
#     for file_path in result_files:
#         print(file_path)
#     print(f"Found {len(result_files)} files with '{substring_to_search}' in the filename:")
#     total_size = get_total_size(result_files) / (1024*1024)
#     print(f"Total size of found files: {total_size} MB")
# else:
#     print(f"No files found with '{substring_to_search}' in the filename.")