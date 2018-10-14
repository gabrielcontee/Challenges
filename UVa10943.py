possible_comb = [[-1 for tentative in range(102)] for y in range(102)] 

def validate(number, comb):
    if(comb == 1):
        return 1
    if(possible_comb[number][comb] != -1):
        return possible_comb[number][comb]
    return -2

def try_numb(number, comb):
    validation = validate(number, comb) 
    if validation != -2:
        return validation
    result = 0
    for tentative in range(0, number+1):
        result = (result + try_numb(number-tentative, comb-1)) % 1000000
        possible_comb[number][comb] = result
    return possible_comb[number][comb]
 
while True:
    data = list(map(int, input().split()))
    if data[0] == 0 and data[1] == 0:
        break
    print(try_numb(data[0], data[1]))