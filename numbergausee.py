winning_number = 45
gaussed_number = int(input('Please Enter a Number Between 1 to 100:- '))
if winning_number == gaussed_number :
    print('Congratulation You Win ')
else:
    if gaussed_number < winning_number:
        print('Oh You gaussed low \nPlease Gausse Correct Number ')
    else:
        print('Oh You Gaussed high \nPlease gausse Correct Number ')
