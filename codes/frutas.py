nome_fruta = input("Tente advinhar a fruta: ")

if nome_fruta == "Laranja":
    print("Sim! Laranja é a melhor fruta!")
elif nome_fruta == "laranja":
    print("Não, eu quero uma laranja maior!")
elif nome_fruta == "Tanjerina":
    print("Não... Mas é quase isso!")
elif nome_fruta == "Toranja":
    print("Não... Mas se você lembrou dessa fruta, facilmente deve advinhar a fruta misteriosa.")
else:
    print("Laranja! Não",nome_fruta+"!")