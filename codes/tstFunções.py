# vvv Função sem parâmetros
def vetores():
    a = []
    a = [input("Digite um valor: ") for i in range(3)]
    [print(a[i]) for i in range(3)]

vetores()

# # vvv Função com parâmetros
def message(x):
    x = str(input("Digite uma messagem: "))
    print(x)

a = ''
b = ''
c = ''

message(a)
message(b)
message(c)

### Outros testes
def somaMedia(a, b, c, d):
    print((a + b + c + d) / 4)

nota = []
nota = [float(input("Digite a sua nota: ")) for i in range(4)]

somaMedia(nota[0], nota[1], nota[2], nota[3])
