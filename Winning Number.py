winning_Number = 45
gaussed_Number = int(input('Please Enter a number between 1 to 100:- '))
if winning_Number == gaussed_Number:
    print('Congratulatins You win \U0001F642')
else:
    print('Please Gauss correct number')
if winning_Number < gaussed_Number:
    print('Oh you gaussed high')
if winning_Number > gaussed_Number:
    print('Oh you gaussed low')