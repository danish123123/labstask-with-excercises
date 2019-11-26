
# coding: utf-8

# In[2]:

# Q1
from datetime import date
first_date = date(2019, 10, 28)
second_date = date(2019, 11, 28)
diff = second_date - first_date
print (diff.days)


# In[16]:

# Q2(A)
from math import pi
from math import sin
a = 16
b = 75
angle = (pi * b) / 180
print (angle)
height = a * sin(angle)
print (height)
# (B)
from math import pi
from math import sin
a = 20
b = 0
angle = (pi * b) / 180
print (angle)
height = a * sin(angle)
print (height)
# (C)
from math import pi
from math import sin
a = 24
b = 45
angle = (pi * b) / 180
print (angle)
height = a * sin(angle)
print (height)
# D
from math import pi
from math import sin
a = 24
b = 8055
angle = (pi * b) / 180
print (angle)
height = a * sin(angle)
print (height)


# In[4]:

# Q3(A)
lst = [2, 4 ,6 , 8, 10]
Lengthoflist = len(lst)
middle_index = int(Lengthoflist / 2 )
print (middle_index)
# (B)
lst = [2, 4, 6, 8, 10]
middle_element= len(lst)
print (middle_element)
# (C)
lst = [2, 4, 6, 8, 10]
lst.sort(reverse = True)
print (lst)
# (D)
lst = [2, 4 ,6 ,8 ,10]
lst.extend([2])
print (lst)


# In[17]:

# Q4(A)
monthsL = ["Jan", "Feb", "Mar", "May"]
monthsT = ("Jan", "Feb", "Mar", "May")
monthsL.insert(3, "Apr")
print (monthsL) 
monthsT.insert(3, "Apr")
print (monthsT)



# In[ ]:

# Q4(B)
monthsL = ["Jan", "Feb", "Mar", "May"]
monthsT = ("Jan", "Feb", "Mar", "May")
monthsL.append("Jun")
print (monthsL)
monthsT.append("Jun")
print (monthsT)


# In[21]:

# Q4(C)
monthsL = ["Jan", "Feb", "Mar", "May"]
monthsT = ("Jan", "Feb", "Mar", "May")
monthsL.pop()
print (monthsL)
monthsT.pop()
print (monthsT)


# In[22]:

# Q4(D)
monthsL = ["Jan", "Feb", "Mar", "May"]
monthsT = ("Jan", "Feb", "Mar", "May")
monthsL.remove ("Feb")
print (monthsL)
monthsT.remove ("Feb")
print (monthsT)


# In[19]:

# Q4(E)
monthsL = ["Jan", "Feb", "Mar", "May"]
monthsT = ("Jan", "Feb", "Mar", "May")
monthsL.reverse()
print (monthsL)
monthsT.reverse()
print (monthsT)


# In[20]:

# Q4(F)
monthsL = ["Jan", "Feb", "Mar", "May"]
monthsT = ("Jan", "Feb", "Mar", "May")
monthsL.sort()
print (monthsL)
monthsT.sort()
print (monthsT)


# In[ ]:

# Q5(A)
print ("The number of the characters in the word anachronisitically is 1 more than the number of the charachters in the word counterintutive")
The number of the characters in the word anachronisitically is 1 more than the number of the charachters in the word counterintutive
# (B)
print ("The word misinterpretation appears earlier in the dicitionary than the word mispresentation")
The word misinterpretation appears earlier in the dicitionary than the word mispresentation
# (C)
print ("The letter e does not appear in the word floccinaucinihilipilification")
The letter e does not appear in the word floccinaucinihilipilification
# (D)
print ("The number of charachters in the word "couterevolution" is equal to the sum of the number of the characters in words "counter" and "resolution")



# In[18]:

# Q6(A)
a= 6
b= 7
# (B)
c= ((a + b) / 2)
print (c)
# (C)
inventory = ['paper', 'staples', 'pencils']
# (D)
fname = 'John'
mname = 'Fitzgerald'
lname = 'Kennedy'
# (E)
fullname = fname + " " + mname + " " + lname
print (fullname)

