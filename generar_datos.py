import json
import random
from datetime import datetime

# Sensores
temperatura = round(random.uniform(20, 35), 2)
humedad = round(random.uniform(40, 80), 2)

# Datos .json
datos = {
    "temperatura": temperatura,
    "humedad": humedad,
    "fecha_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

with open("datos.json", "w") as archivo:
    json.dump(datos, archivo, indent=4)

print("Datos generados correctamente:")
print(datos)