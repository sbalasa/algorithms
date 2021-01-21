 #       A
 #    /  |  \
 #   B   C   D
 # /   \    /  \
 # E   F    G   H
 #    / \    \
 #   I   J    K

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name
        
    def add_child(self, name):
        self.children.append(Node(name))
        return self
    
    def depth_first_search(self, array):
        array.append(self.name)
        for child in self.children:
            child.depth_first_search(array)
        return array

if __name__ == "__main__":
    graph = Node("A")
    graph.add_child("B").add_child("C").add_child("D")
    graph.children[0].add_child("E").add_child("F")
    graph.children[2].add_child("G").add_child("H")
    graph.children[0].children[1].add_child("I").add_child("J")
    graph.children[2].children[0].add_child("K")
    print(graph.depth_first_search([])) 
    
# Outputs ['A', 'B', 'E', 'F', 'I', 'J', 'C', 'D', 'G', 'K', 'H']
