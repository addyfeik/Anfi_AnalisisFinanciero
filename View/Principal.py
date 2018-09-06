'''
    Persona:
    - ID
    - Nombre
    - Apellido Paterno
    - Apellido Materno
    - RFC
    -Movimientos [folio,dict()]
        Folio
        Fecha
        Cantidad
        Conceptos

    Procesos:
    - Cantidad
    - Concepto
    - Ingresos o egresos
    - Fecha

    Salida:
    - Posibles decisiones
    - Estadistica

'''


import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "Ui_Principal.ui" # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self): #constructor
        QtWidgets.QMainWindow.__init__(self) #crea la parte visual
        Ui_MainWindow.__init__(self) #convierte el ui a codigo entendible en python
        self.setupUi(self) #carga el codigo convertido

#Nombre de las tablas en minusculas
#Ruta C:\Users\Cavazos\Desktop\SistemaAnalisisBancario\BankOperationRisk\Anfi_AnalisisFinanciero\View
        #VARIABLES
        self.ID=int()
        self.cont=int()
        self.nombre=str()
        self.apellido_paterno=str()
        self.apellido_materno=str()
        self.RFC=str()
        self.init_listeners()


    def init_listeners(self):
        self.pb_OK.clicked.connect(self.ok)
    # ----------------------------------------------------------------------------------------------------------------------#

    def getnombre(self):
        return str(self.le_nombre.text())
    def getapellido_paterno(self):
        return str(self.le_apellido_paterno.text())
    def getapellido_materno(self):
        return str(self.le_apellido_materno.text())
    def getconcepto(self):
        return str(self.le_concepto.text())
    def getmovimiento(self):
        return str(self.movimiento.text())
    def getcantidad(self):
        return str(self.le_cantidad.text())
    def getfecha(self):
        return str(self.le_apellido_paterno.text())

    def movimiento(self):
        #Esta funcion va a regresar el tipo de movimiento si es enable is 1 ingresos y 0 egresos
        print("movimiento")



    #----------------------------------------------------------------------------------------------------------------------#
#Listeners

        # Push button "Ok"
    def ok(self):
        #Impresion de nombre
        print("Push ok...")
        print(self.getnombre())

        # ----------------------------------------------------------------------------------------------------------------------#

    #Spinner Box "ID"
    #este es un slot del spinner box para cambiar el id
    def llenar_campos(self):
        #Aqui busco el valor del ID
        ######################andamos cagando en esta puta linea me caga#####################
        try:
            print(int(self.sb_ID.value))
        except:
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)

#----------------------------------------------------------------------------------------------------------------------#

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())