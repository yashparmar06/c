""" 
TASK 3 : mini project : 

KALYAN JWELLERS : 

M 
>  65
purchase > 2lk - 3lk    20% 
purchase > 3lk - 5lk 	30% 
purchase > 5lk  	35% 


<65
purchase > 2lk - 3lk    10% 
purchase > 3lk - 5lk 	20% 
purchase > 5lk  	25% 



F
>  65
purchase > 2lk - 3lk    25% 
purchase > 3lk - 5lk 	35% 
purchase > 5lk  	40% 


<65
purchase > 2lk - 3lk    15% 
purchase > 3lk - 5lk 	25% 
purchase > 5lk  	30% 


------------------------------------------------------------
Enter your name : 
Enter gender : 
Enter age : 

Enter product : Ring 
Enter product gram : 20  
current gold price (1 grm) : 5752

-------------------------------------
TOTAL GOLD RATE :  XXXXX 


Making charges (1 gram)  : 845
Total Making CHarges :    TOTAL GOLD  X  MAKING CHARGES 

---------------------------------------
TOTAL AMOUNT : GOLD PRICE + TOTAL MAKING CHARG



DISCOUNT :   25 (AUTOMATIC) 
DIS- AMOUNT : except (making charges) 
-----------------------------------------
total net amount : 

--------------------------------------------
HINT : variables , input , conditional statements 


"""
currentgram = 5752
print("--------------------------------------------------------------------------")
name = input("Enter your name : ")
gender = input("Enter your Gender : ")
age = int(input("Enter your age : "))

product = input("Enter product : ")
gram = int(input("Enter product gram : "))
print("--------------------------------------------------------------------------")
print("current gold price (1gram) : ",currentgram)

TotalGold = gram*currentgram
print("TOTAL GOLD RATE : ",TotalGold)
print("--------------------------------------------------------------------------")
chargesgram = 845
print("Making Charges (1 gram) :",chargesgram)

MakingCharge = chargesgram * gram
print("Total Making Charges : ",MakingCharge)

TotalAmount = TotalGold + MakingCharge
print("Total Amount : ",TotalAmount)
print("--------------------------------------------------------------------------")

discount = 0
if (gender == 'm' or gender == 'M') and age > 65:
    if TotalAmount >= 21000 and TotalAmount <31000:
        discount = (TotalAmount * 20)/100
    elif TotalAmount >=31000 and TotalAmount<51000:
        discount = (TotalAmount * 30)/100
    else:
        discount = (TotalAmount * 35)/100
else:
    if TotalAmount >= 21000 and TotalAmount <31000:
        discount = (TotalAmount * 10)/100
    elif TotalAmount >=31000 and TotalAmount<51000:
        discount = (TotalAmount * 20)/100
    else:
        discount = (TotalAmount * 25)/100
        
if gender == 'f' or gender == 'F' and age > 65:
    if TotalAmount >= 21000 and TotalAmount <31000:
        discount = (TotalAmount * 25)/100
    elif TotalAmount >=31000 and TotalAmount<51000:
        discount = (TotalAmount * 35)/100
    else:
        discount = (TotalAmount * 40)/100
else:
    if TotalAmount >= 21000 and TotalAmount <31000:
        discount = (TotalAmount * 15)/100
    elif TotalAmount >=31000 and TotalAmount<51000:
        discount = (TotalAmount * 25)/100
    else:
        discount = (TotalAmount * 30)/100

print("discount : ",discount)

netamount= TotalAmount-discount
print("Net Amount : ",netamount)