tempo_inicial = int(input('Que horas são agora? '))
tempo_add = int(input('Que horas você quer que passe? '))

# 4 linhas / antes
# 3 linhas / depois
def conta_tempo(a, b):
    if a + b >= 24:
        return (a + b) - 24
    return a + b

print('Então vão ser', conta_tempo(tempo_inicial, tempo_add),'h')