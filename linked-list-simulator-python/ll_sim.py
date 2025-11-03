class Node: # You are not allowed to modify this class
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return f"Node({self.value})"

    __repr__ = __str__
                        
                          
class SortedLinkedList:
    def __init__(self):   # You are not allowed to modify the constructor
        self.head=None
        self.tail=None

    def __str__(self):   # You are not allowed to modify this method
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out) 
        return f'Head:{self.head}\nTail:{self.tail}\nList:{out}'

    __repr__=__str__


    def isEmpty(self):
        return self.head == None

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            current = current.next
            count += 1
        return count

                
    def add(self, value):
        # --- YOUR CODE STARTS HERE
        new_node = Node(value)
        if self.__len__() == 0:
            self.head = new_node
            self.tail = new_node
            
        elif value <= self.head.value:
            new_node.next = self.head
            self.head = new_node
            
        else:
            a = self.head
            while a.next is not None and a.next.value < value:
                a = a.next
            new_node.next = a.next
            a.next = new_node
        
            if new_node.next is None:
                self.tail = new_node
            
                    
      
    def split(self):
        # --- YOUR CODE STARTS HERE
        if self.isEmpty():
            return None

        part1 = SortedLinkedList()
        part2 = SortedLinkedList()
        
        if self.__len__() % 2 == 0:
            a = self.head
            for i in range(1, int(self.__len__() / 2) + 1):
                part1.add(a.value)
                a = a.next
            while a is not None:
                part2.add(a.value)
                a = a.next
        
        else:
            a = self.head
            centre = self.__len__() // 2 + self.__len__() % 2
            for i in range(1, centre + 1):
                part1.add(a.value)
                a = a.next
            while a is not None:
                part2.add(a.value)
                a = a.next
                
        return part1, part2
        

    def removeDuplicates(self):
        # --- YOUR CODE STARTS HERE
        if self.isEmpty():
            return None
        
        a = self.head
        while a is not None and a.next is not None:
            if a.value == a.next.value:
                a.next = a.next.next
            else:
                a = a.next
        if a is not None:
            self.tail = a
        else:
            self.head = a

    def intersection(self, other):
        # --- YOUR CODE STARTS HERE
        a = self.head
        b = other.head
        new = SortedLinkedList()
        
        while a is not None and b is not None:
            if a.value == b.value:
                new.add(a.value)
                a = a.next
                b = b.next
            elif a.value < b.value:
                a = a.next
            else:
                b = b.next

        new.removeDuplicates()
        return new