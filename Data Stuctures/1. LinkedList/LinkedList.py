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

    def delete(self, value):
        temp = self.get_head()
        prev_node = None
        deleted = False

        if self.is_empty():
            return deleted

        if temp.data == value:
            self.delete_at_head()
            deleted = True
            return deleted

        while temp.next:
            if temp.data == value:
                prev_node.next = temp.next
                temp.next = None
                deleted = True
                return deleted
            prev_node = temp
            temp = temp.next
        return deleted

    def length(self):
        length = 0
        temp = self.get_head()
        if self.is_empty():
            return length

        while temp:
            length += 1
            temp = temp.next
        return length
