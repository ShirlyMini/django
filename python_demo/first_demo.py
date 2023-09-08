# #print("hello")
#
# # single or double quotes
# hello_double = "hello python"
# hello_single = 'hello python'
# print(1)
# print(hello_single)
# print(hello_double)
#
# print("'i'm\n shirly'")
# print('"i am \nshirly"')
#
# # \n. \t,\s meta char, escape char

##### formatting
#
# a=10
# b=20
# c="thirty"
# print(a)
# print(a,b,c)
# print(f"{a}\n{b}\n{c}")
# print(f"the values are {a}\n{b}\n{c}")

# userinput

# print("Enter some number")
# a = input() # input will return string
#
# print(f"user inputs are {a} {type(a)}")

# typecast

# a=10  # convert int to str
# a1="10" # convert str to int
# a2=10.0
# b="string" # no
#
# print(f"{a}:{type(str(a))}")
# print(f"{a1}:{type(int(a1))}")
# #print(f"{b}:{type(int(b))}") # throws error
# print(f"float of {a} is {float(a)}")
# print(f"type of {a2} is {type(a2)}")
# print(f"int of {a2} : {int(a2)}")
# print(f"str of {a2} : {str(a2)}")
# # ascii
# print(ord("s")) # returns equivalent ascii value

# data types ---> numbers and string

# number int, float
# a=10 # int
# b=10.0 # float

# num1=100
# num2=200
# print(f"addition: {num1+num2}")
# print(f"subration: {num1-num2}")
# print(f"multiply: {num1*num2}")
# print(f"division: {num1/num2}") # decimal value
# print(f"floor div: {num1//num2}") # floor division returns round off value
# print(f"modulus: {num1%num2}") # returns remainder value

#Strings

str1 = "hello" # array of bytes
str2 = "PYTHON"
print(str1+str2) # concate
print(str1*4) # repeats the str
print(str1[0])# indexing starts from 0 to n
#reverse indexing starts from -1 to -n
print(str1[-1])
print(str1[-2])
print(str1[-3])
print(str1[-4])
print(str1[-5])
