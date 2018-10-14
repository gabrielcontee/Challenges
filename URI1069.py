def removeFromList(the_list, val):
   return [value for value in the_list if value != val]

def checkDiamonds(line, diamondsAmount):
    lineLen = len(line) - 1
    foundDiamonds = False
    while lineLen > 0:
        if (line[lineLen] + line[lineLen - 1] == "><"):
            foundDiamonds = True
            diamondsAmount += 1
            del line[lineLen]
            del line[lineLen - 1]
            lineLen -= 2
        else:
            lineLen -= 1

    if foundDiamonds:
        return checkDiamonds(line, diamondsAmount) 
    else: 
        return diamondsAmount

elements = int(raw_input())
k = 0
diamondsList = []
diamondLineCounter = 0

while k < elements:
    line = raw_input()
    line = list(line)
    line = removeFromList(line, '.')
    diamondLineCounter = checkDiamonds(line, diamondLineCounter)
    diamondsList.append(diamondLineCounter)
    diamondLineCounter = 0
    k += 1


for result in diamondsList:
    print(result)


# <..><.<..>>
# <<<..<......<<<<....>
