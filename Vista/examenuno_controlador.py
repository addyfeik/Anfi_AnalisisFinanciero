
import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "examenuno_vista.ui" # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.Crear_slots()
        self.Crear_listeners()
        self.ejemplo()
        self.llenarCampos()
        self.reg_calific = dict()
        self.reg_alumno=dict()
#---------------------------------------------------------------
    def ejemplo(self):

        #Ejemplo de prueba
        self.calificaciones = [10.0,10.0,10.0]
        self.alumno = {'nombre': 'Adrian Vibanco Rosales','promedio':10,'calificaciones':self.calificaciones}
        self.alumno1 = {'nombre': 'Ana', 'promedio':  5.0, 'calificaciones': [5.0,5.0,5.0]}
        self.alumno2 = {'nombre': 'Adriana', 'promedio': 9, 'calificaciones': [9.0,9.0,9.0]}

        self.grupo = {}
        self.grupo[0] = self.alumno
        self.grupo[1] = self.alumno1
        self.grupo[2] = self.alumno2

    def Crear_slots(self):
        self.pb_nueva.clicked.connect(self.clickNueva)
        self.pb_agregaralumno.clicked.connect(self.clickAgregaralumno)
        self.pb_modificar.clicked.connect(self.clickBorrarcalif)

    def Crear_listeners(self):
        # listeners
        self.actionMostrar.triggered.connect(self.dialogo)

        self.sp_grupo.setMaximum(0)
        self.sp_grupo.setMinimum(0)
        self.sp_grupo.setSingleStep(1)
        self.sp_grupo.setValue(0)
        self.sp_grupo.valueChanged.connect(self.llenarCampos)

#----------------------------------------------------------------------------

    def dialogo(self):
        try:
            nombre=""
            promedio=""
            calificaciones=""
            mayor_promedio=0.0
            menor_promedio=10.0
            self.dialogo  = VentanaDialog()
            self.dialogo.setModal(True)
            self.noesta=dict()

            for i in self.grupo:

                self.reg_alumno = self.grupo.get(i, self.noesta)

                nombre=self.reg_alumno.get('nombre', self.noesta)
                promedio=float(self.reg_alumno.get('promedio', 0.0))

                self.dialogo.te_nombres.setText(self.dialogo.te_nombres.text()+"\n"+nombre)
                self.dialogo.te_id.setText(str(self.dialogo.te_id.text())+"\n"+str(i))
                self.dialogo.te_promedios.setText(str(self.dialogo.te_promedios.text()) + "\n" + str(promedio))

                if promedio > mayor_promedio:
                    mayor_promedio=promedio

                    self.dialogo.le_mayor.setText(str(mayor_promedio))
                    self.dialogo.le_nombremayor.setText(nombre)
                    self.dialogo.le_calificacionesmayor.setText(str(self.reg_alumno.get('calificaciones', "null")))

                if promedio < menor_promedio:
                    menor_promedio = promedio
                    self.dialogo.le_menor.setText(str(menor_promedio))
                    self.dialogo.le_nombremenor.setText(nombre)
                    self.dialogo.le_calificacionesmenor.setText(str(self.reg_alumno.get('calificaciones', "null")))

            self.dialogo.show()

        except:
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)
    def mainWindow(self):
        self.mainW = MyApp()
        self.mainW.show()
