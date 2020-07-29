#!/usr/bin/env python
# coding: utf-8

# In[15]:


def pushZerosToEnd(arr, n): 
	count = 0 
	for i in range(n): 
		if arr[i] != 0: 
			
			
			arr[count] = arr[i] 
			count+=1
	while count < n: 
		arr[count] = 0
		count += 1
array1 = [0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4] 
arr=sorted(array1)
n = len(arr) 
pushZerosToEnd(arr, n) 
print("Array after pushing all zeros to end of array:") 
print(arr)


# In[9]:


l1 = [10,20,40,60,70,80] 
l2 = [5,15,25,35,45,60] 

print ("The original list 1 is : " + str(l1)) 
print ("The original list 2 is : " + str(l2)) 

size_1 = len(l1) 
size_2 = len(l2) 

res = [] 
i, j = 0, 0

while i < size_1 and j < size_2: 
	if l1[i] < l2[j]: 
	    res.append(l1[i]) 
	    i += 1

	else: 
	    res.append(l2[j]) 
	    j += 1

res = res + l1[i:] + l2[j:] 

print ("The combined sorted list is : " + str(res)) 


# In[ ]:





# In[ ]:




