import shutil

# Copy a file
shutil.copy("source.txt", "destination.txt")

# Move a file
shutil.move("old_folder/file.txt", "new_folder/file.txt")

# Delete a directory
shutil.rmtree("old_directory")

# Create a ZIP archive
shutil.make_archive("backup", "zip", "my_folder")

# Get disk usage
total, used, free = shutil.disk_usage("/")
print(f"Total: {total}, Used: {used}, Free: {free}")
