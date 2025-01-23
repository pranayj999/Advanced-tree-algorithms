class SNode:
    def __init__(self):
        self.branches = {}
        self.indices = []

class SuffixTreeCustom:
    def __init__(self, sequence):
        self.head = SNode()
        self.seq = sequence
        self.construct_tree()

    def construct_tree(self):
        for idx in range(len(self.seq)):
            curr_node = self.head
            for ch in self.seq[idx:]:
                if ch not in curr_node.branches:
                    curr_node.branches[ch] = SNode()
                curr_node = curr_node.branches[ch]
                curr_node.indices.append(idx)

    def visualize_tree(self, node=None, depth=0):
        if node is None:
            node = self.head
        for key, child in node.branches.items():
            print(f"{' ' * depth}{key}: {child.indices}")
            self.visualize_tree(child, depth + 2)

# Example usage:
s_tree_custom = SuffixTreeCustom("ACGTACGTG")
print("S-Tree Structure:")
s_tree_custom.visualize_tree()
