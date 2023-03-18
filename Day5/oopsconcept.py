## q1 cal premium_amount of vehicles
class Vehicle:
     def __init__(self,vehicle_id,vehicle_type,cost):
         self.__vehicle_id = vehicle_id
         self.__vehicle_type = vehicle_type
         self.__cost = cost
         self.__premium_amount = None
         
     def cal(self,premium_amount,amount):
        amount = amount+ (premium_amount/100)*amount 
        print(amount)
         
         
    
         
     def vechile_details(self):
        if(self.__vehicle_type == 2):
            self.__premium_amount = 2
        elif(self.__vehicle_type == 4):
            self.__premium_amount = 6
        self.cal(self.__premium_amount,self.__cost)

A = Vehicle(101,4,100000)
A.vechile_details()
##including getter & setter methods

class Vehicle:
    def __init__(self,vehicle_id,vehicle_type,cost):
        self.__vehicle_id = vehicle_id
        self.__vehicle_type = vehicle_type
        self.__cost = cost
        self.__premium_amount = None
    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id = vehicle_id
    def get_vehicle_id(self):
        return self.__vehicle_id
    def set_vehicle_type(self,vehicle_type):
        self.__vehicle_type = vehicle_type
    def get_vehicle_type(self):
        return self.__vehicle_type
    def set_cost(self,cost):
        self.__cost = cost
    def get_cost(self):
        return self.__cost
    def detail(self):
        
        if(self.__vehicle_type == 2):
            self.__premium_amount = 2
        elif(self.__vehicle_type == 4):
            self.__premium_amount = 6
        self.cal(self.__premium_amount)
    def cal(self,premium_amount):
        self.__cost=self.__cost+(premium_amount/100)*self.__cost
        self.set_cost(self.__cost)
A = Vehicle(101,2,100000)
A.set_vehicle_type(4)
A.detail()
print(A.get_cost())

## q2
class Student:
    def __init__(self,id,age,mark):
        self.__id = id
        self.__age = age
        self.__mark = mark
        
        
        
    def validate_age(self):
        if(self.__age >= 20):
            return True
        else:
            return False
    
    def validate_mark(self):
        if(self.__mark>=0 and self.__mark<=100):
            return True
        else:
            return False
    def checkQualification(self):
        if(self.validate_mark() and self.validate_age()):
            if(self.__mark>=65):
                return self.course_fees()
        else:
            print("not qualified")
    def course_fees(self):
        d ={1001:23000,1002:45000,1003:67000}
        discount = 0
        if(self.__mark>=85):
            discount = 0.25
        return d[self.__id]- discount*d[self.__id]
A = Student(1001,20,89)
print(A.checkQualification())
