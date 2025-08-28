"""
A
B B 
C C C 
D D D D 
E E E E E

"""
num=65 
for row in range (1,6):
    for col in range (1,row+1):
        print(chr(num),end=" ")
    num+=1
    print()    
