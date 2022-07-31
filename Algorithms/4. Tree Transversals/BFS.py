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

    # Breadth-First Search
    def BFS(self):
        current = self.root
        queue = []
        results = []
        queue.append(current)
        while len(queue) > 0:
            current = queue.pop(0)
            results.append(current.value)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        return results


# mytree = BST()
# mytree.insert(47)
# mytree.insert(21)
# mytree.insert(76)
# mytree.insert(18)
# mytree.insert(27)
# mytree.insert(52)
# mytree.insert(82)


# print(mytree.BFS())
