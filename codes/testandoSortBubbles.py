var = [0, 0, 0, 0, 0]

for i in range(len(var)):
    var[i] = int(input("Insira o valor: "))

numeroMaior = 0
totalLarg = len(var)
# numeroMenor = var[0]
for i in range(totalLarg):
    if numeroMaior < var[i]:
        numeroMaior = var[i]
        var.append(numeroMaior)
        del var[i]

for i in range(totalLarg, -1):
    if numeroMaior > var[i]:
        var.insert(0, var[i])


# Tá dando erro o valor 'var[2]' tá repetindo mais de uma vez e eu n sei pq...

print(var)
print(numeroMaior)
# print(numeroMenor)
