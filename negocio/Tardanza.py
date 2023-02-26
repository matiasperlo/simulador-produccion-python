from random import Random
import math as mt

class Tardanza:

    def __init__(self, generador: Random, dias_media=3) -> None:
        self.__generador_rnd = generador
        self.__rnd_tardanza = self.__generador_rnd.uniform(0, 1)
        self.__dias_media = dias_media
        self.__dias_tardanza = round(- self.__dias_media * mt.log(1 - self.__rnd_tardanza, mt.e))

    def getTardanza(self):
        return self.__dias_tardanza
    
    def getRndTardanza(self):
        return self.__rnd_tardanza
