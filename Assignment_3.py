#!/usr/bin/env python
# coding: utf-8

# 1.1Q.Write a Python Program to implement your own myreduce() function which works exactly
# like Python's built-in function reduce()

# In[3]:


def factorial(n):
    fact = 1
    for currentValue in range(1,n):
        fact = fact*currentValue
    return fact
fact10 = factorial(10) 


# In[4]:


fact10 


# In[5]:


from functools import reduce

def factorial(n):
    def mult(a,b): return a*b
    return reduce(mult,range(1,n),1)


# In[6]:


fact_10 = factorial(10) 


# In[7]:


fact_10


# In[ ]:


# one more example


# In[8]:


def factorial(n):
    def mult(a,b): return a*b
    return reduce(mult,range(1,n),1)


# In[9]:


from functools import reduce
from operator import add
def sum_1(n):
    return reduce(add,range(1,n), 0)


# In[10]:


sum_num=sum_1(10)


# In[11]:


sum_num


# In[12]:


def sumall(n):
    added=0
    for i in range(1,n):
        added=added+i;
    return added
added_10=sumall(10)        


# In[13]:


added_10


# Q1.2.write a python program to implement your own filter() function which works exactly like python's built-in function filter()

# In[23]:


names = ['Mamatha', 'Manoj', 'Sanoj', 'Pradeep', 'Chakri', 'Tharunika', 'Thanvika']
M_names = []
for name in names:
    if name.startswith('M'):
        M_names.append(name)

print(M_names)



# In[35]:


names = ['Mamatha', 'Manoj', 'Sanoj', 'Pradeep', 'Chakri', 'Tharunika', 'Thanvika']
M_names =list(filter(lambda s: s.startswith('M'), names))
print(M_names)


# Q2.Implement List comprehensions to produce the following lists.
# Write List comprehensions to produce the following Lists
# ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
# [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
# [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

# In[37]:


all_letters = [ letter for letter in 'ACADGILD' ]
print(all_letters)


# In[40]:


ip_list = ['x','y','z']
result = [ item*num for item in ip_list for num in range(1,5)  ]
print(str(result))


# In[41]:


ip_list = ['x','y','z']
result = [ item*num for num in range(1,5) for item in ip_list  ]
print(str(result))


# In[42]:


ip_list = [2,3,4]
result = [ [item+num] for item in ip_list for num in range(0,3)]
print(str(result))


# In[43]:


input_list = [2,3,4,5]
result = [ [item+num for item in ip_list] for num in range(0,4)  ]
print(str(result))


# In[44]:


ip_list=[1,2,3]
result = [ (b,a) for a in input_list for b in ip_list]
print(str(result))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




