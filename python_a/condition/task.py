# 0=100 : water 
# more than 100 : air 
# below 0 : cold 

temperature = int(input("Enter the temperature: "))

if temperature > 100:
    print("Air")
elif temperature >= 0 and temperature <= 100:
    print("Water")
else:
    print("Cold")
