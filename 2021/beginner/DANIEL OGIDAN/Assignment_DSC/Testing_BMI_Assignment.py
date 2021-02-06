#A program that check BMI 

opti_min =18.5
opti_max=25
over_min =18.5


pounds=453.592
inches=2.54
print('Body Mass Index calculator\n')
weight = float(input('Enter your weight: '))
height = float(input('Enter your height: '))

weight_pound = weight/pounds
height_inches = height/inches

BMI = float(weight_pound * 703)/height_inches*height_inches
print("Your Body mass index is:  ", BMI)

if ((BMI>=opti_min) and (BMI<=opti_max)):
    print('You are OPTIMAL size')

elif(BMI<opti_min):
    print('You are UNDERWEIGHT size')

elif(BMI>opti_max):
    print('you are OVERWEIGHT size')
else:
    print('Error!!!, try again.')

