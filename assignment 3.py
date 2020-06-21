#!/usr/bin/env python
# coding: utf-8

# In[43]:


x=input("enter number1 ")
y=input("enter number2 ")
if x==y:
    print("two numbers are equal")
else:
    print("two numbers are not equal")
    


# In[47]:


x=input("enter value of x  ")
y=input("enter value of y ")
z=input("enter value of z  ")
if x==y==z:
    print("all are equal")
elif x==y and x!=z:
    print("x and y are equal")
elif x==z and x!=y:
    print("x and z are equal")
elif y==z:
    print("y and z are equal")
else:
    print("all are not equal")


# In[48]:


x=int(input("enter number1 "))
y=int(input("enter number2 "))
z=x+y
if z>5:
    print("sum is greater than than 5")
elif z==5:
    print("sum is equal to 5")
else:
    print("sum is less than 5")


# In[49]:


x=int(input("enter the marks "))
if x>35:
    print("marks are greater than passing marks")
elif x<35:
    print("marks are less than passing marks")
else:
    print("marks are equal to passing marks")


# 

# In[42]:


x=int(input("enter the number1"))
y=int(input("enter the number2"))
z=int(input("enter the number3"))
if x==y==z:
    print("all are equal")
elif x==y and x>z:
    print("x and y are greater")
elif x==z and x>y:
    print("x and z are greater")
elif y==z and y>x:
    print("y and z are greater ")
elif x>y and x>z:
    print("x is greater")
elif y>x and y>z:
    print("y is greater")
else:
   print("z is greater")

