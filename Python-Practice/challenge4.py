#Create a BMI calculator, BMI which stands for Body Mass Index can be calculated using the formula:
#BMI = (weight in Kg)/(Height in Meters)^2.
#Write python code which can accept the weight and height of a person and calculate his BMI.
#note: Make sure to use a function which accepts the height and weight values and returns the BMI value.

def calculate_BMI(new_weight, new_height):
    new_bmi = new_weight/(pow(new_height, 2))
    return new_bmi

weight = float(input('Enter weight in Kgs'))
height = float(input('Enter height in meters'))
bmi = calculate_BMI(weight, height)
print(bmi)

