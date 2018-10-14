my_input = input()

numbers = my_input.split(" ")

biggest_element = 0

for element in numbers:
	num = int(element)
	if(num > biggest_element):
		biggest_element = num
print(str(biggest_element) + " eh o maior")		