count1=0
count2=0

for i in range (1,6):
    num = int(input("enter the number : "))
    if num % 2 ==0:
        count1=count1+1
    else :
        count2=count2+1 
print("this even number :",count1)
print("this odd number :",count2)          