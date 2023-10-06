#AQUI ESTA A TELA DE CONFIGURAÇÕES DO GRAFICO QUE MAIS TARDE PODE SER MUITO UTIL

from PyQt6.QtCore import QSize, QRect
from PyQt6.QtWidgets import QDialog, QLabel, QComboBox, QPushButton, QHBoxLayout, QWidget, QCheckBox
from funcoes_utils import windowCreate, fontCreate

font = fontCreate()
class ConfigGraph(QDialog):
    def __init__(self, graphic):
        super().__init__()

        windowCreate(self, 400,300, "Config-Graph")

        self.graphicWindow = graphic        
        self.labelBackGround = QLabel(parent=self)
        self.labelBackGround.setGeometry(QRect(0, 0, 400, 300))
        self.labelBackGround.setMinimumSize(QSize(400, 300))
        self.labelBackGround.setStyleSheet("background-image: url(files/icon_Dialog.png);")
        
        self.checkBoxGrid = QCheckBox(parent=self)
        self.checkBoxGrid.setGeometry(QRect(30, 80, 92, 23))
        self.checkBoxGrid.setFont(font)
        self.checkBoxGrid.setText("Grid")
        self.labelGrid = QLabel(parent=self)
        self.labelGrid.setText("Adicionar Grid")
        self.labelGrid.setGeometry(QRect(20, 50, 111, 17))
        self.labelGrid.setFont(font)
        self.labelGrid.setObjectName("labelGrid")

        self.comboBoxCor = QComboBox(parent=self)
        self.comboBoxCor.setGeometry(QRect(20, 150, 101, 25))
        self.comboBoxCor.setFont(font)
        self.comboBoxCor.addItem("Vermelho")
        self.comboBoxCor.addItem("Azul")
        self.comboBoxCor.addItem("Verde")
        self.comboBoxCor.addItem("Amarelo")
        self.labelCor = QLabel(parent=self)
        self.labelCor.setGeometry(QRect(20, 130, 111, 17))
        self.labelCor.setFont(font)
        self.labelCor.setText("Alterar a Cor")

        self.widget = QWidget(parent=self)
        self.widget.setGeometry(QRect(220, 260, 168, 30))


        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        
        self.buttonAplicar = QPushButton(parent=self.widget)
        self.buttonAplicar.setFont(font)
        self.buttonAplicar.clicked.connect(self.apliButton)
        self.buttonAplicar.setText("Aplicar")
        self.horizontalLayout.addWidget(self.buttonAplicar)
        
        self.buttonCancelar = QPushButton(parent=self.widget)
        self.buttonCancelar.setFont(font)
        self.buttonCancelar.setText("Cancelar")
        self.buttonCancelar.clicked.connect(self.closeWindow)
        self.horizontalLayout.addWidget(self.buttonCancelar)

    
    def showWindow(self):
        self.exec()
    def closeWindow(self):
        self.close()
    
    def apliButton(self):
        corEscolhida = self.comboBoxCor.currentText()
        checkbox = self.checkBoxGrid.isChecked()
        self.graphicWindow.gridController(checkbox)
        self.graphicWindow.changeColor(corEscolhida.lower())
        self.closeWindow()
        