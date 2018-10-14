maxCases = []
coins = [50, 25, 10, 5, 1]
ways = [0] * 30001

def printSolution(path):
    for path in range(0,len(maxCases)):
        if ways[maxCases[path]] == 1: #tem que aceitar 0 tambem?
            print('There is only 1 way to produce ' + str(maxCases[path]) + ' cents change.')
        else:
            print('There are ' + str(ways[maxCases[path]]) + ' ways to produce ' + str(maxCases[path]) + ' cents change.')

try:
    while True:
        testCase = int(input())
        maxCases.append(testCase)
except:
    pass

ways[0] = 1;

k = 0
j = 0
for k in range(0, 5):
    for j in range(coins[k], 30001):
        ways[j] += ways[j - coins[k]]
        
printSolution(ways)


