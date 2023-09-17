var = []

for i in range(0, 5):
    # var[i] = i #forma "errada"
    var.append(i + 1) #forma correta
    print(var[i])

print("A largura da variável de", len(var), "\n")

var.append(69)
print(var, "\n")

var.insert(4, 44)
print(var, "\n")
