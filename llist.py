class Node:
	def __init__(self,x):
		self.data = x
		self.next = None
class LinkedList:
    def __init__(self):
        self.top = None
    def printList(self):
        #current = self.top
        while self.top is not None:
            print(self.top.data)
            self.top = self.top.next
    def in_list(self, x):
        current = self.top 
        while current is not None:
            if current.data is x:
                return 1
            current = current.next
        return 0
    def findCellBefore(self, x):
        current = self.top
        if current is None:
            return None
        while current.next is not None:
            if current.next.data is x:
                current = current.next
        return 0
    def findCellBeforeSential(self,x):
        if (self.top.next is None):
            return None 
        while (self.top.next is not None):
            if (self.top.next.data is x):
                return self.top.data
        return None
    def add_0(self, newNode):
        # i. allocate the Node and put in the data
        #newNode = Node(x)
        # ii. make next of new node as head'
        newNode.next = self.top
        # iii. move head to point to new Node
        self.top = newNode
    def add_end(self, newNode):
        current = self.top
        while (current.next is not None):
            current = current.next

        current.next = newNode
        newNode.next = None
    def insertNode(self, after_me, new_cell):
        new_cell.next = after_me.next 
        after_me.next = new_cell
    def  deleteAfter(self, after_me):
            after_me.next = after_me.next.next


Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)

#Node1.next = Node(2)

#Node2.next = Node(3)
#Node3.next = None


list1 = LinkedList()
list1.add_0(Node1)
list1.add_0(Node2)
list1.add_0(Node3)
Node4 = Node(4)
list1.add_end(Node4)
Node5 = Node(5)
#print(list1.findCellBeforeSential(2))
list1.insertNode(Node4, Node5)
list1.deleteAfter(Node4)

list1.printList()


