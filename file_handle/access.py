import re

# Define the regex pattern for IPv4 addresses
pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
pattern1 = r"\d+.\d+.\d+.\d+"
pattern2 = r"\b(\d+)\.(\d+)\.(\d+)\.(\d+)\b"

ip_set = set()

# Open and read the file line by line
with open("access.log", 'r') as file:
    count = 0
    for line in file:
        # Search for the IP pattern in each line
        match = re.search(pattern2, line)
        if match:
            ip_set.add(match.group())
           
print(len(ip_set))