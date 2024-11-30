# Define the Node class for DFS (Graph traversal)
class Node:
    def __init__(self, value):  # Corrected __init__ constructor
        self.value = value
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

# Depth-First Search using a stack
def dfs_stack(start_node):
    visited = set()  
    stack = [start_node]  
    
    while stack:
        current_node = stack.pop()  
        if current_node not in visited:
            print(current_node.value, end=' ')  # Print without a newline
            visited.add(current_node) 
            for neighbor in current_node.neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)

# Define nodes for graph traversal
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')

# Create the graph by adding neighbors
a.add_neighbor(b)
a.add_neighbor(c)
b.add_neighbor(d)
c.add_neighbor(e)
d.add_neighbor(a)
e.add_neighbor(b)

# Perform DFS traversal starting from node 'A'
print("DFS Traversal:")
dfs_stack(a)
print("\n")  # Newline for better readability


# Define the Node class for Binary Tree traversal
class BinaryTreeNode:
    def __init__(self, value):  # Corrected __init__ constructor
        self.value = value
        self.left = None
        self.right = None

# Inorder Traversal (Left, Root, Right)
def inorder(root):
    if root:
        inorder(root.left)      
        print(root.value, end=' ')  # Print without newline        
        inorder(root.right)     

# Preorder Traversal (Root, Left, Right)
def preorder(root):
    if root:
        print(root.value, end=' ')  # Print root first        
        preorder(root.left)   
        preorder(root.right)  

# Postorder Traversal (Left, Right, Root)
def postorder(root):
    if root:
        postorder(root.left)     
        postorder(root.right)  
        print(root.value, end=' ')  # Print root last 

# Create a simple binary tree
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)

# Perform tree traversals
print("Inorder Traversal:")
inorder(root)  # Should print: 4 2 5 1 3
print("\nPreorder Traversal:")
preorder(root)  # Should print: 1 2 4 5 3
print("\nPostorder Traversal:")
postorder(root)  # Should print: 4 5 2 3 1
