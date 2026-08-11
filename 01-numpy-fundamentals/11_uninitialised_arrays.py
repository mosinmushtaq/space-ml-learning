import numpy as np 
# sometimes we want to make an array but just makae it and do nothing and use it later, 
#for that there is a function named empty 

array1=np.empty(4) # creates junk array of 4 elemnts in one row 
print(array1)
    

array2=np.empty((5,4))
print(array2) # here the value as no. of rows and coloumns has to be passed in atuple just like np.zeros and np.ones

#another function np.empty_like() is used to copy the dimensions of an array and add any garbage value in it 

garr=np.empty_like(array2)
print(garr)

# the An important part of these functions is that the garbage values that are randomly generated are the most recent values in your memory. If I make one array and then copy it with the function `np.empty_like()`, it will be the same array because the memory hasn't had anything else after that. 