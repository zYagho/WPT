# AQUI SERÁ FEITA TODA A CONFIGURAÇÃO DO GRÁFICO
#
#
#
import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class GraphicController(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.scene = QGraphicsScene()
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.fig)
        self.scene.addWidget(self.canvas)
        self.setScene(self.scene)
        self.zoomFactor = 0.2

    def graphUpdate(self, amostragem):
        x = np.linspace(0, (int)(amostragem), 100)
        y = np.sin(x)

        self.ax.clear()
        self.ax.plot(x,y)
        self.ax.set_xlabel("Amostragem")
        self.ax.set_ylabel("Y")

        self.canvas.draw()
        
    def gridController(self, on_off):
        if on_off == True:
            self.ax.grid(True)
        else:
            self.ax.grid(False)
        
    def changeColor(self, color):
        cor = ''
        if color == "vermelho":
            cor = "red"
        elif color == "verde":
            cor = "green"
        elif color == "azul":
            cor = "blue"
        else:
            cor = "yellow"
        line = self.ax.lines[0]
        line.set_color(cor)
        self.canvas.draw()
        

    def zoomIn(self):
        x_min, x_max = self.ax.get_xlim()
        y_min, y_max = self.ax.get_ylim()
        x_range = x_max - x_min
        y_range = y_max - y_min
        self.ax.set_xlim(x_min + x_range * self.zoomFactor, x_max - x_range * self.zoomFactor)
        self.ax.set_ylim(y_min + y_range * self.zoomFactor, y_max - y_range * self.zoomFactor)
        self.canvas.draw()

    def zoomOut(self):
        x_min, x_max = self.ax.get_xlim()
        y_min, y_max = self.ax.get_ylim()
        x_range = x_max - x_min
        y_range = y_max - y_min
        self.ax.set_xlim(x_min - x_range * self.zoomFactor, x_max + x_range * self.zoomFactor)
        self.ax.set_ylim(y_min - y_range * self.zoomFactor, y_max + y_range * self.zoomFactor)
        self.canvas.draw()
