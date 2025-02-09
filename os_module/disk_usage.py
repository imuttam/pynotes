import shutil


disk_info = shutil.disk_usage("/")

# Convert to GB
total_gb = disk_info.total / (1024**3)
used_gb = disk_info.used / (1024**3)
free_gb = disk_info.free / (1024**3)

print(f"Total: {total_gb:.2f} GB")
print(f"Used: {used_gb:.2f} GB")
print(f"Free: {free_gb:.2f} GB")