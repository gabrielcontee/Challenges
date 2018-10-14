import math

test_cases = int(input())
test = 0
results = [] * test_cases
is_square = True
rods_last_number = []

def perfect_square(number, pegs_array):
    i = 0
    while i < len(pegs_array):
        # print(rods_last_number)
        n = math.sqrt(number + rods_last_number[i])
        # se for square 
        # print("somando: " + str(number) + " com " + str(rods_last_number[i]))
        if n == math.trunc(n):
            # print("assignou")
            return i
        else:
            # se está vazio
            if pegs_array[i] == 0:
                # print("novo rod")
                return i
        i += 1
    return -1

while test < test_cases:
    pegs_num = int(input())
    rods_last_number = [0] * pegs_num
    number = 1
    is_square = True

    while(is_square):
        # print("testando agora: " + str(number))
        el = perfect_square(number, rods_last_number)
        # print(rods_last_number)
        if el != -1:
            rods_last_number[el] = number
            # print(rods_last_number)
            number += 1
        else:
            is_square = False
            results.append(number - 1)
    test += 1

for result in results:
    print(result)




