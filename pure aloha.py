
import random
packet_arrival_prob = 0.5
transmission_time = 1
num_slots = 10
packets = [1 if random.random() < packet_arrival_prob else 0 for _ in range(num_slots)]
transmitted_packets = []

for i, packet in enumerate(packets):
    if packet == 1:
        if all([i < t or i > t + transmission_time for t in transmitted_packets]):
            transmitted_packets.append(i)

print(transmitted_packets)