##Queue
class Queue:
    def __init__(self,max_size):
        self.__max_size = max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0
        
    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False
        
    def is_empty(self):
        if(self.__front > self.__rear):
            return True
        return False
        
    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full")
        else:
            self.__rear +=1
            self.__elements[self.__rear]=data
    
    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty")
        else:
            data = self.__elements[self.__front]
            self.__front+=1 
            return data
            
    def display(self):
        for index in range(self.__front,self.__rear +1):
            print(self.__elements[index])
        
                
    def get_max_size(self):
        return self.__max_size
Queue1 = Queue(10)
print('Is it empty',Queue1.is_full())
print('Is it empty',Queue1.is_empty())
Queue1.enqueue(500)
Queue1.enqueue(600)
Queue1.enqueue(700)
Queue1.enqueue(800)
Queue1.display()
print("element deleted",Queue1.dequeue())
Queue1.display()
print("size of the queue",Queue1.get_max_size())

##q1 python function to return a new queue which contains the evenly divisible numbers
class Queue:
    def __init__(self,max_size):
        self.__max_size = max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0
        
    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False
        
    def is_empty(self):
        if(self.__front > self.__rear):
            return True
        return False
        
    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full")
        else:
            self.__rear +=1
            self.__elements[self.__rear]=data
    
    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty")
        else:
            data = self.__elements[self.__front]
            self.__front+=1 
            return data
            
    def display(self):
        for index in range(self.__front,self.__rear +1):
            for i in range(1,10+1):
                if(self.__elements[index]% i==0):
                    s = True
                else:
                    s = False
                    break
            if(s):
                print(self.__elements[index])
        
    def get_max_size(self):
        return self.__max_size
Queue1 = Queue(10)
print('Is it empty',Queue1.is_full())
print('Is it empty',Queue1.is_empty())
Queue1.enqueue(13983)
Queue1.enqueue(10080)
Queue1.enqueue(7113)
Queue1.enqueue(2520)
Queue1.enqueue(2500)
Queue1.display()

##q2 complete the sentence by concatinating list1 with reverse of list2
list1 = ['A','app','a','d','ke','th','doc','awa']
list2 = ['y','tor','e','eps','ay',None,'le','n']
list2rev = list2[::-1]

for i in range(len(list1)):
    if(list2rev[i] == None):
        print(list1[i] + '',end=" ")
    else:
        
        print(list1[i]+list2rev[i],end = " ")
