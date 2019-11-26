#!/usr/bin/env python
# coding: utf-8

# # SYED MUHAMMAD DANISH,  LAB 3, 19b-001-SE, SEC A

# In[11]:


#Q1 Determine the magnitude of the linear velcoity of a point.

#Data 

r1=0.5
r2=1
r3=3
Angularspeed=10

v1= r1*Angularspeed
print ("Linear velocity when the radius is 0.5 meter and Angularspeed is 10:" + str(v1) +  " m/s")
v2= r2*Angularspeed
print ("Linear velocity when the radius is 1 meter and Angularspeed is 10:" + str(v2) +  " m/s")
v3= r3*Angularspeed
print ("Linear velocity when the radius is 3 meter and Angularspeed is 10:" + str(v3) + " m/s")


# In[19]:


#Q2 Determine the magnitude of the linear velocity of a blender

#Data

r1=5
r2=10
w=5000/60
v1=r1*w
print ("The magnitude of the linear velocity when radius is 5 cm : " + str(v1) + " m/s" )
v2=r2*w
print ("The magnitude of the linear velocity when radius is 10 cm : " + str(v2) + " m/s" )


# In[22]:


#Q3 What is the magnitude of the angular velocity 

#Data 

r=0.3
constantspeed=10
w=constantspeed/r
print ("The angular velocity is : " +str(w) + " sec-1" )


# In[24]:


#Q4 Angular velocity of a car

#Data

v=10
r=0.25
angularspeed=v/r
print ("Angularspeed of the car is : " +str(angularspeed) + " sec-1 ")


# In[32]:


#Q5 The angular speed of a wheel?

#Data

r= float (0.2)
angularspeed= float (12.56)
t= 10
d=r* angularspeed* t
print ("The distance covered by the car in meters is : " + str(d) + " meters ")


# In[34]:


#Q6 How far does the car travels?

#Data 

u=50
a=10
t=2
v=u+a*t
print ("The distance of the car in miles per hour is : " + str(v) + " miles/hr ")


# In[41]:


#Q7 Find velocity?

#Data

from math import sqrt
u=0
h=100
a=32
v= sqrt(2*a*h**2)
print ("The velcoity os the stone in meter per sec is : " + str(v) + " m/s ") 


# In[ ]:




