from datetime import datetime

data_hora_atual = datetime.now()
data_hora_string = "2023-10-20 10:20"
mascara_ptbr = "%d/%m/%Y %A"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))

data_convertida = datetime.strptime(data_hora_string, mascara_en)
print(data_convertida)
print(type(data_convertida))