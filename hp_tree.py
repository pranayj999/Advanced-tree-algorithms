class HeavyPathNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.descendants = []
        self.weight = 0
        self.main_path = None

class HeavyPathDecomposer:
    def __init__(self):
        self.tree = {}

    def add_node(self, node_id, parent_id=None, weight=1):
        if node_id not in self.tree:
            self.tree[node_id] = HeavyPathNode(node_id)
        self.tree[node_id].weight = weight
        if parent_id:
            if parent_id not in self.tree:
                self.tree[parent_id] = HeavyPathNode(parent_id)
            self.tree[parent_id].descendants.append(node_id)

    def find_heavy_paths(self):
        for node in self.tree:
            if not self.tree[node].main_path:  # Root or not assigned yet
                self._assign_path(node)

    def _assign_path(self, node_id, path=None):
        if path is None:
            path = []
        path.append(node_id)
        children = self.tree[node_id].descendants
        if not children:
            self.tree[node_id].main_path = path
            return path

        # Find heaviest child
        heaviest = max(children, key=lambda x: self.tree[x].weight)
        for child in children:
            if child != heaviest:
                self._assign_path(child)
        return self._assign_path(heaviest, path)

    def display_heavy_paths(self):
        visited_paths = set()
        for node in self.tree:
            path = tuple(self.tree[node].main_path or [])
            if path and path not in visited_paths:
                visited_paths.add(path)
                print(f"Heavy Path: {path}")

# Example usage:
hp_decomposer = HeavyPathDecomposer()
hp_decomposer.add_node(1)  # Root
hp_decomposer.add_node(2, 1, weight=8)
hp_decomposer.add_node(3, 1, weight=3)
hp_decomposer.add_node(4, 2, weight=5)
hp_decomposer.add_node(5, 2, weight=7)
hp_decomposer.add_node(6, 3, weight=2)
hp_decomposer.find_heavy_paths()
print("\nHeavy Path Decomposition Results:")
hp_decomposer.display_heavy_paths()
