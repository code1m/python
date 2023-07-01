#Python program to illustrate 
# how to calculate BMI
height=float(input("enter the height in cm"))
weight=float(input("enter the weight in kg"))
def BMI(height, weight):
    bmi = weight/(height**2)
    return bmi
# calling the BMI function
bmi = BMI(height, weight)
print("The BMI is", format(bmi))
  
