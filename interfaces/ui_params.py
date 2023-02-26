from ast import Param
from pathlib import Path
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp
from soporte.Parametros import Parametros


class UiParams(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.parametros = Parametros.getDefault()
        self.loadUi()
        # self.cargarParametros()

    def getParams(self):
        return self.parametros

    def loadUi(self):
        qtcreator_file = Path(__file__).resolve().parent / "qt" / "params.ui"
        uic.loadUi(qtcreator_file, self)

        self.configurarValidadores()
        self.btnCargar.clicked.connect(self.validar)
        self.btnRestablecer.clicked.connect(self.restablecer)
        # self.Form.show.connect(self.cargarParametros)

    def show(self):
        QtWidgets.QWidget.show(self)
        self.cargarParametros()
        print("Configurando")

    def configurarValidadores(self):
        validador_coef = QRegExp("[0-9]|[1-9][0-9]*|-[1-9]+[0-9]*")
        validador_ent_positivo = QRegExp("[1-9][0-9]*")
        validador_proporcion = QRegExp("^[01]|^0\.[0-9]+$")

        self.txtCantAnios.setValidator(QRegExpValidator(
            validador_ent_positivo, self.txtCantAnios))
        self.txtCoefSoleado.setValidator(
            QRegExpValidator(validador_coef, self.txtCoefSoleado))
        self.txtCoefLluvia.setValidator(
            QRegExpValidator(validador_coef, self.txtCoefLluvia))
        self.txtCoefNublado.setValidator(
            QRegExpValidator(validador_coef, self.txtCoefNublado))
        self.txtCoefTardanza.setValidator(
            QRegExpValidator(validador_coef, self.txtCoefTardanza))

        self.txtSeedClima.setValidator(QRegExpValidator(
            validador_ent_positivo, self.txtSeedClima))
        self.txtSeedTardanza.setValidator(QRegExpValidator(
            validador_ent_positivo, self.txtSeedTardanza))

        self.Prob_DS_DS.setValidator(QRegExpValidator(
            validador_proporcion, self.Prob_DS_DS))
        self.Prob_DS_DL.setValidator(QRegExpValidator(
            validador_proporcion, self.Prob_DS_DL))
        self.Prob_DS_DN.setValidator(QRegExpValidator(
            validador_proporcion, self.Prob_DS_DN))

        self.Prob_DL_DS.setValidator(QRegExpValidator(
            validador_proporcion, self.Prob_DL_DS))
        self.Prob_DL_DL.setValidator(QRegExpValidator(
            validador_proporcion, self.Prob_DL_DL))
        self.Prob_DL_DN.setValidator(QRegExpValidator(
            validador_proporcion, self.Prob_DL_DN))

        self.Prob_DN_DS.setValidator(QRegExpValidator(
            validador_proporcion, self.Prob_DN_DS))
        self.Prob_DN_DL.setValidator(QRegExpValidator(
            validador_proporcion, self.Prob_DN_DL))
        self.Prob_DN_DN.setValidator(QRegExpValidator(
            validador_proporcion, self.Prob_DN_DN))

        self.txtMediaTardanza.setValidator(QRegExpValidator(
            validador_ent_positivo, self.txtMediaTardanza))

    def validar(self):
        for entrada in [self.txtCoefSoleado,
                        self.txtCantAnios,
                        self.txtCoefLluvia,
                        self.txtCoefNublado,
                        self.txtCoefTardanza,
                        self.txtSeedClima,
                        self.txtSeedTardanza,
                        self.Prob_DS_DS,
                        self.Prob_DS_DL,
                        self.Prob_DS_DN,
                        self.Prob_DL_DS,
                        self.Prob_DL_DL,
                        self.Prob_DL_DN,
                        self.Prob_DN_DS,
                        self.Prob_DN_DL,
                        self.Prob_DN_DN,
                        self.txtMediaTardanza]:
            if not entrada.hasAcceptableInput():
                self.msgEstado.setText("Error: Parametros Incorrectos")
                return 1

        for probs in (
            [self.Prob_DS_DS, self.Prob_DS_DL, self.Prob_DS_DN, ],
            [self.Prob_DL_DS, self.Prob_DL_DL, self.Prob_DL_DN, ],
            [self.Prob_DN_DS, self.Prob_DN_DL, self.Prob_DN_DN, ]):

            prob_ac = float(probs[0].text()) + float(probs[1].text()) + float(probs[2].text())
            if prob_ac != 1.0:
                self.msgEstado.setText("Error: Parametros Incorrectos")
                return 1

        self.guardarParametros()
        self.msgEstado.setText("Parametros Guardados")
        # self.cargarParametros()
        return 0

    def restablecer(self):
        self.parametros = Parametros.getDefault()
        self.cargarParametros()
        self.msgEstado.setText("Parametros Restablecidos")

    def cargarParametros(self):
        self.txtCantAnios.setText(str(self.parametros.cant_anios))
        self.txtCoefSoleado.setText(str(self.parametros.coef_soleado))
        self.txtCoefLluvia.setText(str(self.parametros.coef_lluvia))
        self.txtCoefNublado.setText(str(self.parametros.coef_nublado))
        self.txtCoefTardanza.setText(str(self.parametros.coef_tardanza))

        self.txtSeedClima.setText(str(self.parametros.seed_climas))
        self.txtSeedTardanza.setText(str(self.parametros.seed_tardanzas))

        self.Prob_DS_DS.setText(
            str(self.parametros.prob_despues_de_dia_soleado[0]))
        self.Prob_DS_DL.setText(
            str(self.parametros.prob_despues_de_dia_soleado[1]))
        self.Prob_DS_DN.setText(
            str(self.parametros.prob_despues_de_dia_soleado[2]))

        self.Prob_DL_DS.setText(
            str(self.parametros.prob_despues_de_dia_lluvia[0]))
        self.Prob_DL_DL.setText(
            str(self.parametros.prob_despues_de_dia_lluvia[1]))
        self.Prob_DL_DN.setText(
            str(self.parametros.prob_despues_de_dia_lluvia[2]))

        self.Prob_DN_DS.setText(
            str(self.parametros.prob_despues_de_dia_nublado[0]))
        self.Prob_DN_DL.setText(
            str(self.parametros.prob_despues_de_dia_nublado[1]))
        self.Prob_DN_DN.setText(
            str(self.parametros.prob_despues_de_dia_nublado[2]))
        self.txtMediaTardanza.setText(
            str(self.parametros.media_dias_tardanza_fertilizante))

    def guardarParametros(self):
        self.parametros.cant_anios = int(self.txtCantAnios.text())
        self.parametros.coef_soleado = int(self.txtCoefSoleado.text())
        self.parametros.coef_lluvia = int(self.txtCoefLluvia.text())
        self.parametros.coef_nublado = int(self.txtCoefNublado.text())
        self.parametros.coef_tardanza = int(self.txtCoefTardanza.text())

        self.parametros.seed_climas = int(self.txtSeedClima.text())
        self.parametros.seed_tardanzas = int(self.txtSeedTardanza.text())

        self.parametros.prob_despues_de_dia_soleado = [
            float(self.Prob_DS_DS.text()),
            float(self.Prob_DS_DL.text()),
            float(self.Prob_DS_DN.text())
        ]
        self.parametros.prob_despues_de_dia_lluvia = [
            float(self.Prob_DL_DS.text()),
            float(self.Prob_DL_DL.text()),
            float(self.Prob_DL_DN.text())
        ]
        self.parametros.prob_despues_de_dia_nublado = [
            float(self.Prob_DN_DS.text()),
            float(self.Prob_DN_DL.text()),
            float(self.Prob_DN_DN.text())
        ]
        self.parametros.media_dias_tardanza_fertilizante = float(
            self.txtMediaTardanza.text())
