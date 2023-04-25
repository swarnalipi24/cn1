
bucket_size = 10
tokens = 0
token_rate = 1
packet_sizes = [3, 4, 2, 6, 7, 1, 5]

for packet_size in packet_sizes:
    if packet_size <= tokens:
        tokens -= packet_size
        print(f"Packet of size {packet_size} sent")
    else:
        print(f"Packet of size {packet_size} delayed")
    tokens = min(tokens + token_rate, bucket_size)