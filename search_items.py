from pathlib import Path

def find_pdfs(directory):
    pdf_files = []
    # Iterate through all PDF files in the directory and subdirectories
    for file_path in Path(directory).rglob("*.txt"):
        try:
            # Check for read permissions
            if file_path.is_file():
                pdf_files.append(file_path)
        except PermissionError:
            # Skip files or directories with permission errors
            continue
            
    return pdf_files

# Set the root directory for the search
path = Path('C:/Users/uttam')
pdf_files = find_pdfs(path)

# Print all found PDF files
# for pdf in pdf_files:
#     print(pdf)

print(len(pdf_files))
