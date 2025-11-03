class MinBinaryHeap:
    '''
        >>> h = MinBinaryHeap()
        >>> h.getMin
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h
        [5, 10]
        >>> h.insert(14)
        >>> h._heap
        [5, 10, 14]
        >>> h.insert(9)
        >>> h
        [5, 9, 14, 10]
        >>> h.insert(2)
        >>> h
        [2, 5, 14, 10, 9]
        >>> h.insert(11)
        >>> h
        [2, 5, 11, 10, 9, 14]
        >>> h.insert(14)
        >>> h
        [2, 5, 11, 10, 9, 14, 14]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20, 20]
        >>> h.getMin
        2
        >>> h._leftChild(1)
        5
        >>> h._rightChild(1)
        11
        >>> h._parent(1)
        >>> h._parent(6)
        11
        >>> h._leftChild(6)
        >>> h._rightChild(9)
        >>> h.deleteMin()
        2
        >>> h._heap
        [5, 9, 11, 10, 20, 14, 14, 20]
        >>> h.deleteMin()
        5
        >>> h
        [9, 10, 11, 20, 20, 14, 14]
        >>> len(h)
        7
        >>> h.getMin
        9
    '''

    def __init__(self):
        self._heap=[]
        
    def __str__(self):
        return f'{self._heap}'

    __repr__=__str__

    def __len__(self):
        return len(self._heap)

    @property
    def getMin(self):
        # - YOUR CODE STARTS HERE -
        if len(self._heap) > 0:
            return self._heap[0]
        return None
    
    def _parent(self,index):
        # - YOUR CODE STARTS HERE -
        if index > 1:
            return self._heap[(index // 2) - 1]
        return None
        

    def _leftChild(self,index):
        # - YOUR CODE STARTS HERE -
        left_index = 2 * index
        if left_index <= len(self._heap):
            return self._heap[left_index - 1]
        return None

    def _rightChild(self,index):
        # - YOUR CODE STARTS HERE -
        right_index = 2 * index + 1
        if right_index <= len(self._heap):
            return self._heap[right_index - 1]
        return None
 
      

    def insert(self,item):
        # - YOUR CODE STARTS HERE -
        self._heap.append(item)
        index = len(self._heap)
        while index > 1 and item < self._parent(index):
            self._heap[index - 1] = self._parent(index)
            index = index // 2
        self._heap[index - 1] = item
        
        
    def deleteMin(self):
        if len(self) == 0:
            return None
        elif len(self) == 1:
            value = self._heap[0]
            self._heap = []
            return value

        # - YOUR CODE STARTS HERE -
        minimum = self._heap[0]
        self._heap[0] = self._heap.pop()
        index = 1
        while index * 2 <= len(self._heap):
            left = self._leftChild(index)
            right = self._rightChild(index)
            small = index
            if left is not None and self._heap[2 * index - 1] < self._heap[index - 1]:
                small = 2 * index
            if right is not None and self._heap[2 * index] < self._heap[small - 1]:
                small = 2 * index + 1
            if small != index:
                self._heap[index - 1], self._heap[small - 1] = self._heap[small - 1], self._heap[index - 1]
                index = small
            else:
                index = len(self._heap) + 1
        return minimum
    
    
class PriorityQueue:
    '''
        >>> priority_q = PriorityQueue()
        >>> priority_q.isEmpty()
        True
        >>> priority_q.peek()
        >>> priority_q.enqueue('sara',0)
        >>> priority_q
        [(0, 'sara')]
        >>> priority_q.enqueue('kyle',3)
        >>> priority_q
        [(0, 'sara'), (3, 'kyle')]
        >>> priority_q.enqueue('harsh',1)
        >>> priority_q
        [(0, 'sara'), (3, 'kyle'), (1, 'harsh')]
        >>> priority_q.enqueue('ajay',5)
        >>> priority_q
        [(0, 'sara'), (3, 'kyle'), (1, 'harsh'), (5, 'ajay')]
        >>> priority_q.enqueue('daniel',4)
        >>> priority_q.isEmpty()
        False
        >>> priority_q
        [(0, 'sara'), (3, 'kyle'), (1, 'harsh'), (5, 'ajay'), (4, 'daniel')]
        >>> priority_q.enqueue('ryan',7)
        >>> priority_q
        [(0, 'sara'), (3, 'kyle'), (1, 'harsh'), (5, 'ajay'), (4, 'daniel'), (7, 'ryan')]
        >>> priority_q.dequeue()
        (0, 'sara')
        >>> priority_q.peek()
        'harsh'
        >>> priority_q
        [(1, 'harsh'), (3, 'kyle'), (7, 'ryan'), (5, 'ajay'), (4, 'daniel')]
        >>> priority_q.dequeue()
        (1, 'harsh')
        >>> len(priority_q)
        4
        >>> priority_q.dequeue()
        (3, 'kyle')
        >>> priority_q.dequeue()
        (4, 'daniel')
        >>> priority_q.dequeue()
        (5, 'ajay')
        >>> priority_q.dequeue()
        (7, 'ryan')
        >>> priority_q.dequeue()
        >>> priority_q.isEmpty()
        True
    '''

    def __init__(self):
        self._items = MinBinaryHeap()
    
    def enqueue(self, value, priority):
        # - YOUR CODE STARTS HERE -
        self._items.insert((priority, value))

    
    def dequeue(self):
        # - YOUR CODE STARTS HERE -
        if len(self._items) == 0:
            return None
        return self._items.deleteMin()
    
    def peek(self):
        # - YOUR CODE STARTS HERE -
        if len(self._items) == 0:
            return None
        priority, value = self._items.getMin
        return value

    def isEmpty(self):
        # - YOUR CODE STARTS HERE -
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    __repr__ = __str__





class Graph:
    """
        >>> d_g1={
        ... 'A':[('B',2),('C',6),('D',7)],
        ... 'B':[('C',3),('G',12)],
        ... 'C':[('D',2),('E',3)],
        ... 'D':[('C',1),('E',2)],
        ... 'E':[('G',5)],
        ... 'F':[('D',2),('E',4)]}
        >>> my_graph = Graph(d_g1)
        >>> my_graph.addEdge('G', 'C', 4)
        >>> my_graph
        {'A': [('B', 2), ('C', 6), ('D', 7)], 'B': [('C', 3), ('G', 12)], 'C': [('D', 2), ('E', 3)], 'D': [('C', 1), ('E', 2)], 'E': [('G', 5)], 'F': [('D', 2), ('E', 4)], 'G': [('C', 4)]}
        >>> my_graph.dijkstra_table('A')   # ---> order of key,value pairs does not matter 
        {'A': 0, 'B': 2, 'C': 5, 'D': 7, 'E': 8, 'F': inf, 'G': 13}
    """
    def __init__(self, graph_repr=None):
        if graph_repr is None:
            self.vertList = {}
        else:
            self.vertList = graph_repr

    def __str__(self):
        return str(self.vertList)

    __repr__ = __str__

    def addVertex(self, key):
        if key not in self.vertList:
            self.vertList[key] = []
            return self.vertList

    def addEdge(self, frm, to, cost=1):
        if frm not in self.vertList:
            self.addVertex(frm)
        if to not in self.vertList:
            self.addVertex(to)
        self.vertList[frm].append((to, cost))


    def dijkstra_table(self,start):
        # - YOUR CODE STARTS HERE -
        temp = PriorityQueue()
        distmin = {}
        for vertex in self.vertList:
            distmin[vertex] = float('inf')
            
        distmin[start] = 0
        temp.enqueue(start, 0)

        while not temp.isEmpty():
            current = temp.dequeue()
            if isinstance(current, tuple):
                current = current[1]

            for neighbor, cost in self.vertList[current]:
                distance = distmin[current] + cost
                if distance < distmin[neighbor]:
                    distmin[neighbor] = distance
                    temp.enqueue(neighbor, distance)

        return distmin