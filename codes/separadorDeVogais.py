sem_vogal = ""

n = input("Digite uma palavra aqui: ")
n = n.upper()

for letter in n:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        sem_vogal += letter

print(sem_vogal)
