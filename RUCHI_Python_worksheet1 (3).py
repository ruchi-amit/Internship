#!/usr/bin/env python
# coding: utf-8

# Write a python program to find the factorial of a number

# In[1]:


import pandas as pd


# In[2]:


num = int(input("Enter a number: "))
factorial = 1
if num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        factorial=factorial*i
    print("The factorial of",num,"is",factorial)


# 2. Write a python program to find whether a number is prime or composite

# In[3]:


num = int(input("Enter any number "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is NOT a prime number")
            break
    else:
        print(num, "is a PRIME number")
elif num == 0 or 1:
    print(num, "is a neither prime NOR composite number")
else:
    print(num, "It is a COMPOSITE number")


# 3. Write a python program to check whether a given string is palindrome or not

# In[4]:


def isPalindrome(s):
    return s == s[::-1]
  
s = "malayalam"
ans = isPalindrome(s)
  
if ans:
    print("Yes")
else:
    print("No")


# 4. . Write a Python program to get the third side of right-angled triangle from two given sides.

# In[5]:


import math


# In[9]:


a = float(input("Give side a: "))
b = float(input("Give side b: "))
c = math.sqrt(a ** 2 + b ** 2)
print(f"Side C of triangle is {c}")


# 5. Write a python program to print the frequency of each of the characters present in a given string

# In[10]:


str1 = input ("Enter the string: ")
d = dict()
for c in str1:
    if c in d:
        d[c] = d[c] + 1
    else:
        d[c] = 1
print(d)


# In[ ]:




