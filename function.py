#the function in which users can input argument and gets output it is said to be -->  dynammic function

def add_numbers(n1,n2):
    result=n1+n2
    print ("the sum is",result)
number1=5
number2=6
add_numbers(number1,number2) #output--> the sum is 11

#this is an simple example of adding two numbers


#return statement

def add(a,b):
    sum=a+b
    return sum
x=1
y=4
result=add(x,y)
print(result)