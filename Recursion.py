#!/usr/bin/env python
# coding: utf-8

# ## No 1

# In[7]:


def sum_of_digits(num):
    if num <= 0 or not isinstance(num,int):
        return 0
    elif num < 10:
        return num
    else : 
        return num % 10 + sum_of_digits(num // 10)
print(sum_of_digits(20))


# ## No 2

# In[8]:


def power(x,n):
    if n == 0 :
        return 1
    elif n > 0 :
        return x * power(x,n -1)
    else :
        return 1 / power(x,abs(n))
print(power(-1,2))


# ## No 3

# In[9]:


def gcd(a,b):
    a = abs(a)
    b = abs(b)
    if b == 0:
        return a
    else:
        return gcd(b,a % b)
print(gcd(8,12))


# ## No 4

# In[10]:


def decimal_to_binary(n):
    if n <= 1:
        return str(n)
    else:
        quotinent = n // 2
        remainder = n % 2
        return decimal_to_binary(quotinent) + str (remainder)
    
n = 13
binary_num = decimal_to_binary(n)
print(f"The binary representation of {n} is {binary_num}")

