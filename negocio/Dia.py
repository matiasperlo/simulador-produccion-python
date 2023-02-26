from enum import Enum
from random import Random



class Clima(Enum):
    INICIAL = "Inicial"
    SOLEADO = "Soleado"
    LLUVIA = "Lluvia"
    NUBLADO = "Nublado"

class Dia:

    # random y generadores
    __generador_clima: Random = Random()

    __climas = (Clima.SOLEADO, Clima.LLUVIA, Clima.NUBLADO)
    __clima_anterior = Clima.INICIAL
    __tablas_probabilidades = {
        Clima.INICIAL: (0.33, 0.33, 0.34),
        Clima.SOLEADO: (0.8 , 0.1, 0.1),
        Clima.LLUVIA:  (0.4 , 0.2, 0.4),
        Clima.NUBLADO: (0.6 , 0.1, 0.3)
        }

    def setGeneradorClima(generador: Random) -> None:
        Dia.__generador_clima = generador
    
    def setProbDpsSoleado(probs: list):
        Dia.__tablas_probabilidades[Clima.SOLEADO] = probs

    def setProbDpsLluvia(probs: list):
        Dia.__tablas_probabilidades[Clima.LLUVIA] = probs

    def setProbDpsNublado(probs: list):
        Dia.__tablas_probabilidades[Clima.NUBLADO] = probs

    def resetInicial():
        Dia.__clima_anterior = Clima.INICIAL

    def __init__(self) -> None:
        self.__clima: Enum = ''
        self.__rnd_clima = -1
        self.__calcularClima()
    
    def __calcularClima(self) -> str:
        self.__rnd_clima = Dia.__generador_clima.uniform(0,1)
        self.__clima = self.__elegirClima(self.__rnd_clima, Dia.__tablas_probabilidades[Dia.__clima_anterior])
        Dia.__clima_anterior = self.__clima

    def __elegirClima(self, rnd, climas):
        ac = 0
        for i in range(3):
            ac += climas[i]
            if rnd <= ac:
                return Dia.__climas[i]
        return Dia.__climas[i]
        
    def getClima(self) -> str:
        return self.__clima.value

    def getRndClima(self) -> float:
        return self.__rnd_clima

