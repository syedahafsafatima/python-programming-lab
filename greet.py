def greet(name):
    print("welcome",name)

greet("adiba")

name=input("enter the user")
greet(name)

def multiplication(n):
    for i in range(1,6):
        print(f"{n}*{i}={n*i}")
multiplication(4)
multiplication(87)

def even_odd(num):
    if(num%2)==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
even_odd(5)
even_odd(10)

def dispnum(num,start=1):
    for i in range(start,num+1):
        print(i,end=" ")
dispnum(4)
dispnum(8,2)

def std(*details):#* when no of details are not sure
    for i in details:
        print("data is",i)
std("hafsa",71,"aidsb")

def details(**data):
    print("details are")
    print("name is ",data["name"])
    print("age is ",data["age"])
    print("bday is",data["bday"])
details(name="mariya",age=15,bday="march")

def cr(cr1,cr2):
	print(f"1st cr is {cr1}")
	print(f"2nd cr is {cr2}")
cr(cr1="adiba",cr2="heena")

def name(first,last):
    print(first,last)
name(first="hafsa",last="fatima")
name(last="khusboo",first="adiba")
name("heena","safa")
name("safa","heena")

import string
def shift(word,value):
	letters=string.ascii_lowercase
	print(letters)
	new=''
	for i in range(len(word)):
		if word[i] in letters:
			index=letters.index(word[i])
			new=new+letters[(index+value)%26]
		else:
			new=new+word[i]
	return new
word=input("enter ur name")
print(shift(word,1))
