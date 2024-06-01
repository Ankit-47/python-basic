#the order in which the code are executed is determined by control flow

#logical operators



# AND 
age=21
salary=20000
is_employ=age>=18 and salary>10000 #this will show the answer true
print(is_employ)  #and operator will show if both conditions are true

#OR

age=21
salary=20000
is_employ=age>=18 and salary>5000 #this will show the answer true
print(is_employ)  #or operator will show even if one condition is right

#NOT

age=21
salary=20000
is_employ=not age>=18 and salary>10000 #this will show the answer false
print(is_employ) #if not is added in true condition it will show fasle