from abc import ABC, abstractmethod

class CustomArray:
    def __init__(self, sorting_technique, arr):
        self.sorting_technique = sorting_technique
        self.array = []
        self.array.extend(arr)

    def sort(self):
        self.sorting_technique.sort(self.array)

    def print_arr(self):
        print(self.array)

class SortingMethod(ABC):
    def sort(self, arr):
        pass

class BubbleSort(SortingMethod):
    def sort(self, arr):
        print("Sorting by bubble sort... ")
        arr.sort()


class InsertionSort(SortingMethod):
    def sort(self, arr):
        print("Sorting by insertion sort... ")
        arr.sort()


class CountingSort(SortingMethod):
    def sort(self, arr):
        print("Sorting by counting sort... ")
        arr.sort()


class QuickSort(SortingMethod):
    def sort(self, arr):
        print("Sorting by quick sort... ")
        arr.sort()


class MergeSort(SortingMethod):
    def sort(self, arr):
        print("Sorting by merge sort... ")
        arr.sort()

if __name__ == "__main__":
    arr = [13,9,3,5,4,9,17]
    l1 = CustomArray(BubbleSort(),arr)
    l2 = CustomArray(InsertionSort(), arr)
    l3 = CustomArray(CountingSort(), arr)
    l4 = CustomArray(QuickSort(), arr)
    l5 = CustomArray(MergeSort(), arr)

    l1.sort()
    l1.print_arr()
    l2.sort()
    l2.print_arr()
    l3.sort()
    l3.print_arr()
    l4.sort()
    l4.print_arr()
    l5.sort()
    l5.print_arr()