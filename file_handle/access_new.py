import re
pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"

ips = set()
with open("access.log", 'r') as file:
    lines = (re.search(pattern, line).group()  for line in file if re.search(pattern, line))
    for ip in lines:
        ips.add(ip)

print(len(ips))

ip = set()
with open("access.log", 'r') as file: 
    for line in file: 
        match = re.search(pattern, line) 
        if match: ip.add(match.group())