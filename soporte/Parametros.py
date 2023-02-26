from email.policy import default


class Parametros:

    def getDefault():
        '''Singleton de Parametros por defecto'''
        default = Parametros()
        default.cant_anios = 40
        default.coef_soleado =   250
        default.coef_lluvia =    390
        default.coef_nublado =   -150
        default.coef_tardanza =  -600
        default.seed_climas =    7
        default.seed_tardanzas = 17
        default.prob_despues_de_dia_soleado =  [0.8, 0.1, 0.1]
        default.prob_despues_de_dia_lluvia =   [0.4, 0.2, 0.4]
        default.prob_despues_de_dia_nublado =  [0.6, 0.1, 0.3]
        default.media_dias_tardanza_fertilizante = 3
        return default

    def __init__(self) -> None:
        self.cant_anios = 0
        self.coef_soleado =   0
        self.coef_lluvia =    0
        self.coef_nublado =   0
        self.coef_tardanza =  0

        self.seed_climas =    0
        self.seed_tardanzas = 0

        self.prob_despues_de_dia_soleado =  [0, 0, 0]
        self.prob_despues_de_dia_lluvia =   [0, 0, 0]
        self.prob_despues_de_dia_nublado =  [0, 0, 0]

        self.media_dias_tardanza_fertilizante = 0




