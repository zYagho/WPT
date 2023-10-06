#IMPORTS
from PyQt6.QtWidgets import (QWidget, QLabel, QStackedWidget,
                             QComboBox, QMainWindow, 
                             QPushButton, QMenuBar, QMenu)
from PyQt6.QtCore import QSize, QRect
from PyQt6.QtGui import QAction
from funcoes_utils import windowCreate, fontCreate
from aquisicao_de_sinais import AquisicaoDeSinais
from aquisicao_geracao_sinais import AquisicaoGerDeSinais
from varredura_frequencia import Varredura

font = fontCreate()

class FirstWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Criando a Janela
        windowCreate(self, 800, 600, "Escolha o Experimento")
    
        self.centralwidget = QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.stackWidget = QStackedWidget()

        #Label para o BackGround
        self.labelBackground = QLabel(parent=self.centralwidget)
        self.labelBackground.setGeometry(QRect(0, 0, 821, 600))
        self.labelBackground.setMinimumSize(QSize(800, 600))
        self.labelBackground.setStyleSheet("background-image: url(files/icon_wpt.png);")
        
        
        self.comboBoxSelExp = QComboBox(parent=self.centralwidget)
        self.comboBoxSelExp.setGeometry(QRect(180, 250, 171, 25))
        self.comboBoxSelExp.addItem("Aquisição de Sinais")
        self.comboBoxSelExp.addItem("Aquisição e Geração de Sinais")
        self.comboBoxSelExp.addItem("Varredura em Frequência")
        self.labelSelExp = QLabel(parent=self.centralwidget)
        self.labelSelExp.setGeometry(QRect(180, 230, 201, 17))
        self.labelSelExp.setFont(font)
        self.labelSelExp.setText("Selecione o Experimento")
        self.labelSelExp.setObjectName("labelSelExp")
        
        self.buttonConfirmar = QPushButton(parent=self.centralwidget)
        self.buttonConfirmar.setGeometry(QRect(420, 250, 89, 25))
        self.buttonConfirmar.setText("Confirmar")
        self.buttonConfirmar.setFont(font)
        self.buttonConfirmar.clicked.connect(self.openExper)
        self.buttonConfirmar.setObjectName("pushButton")
        
        #CONFIGURANDO O MENU
        self.menubar = QMenuBar(parent=self)
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")

        self.menuFile = QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuFile.setTitle("File")
        
        self.actionSalvar = QAction(parent=self)
        self.actionSalvar.setText("Salvar")
        self.actionSalvar.setObjectName("actionSalvar")
        
        self.actionExportar = QAction(parent=self)
        self.actionExportar.setText("Exportar")
        self.actionExportar.setObjectName("actionExportar")
        
        self.actionImportar = QAction(parent=self)
        self.actionImportar.setText("Importar")
        self.actionImportar.setObjectName("actionImportar")
        
        self.actionNovo = QAction(parent=self)
        self.actionNovo.setText("Novo")
        self.actionNovo.setObjectName("actionNovo")
        
        self.menuFile.addAction(self.actionNovo)
        self.menuFile.addAction(self.actionSalvar)
        self.menuFile.addAction(self.actionExportar)
        self.menuFile.addAction(self.actionImportar)
        
        self.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuFile.menuAction())


        self.stackWidget.addWidget(self.centralwidget)
        self.setCentralWidget(self.stackWidget)

    def openExper(self):
        experimento = self.comboBoxSelExp.currentText()

        if experimento == "Aquisição de Sinais":
            self.openAqS()
        elif experimento == "Aquisição e Geração de Sinais":
            self.openAqGS()
        elif experimento == "Varredura em Frequência":
            self.openVF()

    
    def openAqS(self):
        self.janelaAqS = AquisicaoDeSinais(self)
        self.stackWidget.addWidget(self.janelaAqS)
        self.setWindowTitle("Aquisição de Sinais")
        self.stackWidget.setCurrentWidget(self.janelaAqS)

    def openAqGS(self):
        self.janelaAqGS = AquisicaoGerDeSinais(self)
        self.stackWidget.addWidget(self.janelaAqGS)
        self.setWindowTitle("Aquisição e Geração de Sinais")
        self.stackWidget.setCurrentWidget(self.janelaAqGS)

    def openVF(self):
        self.janelaVF = Varredura(self)
        self.stackWidget.addWidget(self.janelaVF)
        self.setWindowTitle("Varredura em Frequência")
        self.stackWidget.setCurrentWidget(self.janelaVF)

    def openMainWindow(self):
        self.setWindowTitle("Escolhha o Experimento")
        self.stackWidget.setCurrentWidget(self.centralwidget)