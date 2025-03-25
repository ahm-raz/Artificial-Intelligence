# WHILE LOOP

count = 0
while count < 3:
    count = count + 1
print(count)


# SINGLE STATEMENT WHILE BLOCK 
# count = 0
# while count == 0 : print("Hello World!")


# FOR loop over list 
li = ['geeks','for','geeks']
for i in li:
    print(i,end=" ")
print()


# FOR loop over tuple
tu = ('geeks','for','geeks')
for i in tu:
    print(i,end=" ")
print()



# FOR loop over String
st = 'geeks for geeks'
for i in st:
    print(i,end=" ")
print()


# Iterating by index of Sequences
li = ['geeks','for','geeks']
j = 0
for i in range(len(li)):
    print(li[j],end=" ")
    j = j + 1
print()



# Continue Statement
# Print all letters except 'e' and 's':
st = 'geeksforgeeks'
j = 0
for i in st:
    if i == 'e' or i == 's':
        continue
    print(i,end=" ")
print()


# Break Statement
# Print letters until we reach 'e' or 's':
st = 'geeksforgeeks'
j = 0
for i in st:
    if i == 'e' or i == 's':
        break
    print(i,end=" ")
print()


# function
def my_func():
    print("Hello From Functions")

my_func()


# function
def my_country(country):
    print(f"I am from {country}")

my_country("Sweden")
my_country("Pakistan")
my_country("America")
my_country("Brazil")


# function
def my_func(li):
    for i in li:
        print(i)
    return

li = ['apple','banana','cherry']
my_func(li)


# function
def my_func(x):
    return 5 * x

print(my_func(4))
print(my_func(5))
print(my_func(7))
print(my_func(9))
print(my_func(3))


# function
def key_arg(child2,child1,child3):
    print(f"The Youngest Child is {child3}")
    print(f"The Middle Child is {child2}")
    print(f"The Eldest Child is {child1}")
    return

key_arg(child1='Emil',child2='Tobias',child3='Linus')


# function
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def my_func(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")

p1=Person('Ahmad Raza',21)
p1.my_func()