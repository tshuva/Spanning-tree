class Heap:

    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def left(self, i):
        return 2 * i

    def right(self, i):
        return 2 * i + 1

    def parent(self, i):
        return int(i / 2)

    def exchange(self, i, j):
        temp = self.heapList[j]
        self.heapList[j] = self.heapList[i]
        self.heapList[i] = temp

    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l <= self.currentSize and self.heapList[l] < self.heapList[i]:
            smallest = l
        else:
            smallest = i
        if r <= self.currentSize and self.heapList[r] < self.heapList[smallest]:
            smallest = r
        if smallest != i:
            self.exchange(i, smallest)
            self.heapify(smallest)

    def build_heap(self, array):
        self.heapList[1:] = array
        self.currentSize = len(array)
        for i in range(int(len(array)/2), 0, -1):
            self.heapify(i)

    def extract_min(self):
        ret_val = self.heapList[1]
        self.exchange(1, self.currentSize)
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.heapify(1)
        return ret_val