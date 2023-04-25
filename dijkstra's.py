
def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]
    while heap:
        (current_distance, current_node) = heap.heappop(heap)
        
        if current_node == end:
            return distances[end]
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heap.heappush(heap, (distance, neighbor))
    return float('inf')