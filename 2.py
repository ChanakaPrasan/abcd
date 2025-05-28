class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next




l1 = LinkedList()
l1.head = Node("toyota")
l2 = Node("BMW")
l3 = Node("Audi")
l4 = Node("Lambogini")

l1.head.next = l2
l2.next = l3
l3.next =l4


l1.listprint()
print(" ")

