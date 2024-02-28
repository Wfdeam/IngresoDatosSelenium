import pandas as pd

class lecturaPersonal():
    try: 
        def __init__(self, ruta):
            self.ruta = ruta

        def lecturaCSV(self):
            df = pd.read_csv(self.ruta, sep= ';')
            return df
        
    except Exception as e:
        print(e)