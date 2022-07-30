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

    def BFS(self):
        current = self.root
        queue = []
        results = []
        queue.append(current.value)
        while len(queue) > 0:
            current = queue.pop(0)
            results.append(current.value)
            if current.left is not None:
                results.append(current.left)
            if current.right is not None:
                results.append(current.right)
        return results
