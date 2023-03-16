class List:
    def __init__(self, n):
        self.data = n
        self.address = None
class LinkList:
    def __init__(self):
        self.head = None
        self.last = None
    def createlist(self, n):
        newnode = List(n)
        if self.head is None:
            self.head = newnode
        else:
            self.last.address = newnode
        self.last = newnode
    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.address
    def countnumbers(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.address
        print(count)
    def max(self):
        temp=self.head
        max=temp.data
        while temp is not None:
            if temp.data>max:
                max=temp.data
            temp=temp.address
        print(max)
s = LinkList()
s.createlist(10)
s.createlist(20)
s.createlist(30)
s.countnumbers()
s.max()
s.printlist()
