#!/usr/bin/env python
# coding: utf-8

# In[7]:


n=int(input("Enter number to check if it is prime or not: "))
if n > 1:
    for i in range(2,n):
        if(n%i==0):
            print(n,"is not a prime Number")
            break
    else:
        print(n,"is a prime number")
            
else:
    print(n,"is a prime number")


# In[ ]:





# In[ ]:




