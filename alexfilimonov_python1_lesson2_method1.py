import math 
l1 = [2,-5,8,9,-25,25,4]
l2 = []
for e in l1 : 
    if e>=0 :
        if math.sqrt(e)== int(math.sqrt(e)) :	
            l2.append(int(math.sqrt(e)))	
print("Output list is ", l2)	