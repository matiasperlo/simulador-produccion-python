
from pathlib import Path
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
# from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp

from negocio.Simulador import SimuladorMontecarloSimple, VectorEstado
from interfaces.ui_params import UiParams
from interfaces.Ui_Ejercicio import UiEjercicio
from soporte.Parametros import Parametros

class UiMain(QtWidgets.QMainWindow):
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.loadUi()
        # self.parametros: Parametros = None
        self.vtnParams: UiParams = UiParams()
        self.vtnEjercicio: UiEjercicio = UiEjercicio()
    
    def setParametros(self, params: Parametros):
        self.parametros = params

    def loadUi(self):
        # carga ui
        qtcreator_file = Path(__file__).resolve().parent / "qt" / "main_v2.ui"
        uic.loadUi(qtcreator_file, self)

        # configuracion
        self.configurarTabla()

        self.btnIr.clicked.connect(self.IrA)
        self.txtIrA.setValidator(QRegExpValidator(QRegExp("[1-9][0-9]*"), self.txtIrA))

        # bindings
        self.actionGenerar_Simulacion.triggered.connect(self.cargarSimulaciones)
        self.actionConfigurar_Parametros.triggered.connect(self.cargarVentanaParametros)
        self.actionLimpiarContenido.triggered.connect(self.limpiarContent)
        self.actionSobre_El_Ejercicio.triggered.connect(self.cargarVentanaEjercicio)


    def configurarTabla(self):
        # span
        # climas de los dias
        self.tablaHeader.setSpan(0, 1, 1, 20)
        
        # total de dias por clima
        self.tablaHeader.setSpan(0, 21, 1, 3)

        # tardanza del fertilizante
        self.tablaHeader.setSpan(0, 24, 1, 2)

        # produccion anual
        self.tablaHeader.setSpan(0, 26, 1, 2)


    def cargarSimulaciones(self):
        self.limpiarContent()
        simulador = SimuladorMontecarloSimple(self.vtnParams.getParams())
        vector: VectorEstado = None
        produccion_ac = 0
        
        for i in range(self.vtnParams.getParams().cant_anios):
            vector = simulador.ejecutarSimulacion()
            self.tablaResultados.insertRow(self.tablaResultados.rowCount())
            self.tablaResultados.setItem(self.tablaResultados.rowCount() - 1, 0, QTableWidgetItem(str(vector.getYear())))
            # self.tablaResultados.setItem(self.tablaResultados.rowCount() - 1, 1, QTableWidgetItem(str(self.__truncarFloat(vector.getRndClima(), 4))))
            dia = 1
            for j in range(0, 20, 2):
                self.tablaResultados.setItem(self.tablaResultados.rowCount() - 1, 1 + j, QTableWidgetItem(str(self.__truncarFloat(vector.getRndClima(dia), 4))))
                self.tablaResultados.setItem(self.tablaResultados.rowCount() - 1, 2 + j, QTableWidgetItem(str(vector.getClimaDia(dia))))
                dia += 1

            self.tablaResultados.setItem(self.tablaResultados.rowCount() - 1, 21, QTableWidgetItem(str(vector.getCantDiasSoleados())))
            self.tablaResultados.setItem(self.tablaResultados.rowCount() - 1, 22, QTableWidgetItem(str(vector.getCantDiasLluviosos())))
            self.tablaResultados.setItem(self.tablaResultados.rowCount() - 1, 23, QTableWidgetItem(str(vector.getCantDiasNublados())))
            self.tablaResultados.setItem(self.tablaResultados.rowCount() - 1, 24, QTableWidgetItem(str(self.__truncarFloat(vector.getRndTardanzas(), 4))))
            self.tablaResultados.setItem(self.tablaResultados.rowCount() - 1, 25, QTableWidgetItem(str(vector.getDiasTardanza())))
            self.tablaResultados.setItem(self.tablaResultados.rowCount() - 1, 26, QTableWidgetItem(str(self.__truncarFloat(vector.getProduccionTotalAnual(), 4))))
            produccion_ac += vector.getProduccionTotalAnual()
            self.tablaResultados.setItem(self.tablaResultados.rowCount() - 1, 27, QTableWidgetItem(str(self.__truncarFloat(produccion_ac, 4))))
        
        self.statusbar.showMessage(f"Total Acumulado: {produccion_ac}")
        self.habilitarIrA()
        

    def habilitarIrA(self):
        self.btnIr.setEnabled(True)
        self.txtIrA.setEnabled(True)
    
    def DesHabilitarIrA(self):
        self.btnIr.setEnabled(False)
        self.txtIrA.setEnabled(False)

    def IrA(self):
        if(self.txtIrA.text() == ''):
            return
        
        IrANro = int(self.txtIrA.text())
        if( IrANro > self.tablaResultados.rowCount()):
            return
        
        self.tablaResultados.scrollToItem(self.tablaResultados.item(IrANro - 1, 0))
        
        
    
    def cargarVentanaParametros(self):
        self.vtnParams.show()
    
    def cargarVentanaEjercicio(self):
        self.vtnEjercicio.show()
        
    def limpiarContent(self):
        self.tablaResultados.setRowCount(0)

    def __truncarFloat(self, num:float, decimales:int) -> float:
        numero = str(num).split(".")
        return float(numero[0] + "." + numero[1][:decimales])





        




