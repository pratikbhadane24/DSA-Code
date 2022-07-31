from Node import Node


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                print("Duplicate Found")
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            elif new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    # Pre-Order Depth-First Search
    def DFS_preOrder(self):
        results = []

        def traverse(current):
            results.append(current.value)
            if current.left is not None:
                traverse(current.left)
            if current.right is not None:
                traverse(current.right)
        traverse(self.root)
        return results

    # Post-Order Depth-First Search
    def DFS_postOrder(self):
        results = []

        def traverse(current):
            if current.left is not None:
                traverse(current.left)
            if current.right is not None:
                traverse(current.right)
            results.append(current.value)

        traverse(self.root)
        return results

    # In-Order Depth-First Search
    def DFS_inOrder(self):
        results = []

        def traverse(current):
            if current.left is not None:
                traverse(current.left)
            results.append(current.value)
            if current.right is not None:
                traverse(current.right)
        traverse(self.root)
        return results


mytree = BST()
mytree.insert(47)
mytree.insert(21)
mytree.insert(76)
mytree.insert(18)
mytree.insert(27)
mytree.insert(52)
mytree.insert(82)

print(mytree.DFS_preOrder())
print(mytree.DFS_postOrder())
print(mytree.DFS_inOrder())
