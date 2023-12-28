Weight = float(input("Enter your weight in Kg:"))
hight = float(input("Enter your hight in Meter:"))

BMI = Weight / (hight/100)**2

print("Your BMI is:",BMI)

if BMI <= 18.5:
    print("Underwight")

elif BMI <= 24.9:
    print("Normal")

elif BMI <= 29.9:
    print("Overwaight")

else:
   print("Obese" )