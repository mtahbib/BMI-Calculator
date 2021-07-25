





height = input("enter your height in m: ")
height=float(height)
weight = input("enter your weight in kg: ")
weight=float(weight)
BMI=float(weight/(height**2))
print("Your Current BMI is "+str(BMI))

if BMI >= 30:
  print("You are Obsese")
if BMI<=18:
  print("UNDER WEIGHT")
if 18<=BMI and BMI<=25:
  print("YOUR BMI Is fine")
if BMI>=25.01 and BMI<30:
  print("you are over weight") 


