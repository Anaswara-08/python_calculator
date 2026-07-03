print("-----simple calculator")
num1 = float(input('enter first number'))
num2 = float(input('enter second number'))
print('\nchoose an operation')
print('1.Addition')
print('2.Substraction')
print('3.Multiplication')
print('4.Division')
print('5.Remainder')
choice = input(' enter your choice(1-5):')
if choice == '1':
    print('Answer =',num1+num2)
elif choice == '2':
    print('Answer =',num1-num2)
elif choice == '3':
    print('Answer =',num1*num2)
elif choice == '4':
    if num2 != '0' :
        print('Ánswer =',num1 / num2)
    else:
        print ('cannot divide by zero.')
elif choice == '5':
    if num2 != 0:
        print("Answer =",num1 % num2)
    else:
        print("cannot find remainder with zero")
else :
    print("invalid choice")
print('\n Thanks for using this calculator')