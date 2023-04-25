
import random
def slotted_aloha(num_nodes, p):
    slots = [0] * num_nodes
    successful_transmissions = 0
    
    for i in range(num_nodes):
        if random.random() < p:
            slots[i] = 1
            
    for i in range(num_nodes):
        if slots[i] == 1:
            successful_transmissions += 1
            for j in range(i+1, num_nodes):
                if slots[j] == 1:
                    slots[j] = 0
                    break
                    
    return successful_transmissions