print('Using this program, you can convert degrees into radian and radian into degrees.')

print('Select from the menu:')
print(' 1. Convert degrees to radians')
print(' 2. Convert radians to degrees')
input_choice = input('Enter your choice: (1 or 2?) ')

if input_choice == '1':
    degrees = float(input('What is the degrees? '))
    print(f'{degrees} degrees equals to {degrees * 3.1416/180} radians.')
elif input_choice == '2':
    radian = float(input('What is the radian value? '))
    print(f'{radian} degrees equals to {radian * 180/3.1416} radians.')
else:
    print('Invalid input. Please type 1 or 2.')
