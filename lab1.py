print("Ahmad Raza")
# --> Ahmad Raza

x=1
# if x > 0
# SyntaxError: expected ':'
if x > 0:
  print("These are two comments")
# --> These are two comments

print("Statement 1")
# --> Statement 1

print("Statement 1");print("Statement 2")
# --> Statement 1
# --> Statement 2

x = 1
if x > 0:
  print("Statement 1")
  print("Statement 1")
# --> Statement 1
# --> Statement 1

a = 123
print(type(a))
# --> <class 'int'>

a = 0.342
print(type(a))
# --> <class 'float'>

x = complex(1,2)
print(type(x))
#--> <class 'complex'>

print(x)
# --> (1+2j)

b = True
print(type(b))
# --> <class 'bool'>

if b:
 print("true")
# --> true

print("This is a (\\) mark")
# --> This is a (\) mark

print("This is Tab /t key")     
# --> This is Tab /t key

print("This is Tab \t key")       
# --> This is Tab 	 key

print("these are \'single quotes\'")      
# --> these are 'single quotes'

print("these are \"double quotes\"")
# --> these are "double quotes"

print("these are \"double quotes\"")      
# --> these are "double quotes"

print("this is a new line \nNew line")
# --> this is a new line
# --> New line

string = "abcdef"
print(string[0])
# --> a

print(string[-1])
# -->f

list1 = [12,7,"abc"]      
print(list1)
# --> [12, 7, 'abc']

print(list1[0],list1[-1])      
# --> 12 abc

list2 = [1,2,3,4,5,6]
print(list2[0:2])
# --> [1, 2]

print(list2[0:-2])
# --> [1, 2, 3, 4]

print(list2[:3])
# --> [1, 2, 3]

print(list2[:])
# --> [1, 2, 3, 4, 5, 6]