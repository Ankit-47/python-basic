lst=[1,"ankit",2,3,"katwal"]  #list initialized
a=len(lst)  #print the length of the list
print({lst[-1]}) #if u dont know the no or length of strings simply use [-index number] to find the last element

lst2=lst[1:3] #this will show the items listed between 1-3 excluding 3 : it means last index no i.e 3 will be excluded

#del lst[1]  --> delete all the item of the list
#lst2=lst[:3]-->  HERE YOU WILL GOT ITEM BEFORE INDEX 3  UPTO FIRST
#lst2=lst[1:] --> HERE YOU WILL GOT ITEM AFTER INDEX 1 UPTO LAST

#list methods

lst.append("nosk"); #this will add the "nosk" to the last pf the above list
print(lst)

lst2=[1,2,3]
lst.extend(lst2) #this will add the 
print(lst)


lst1= [1,"ankit",2,3,"katwal"]
lst1.insert(1,4) #(1,4)  1 is index and 4 is the value to be inserted  so here in place of ankit 4 will be replaced and ankit will goes to index no 2
print(lst1)

lst1= [1,"ankit",2,3,"katwal"]
lst2=lst1.copy(); #copies the list items of lst1 to lst2 as it is 
print(lst2)


#USING FOR LOOP IN LIST

st1= [1,"ankit",2,3,"katwal"]
for val in lst1: #this will shwo up the list one by one  as shown below:
#1
#ankit
#2
#3
#katwal
  print (val)

  


