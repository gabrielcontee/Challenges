def isJolly(num):

	if elementsNumber > 3000:
		print("Not jolly")
		return

	for index in range(numbersLength):

		# Distancia absoluta
		distance = abs(numbers[index] - numbers[index + 1])

		# Se nao passou pelo numero ainda, marca como true
		if(distance <= len(boolList)):
			if(not(boolList[distance - 1])):
				boolList[distance - 1] = True

		# Se ja passou pelo numero alguma vez (se ele ja eh true), significa que ta repetido 
		else:
			print("Not jolly")
			return

		# print(boolList)

	# Checa se nao passou por algum numero ainda, ou seja, se ainda ha algum em False	
	for i in boolList:
		if not(i):
			print("Not jolly")
			return

	# Se tudo ta true, eh jolly			
	else:
		print("Jolly")

# Cria uma lista do tamanho de numeros que vai ter que verificar 
def createBoolList(size):
	lst = []
	for i in range(size):
		lst.append(False)
	return lst


while (True):
	my_input = input()

	numbers = my_input.split(" ")

	numbers = list(map(int, numbers))

	elementsNumber = numbers[0]

	# lista de numeros menos o primeiro, que apenas diz quantos elementos serao
	numbers.pop(0)

	# Tamanho da lista = numero de elementos a serem checados - 1 
	numbersLength = elementsNumber - 1

	boolList = createBoolList(numbersLength)

	isJolly(numbers)

