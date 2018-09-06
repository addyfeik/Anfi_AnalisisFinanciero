import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "prog6_6i.ui" # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.actionAbrir.triggered.connect(self.abrir)
        self.actionGuardar.triggered.connect(self.guardar)
        self.actionVentana_2.triggered.connect(self.ventana_2)

        self.rb_hombre.clicked.connect(self.hombre)
        self.rb_mujer.toggled.connect(self.mujer)

        self.genero = ""

        self.btn_registrar.clicked.connect(self.registrar)

    def registrar(self):
        print(f"Genero: {self.genero}")

    def hombre(self):
        valor = self.rb_hombre.isChecked()
        if valor == True:
            self.genero = "hombre"
        print(valor)
        #MyApp.mensaje(self,"Hombre: " + valor)

    def mujer(self):
        valor = self.rb_mujer.isChecked()
        if valor == True:
            self.genero = "mujer"
        print(valor)
        #MyApp.mensaje(self,"Hombre: " + valor)


    def mensaje(self,msj):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText(msj)
        resp = msgBox.exec_()
        #print(f"Respuesta: {resp}");

    def abrir(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Presionaste Abrir")
        resp = msgBox.exec_()
        print(f"Respuesta: {resp}");

    def guardar(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Presionaste Guardar")
        resp = msgBox.exec_()
        print(f"Respuesta: {resp}");

    def ventana_2(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Presionaste Abrir Ventana 2")
        resp = msgBox.exec_()
        print(f"Respuesta: {resp}");

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())