import random
number = random.randint(-10000, 10000)
x = number % 10
if x > 5:
	print(f'last digit of {number} is {x} and is greater than 5')
elif x == 0:
	print(f'last digit of {number} is {x} and is 0')
else:
	print(f'last digit of {number} is {x} and is less than 6 and not 0')
