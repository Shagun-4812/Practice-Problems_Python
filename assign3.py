import heapq

class ShippingNetwork:
    def __init__(self):
        self.routes = {}

    def add_route(self, city1, city2, distance):
        self.routes.setdefault(city1, []).append((distance, city2))
        self.routes.setdefault(city2, []).append((distance, city1))

    def shortest_paths(self, start):
        min_heap = [(0, start)]
        distances = {city: float('inf') for city in self.routes}
        distances[start] = 0

        while min_heap:
            current_distance, current_city = heapq.heappop(min_heap)

            for neighbor_distance, neighbor in self.routes[current_city]:
                new_distance = current_distance + neighbor_distance
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(min_heap, (new_distance, neighbor))

        return distances

# Example usage
network = ShippingNetwork()
network.add_route("A", "B", 50)
network.add_route("A", "C", 30)
network.add_route("B", "D", 70)
network.add_route("C", "D", 40)
network.add_route("C", "E", 60)
network.add_route("D", "F", 20)
network.add_route("E", "F", 50)
network.add_route("B", "E", 90)

distances = network.shortest_paths("A")
for city, distance in distances.items():
    print(f"Distance from A to {city}: {distance} km")