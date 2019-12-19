class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None

    def Add_To_Front(self, val):
        newNode = Node(val)
        #check if head is already pointing to a node or no
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        return self
    def RemoveFromFront(self):
        #check if head is none or not
        if self.head != None:
            #reassign the head and delete
            self.head = self.head.next
            return self



mylist = SList()
mylist.Add_To_Front("test1").Add_To_Front("test2").Add_To_Front("test3")
mylist.RemoveFromFront().RemoveFromFront().RemoveFromFront()
