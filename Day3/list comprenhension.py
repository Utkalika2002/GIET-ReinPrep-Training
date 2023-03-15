##list comprehension

#for loop version
result=[]
l1=[1,2,3,4,5,8,9,0,3,3,2]
for i in (l1):
    result.append(i)
print(result)

#list comprehension version
print([i for i in (l1)])
#for loop version-->odd elements
result=[]
for i in (l1):
    if i%2!=0:result.append(i)
print(result)
print([i for i in (l1)if i%2!=0])

##list comprehension
re=[]
re.append([j**2 if j%2 != 0  else j**3 for i in mat for j in i  ])
print(re)

##loop 2D
for i in mat:
    re1=[]
    for j in i:
        if(j%2!=0):
            re1.append(j**2)
        else:
            re1.append(j**3)
    res.append(re1)
print(res)

##loop 2D list comprenhension

print([[j**2 if j%2!=0 else j**3 for j in i]for i in mat])

##q1 each no in list_b,get the no & its position(index) as are turn list of tuples

my_list=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2] #res=[(6,2),(4,8)]
res=[]
for i in list_b:
    res.append((i,my_list.index(i)))
print(res)

print([(i,my_list.index(i))for i in list_b])

##show the result part in dict
my_list=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2] #res=[(6,2),(4,8)]

print({i:my_list.index(i)for i in list_b})

##q2
sentences = ["a new world record was set",
            "in the holy city of Ayodhya",
            "on the eve of diwali on Tuesday",
            "with over three lakh diya or earthen lamps",
            "lit up simulataneously on the banks of the sarayu river"]
stopwords = ['for','a','of','the','and','to','in','on','with','was']
res=[]
for sentence in sentences:
    row=[]
    for word in sentence.split():
        if word not in stopwords:
            row.append(word)
    res.append(row)
print(res)
##list comprehension
print([[word for word in sentence.split()if word not in stopwords]for sentence in sentences])

##q3 assume 8 always comes after 5 in a list--num1:add the nos which don't lie between 5&8--num2:no formed by concatenating all nos from 5 to 8.o/p-num1+num2

array=list(map(int,input().split(","))) #3,2,6,5,1,4,8,9
num1 = sum(array[:array.index(5)])+sum(array[array.index(8)+1:])
l = array[array.index(5):array.index(8)+1]
num2 = ""
for i in l:
    num2 += str(i)
print(num1)
print(num2)
print(int(num2)+num1)

##q4 string rotation if sum of squares of digits is even so rotate right by 1 or if it's odd,then rotate left by 2

array = "rhdt:246,ghftd:1246"
s = array.split(",")
sttr = []
num = []
for i in s:
    s1,n = i.split(":")
    sttr.append(s1)
    num.append(n)
def rotate(ss,nu):
    s1 = 0
    for i in nu:
        s1 += int(i)**24
    if s1%2 == 0:
        return ss[-1]+ss[:-1]
    else:
        return ss[2:]+ss[:2]
        
for i in range(len(sttr)):
    print(rotate(sttr[i],num[i]))

##q5 find sum of largest prime factors of each of 9 consecutive numbers starting from n




