#basically we have two loops in python and they are FOR AND WHILE loops  

#while loop
#syntax
 #while condition:
#do

count=5
while count>0:
    print ("hello")
    count=count-1

    #this example will print hello*times



#for  loop 
fruits=["apple","banana","mango"]
for items in fruits:    
    print (items)

    #range
for number in range(0,6):
        print(number)
        #this will print 0-5 as result which is same as indexing list

#break and continue

count=5
while count>0:
    print ("hello")
    if count==3:
         break  #we will g0t hello*3 as as it breaks when the if condition as met
    count=count-1 