
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(set)

    def add_edge(self, node1, node2, **kwargs):
        self.graph[node1].add(node2)

        if not kwargs.get('oneway'):
            self.graph[node2].add(node1)

    def get(self, node):
        return self.graph.get(node)

    def shortest_path(self, node1, node2):
        paths = [[node1]]
        path_index = 0
        previous_nodes = {node1}

        if node1 == node2:
            return paths[0]

        while path_index < len(paths):
            current_path = paths[path_index]
            last_node = current_path[-1]
            next_nodes = self.graph.get(last_node)

            if node2 in next_nodes:
                current_path.append(node2)
                return current_path
            
            for next_node in next_nodes:
                if not next_node in previous_nodes:
                    new_path = current_path[:]
                    new_path.append(next_node)
                    paths.append(new_path)
                    previous_nodes.add(next_node)
            
            path_index += 1
        
        return []