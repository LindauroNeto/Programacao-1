def mensagem(x):
    if x == 'noite':
        return 'É melhor ficar em casa.'
    elif x == 'dia':
        return 'É uma ótima oportunidade para passear!'
    elif x == 'tarde':
        return 'Seria uma boa ir ao cinema!'
    else:
        return 'Você digitou algo errado ou com alguma letra maiúscula.'

y = str(input('Mas que tempo do dia é? '))
print(mensagem(y))