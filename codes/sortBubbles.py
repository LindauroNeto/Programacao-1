var = []
troca = True

qnt = int(input("quantos valores você quer colocar? "))

for i in range(qnt):
    val = int(input("insira o valor: "))
    var.append(val)

print(len(var))

while troca:
    troca = False
    for i in range(len(var) - 1):
        if var[i] > var[i + 1]:
            troca = True
            var[i], var[i + 1] = var[i + 1], var[i]

print(var)
print(len(var))
