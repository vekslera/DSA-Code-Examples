import numpy as np

class Array:

    def __init__(self, arg):
        if type(arg) == list or type(arg) == tuple or type(arg) == np.ndarray:
            self.arr = np.array(arg)
        elif type(arg) == int and arg >= 0:
            self.arr = np.zeros(arg)
        else:
            raise TypeError("arg must be an array or an integer")

    @property
    def size(self):
        return self.arr.size

    def get_by_index(self, index):
        if index < 0 or index >= self.size:
            return None
        return self.arr[index]

    def search_by_value(self, value):
        for index, val in enumerate(self.arr):
            if value == val:
                return index
        return None

    def update(self, index, value):
        if index < 0 or index >= self.size:
            return None
        self.arr[index] = value
        return index

    def __str__(self):
        if self.size == 0:
            return "[]"
        s = '[ '
        for val in self.arr:
            s += f'{str(val)}, '
        s = s[:-2] + ']'
        return s


class DynArray:

    def __init__(self, value=None):
        if value is None:
            self.lst = []
        else:
            self.lst = [value]

    @property
    def size(self):
        return len(self.lst)

    def insert(self, index, value):
        if index < 0 or index > self.size:
            return None
        elif index == self.size:
            self.lst.append(value)
        else:
            self.lst.insert(index, value)
        return index

    def get_by_index(self, index):
        if index < 0 or index >= self.size:
            return None
        return self.lst[index]

    def search_by_value(self, value):
        for index, val in enumerate(self.lst):
            if val == value:
                return index
        return None

    def update(self, index, value):
        if index < 0 or index >= self.size:
            return None
        self.lst[index] = value
        return True

    def delete(self, index):
        if index < 0 or index >= self.size:
            return None
        self.lst.pop(index)
        return True

    def __str__(self):
        if self.size == 0:
            return "[]"
        s = '[ '
        for val in self.lst:
            s += f'{str(val)}, '
        s = s[:-2] + ']'
        return s

class LinkedList:

    class Node:

        def __init__(self, value):
            self.value = value
            self.next = None

        def __str__(self):
            return f"{self.value} ==> {self.next}"

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
        new_node = self.Node(value)
        if self.is_empty():
            self.insert_at_empty(new_node)
        if isinstance(location, str):
            match location:
                case "head":
                    self.insert_at_head(new_node)
                case "tail":
                    self.insert_at_tail(new_node)
                case _: return None
        elif isinstance(location, int):
            self.insert_at_index(new_node, location)
        elif isinstance(location, self.Node):
            self.insert_after(new_node, location)
        else:
            return None
        self._size += 1
        return location

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def insert_at_tail(self, node):
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
            for i in range(index):
                temp = temp.next
            self.insert_after(node, temp)

    def search_by_value(self, value):
        temp = self.head
        index = 0
        while not temp is None:
            if temp.value == value:
                return index
            temp = temp.next
            index += 1
        return None

    def search_by_index(self, index):
        if index < 0 or index >= self.size:
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp.value

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

    def delete_from_head(self):
        if self.is_empty():
            return None
        value = self.head.value
        self.head = self.head.next
        self._size -= 1
        return value

    def delete_from_tail(self):
        if self.is_empty():
            return None
        temp = self.head
        value = self.tail.value
        while not temp.next is None and not temp.next.next is None:
            temp = temp.next
        self.tail = temp
        self.tail.next = None
        self._size -= 1
        return value

    def delete_by_index(self, index):
        if index < 0 or index >= self.size:
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        value = temp.next.value
        temp.next = temp.next.next
        self._size -= 1
        return value


if __name__ == "__main__":
    arr_size = 10
    arr1 = Array(arr_size)
    print(arr1)
    arr2 = Array([i for i in range(arr_size)])
    print(arr2)
    for i in range(arr_size):
        arr1.update(i, arr2.get_by_index(i))
    print(arr1)

    dyn_arr1 = DynArray()
    print(dyn_arr1)
    for i in range(arr_size):
        dyn_arr1.insert(i, i)
    print(dyn_arr1)
    dyn_arr1.insert(arr_size // 2, arr_size // 2)
    print(dyn_arr1)