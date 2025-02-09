import os

def find_file(root_folder, file_name):
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for file in filenames:
            if file.endswith('.pdf'):
                print(file)
                if file_name.lower() in file.lower():  # Check if file_name is in the file
                    return os.path.join(dirpath, file)  # Return full path to the matched file
    return None

# Usage
root_folder = 'C:\\Users\\uttam\\Downloads'
file_name = 'earning'

file_path = find_file(root_folder, file_name)
if file_path:
    print(f"File found at: {file_path}")
else:
    print("File not found.")
