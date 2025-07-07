class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value} ==> "

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self):
        return self.head is None

    @property
    def size(self):
        return self._size

    def insert(self, value, location="head"):
        new_node = Node(value)
        if self.is_empty():
            self.insert_at_empty(new_node)
        elif type(location) == str:
            match location:
                case "head":
                    self.insert_at_head(new_node)
                case "tail":
                    self.insert_at_tail(new_node)
                case _: return None
        elif type(location) == int:
            self.insert_at_index(new_node, location)
        elif isinstance(location, Node):
            self.insert_after(new_node, location)
        else:
            return None
        self._size += 1
        return location

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def insert_at_tail(self, node):
        self.tail.next = node
        self.tail = node

    def insert_at_empty(self, node):
        self.head = node
        self.tail = node

    def insert_after(self, node, after_node):
        if after_node is None:
            self.insert_at_tail(node)
        node.next = after_node.next
        after_node.next = node

    def insert_at_index(self, node, index):
        if index < 0:
            self.insert_at_head(node)
        elif index >= self.size:
            self.insert_at_tail(node)
        else:
            temp = self.head
            for i in range(index-1):
                temp = temp.next
            self.insert_after(node, temp)

    def search_by_value(self, value):
        temp = self.head
        index = 0
        while not temp is None:
            if temp.value == value:
                return temp
            temp = temp.next
            index += 1
        return None

    def search_by_index(self, index):
        if index < 0 or index >= self.size:
            return None
        temp = self.head
        for i in range(index-1):
            temp = temp.next
        return temp

    def update_by_index(self, index, new_value):
        if index < 0 or index >= self.size:
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        temp.value = new_value
        return index

    def update_by_value(self, old_value, new_value):
        temp = self.head
        while not temp is None:
            if temp.value == old_value:
                temp.value = new_value
                return new_value
            temp = temp.next
        return None

    def remove(self, location="head"):
        if self.is_empty():
            return None
        if type(location) == str:
            match location:
                case "head":
                    return self.remove_from_head()
                case "tail":
                    return self.remove_from_tail()
                case _: return None
        if type(location) == int:
            return self.remove_by_index(location)
        if type(location) == Node:
            return self.remove_after_node(location)
        return None


    def remove_from_head(self):
        if self.is_empty():
            return None
        temp = self.head
        self.head = self.head.next
        self._size -= 1
        return temp

    def remove_from_tail(self):
        if self.is_empty():
            return None
        temp = self.head
        while not temp.next is None and not temp.next.next is None:
            temp = temp.next
        self.tail = temp
        temp = temp.next
        self.tail.next = None
        self._size -= 1
        return temp

    def remove_by_index(self, index):
        if index < 0 or index >= self.size:
            return None
        temp = self.head
        for i in range(index-1):
            temp = temp.next
        return self.remove_after_node(temp)

    def remove_after_node(self, node):
        if node is None or node.next is None:
            return None
        temp = node.next
        node.next = node.next.next
        self._size -= 1
        return temp

    def __str__(self):
        temp = self.head
        s = ""
        while not temp is None:
            s += str(temp)
            temp = temp.next
        return s


if __name__ == "__main__":
    linked_list = LinkedList()
    print(linked_list)
    linked_list.insert(1)
    print(linked_list)
    linked_list.insert(2, "tail")
    print(linked_list)
    linked_list.insert(0, "head")
    print(linked_list)
    linked_list.insert(5, "tail")
    print(linked_list)
    linked_list.insert('c', 3)
    print(linked_list)
    linked_list.update_by_index(3, 3)
    print(linked_list)
    my_node = linked_list.search_by_value(3)
    linked_list.insert(4, my_node)
    print(linked_list)
    linked_list.remove()
    print(linked_list)
    linked_list.remove("tail")
    print(linked_list)
    my_node = linked_list.search_by_index(3)
    linked_list.remove(my_node)
    print(linked_list)
    linked_list.remove(2)
    print(linked_list)