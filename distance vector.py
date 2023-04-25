
import numpy as np
def distance_vector_routing(cost_matrix):
    num_nodes = len(cost_matrix)
    distances = np.array(cost_matrix)
    
    for _ in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if distances[i][j] > distances[i][_]+distances[_][j]:
                    distances[i][j] = distances[i][_]+distances[_][j]
                    
    return distances