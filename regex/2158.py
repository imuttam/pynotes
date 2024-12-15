from scapy.all import rdpcap
import re

data = []
# Load .pcapng file
packets = rdpcap("2158.pcapng")

# Correct pattern to match IP addresses starting with 10.221
pattern = r'10\.221\.\d{1,3}\.\d{1,3}'


for packet in packets:
    # Convert packet to string and search for the pattern
    packet_str = str(packet)
    match = re.findall(pattern, packet_str)
    if match:
        print(packet)
        data.append(packet)

# Now 'data' contains all packets with IP addresses starting with 10.221


# # Save to CSV
# df = pd.DataFrame(data)
# df.to_csv("tcp.csv", index=False)