import pandas as pd

df = pd.read_csv("C:/Users/queli/OneDrive/Documentos/Python Scripts/selenium/Personal.csv", sep= ';')
print(df)

for indice, fila in df.iterrows():
    # Obtiene la información de cada columna para la fila actual
    nombreAIngressar = fila['nombre']
    print(f'el nombre a ingresar es {nombreAIngressar}')
    correoElectronico = fila['correo']
    print(correoElectronico)
    direccion = fila['direccion']
    print(direccion)
    direccionPersonal = fila['direccionPermanente']
    print(direccionPersonal)