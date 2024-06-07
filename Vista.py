import Controlador
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

class Vista(QtWidgets.QWidget):
    """
    Clase Vista encargada de la interfaz
    """
    def __init__(self):
        """
        Constructor de la clase Vista
        """
        super(Vista, self).__init__()
        
        self.initUI()

    def initUI(self):
        """
        Constructor de la UI
        """
        self.famortiguador_delantero = False
        self.famortiguador_trasero = False
        
        title = QtWidgets.QLabel("Bike Configurator", self)
        title.setFont(QtGui.QFont("Arial", 18, QtGui.QFont.Bold))

        cad = ("Bienvenido a Bike Configurator!\n"
               "Nos encargaremos de proporcionarte la mejor bicicleta posible adaptada a tus exigencias\n"
               "Los pasos a seguir son sencillos:\n\n"
               "- Introduce el precio máximo que deseas\n"
               "- Selecciona el tipo de bicicleta que quieres\n"
               "- Selecciona opciones extra\n"
               "Y por último pulsa Configurar")
        
        self.lbl = QtWidgets.QLabel("Introduce un presupuesto", self)
        self.lbl.setFont(QtGui.QFont("Arial", 14))

        self.le = QtWidgets.QLineEdit(self)
        self.le.setFont(QtGui.QFont("Arial", 12))
        
        self.combo = QtWidgets.QComboBox()
        self.combo.addItem("MTB")
        self.combo.addItem("Road")
        self.combo.addItem("Paseo")
        self.combo.currentTextChanged.connect(self.toggle_amortiguadores)
        self.combo.currentTextChanged.connect(self.update_precio_range)
        self.combo.setFont(QtGui.QFont("Arial", 12))

        self.precio_range = QtWidgets.QLabel("", self)
        self.precio_range.setFont(QtGui.QFont("Arial", 12))

        self.checkbox_AmortiguadorDelantero = QtWidgets.QCheckBox("Amortiguador Delantero", self)
        self.checkbox_AmortiguadorDelantero.setFont(QtGui.QFont("Arial", 12))
        self.checkbox_AmortiguadorDelantero.stateChanged.connect(self.cambiar)
        
        self.checkbox_AmortiguadorTrasero = QtWidgets.QCheckBox("Amortiguador Trasero", self)
        self.checkbox_AmortiguadorTrasero.setFont(QtGui.QFont("Arial", 12))
        self.checkbox_AmortiguadorTrasero.stateChanged.connect(self.cambiar)
        
        self.texto = QtWidgets.QTextEdit()
        self.texto.setFont(QtGui.QFont("Arial", 12))
        self.texto.setReadOnly(True)
        self.texto.setText(cad)
        
        self.AcceptButton = QtWidgets.QPushButton('Configurar', self)
        self.AcceptButton.setFont(QtGui.QFont("Arial", 12))
        self.AcceptButton.clicked.connect(self.activacion)
        
        self.ExitButton = QtWidgets.QPushButton('Salir', self)
        self.ExitButton.setFont(QtGui.QFont("Arial", 12))
        self.ExitButton.clicked.connect(self.close)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(title)
        layout.addWidget(self.lbl)
        layout.addWidget(self.le)
        layout.addWidget(self.combo)
        layout.addWidget(self.precio_range)
        layout.addWidget(self.checkbox_AmortiguadorDelantero)
        layout.addWidget(self.checkbox_AmortiguadorTrasero)
        layout.addWidget(self.texto)
        layout.addWidget(self.AcceptButton)
        layout.addWidget(self.ExitButton)
        
        self.setLayout(layout)
        self.setWindowTitle('Bike Configurator')
        self.setWindowIcon(QtGui.QIcon('icono.jpg'))
        self.setGeometry(100, 100, 800, 600)
        
        self.update_precio_range(self.combo.currentText())
        
        self.show()

    def cambiar(self):
        """
        Método para controlar las flags de los checkbox
        """
        self.famortiguador_delantero = self.checkbox_AmortiguadorDelantero.isChecked()
        self.famortiguador_trasero = self.checkbox_AmortiguadorTrasero.isChecked()

    def toggle_amortiguadores(self, text):
        """
        Método para mostrar/ocultar opciones de amortiguadores según el tipo de bicicleta
        """
        if text == "MTB":
            self.checkbox_AmortiguadorDelantero.show()
            self.checkbox_AmortiguadorTrasero.show()
        else:
            self.checkbox_AmortiguadorDelantero.hide()
            self.checkbox_AmortiguadorTrasero.hide()
            self.famortiguador_delantero = False
            self.famortiguador_trasero = False

    def update_precio_range(self, tipo):
        """
        Método para actualizar el rango de precios según el tipo de bicicleta
        """
        if tipo == "MTB":
            self.precio_range.setText("Para bicicletas de tipo MTB disponemos de opciones a partir de 380€")
        elif tipo == "Road":
            self.precio_range.setText("Para bicicletas de tipo Road disponemos de opciones a partir de 565€")
        elif tipo == "Paseo":
            self.precio_range.setText("Para bicicletas de tipo Paseo disponemos de opciones a partir de 455€")

    def activacion(self):
        """
        Método que controla la activación de los checkbox.
        """
        tipo = self.combo.currentText()
        precio = self.le.text()
        
        if not precio.isdigit() or int(precio) <= 0:
            self.texto.setText("Error: Por favor, introduce un presupuesto válido.")
            return
        
        configurado = Controlador.control(precio, tipo, self.famortiguador_delantero, self.famortiguador_trasero)
        self.texto.setText(configurado)

def main():

    app = QtWidgets.QApplication(sys.argv)
    ex = Vista()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
