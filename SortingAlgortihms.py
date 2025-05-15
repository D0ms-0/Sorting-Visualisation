import random
from tokenize import String


class SortingAlgorithms:
    def __init__(self, observer, array: list, delay: float):
        self.observer = observer
        self.array = array
        self.delay = delay

    def selection_sort(self) -> list:
        for iteration in range(len(self.array)):
            minimum = iteration
            for i in range(iteration + 1, len(self.array)):
                if self.array[i] < self.array[minimum]:
                    minimum = i
            (self.array[minimum], self.array[iteration]) = (self.array[iteration], self.array[minimum])
            self._update()
        return self.array

    def bubble_sort(array) -> list:
        """for iteration in range(len(array)):
            for i in range(len(array) - 1):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
        return array
        """
        pass

    def insertion_sort(array) -> list:
        """
        for iteration in range(1, len(array)):
            index = iteration
            element = array.pop(iteration)
            for i in range(iteration - 1, -1, -1):
                if element < array[i]:
                    index = i
            array.insert(index, element)
        return array
        """
        pass

    def bogosort(array):
        """
        def isSorted(array):
            if len(array) < 2:
                return True
            for i in range(len(array) - 1):
                if array[i] > array[i + 1]:
                    return False
            return True

        while not isSorted(array):
            random.shuffle(array)
        return array
        """
        pass

    def _update(self):
        self.observer.update(self.array)

    def _mark(self, indices: list, color = str):
        pass
