#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input()) #enter number                #problem 1
m=n #copying input
def l_t(n):
    lst=[]
    while(n!=0):
        k=int(n%10)
        lst.append(k)
        n=int(n/10) 
    return lst
def s_m(lst):
    p=sum(lst)
    if(int(p/10)!=0):
        return(1)
    else:
        return(0)
i=1
while(int(n/10)!=0):
    n1=l_t(n)
    m1=sum(n1)
    if(int(m1/10)!=0):
         i+=1
    n=sum(n1)
if(int(m/10)==0):
    print('0')
else:
    print(i)


# In[7]:


#problem2
n=int(input())  #wall length
m=int(input())  #number of bricks
s=list(map(int,input().strip().split()))[:m] #to input strength of each brick
from itertools import combinations
r=[];ss=sum(s);test=0
for i in range(m-1):
    comb=combinations(s,i)
    for item in comb:
        s1=sum(item)
        k=ss-s1
        r.append(min(s1,k))
if(m in range(1,10**5+1)):
    for q in range(m):
        if(s[q] in range(1,10**9+1)):
            test=1
if((test==1)&(n==2)):
    print(max(r))
elif(n==1):
    print(ss)


# In[50]:


#problem 3
n=int(input()) #Number given by dhruv
def p_c(m):
    for i in range(2,m):
        if(m%i==0):
            return(0)
k=1
lst=[]
for i in range(2,n+1):
    if(p_c(i)!=0):
        lst.append(k)
        k+=1
if((n>=2)&(n<=10**5)):
    print(sum(lst))        #Print total sum of all such DISTINCT Ci.


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




