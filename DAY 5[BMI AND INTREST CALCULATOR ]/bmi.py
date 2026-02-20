#maing a bmi calculator using functions and mathematical operators
#taking hight in cm and weight in kg as a input form user
#defining a function 
def bmi(hight,weight):
    body_mass_index = weight/((hight/100)**2)
    print(f"acc to yout hight {hight} and weight{weight} your bmi is {body_mass_index}")

hight = float(input("give your hight in cm :"))
weight = float(input("give your weight in kg:"))
bmi(hight,weight)

# sample input and output 
# give your hight in cm :175
# give your weight in kg:70
# acc to yout hight 175.0 and weight70.0 your bmi is 22.857142857142858