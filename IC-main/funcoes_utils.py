#Criei este arquivo para simplesmente colocar aqui algumas funções que eu julgo como uteis

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QMessageBox


#Criar uma janela
def windowCreate(window, width, height, title):
    window.resize(width, height)
    window.setMinimumSize(QSize(width, height))
    window.setMaximumSize(QSize(width, height))
    window.setWindowTitle(title)

#Definindo a fonte que iremos utilizar
def fontCreate():
    font = QFont()
    font.setPointSize(13)
    return font


def showMessageError(erro):
    msg = QMessageBox()
    if erro == 1:
        msg.setText("ERROR: Insira um valor de amostragem!")
        msg.setIcon(msg.Icon.Critical)
        msg.exec()
    elif erro == 2:
        msg.setText("ERROR: É preciso iniciar um experimento antes!")
        msg.setIcon(msg.Icon.Critical)
        msg.exec()

