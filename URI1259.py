def input_lines():
    k = 0
    numbers = []
    numberOfElements = int(input())
    while k < numberOfElements:
        numbers.append(input())
        k += 1
    return numbers

text = list(input_lines())

evens = []
odds = []
i = 0
while i < len(text):
    element = int(text[i])
    if (element % 2 == 0):
        evens.append(element)
    else:
        odds.append(element)
    i += 1
evens.sort()
odds.sort(reverse=True)
finalArray = []
finalArray = evens + odds
for el in finalArray:
    print(el) 
