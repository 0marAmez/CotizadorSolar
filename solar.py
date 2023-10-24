import math
class PanelSolar:
    kw_bimestral = 0.0 
    cantidad_de_paneles = 0.0
    capacidad_instalar = 0.0
    modelo_inversor = " "
    cantidad_inversores = 0
    costo_invesor = 0.0
    costo_de_paneles = 0.0
    costo_de_obra = 0.0
    produccion_del_sistema = 0.0

    #Formato del diccionario
    #Cantida de Paneles : [Modelo del Inversor, Costo del Inversor, Cantidad de inversores, USD,Costo de Contado, Costo financiado ] 
    inversor_data = { 
                     1:["MIC 2000 TL-X","330","?","?","?"],
                     2:["MIC 2000 TL-X","330","?","?"],
                     3:["MIC 2000 TL-X","330","?","?","?"],
                     4:["MIC 2500 TL-X","360","1","$56,542.5","$64,620"],
                     5:["MIC 3000 TL-X","400","1","$69,074.5","$78,940"],
                     6:["MIC 3300 TL-X","420","1","$90,352.5","$103,260"],
                     7:["MIN 4200 MTL-X","520","1","$102,184.5","$116,780"],
                     8:["MIN 4600 TL-X","540","1","$112,535.5","$116,780"],
                     9:["MIN 5000 MTL-X","570","1","$129,355.5","$147,845"],
                     10:["MIN 6000 TL-X","610","1","$139,028.5","$158,890"],
                     11:["MIN 6000 TL-X","610","?","?","?"],
                     12:["MIN 7000 TL-X","860","1","$179,259.5","$204,868"],
                     13:["MIN 4200 MTL-X y MIC 3000 TL-X","920","2","$190,443.5","$217,650"],
                     14:["MIN 8000 TL-X","880","1","$202,864.5","$231,845"],
                     15:["MIN 9000 TL-X","1000","1","$227,489.5","$274,845"],
                     16:["MIN 9000 TL-X","1000","1","$227,489.5","$274,845"],
                     17:["Dos modulos de MIN 5000 MTL-X","1140","2","$240,489.5","$274,845"],
                     18:["Dos modulos de MIN 5000 MTL-X","1140","2","$240,489.5","$274,845"],
                     19:["MIN 11400 TL-X","1300","?","?","?"],
                     20:["MIN 11400 TL-X","1300","?","?","?"],
                     21:["MIN 7000 TL-X y MIN 6000 TL-X","2","1470","$274,687.5","$336,786"],
                     22:["MIN 7000 TL-X y MIN 6000 TL-X","2","1470","$274,687.5","$336,786"],
                     35:["Dos modulos de MIN 10,000 TL-X","2","1140","$240,489.5","$274,845"]
                     }
    
    def __init__(self,kw_bimestral):
        self.kw_bimestral = kw_bimestral
        #print(self.kw_bimestral)

    def calcular_paneles(self):
        # Calcula cantidad de paneles
        self.cantidad_de_paneles = (self.kw_bimestral/0.5)
        self.cantidad_de_paneles = (self.cantidad_de_paneles /0.6)
        self.cantidad_de_paneles = (self.cantidad_de_paneles/550)
        self.cantidad_de_paneles =  math.ceil(self.cantidad_de_paneles)
        if self.cantidad_de_paneles<4:
            self.cantidad_de_paneles = 4

        # Calcula gastos de los paneles
        self.costo_de_paneles = self.cantidad_de_paneles*145*20 # costo por panel solar
        self.costo_de_paneles = self.costo_de_paneles + (self.costo_de_paneles*0.5)
        # Calcula gastos de la obra
        self.costo_de_obra = (50.0*20.0)+(650*self.cantidad_de_paneles)+(1000*self.cantidad_de_paneles)+(1000+1000+500+1500)
        self.costo_de_obra = self.costo_de_obra + (self.costo_de_obra*0.5)

    def info_inversor(self):

        self.capacidad_instalar = (self.cantidad_de_paneles*550)/1000
        self.produccion_del_sistema = (self.capacidad_instalar) *5*60
        # Obtiene el modelo inversor
        temp = self.inversor_data[ int(self.cantidad_de_paneles)]
        self.modelo_inversor = temp[0]
        # Calcula gasto del inversor
        self.costo_invesor = int(temp[1])*20
        self.costo_invesor = self.costo_invesor+(self.costo_invesor*0.5)
        # Obtiene la cantidad de inversores
        self.cantidad_inversores = int(temp[2])