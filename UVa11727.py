test_cases = int(input())
k = 0
answers = []

while k < test_cases:
    employees = list(map(int, input().split(' ')))
    employees.sort()
    answers.append(employees[1])
    k += 1

k = 1
for answer in answers:
	print ("Case " + str(k) + ": " + str(answer))
	k += 1