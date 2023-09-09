hour = int(input("Tempo inicial (horas): "))
mins = int(input("Tempo inicial (minutos): "))
dura = int(input("Duração do evento (minutos): "))

# não tá funcionando totalmente
hour_mins = (hour * 60) + mins

tempo_total = hour_mins + dura

rst_hrs = round(tempo_total // 60)
rst_min = round(tempo_total % 60)

print(rst_hrs, ":", rst_min)