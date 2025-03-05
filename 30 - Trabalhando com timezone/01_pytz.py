from datetime import datetime

import pytz
# Comando para instalar o pytz: pip install pytz

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data)
print(data2)