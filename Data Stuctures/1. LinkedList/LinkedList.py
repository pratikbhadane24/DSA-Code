from requests import delete
import Node


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        return self.head_node == None

    def print_list(self):
        if self.is_empty():
            return "List is Empty"
        temp = self.get_head()
        while temp.next is not None:
            print(temp.data, end=" ->")
            temp = temp.next
        print(temp.data, "-> None")
        return True

    def insert_at_tail(self, value):
        new_node = Node(value)
        temp = self.get_head()

        while temp:
            temp = temp.next
        temp.next_element = new_node
        return

    def search(self, value):
        if self.is_empty():
            return False

        temp = self.get_head()
        while temp:
            if temp.data == value:
                return True
            temp = temp.next

        return False
