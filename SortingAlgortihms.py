import random

class SortingAlgorithms:
    def __init__(self, observer, array, delay):
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

    def bubble_sort(self) -> list:
        for iteration in range(len(self.array)):
            for i in range(len(self.array) - 1):
                if self.array[i] > self.array[i + 1]:
                    self.array[i], self.array[i + 1] = self.array[i + 1], self.array[i]
            self._update()
        return self.array

    def insertion_sort(self) -> list:
        for iteration in range(1, len(self.array)):
            index = iteration
            element = self.array.pop(iteration)
            for i in range(iteration - 1, -1, -1):
                if element < self.array[i]:
                    index = i
            self.array.insert(index, element)
            self._update()
        return self.array


    def bogo_sort(self):
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

    def _mark(self, indices: list, color):
        self.observer.mark(indices, color)
