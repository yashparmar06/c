"""
1
2 3
4 5 6
7 8 9 10 

"""
num = 1 
for row in range (1,5):
    for col in range (1,row+1):
            print(num,end="")
            num +=1    
    print()         