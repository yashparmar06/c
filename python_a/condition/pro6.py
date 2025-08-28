"""
3) elif statments    
     
syntax :
             
if condition :
        block of chode 
elif condition 
          block of code 
else condition 
          block of code 

"""

marke = int(input("enter the marks :"))

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


