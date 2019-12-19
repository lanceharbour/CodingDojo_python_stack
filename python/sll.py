class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def AddToFront(self,val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        return self

    def AddToBack(self, val):
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = Node(val)
        return self

    def Contains(self, val):
        if self.head:
            runner = self.head
            while runner:
                print(f"Does {val} = {runner.val}?")
                if runner.val == val:
                    print(f"Yes...{val} = {runner.val}")
                    return True
                runner = runner.next
                print("no...")
        print(f"Doesn't contain {val}")
        return False

myList = SLL()
myList.Contains(1)
myList.AddToFront(4).AddToFront(3).AddToFront(2).AddToFront(1).Contains(5)
