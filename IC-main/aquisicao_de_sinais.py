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

font = fontCreate()

class AquisicaoDeSinais(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        #Criando a janela
        windowCreate(self, 800, 600, "Aquisição de Sinais")
        
        self.pai = parent
        self.centralwidget = QWidget()
        
        #Grafico
        self.graphicsView = GraphicController(parent=self.centralwidget)
        self.graphicsView.setGeometry(QRect(220, 10, 561, 431))
        self.graphicsView.setAutoFillBackground(False)
        self.graphicsView.setInteractive(True)
        
        #Amostragem
        self.lineEditAmostragem = QLineEdit(parent=self.centralwidget)
        self.lineEditAmostragem.setGeometry(QRect(20, 110, 113, 25))
        self.lineEditAmostragem.setValidator(QIntValidator())
        self.labelAmostragem = QLabel(parent=self.centralwidget)
        self.labelAmostragem.setGeometry(QRect(20, 90, 111, 17))
        self.labelAmostragem.setFont(fontCreate())
        self.labelAmostragem.setText("Amostragem")
        
        #Canais
        self.comboBoxCanais = QComboBox(parent=self.centralwidget)
        self.comboBoxCanais.setGeometry(QRect(20, 190, 111, 25))
        self.comboBoxCanais.addItem("1")
        self.comboBoxCanais.addItem("2")
        self.comboBoxCanais.addItem("3")
        self.labelCanais = QLabel(parent=self.centralwidget)
        self.labelCanais.setGeometry(QRect(20, 170, 81, 17))
        self.labelCanais.setFont(font)
        self.labelCanais.setText("Canais")
        
        #Tempo Experimento
        self.comboBoxTempoExp = QComboBox(parent=self.centralwidget)
        self.comboBoxTempoExp.setGeometry(QRect(20, 270, 111, 25))
        self.comboBoxTempoExp.addItem("2")
        self.comboBoxTempoExp.addItem("4")
        self.comboBoxTempoExp.addItem("6")
        self.comboBoxTempoExp.addItem("8")
        self.comboBoxTempoExp.addItem("10")
        self.labelExperi = QLabel(parent=self.centralwidget)
        self.labelExperi.setGeometry(QRect(20, 250, 191, 17))
        self.labelExperi.setText("Tempo Exp - (segundos)")
        self.labelExperi.setFont(font)
        
        #BackGround
        self.labelBackground = QLabel(parent=self.centralwidget)
        self.labelBackground.setGeometry(QRect(0, -20, 800, 600))
        self.labelBackground.setMinimumSize(QSize(800, 600))
        self.labelBackground.setMaximumSize(QSize(800, 600))
        self.labelBackground.setStyleSheet("background-image: url(files/icon_wpt.png);")
        self.labelBackground.setText("")

        #Criando os layouts para adicionar os botões
        self.layoutWidget = QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QRect(350, 490, 431, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.layoutWidget_2 = QWidget(parent=self.centralwidget)
        self.layoutWidget_2.setGeometry(QRect(620, 450, 161, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        
        #botão iniciar
        self.buttonIniciar = QPushButton(parent=self.layoutWidget)
        self.buttonIniciar.setFont(font)
        self.buttonIniciar.setText("Iniciar")
        self.buttonIniciar.clicked.connect(self.iniButton)
        self.horizontalLayout.addWidget(self.buttonIniciar)
        
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
        self.buttonConfigGraph.setText("Config.Graph")
        self.buttonConfigGraph.clicked.connect(self.openWindowConfigGraph)
        self.horizontalLayout.addWidget(self.buttonConfigGraph)

        
        self.buttonZoomIn = QPushButton(parent=self.layoutWidget_2)
        self.buttonZoomIn.setFont(font)
        self.buttonZoomIn.clicked.connect(self.graphicsView.zoomIn)
        self.buttonZoomIn.setText("Zoom +")
        self.horizontalLayout_2.addWidget(self.buttonZoomIn)

        self.buttonZoomOut = QPushButton(parent=self.layoutWidget_2)
        self.buttonZoomOut.setFont(font)
        self.buttonZoomOut.clicked.connect(self.graphicsView.zoomOut)
        self.buttonZoomOut.setText("Zoom -")
        self.horizontalLayout_2.addWidget(self.buttonZoomOut)

        self.buttonVoltar = QPushButton(parent=self.centralwidget)
        self.buttonVoltar.setGeometry(QRect(20, 490, 99, 28))
        self.buttonVoltar.setText("Voltar")
        self.buttonVoltar.clicked.connect(self.openPJ)
        self.buttonVoltar.setFont(font)

        #setando para tudo na janela ficar na frente da label de backGround
        self.labelBackground.raise_()
        self.layoutWidget.raise_()
        self.graphicsView.raise_()
        self.lineEditAmostragem.raise_()
        self.labelAmostragem.raise_()
        self.comboBoxCanais.raise_()
        self.labelCanais.raise_()
        self.comboBoxTempoExp.raise_()
        self.labelExperi.raise_()
        self.layoutWidget_2.raise_()
        self.buttonVoltar.raise_()

        self.setCentralWidget(self.centralwidget)
       

    def iniButton(self):
        # NESTA FUNÇÃO SERÁ ONDE PODERA SER FEITO O CONTROLE DOS DADOS VIA SERIAL E TAL, ASSIM QUE O USUÁRIO APERTAR O BOTÃO INICIAR 
        # ESTE CONTROLE IRÁ COMEÇAR
        valorAmostragem = self.lineEditAmostragem.text()
        canalEscolhido = self.comboBoxCanais.currentText()
        tempoExperimento = self.comboBoxTempoExp.currentText()
        
        
        if valorAmostragem == '':
            showMessageError(1)
        else: 
            self.graphicsView.graphUpdate(valorAmostragem)

        
    def openPJ(self):
        self.pai.openMainWindow()

    def openWindowConfigGraph(self):
        self.windowGraph = ConfigGraph(self.graphicsView)
        self.windowGraph.showWindow()