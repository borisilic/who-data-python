vaccines = {'australia': ["1a", 2, 3, 4], 'new zealand': [1, 2, 3, 4]}
list = {}
for i in range(0, 3):
    details = []

    for j in range(0, 4):
        details.append(j)

    list[i] = details

print(list)