class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.dic = {}
        for start, end in edges:
            if start in self.dic:
                self.dic[start].append(end)
            else:
                self.dic[start] = [end]
        print("Graph Dictionary:", self.dic)

    def get_path(self, start, end, path=[]):
        path = path + [start]  # Keep extending the current path

        if start == end:
            return [path]  # If start and end are the same, return the path

        if start not in self.dic:
            return []  # If start is not in the graph, return empty list

        paths = []  # List to store all paths
        for node in self.dic[start]:
            if node not in path:  # Avoid revisiting nodes
                new_paths = self.get_path(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]  # Keep extending the current path

        if start == end:
            return path  # Return the path when start == end

        if start not in self.dic:
            return None  # Return None if start is not in the graph

        shortest_path = None  # Variable to track the shortest path
        for node in self.dic[start]:
            if node not in path:  # Avoid revisiting nodes
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp  # Update if a shorter path is found
        return shortest_path

if __name__ == '__main__':
    route = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_graph = Graph(route)  # Create the graph object
    start = "Mumbai"
    end = "New York"
    print(f"All the paths between {start} and {end}: {route_graph.get_path(start, end)}")
    print(f"Shortest path between {start} and {end}: {route_graph.get_shortest_path(start, end)}")