class Produccion:
    def __init__(self, tindependiente, csoleado,
     clluvia, cnublado, ctardanza) -> None:
        self.__independiente = tindependiente
        self.__coef_soleado = csoleado
        self.__coef_lluvia = clluvia
        self.__coef_nublado = cnublado
        self.__coef_tardanza = ctardanza

    def calcular(self, probsoleado: float,
     problluvia: float, probnublado: float, diastardanza: float) -> float:
        return self.__independiente + self.__coef_soleado * probsoleado + \
            self.__coef_lluvia * problluvia + \
            self.__coef_nublado * probnublado + \
            self.__coef_tardanza * diastardanza