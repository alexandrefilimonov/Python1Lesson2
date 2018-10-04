from random import *
n = int(input("Enter qty of elements:"))
i = 0
empty_list = []
while  (i<n) :
    empty_list.append(randint(-100,100))
    print("Element ",(i+1),":",empty_list[i])
    i+=1
