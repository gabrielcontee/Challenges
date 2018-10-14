def diameter(radius):
    return radius * 2

def minorValue(first, second):
    return second if (second < first) else first
        
def majorValue(first, second):
    return second if (second > first) else first

def sqr(element):
    return element * element

while True:
    element = list(map(int, input().split()))
    if element[0] == 0:
        break
    
    raios = element[2] + element[3]
    firstDiameter = diameter(element[2])
    secondDiameter = diameter(element[3])
    
    # Ve se o maior diametro dos cilindros é menor do que o menor lado (L ou C)
    if (majorValue(firstDiameter, secondDiameter) <= minorValue(element[0], element[1])):  
        # Faz as somas dos catetos ao quadrado para ver se eles cabem na diagonal também
        if((raios * raios) <= ((element[0] - raios) * (element[0] - raios)) + (element[1] - raios) * (element[1] - raios)):
            print('S')
        else:
            print('N')
    else:
        print('N')

