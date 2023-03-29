##Traversing a linked list
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
class LinkedList:
    def __init__(self):
        self.headval = None
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    def AtBegining(self,newdata): #Sun
        NewNode = Node(newdata) #newnode=4000
        #update the new nodes next val to existing node 
        NewNode.nextval = self.headval
        self.headval = NewNode
list = LinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list.headval.nextval = e2
e2.nextval = e3
list.AtBegining("Sun")
list.listprint()
##-------------------------------------------
#At end

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
class LinkedList:
    def __init__(self):
        self.headval = None
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    def AtEnd(self,newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste=laste.nextval
        laste.nextval=NewNode
list = LinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list.headval.nextval = e2
e2.nextval = e3
list.AtEnd("Sun")
list.listprint()
##----------------------------------------------
##in between
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
class LinkedList:
    def __init__(self):
        self.headval = None
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    def InBetween(self,middle_node,data):
        if middle_node is None:
            print("The mentioned element is not available")
        else:
            newNode = Node(data)
            newNode.nextval = middle_node.nextval
            middle_node.nextval = newNode
            
list = LinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list.headval.nextval = e2
e2.nextval = e3
list.InBetween(e2,"Fri")
list.listprint()
##--------------------------------------------------------------------------
class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None
class LinkedList:
    def __init__(self):
        self.start_node = None
    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item , " ")
                n = n.ref
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node= new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n=self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node
    def delete_at_start(self):
        if self.start_node is None:
            print("List has no element to delete")
            return
        self.start_node=self.start_node.ref
    def delete_at_end(self):
        if self.start_node is None:
            print("List has no element to delete")
            return
        n = self.start_node#2000
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None
    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("List has no element to delete")
            return
        if self.start_node.item == x:#30
            self.start_node = self.start_node.ref
            return
        n = self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("item not found in the list")
        else:
            n.ref = n.ref.ref
new_linked_list = LinkedList()
new_linked_list.insert_at_end(5)
new_linked_list.insert_at_end(10)
new_linked_list.insert_at_end(15)
new_linked_list.insert_at_end(20)
new_linked_list.insert_at_end(25)
new_linked_list.insert_at_end(30)
new_linked_list.insert_at_end(35)
new_linked_list.insert_at_end(40)
new_linked_list.insert_at_end(45)
new_linked_list.traverse_list()
new_linked_list.delete_at_start()
print("after deletion at the beginning")
new_linked_list.traverse_list()
new_linked_list.delete_at_end()
print("after deletion at the end")
new_linked_list.traverse_list()
new_linked_list.delete_element_by_value(30)
print("after deleting 30")
#new_linked_list.traverse_list()
