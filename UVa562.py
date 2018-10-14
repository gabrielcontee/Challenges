import math

def findResult(amount, coins, sumOfCoinsValues):

    # inicializa as coins
    coinsV = [0] * (sumOfCoinsValues + 1)

    coinsV[0] = 1

    coinsV[coins[0]] = 1

    # itera sobre os valores
    for c in range(1, amount):

        for v in range(sumOfCoinsValues + 1, -1, -1):

            if v >= coins[c] and coinsV[v - coins[c]] == 1:

                coinsV[v] = 1
    # pega o menor dos valores
    lesserValue = math.inf

    # procura o valor para encaixar
    for c in range(0, sumOfCoinsValues + 1):

        if coinsV[c]:

            lesserValue = min(lesserValue, abs(sumOfCoinsValues - 2 * c))

    return lesserValue

# main 
problems = int(input())

for problem in range(0,problems):

    numOfCoins = int(input())

    # le as coins
    coins = list(map(int, input().split()))

    if numOfCoins != 0:
        
        print(findResult(numOfCoins, coins, sum(coins)))
    else:
        # se nao houver coins, retorna zero
        print("0")