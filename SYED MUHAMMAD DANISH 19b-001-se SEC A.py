
# coding: utf-8

# # LAB 3 Syed Muhammad Danish 19B-001-SE

# In[2]:


#PROGRAM 1

# Math operators in Python
# Taking two values

a=10
b=22

# Using sum operator
print ("Sum is : ", a+b )

# Using subtract operator
print ("Difference is :", a-b)

# Using multiplication operator
print ("Product is :", a*b)

# Using division operator
print ("Division is:", a/b)

# Using integer divison operator
print ("Integer Division is:", a/b)

# Using Power operator
print ("Raised to the power is:", a**b)

#Using modulous operator
print ("Remainder is:", a%b)


# In[4]:


#PROGRAM 2

x=5
x+=3
print (x)

x=5
x-=3
print (x)

x=5
x*=3
print (x)

x=5
x/=3
print (x)

x=5
x%=3
print (x)

x=5
x//=3
print (x)

x=5
x**=3
print (x)

x=5
x&=3
print (x)

x=5
x|=3
print (x)

x=5
x^=3
print (x)

x=5
x>>=3
print (x)

x=5
x<<=3
print (x)


# In[33]:


#Program 3

x=20
y=15

print ("x is equal to y:", x==y)
print ("x is not equal to y:", x!=y)
print ("x is greater than y:", x>y)
print ("x is less than y:", x<y)
print ("x is the greater than or equal to y:", x>=y)
print ("x is less than or equal to y:", x<=y)


# In[9]:


#Program 4

x=15
print (x>13 and x<20)

x=25
print (x>23 or x<24)

x=35
print (not(x>33 and x<40))


# In[12]:


#Program 5

x=["ahmed", "bashir"]
y=["ahmed", "bashir"]
z=x

print (x is z)
print (x is y)
print (x==y)


# In[35]:


#Program 6

x=["ahmed", "bashir"]
y=["ahmed", "bashir"]
z=x

print (x is not z)
print (x is not y)
print (x<y)



# In[37]:


#ERROR
x=["ahmed", "bashir"]
y=["ahmed", "bashir"]
z=x

print (x is not z)
print (x is not y)
print (x<>y)


# In[30]:


#Program 7

x=["wasim", "Lubaid", "shahroz", "usman", "faisal", "farhan"]
print ("faisal" in x)


# In[17]:


#Program 8

x=["wasim", "lubaid", "shahroz", "usman", "faisal", "farhan"]
print ("parkash" not in x)


# In[34]:


#Program 9

import math
#User inputs
velocity= float(input('Give me a velocity to fire at (in m/s):'))
angle= float(input('Give me an angle to fire at:'))
distance= float(input('Give me how far away you are from the structure;'))
height= float(input('Give me the height of the structure (in meters):'))
slingshot= 5 #Height os slingshot in meters
gravity= 9.8 #Earth gravity

#Converting angles to radians
angleRad=math.radians(angle)
#computing our x and y coordinate
x= math.cos(angleRad)
y= math.sin(angleRad)

#Caclulations

time= distance/(velocity*x)
vx=x
vy=y = (-9.8*time)
finalVelocity=math.sqrt((vx**2)+(vy**2))
print ("Time is", time)
print ("Velocity along x axis is", vx)
print ("Velcity along y axis is", vy)
print ("Final Velocity is ", finalVelocity)

