## linear search in python

def linearSearch(array,n,x):
    for i in range(0,n):
        if (array[i] == x):
            return i 
    return -1
array = [2,4,0,1,9]
x = 10
n = len(array)
result = linearSearch(array,n,x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index:",result)

## Binary search in python
    
def binarySearch(array,x,low,high):
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid+1 
        else:
            high = mid-1
    return -1 
array = [2,4,0,1,9]
x = 4
result = binarySearch(array,x,0,len(array)-1)
if result!= -1:
    print("Element is present at index"+ str(result))
else:
    print("Not found")
## inorder,preorder,postorder

class Node:
    def __init__(self,item):
        self.left = None
        self.right = None
        self.val = item
def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val)+ "->",end='')
        inorder(root.right)
def postorder(root):
    if(root):
        postorder(root.left)
        postorder(root.right)
        print(str(root.val)+ "->",end='')
def preorder(root):
    if(root):
        print(str(root.val)+ "->",end='')
        preorder(root.left)
        preorder(root.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Inorder traversal")
inorder(root)
print("\nPreorder traversal")
preorder(root)
print("\nPostorder traversal")
postorder(root)

##Binary search operations in python
##insertion operation

class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key)+ "->",end='')
        inorder(root.right)
def insert(node,key):
    if node is None:
        return Node(key)
    if key<node.key:
        node.left = insert(node.left,key)
    else:
        node.right = insert(node.right,key)
    return node 
root = None
root = insert(root,8)
root = insert(root,3)
root = insert(root,6)
root = insert(root,7)
root = insert(root,10)
root = insert(root,14)
root = insert(root,4)
print("Inorder traversal:",end='')
inorder(root)

##A train is identified by its name and list of compartments.
##The compartments are identified by its name,total seating 
##capacity and the number of passengers.
##Implement the class Train as given in the class diagram.
##Train
##- train_name
##- compartment_list
##_init_(train_name,compartment_list)
##+ get_train_name()
##+ get_compartment_list()
##+ count_compartments ()
##+ check_vacancy():
##Write a python program to implement the following:
##count_compartments()- returns the total number of compartments
 ##in the train
##check_vacancy()-returns the count of the compartments in which
 ##more than 50% of the seats are vacant
##Note : Compartment list is maintained as a linked list where 
##data in each node refers to a compartment.
##A train is identified by its name and list of compartments.
##The compartments are identified by its name,total seating 
##capacity and the number of passengers.
##Implement the class Train as given in the class diagram.
##Train
##- train_name
##- compartment_list
##_init_(train_name,compartment_list)
##+ get_train_name()
##+ get_compartment_list()
##+ count_compartments ()
##+ check_vacancy()
##Write a python program to implement the following:

##count_compartments()- returns the total number of compartments in the train
##check_vacancy()-returns the count of the compartments in which more than 50% of the seats are vacant
##Note : Compartment list is maintained as a linked list where data in each node refers to a compartment.
##compartment1=Compartment("SL",250,400)
##compartment2=Compartment("2AC",125,280)
##compartment3=Compartment("3AC",120,300)
##compartment4=Compartment("FC",160,300)
##compartment5=Compartment("1AC",100,210)


    







    