#----------------------------------------------------------------------------------------------------------------------

    def clickBorrarcalif(self):

        try:
            self.calificaciones.pop()
            self.calculo_promediop()
            self.panel.setText(str(self.calificaciones))
        except:
            self.panel.setText("null")
    def clickModificarcalif(self):
        try:
            self.reg_calific = self.reg_alumno.get('calificaciones', "No estaba")

            posicion=2
            cambio=10
            #Supuuse que seria mejor un mensaje se ejecute con botones que se crean en tiempo de ejecucion con las calificaciones contenidas
            # especificando que devuelva cada uno la posicion donde se encuetre
            #
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Cual calificacion?")
            for i in list(self.reg_calific):
                cont=1
                calif=str(i)
                btn = QtWidgets.QPushButton(calif)
                msgBox.addButton(btn, cont)

            ret = msgBox.exec_()
            print(f"Respuesta: {ret}");

            posicion=int(ret)
            print()
            #calif = float(self.le_calificacion.text())
            self.reg_calific[1] = 10

            #Calculo de promedio
            self.cont = 0

            self.promedio = 0
            print("Todo bien")
            for i in list(self.reg_calific):
                self.promedio += int(i)
                self.cont += 1
                self.le_calificacionn.setText("Calificacion " + str(self.cont) + ":")
            self.promedio /= len(self.reg_calific)
            self.le_promedio.setText(str(self.promedio))
            self.calificaciones=self.reg_calific

            self.le_calificacion.setText("")
            self.panel.setText(f"Calificaciones{self.reg_calif}")


            self.alumno = {'calificaciones': self.reg_calific}

            print(self.reg_calific)
        except:
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)
    def clickAgregaralumno(self):
        try:
            #Se guada `valor del spin ID alumno desde grupo
            valorspin=int(self.sp_grupo.value())

            # creacion de la variable para su modicficacion en el dicc
            alumnoagregar=self.le_nombre.text()
            promedio=self.le_promedio.text()

            print("antes", valorspin, alumnoagregar, promedio, type(valorspin))


            #Ubicandonos en el ID
            self.grupo[valorspin] = self.alumno
            print("entro")

            ##Buscar
            #por el ID del alumno
            self.reg_alumno=self.grupo.get(valorspin, "No estaba")
            #obtener la lista de calif
            self.calificaciones=self.reg_alumno.get('calificaciones',[])

            self.alumno = {'nombre': alumnoagregar, 'promedio': promedio,'calificaciones':self.calificaciones}

            self.lcd_id.display(str(len(self.grupo)))
        except:
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)
    def clickNueva(self):
        try:
            calif = float(self.le_calificacion.text())
            self.calificaciones.append(calif)

            self.calculo_promediop()
            self.le_calificacion.setText("")
            self.panel.setText(str(self.calificaciones))
        except:
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)
#---------------------------------------------------------------------------------------------------------------------
    def calculo_promediop(self):
        self.cont = 0

        self.promedio = 0

        for i in self.calificaciones:
            self.promedio += float(i)
            self.cont += 1
            self.le_calificacionn.setText("Calificacion " + str(self.cont) + ":")
        self.promedio /= len(self.calificaciones)
        self.le_promedio.setText(str(self.promedio))
    def llenarCampos(self):
        self.calificaciones=[]
        print()
        valorspin = int(self.sp_grupo.value())

        # obtengo el alumno
        self.reg_alumno = self.grupo.get(valorspin, self.noesta)

        # obtengo sus campos
        self.nombre=self.reg_alumno.get('nombre',"null")
        #En caso de que no este me devuelva una lista vacia para que asi en el otro metodo
        #de agregar no me genere error al querer agregar uno
        self.reg_calific = self.reg_alumno.get('calificaciones',[])
        self.promedio=self.reg_alumno.get('promedio',"null")

        self.le_nombre.setText(str(self.nombre))
        self.le_promedio.setText(str(self.promedio))
        self.panel.setText(str(self.reg_calific))

        self.calificaciones = self.reg_calific
        self.le_calificacionn.setText(f"Calificacion {len(self.calificaciones)} :")

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, "Mensaje", "Salir", QtWidgets.QMessageBox.Yes,
                                           QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

qtCreatorFile3 = "prog7_subVentanaDialog_6i.ui" # Nombre del archivo

Ui_MainWindow3, QtBaseClass3 = uic.loadUiType(qtCreatorFile3)

class VentanaDialog(QtWidgets.QDialog, Ui_MainWindow3):
    def __init__(self): #constructor
        QtWidgets.QDialog.__init__(self) #crea la parte visual
        Ui_MainWindow3.__init__(self) #convierte el ui a codigo entendible en python
        self.setupUi(self) #carga el codigo convertido



if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())