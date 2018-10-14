my_input = input()

numbers = my_input.split(" ")

num0 = int(numbers[0])
num1 = int(numbers[1])
num2 = int(numbers[2])

if((num0 == num1) or (num1 == num2) or (num0 == num2)):
	print("S")
	exit()
	
if(num0 == (num1 + num2)):
	print("S")
	exit()
	
if(num1 == (num0 + num2)):
	print("S")
	exit()


if(num2 == (num0 + num1)):
	print("S")
	exit()
	
else:
	print("N")
	exit()