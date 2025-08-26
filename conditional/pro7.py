"""
4) nested if statement 

if condition :
    if condition statement 
    else:
        truse statement 

elif condition 
        true statement
elif  conditon statement 
     truse statement 
else:
     statemant
     """                      
marke = int(input("enter the marks :"))

if marke >=0 and marke <=100:
 if marke >= 70:
    print("A grade")
 elif marke >= 60 and marke <70:
    print("B grade")
 elif marke >= 50 and marke <60:
    print("C grade ")
 elif marke >= 40 and marke <50:
    print("D grade")
 else: 
    print("Fail")   
    
else: 
      print("invalid input")
         


    