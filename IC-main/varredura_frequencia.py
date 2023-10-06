#TELA DE AQUISIÇÃO DE SINAIS

#IMPORTS
from PyQt6.QtWidgets import (QWidget, QLabel, 
                             QComboBox, QMainWindow, 
                             QPushButton, QLineEdit, QHBoxLayout)
from PyQt6.QtCore import QSize, QRect
from PyQt6.QtGui import QIntValidator
from funcoes_utils import windowCreate, fontCreate, showMessageError
from graphic_control import GraphicController
from window_configGraph import ConfigGraph
from config_GeradorWindow import ConfigGerador

font = fontCreate()

class Varredura(QMainWindow):
    def __init__(self, parente=None):
        super().__init__()

        self.pai = parente
        windowCreate(self, 800, 600, "Varredura em Frequência")

        self.centralwidget = QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QRect(350, 510, 431, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        

        self.comboBoxStep = QComboBox(parent=self.centralwidget)
        self.comboBoxStep.setGeometry(QRect(21, 200, 91, 25))
        self.comboBoxStep.setFont(font)
        self.comboBoxStep.addItem("2")
        self.comboBoxStep.addItem("4")
        self.comboBoxStep.addItem("6")
        self.comboBoxStep.addItem("8")
        self.comboBoxStep.addItem("10")

        self.graphicsView = GraphicController(parent=self.centralwidget)
        self.graphicsView.setGeometry(QRect(220, 30, 561, 431))
        self.graphicsView.setAutoFillBackground(False)
        self.graphicsView.setInteractive(True)
       
        self.lineEditAmostragem = QLineEdit(parent=self.centralwidget)
        self.lineEditAmostragem.setGeometry(QRect(21, 60, 99, 25))
        
        self.buttonIniciar = QPushButton(parent=self.layoutWidget)
        self.buttonIniciar.setFont(font)
        self.buttonIniciar.clicked.connect(self.iniButton)
        self.horizontalLayout.addWidget(self.buttonIniciar)
        self.buttonIniciar.setText("Iniciar")

        
        self.buttonPausar = QPushButton(parent=self.layoutWidget)
        self.buttonPausar.setFont(font)
        self.buttonPausar.setText("Pausar")
        self.horizontalLayout.addWidget(self.buttonPausar)
        
        self.buttonZerar = QPushButton(parent=self.layoutWidget)
        self.buttonZerar.setFont(font)
        self.buttonZerar.setText("Zerar")
        self.horizontalLayout.addWidget(self.buttonZerar)
        
        self.buttonConfigGraph = QPushButton(parent=self.layoutWidget)
        self.buttonConfigGraph.setFont(font)
        self.buttonConfigGraph.clicked.connect(self.openWindowConfigGraph)
        self.buttonConfigGraph.setText("Cfg.Graph")
        self.horizontalLayout.addWidget(self.buttonConfigGraph)


        self.buttonVoltar = QPushButton(parent=self.centralwidget)
        self.buttonVoltar.setGeometry(QRect(20, 510, 99, 28))
        self.buttonVoltar.setFont(font)
        self.buttonVoltar.clicked.connect(self.openPJ)
        self.buttonVoltar.setText("Voltar")
        
        self.labelTempoStep = QLabel(parent=self.centralwidget)
        self.labelTempoStep.setGeometry(QRect(21, 180, 92, 20))
        self.labelTempoStep.setFont(font)
        self.labelTempoStep.setText("Step")


        self.labelCanais = QLabel(parent=self.centralwidget)
        self.labelCanais.setGeometry(QRect(21, 110, 50, 20))
        self.labelCanais.setFont(font)
        self.labelCanais.setText("Canais")
        self.labelCanais.setObjectName("labelCanais")

        self.comboBoxCanais = QComboBox(parent=self.centralwidget)
        self.comboBoxCanais.setGeometry(QRect(21, 130, 81, 25))
        self.comboBoxCanais.setFont(font)
        self.comboBoxCanais.addItem("1")
        self.comboBoxCanais.addItem("2")
        self.comboBoxCanais.addItem("3")

        self.labelAmostragem = QLabel(parent=self.centralwidget)
        self.labelAmostragem.setGeometry(QRect(21, 30, 99, 37))
        self.labelAmostragem.setFont(font)
        self.labelAmostragem.setText("Amostragem")

        self.buttonZoomIn = QPushButton(parent=self.centralwidget)
        self.buttonZoomIn.setGeometry(QRect(614, 470, 80, 28))
        self.buttonZoomIn.setFont(font)
        self.buttonZoomIn.clicked.connect(self.graphicsView.zoomIn)
        self.buttonZoomIn.setText("Zoom +")

        self.buttonZoomOut = QPushButton(parent=self.centralwidget)
        self.buttonZoomOut.setGeometry(QRect(700, 470, 80, 28))
        self.buttonZoomOut.setText("Zoom -")
        self.buttonZoomOut.clicked.connect(self.graphicsView.zoomOut)
        self.buttonZoomOut.setFont(font)

        
        self.lineEditFreqInicial = QLineEdit(parent=self.centralwidget)
        self.lineEditFreqInicial.setGeometry(QRect(21, 340, 99, 25))
        self.lineEditFreqInicial.setText("")

        self.labelFreqInicial = QLabel(parent=self.centralwidget)
        self.labelFreqInicial.setGeometry(QRect(21, 318, 88, 20))
        self.labelFreqInicial.setText("Freq. Inicial")
        self.labelFreqInicial.setFont(font)

        self.labelFreqFinal = QLabel(parent=self.centralwidget)
        self.labelFreqFinal.setGeometry(QRect(21, 392, 80, 20))
        self.labelFreqFinal.setFont(font)
        self.labelFreqFinal.setText("Freq. Final")

        self.lineEditFreqFinal = QLineEdit(parent=self.centralwidget)
        self.lineEditFreqFinal.setGeometry(QRect(21, 420, 99, 25))
        self.lineEditFreqFinal.setText("")
       
        self.labelAmplitude = QLabel(parent=self.centralwidget)
        self.labelAmplitude.setGeometry(QRect(21, 250, 81, 20)) 
        self.labelAmplitude.setObjectName("labelAmplitude")
        self.labelAmplitude.setText("Amplitude")
        self.labelAmplitude.setFont(font)

        self.lineEditAmplitude = QLineEdit(parent=self.centralwidget)
        self.lineEditAmplitude.setGeometry(QRect(21, 270, 99, 25))
        self.lineEditAmplitude.setText("")
        self.lineEditAmplitude.setObjectName("lineEditAmplitude")

        self.labelBackground = QLabel(parent=self.centralwidget)
        self.labelBackground.setGeometry(QRect(0, 0, 800, 600))
        self.labelBackground.setMinimumSize(QSize(800, 600))
        self.labelBackground.setMaximumSize(QSize(800, 600))
        self.labelBackground.setStyleSheet("background-image: url(files/icon_wpt.png);")
        self.labelBackground.setText("")
        
        self.labelBackground.raise_()
        self.labelFreqFinal.raise_()
        self.lineEditFreqInicial.raise_()
        self.comboBoxStep.raise_()
        self.labelAmostragem.raise_()
        self.lineEditAmostragem.raise_()
        self.comboBoxCanais.raise_()
        self.labelCanais.raise_()
        self.lineEditFreqFinal.raise_()
        self.labelFreqInicial.raise_()
        self.labelTempoStep.raise_()
        self.graphicsView.raise_()
        self.layoutWidget.raise_()
        self.buttonVoltar.raise_()
        self.buttonZoomOut.raise_()
        self.buttonZoomIn.raise_()
        self.buttonZoomIn.raise_()
        self.buttonZoomOut.raise_()
        self.labelAmplitude.raise_()
        self.lineEditAmplitude.raise_()
        self.setCentralWidget(self.centralwidget)


    def iniButton(self):
        # NESTA FUNÇÃO SERÁ ONDE PODERA SER FEITO O CONTROLE DOS DADOS VIA SERIAL E TAL, ASSIM QUE O USUÁRIO APERTAR O BOTÃO INICIAR 
        # ESTE CONTROLE IRÁ COMEÇAR
        valorAmostragem = self.lineEditAmostragem.text()
        # canalEscolhido = self.comboBoxCanais.currentText()
        # tempoExperimento = self.comboBoxTempoExp.currentText()
        
        
        if valorAmostragem == '':
            showMessageError(1)
        else: 
            self.graphicsView.graphUpdate(valorAmostragem)

        
    def openPJ(self):
        self.pai.openMainWindow()

    def openWindowConfigGraph(self):
        self.windowGraph = ConfigGraph(self.graphicsView)
        self.windowGraph.showWindow()