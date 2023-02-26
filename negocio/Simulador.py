from random import Random
from negocio.Produccion import Produccion

from negocio.Tardanza import Tardanza
from soporte.Parametros import Parametros
from .Dia import Dia, Clima

class VectorEstado:
    def __init__(self, year, dias:list[Dia], tardanza:Tardanza, produccion:Produccion) -> None:
        self.__year = year
        self.__dias: list[Dia] = dias
        self.__contadores_dias = {
            Clima.SOLEADO.value: 0,
            Clima.LLUVIA.value: 0,
            Clima.NUBLADO.value: 0
        }
        self.__tardanza = tardanza
        self.__produccion = produccion
        
        self.__contar_dias()
    
    def __contar_dias(self):
        for dia in self.__dias:
            self.__contadores_dias[dia.getClima()] += 1
        
    # gets de los valores importantes de la simulacion
    def getYear(self) -> int:
        return self.__year

    def getRndClima(self, dia: int) -> float:
        return self.__dias[dia - 1].getRndClima()

    def getClimaDia(self, dia: int) -> str:
        return self.__dias[dia - 1].getClima()

    def getCantDiasSoleados(self) -> int:
        return self.__contadores_dias[Clima.SOLEADO.value]

    def getCantDiasLluviosos(self) -> int:
        return self.__contadores_dias[Clima.LLUVIA.value]

    def getCantDiasNublados(self) -> int:
        return self.__contadores_dias[Clima.NUBLADO.value]

    def getRndTardanzas(self) -> float:
        return self.__tardanza.getRndTardanza()

    def getDiasTardanza(self) -> int:
        return self.__tardanza.getTardanza()

    def getProduccionTotalAnual(self) -> float:
        return self.__produccion.calcular(
            self.getCantDiasSoleados() / 10,
            self.getCantDiasLluviosos() / 10,
            self.getCantDiasNublados() / 10 ,
            self.getDiasTardanza())

class SimuladorMontecarloSimple:
    def __init__(self, params: Parametros) -> None:
        
        # parametros cargados
        self.__parametros = params

        # generadores de numeros pseudoaleatorios
        self.__generador_clima = Random(self.__parametros.seed_climas)
        self.__generador_tardanza = Random(self.__parametros.seed_tardanzas)

        # datos del vector estado
        self.__year = 0

        # configuracion de los dias
        Dia.setGeneradorClima(self.__generador_clima)
        Dia.setProbDpsSoleado(self.__parametros.prob_despues_de_dia_soleado)
        Dia.setProbDpsLluvia(self.__parametros.prob_despues_de_dia_lluvia)
        Dia.setProbDpsNublado(self.__parametros.prob_despues_de_dia_nublado)



    def ejecutarSimulacion(self) -> VectorEstado:

        dias = []
        
        Dia.resetInicial()
        for i in range(10):
            dias.append(Dia())

        tardanza = Tardanza(self.__generador_tardanza, self.__parametros.media_dias_tardanza_fertilizante)
        produccion = Produccion(3350,
        self.__parametros.coef_soleado,
        self.__parametros.coef_lluvia,
        self.__parametros.coef_nublado,
        self.__parametros.coef_tardanza)

        self.__year += 1
        return VectorEstado(self.__year, dias, tardanza, produccion)
