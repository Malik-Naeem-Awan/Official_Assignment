#!/usr/bin/env python
# coding: utf-8

# # Assignment 01 

# In[1]:


#Write Python Program to Check Whether a Number is Positive or Negative 
#1. Take the value of the integer and store in a variable. 
#2. Use an if statement to determine whether the number is positive or negative. 
#3. Exit. 


# In[15]:


number=int(input("Enter a number to check if it is positive or negative:"))
if number>0:
    print("Number",number," Is Positive!")
elif number==0:
    print("Number",number,"Is neither Positive nor Negative it is Zero")
else:
    print("Number",number,"is Negative")


# In[21]:


#Write Python Program to Take in the Marks of 5 Subjects and Display the Grade 
#1. Take in the marks of 5 subjects from the user and store it in different variables. 
#2. Find the average of the marks. 
#3. Use an else condition to decide the grade based on the average of the marks. 
#4. Exit. 


# In[24]:


sub1=int(input("Enter marks of 1st subject: "))
sub2=int(input("Enter marks of 2nd subject: "))
sub3=int(input("Enter marks of 3rd subject: "))
sub4=int(input("Enter marks of 4th subject: "))
sub5=int(input("Enter marks of 5th subject: "))

average=(sub1+sub2+sub3+sub4+sub5)/5

if average >=90 and average <=100:
    print("Congratulations! you have Got A1 Grade!")
elif average >=80 and average <=89:
    print("Congratulations! you have Got A Grade!")
elif average >=70 and average <=79:
    print("Congratulations! you have Got B Grade!")
elif average >=60 and average <=69:
    print("Congratulations! you have Got C Grade!")
elif average >=50 and average <=59:
    print("Congratulations! you have Got D Grade!")
elif average >=40 and average <=49:
    print("Congratulations! you have Got E Grade!")
elif average <40:
    print("Alas! You have failed! F Grade Unforunately... Better luck next time")
elif average >100 or average <0:
    print("Exception in the marks of subject. Invalid Input Enter Valid marks!")


# In[25]:


#Write Python Program to Read Two Numbers and Print Their Quotient and Remainder 
#1. Take in the first and second number and store it in separate variables. 
#2. Then obtain the quotient using division and the remainder using modulus operator. 
#3. Exit


# In[27]:


a=int(input("Enter 1st Number:"))
b=int(input("Enter 2nd Number: "))

qoutient=a//b
remainder=a%b

print("Qoutient: ",qoutient)
print("remainder: ",remainder)


# In[28]:


#Write Python Program to Print all Integers that Aren’t Divisible by Either 2 or 3 and Lie between 1 and 50. 
#1. Use a for-loop ranging from 0 to 51. 
#2. Then use an if statement to check if the number isn’t divisible by both 2 and 3. 
#3. Print the numbers satisfying the condition. 
#4. Exit


# In[30]:


count=0
c=1
for a in range(1,51):
    if a%2==0 or a%3==0:
        continue
    else:
        count=count+1
        print(c,":",a,"  ")
        c=c+1


# In[31]:


#Write Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable 
#Problem Solution 
#1. Take the values of both the elements from the user. 
#2. Store the values in separate variables. 
#3. Add both the variables and store it in the first variable. 
#4. Subtract the second variable from the first and store it in the second variable. 
#5. Then, subtract the first variable from the second variable and store it in the first variable. 
#6. Print the swapped values. 
#7. Exit


# In[35]:


n1=int(input("Enter 1st Number: "))
n2=int(input("Enter 2nd Number: "))

n1=n1+n2
n2=n1-n2
n1=n1-n2
print("Swapped Values: ", n1, "    ", n2)


# In[ ]:


#Write Python Program to Find the Area of a Triangle Given All Three Sides 
#Problem Solution 
#1. Take in all the three sides of the triangle and store it in three separate variables. 
#2. Then using the Heron’s formula, compute the area of the triangle. 
#3. Print the area of the triangle. 


# In[46]:


a=float(input("Enter value of first side: "))
b=float(input("Enter value of second side: "))
c=float(input("Enter value of third side: "))

s1=(a+b+c)/2

area1=(s1*(s1-a)*(s1-b)*(s1-c)) ** 0.5

print("Area of Triangle with side 1:", a, "side 2:", b, "side 3: " ,c ,"is: %0.2f " %area1 )


# In[47]:


#Write Python Program to Print Largest Even and Largest Odd Number in a List 
#1. Take in the number of elements to be in the list from the user. 
#2. Take in the elements from the user using a for loop and append to a list. 
#3. Using a for loop, get the elements one by one from the list and check if it odd or even and append them
#to different lists. 
#4. Sort both the lists individually and get the length of each list.
#5. Print the last elements of the sorted lists. 
#6. Exit.


# In[56]:


n=int(input("Enter Number of elements to be entered into list: "))
list1=[]
Elist=[]
Olist=[]
for a in range(1,n+1):
    enum=input("Enter the Number : ")
    list1.append(enum)
for a in range(1,n):
    cn=int(list1[a])
    if cn%2==0:
        tn=list1[a]
        Elist.append(tn)
    else:
        tn=list1[a]
        Olist.append(tn)
Elist.sort()
Olist.sort()

print("The Largest Even Number is : ",Elist.pop())
print("The Largest ODD Number is : ",Olist.pop())
        


# In[ ]:


#Write Python Program to Find the Second Largest Number in a List 
#1. Take in the number of elements and store it in a variable. 
#2. Take in the elements of the list one by one. 
#3. Sort the list in ascending order. \
#4. Print the second last element of the list. 
#5. Exit.


# In[64]:


list1=[]
n=int(input("Enter Number of elements to be entered into list: "))
for a in range(1,n+1):
    tn=input("Enter the Number: ")
    list1.append(tn)
list1.sort()
print("The Second Largest Number of the list is : ",list1[n-2])


# In[ ]:


#Write Python Program to Find the Union of two Lists 
#1. Define a function which accepts two lists and returns the union of them. 
#2. Declare two empty lists and initialise to an empty list. 
#3. Consider a for loop to accept values for two lists.
#4. Take the number of elements in the list and store it in a variable.
#5. Accept the values into the list using another for loop and insert into the list.
#6. Repeat 4 and 5 for the second list also. 
#7. Find the union of the two lists. 
#8. Print the union. 
#9. Exit 


# In[67]:


def union_function(list1,list2):
    final_List=list1+list2
    return final_List
list1=[]
list2=[]
n=int(input("Enter Number of elements to be entered into list: "))
for a in range(1,n+1):
    tn=input("Enter the Number: ")
    list1.append(tn)
n=int(input("Enter Number of elements to be entered into list: "))
for a in range(1,n+1):
    tn=input("Enter the Number: ")
    list2.append(tn)

print("Union of Two Lists: ",union_function(list1,list2))

