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