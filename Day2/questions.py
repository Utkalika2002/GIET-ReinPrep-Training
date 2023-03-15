##question 1 - return list counting the letters & digits
def count_letter_digits(n):

    d = 0
    c=0
    for i in n:
        if(i.isdigit()):
            d +=1
        elif(i.isalpha()):
            c +=1
    l=[c,d]
    return l

print(count_letter_digits(input()))

##question 2 - find pairs of numbers having positive integers with no repetations & return count of pair of numbers adds up to n
def find_pairs_of_numbers(l,n):
    c = 0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if(l[i]+l[j] == n):
                c +=1
    return c
l1=[1,2,7,4,5,6,0,3]
n = int(input())
print(find_pairs_of_numbers(l1,n))

##question 3 - return a string made of 1st 2 & last 2 characters.if string < 2,return-1.
def strreturn(s):
    if(len(s)<2):
        return -1
    elif(len(s)==2):
        return s+s
    else:
        return s[0]+s[1]+s[-2]+s[-1]
s = input()
print(strreturn(s))
    
## q4 add ing at the end of a string ,add ly ,if string<3,leave it unchanged
n = input()
if(len(n)>3):
    if(n[-3:] == 'ing'):
        n = n+'ly'
        print(n)
        exit()
    if(n[-3:]!= 'ing'):
        n = n+'ing'
        print(n)
        exit()

##q5 check_double(number)which accepts a whole number & return true if the no should have exactly the same no of digits in different order.
n = int(input())
double = n*2
l1=list(str(n))
l2=list(str(double))
l1.sort()
l2.sort()
if(l1 == l2):
    print("yes")
else:
    print("No")

##q6 percentage of student who have secured more than average
def cal_avg(l): #average
    c = 0
    avg = 18
    for i in l:
        if(i>=avg):
            c +=1
    per = c/10*100
    return per
l= [12,18,25,24,2,5,18,20,20,21]
print(cal_avg(l))
def frequency(l):  #frequency
    l1 =[]
    for i in range(0,25):
        l1.append(l.count(i))
    return l1
print(frequency(l))
def sort_mark(l):  #sorting
    l.sort()
    return l
print(sort_mark(l))

##q7 translate that accepts bilingual dictionary & a list of English words & returns a list of equivalent Swedish words.
def translate(dict1,list1):
    list2 =[]
    for i in list1:
        list2.append(dict1[i])
    return list2
dict1 ={"merry":"god", "christmas":"Jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
list1=("merry","christmas")
print(translate(dict1,list1))
        
##q8 no of distinct subarrays & sum of subarray is an odd integer, two subarray are diff if they start or end at diff index input.
n1 = int(input())
n2 = int(input())
l1 =[]
l2 =[]
for i in range(n1,n2+1):
    l1.append(i)
    
for i in range(len(l1)+1):
    for j in range(i,len(l1)):
        l2.append(l1[i:j+1])
print(l2)
