class PanelSolar:
    def __init__(self,kw_bimestral):
        self.kw_bimestral = kw_bimestral
        self.inversor = 0
        #Formato del diccionario
        # Cantida de Paneles : [Capacidad a instalar, Inversor, PTR, Costo de Contado, Costo financiado] 
        self.data = {
            4: [2200.0,2500.0,4.0,56542.5,64620.0],
            5: [2750.0, 3000.0 ,5.0,69074.5,78940.0],
            6: [3300.0, 3300.0,6.0,90352.5,103260.0],
            7: [3850.0,4200.0,7.0,102184.5,116780.0],
            8: [4400.0,4600.0,8.0,112535.5,116780.0],
            9: [4950.0,5000.0,9.0,129355.5,147845.0],
            10: [5500.0,6000.0,10.0,139028.5,158890.0],
            12: [6600.0, 7000.0,12.0, 179259.5,204868.0],
            13: [7150.0,4200.0,13.0,190443.5,231845.0],  #<- 4200+3000 Inversor
            14: [7700.0,8000.0,14.0,202864.5,231845.0],
            16: [8800.0,9000.0,16.0,227377.5,259,860.0],
            18: [9900.0,5000.0,18.0,240489.5,274845.0],
            22: [12100.0,7000.0,22.0,294687.5,336786.0],
            35: [19250.0,10000.0,35.0,481031.5,549750.0],
        }

    def get_value(self, key):
        return self.data.get(key)

    def set_value(self, key, value):
        self.data[key] = value

    # ... other methods for data manipulation ...




