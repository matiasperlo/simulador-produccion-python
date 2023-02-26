if __name__ == "__main__":
    import sys
    from PyQt5 import QtWidgets
    from interfaces.ui_main import UiMain

    
    app = QtWidgets.QApplication(sys.argv)
    window = UiMain()
    window.show()
    sys.exit(app.exec_())