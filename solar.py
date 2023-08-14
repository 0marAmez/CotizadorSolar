class PanelSolar:
    def __init__(self,kw_bimestral):
        self.kw_bimestral = kw_bimestral
        self.inversor = 0
        #Formato del diccionario
        # Cantida de Paneles : [Capacidad a instalar, Inversor, PTR, Costo de Contado, Costo financiado] 
        self.data = {
            4: [2200.0,2500.0,4,56542.5,64620],
            5: [2750.0, 3000.0 ,69074.5,78940],
            6: [3300.0, 3300.0, 90352.5,103260],
            7:[3850],
            8:[],
            9:[],
            10:[],
            11:[],
            12:[],
            13:[],
            14:[],
            15:[],
            16:[],
            18:[],
            20:[],
            22:[],
            35:[],
        }

    def get_value(self, key):
        return self.data.get(key)

    def set_value(self, key, value):
        self.data[key] = value

    # ... other methods for data manipulation ...




