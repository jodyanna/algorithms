"""Class module for testing the time complexity of various sorting algorithms."""


def timer(func):
    """
    Wrapper function to time functions and print result to console.
    :param func:
    :return wrapper:
    """
    from time import time
    from functools import wraps
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        print(f"Runtime: {time() - start_time} s")
        return result

    return wrapper


def swap(a, b):
    """
    Simple swapping function that takes two variables and swaps their values.
    :param a:
    :param b:
    :return a, b:
    """
    temp = a
    a = b
    b = temp
    return a, b


def copy_array(array):
    """
    Returns a copy of the parameter array.
    :param array:
    :return array:
    """
    return [array[i] for i in range(len(array))]


def merge_arrays(left_array, right_array):
    """
    Merge two arrays into one sorted array.
    :param left_array:
    :param right_array:
    :return array:
    """
    result = []

    while left_array and right_array:
        if left_array[0] <= right_array[0]:
            result.append(left_array[0])
            left_array.pop(0)
        else:
            result.append(right_array[0])
            right_array.pop(0)

    while left_array:
        result.append(left_array[0])
        left_array.pop(0)

    while right_array:
        result.append(right_array[0])
        right_array.pop(0)

    return result


class Sort:
    def quick_sort(self, array):
        pass

    @timer
    def merge_sort_top_down(self, array):
        if len(array) < 2:
            return array

        left = [array[i] for i in range(len(array)) if i < (len(array) / 2)]
        right = [array[i] for i in range(len(array)) if i > ((len(array) - 1) / 2)]

        left = self.merge_sort_top_down(left)
        right = self.merge_sort_top_down(right)

        return merge_arrays(left, right)

    def tim_sort(self, array):
        pass

    def heap_sort(self, array):
        pass

    @staticmethod
    @timer
    def bubble_sort(array):
        n = len(array)
        is_swapped = True
        while is_swapped:
            is_swapped = False
            for i in range(1, n):
                if array[i - 1] > array[i]:
                    array[i - 1], array[i] = swap(array[i - 1], array[i])
                    is_swapped = True
            n -= 1

    @staticmethod
    @timer
    def bubble_sort_v2(array):
        n = len(array)
        while n > 2:
            new_n = 0
            for i in range(1, n):
                if array[i - 1] > array[i]:
                    array[i - 1], array[i] = swap(array[i - 1], array[i])
                    new_n = i
            n = new_n

    @staticmethod
    @timer
    def insertion_sort(array):
        i = 1
        while i < len(array):
            j = i
            while j > 0 and array[j - 1] > array[j]:
                array[j], array[j - 1] = swap(array[j], array[j - 1])
                j -= 1
            i += 1

    @staticmethod
    @timer
    def insertion_sort_v2(array):
        i = 1
        while i < len(array):
            temp = array[i]
            j = i - 1
            while j > -1 and array[j] > temp:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = temp
            i += 1

    @timer
    def insertion_sort_r(self, array, n):
        if n > 0:
            self.insertion_sort_r(array, n - 1)
            temp = array[n]
            i = n - 1
            while i > -1 and array[i] > temp:
                array[i + 1] = array[i]
                i -= 1
            array[i + 1] = temp
        return array

    @staticmethod
    @timer
    def selection_sort(array):
        for i in range(len(array) - 1):
            j = i + 1
            j_min = i
            while j < len(array):
                if array[j] < array[j_min]:
                    j_min = j
                j += 1
            if j_min != i:
                array[i], array[j_min] = swap(array[i], array[j_min])

    def tree_sort(self, array):
        pass

    def shell_sort(self, array):
        pass

    def bucket_sort(self, array):
        pass

    def radix_sort(self, array):
        pass

    def counting_sort(self, array):
        pass

    def cube_sort(self, array):
        pass
