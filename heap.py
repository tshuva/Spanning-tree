class MinHeap:
    def __init__(self, max_size):
        self.maxsize = max_size
        self.size = 0
        self.Heap = [0] * self.maxsize
        self.FRONT = 1

    def get_parent(self, pos):
        return pos // 2

    def get_left_child(self, pos):
        return 2 * pos

    def get_right_child(self, pos):
        return (2 * pos) + 1

    def is_leaf(self, pos):
        return (self.size // 2) <= pos <= self.size

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size - 1] = element

        current = self.size - 1

        while self.Heap[current] < self.Heap[self.get_parent(current)]:
            self.swap(current, self.get_parent(current))
            current = self.get_parent(current)

    def min_heapify(self, pos):

        # If the node is a non-leaf and greater than any of its children
        if not self.is_leaf(pos):
            if (self.Heap[pos] > self.Heap[self.get_left_child(pos)] or
                    self.Heap[pos] > self.Heap[self.get_right_child(pos)]):

                # Swap with the left child and heapify
                # the left child
                if self.Heap[self.get_left_child(pos)] < self.Heap[self.get_right_child(pos)]:
                    self.swap(pos, self.get_left_child(pos))
                    self.min_heapify(self.get_left_child(pos))

                    # Swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.get_right_child(pos))
                    self.min_heapify(self.get_right_child(pos))

    def build_heap(self, nodes):
        for node in nodes:
            self.insert(node)
        for pos in range(self.size // 2, 0, -1):
            self.min_heapify(pos)

    def extract_min(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size - 1]
        self.size -= 1
        if self.size > 0:
            self.min_heapify(self.FRONT)
        return popped
