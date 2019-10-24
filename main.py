from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import math
import time

class JanelaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        
        w = QWidget()
        l = QVBoxLayout()
        w.setLayout(l)

        self.label =QLabel()
        self.canvas = QPixmap(400, 300)
        self.label.setPixmap(self.canvas)

        self.buttonPonto = QPushButton('Adicionar Ponto')
        self.buttonPonto.clicked.connect(self.on_buttonPonto_clicked)

        self.buttonLinhas = QPushButton('Adicionar Linhas')
        self.buttonLinhas.clicked.connect(self.desenhaLinhas)


        self.button = QPushButton('Limpar')
        self.button.clicked.connect(self.on_button_clicked)


        l.addWidget(self.buttonPonto)
        l.addWidget(self.buttonLinhas)
        l.addWidget(self.button)
        l.addWidget(self.label)

        self.setCentralWidget(w)
        self.desenhaLinhas()

        
    def desenhaLinhas(self):
        from random import randint
        pen = QPen()
        pen.setWidth(3)
            
        
        painter = QPainter(self.label.pixmap())
        
        painter.fillRect(0,0,400,300,QColor('white'))
        painter.setPen(pen)
        
        #100,50

        xOri = 200
        yOri = 150

        for a in range(360):
            hip = randint(0,100)
            
            x= xOri + (math.cos(a)*hip)
            y = yOri + (math.sin(a)*hip)
            
            if(hip > 70):
                pen.setColor(QColor('red'))
            else:
                pen.setColor(QColor('blue'))
            
            painter.setPen(pen)
            painter.drawLine(xOri,yOri,x,y)

        
        painter.end()

        self.label.repaint()



    def on_buttonPonto_clicked(self):
        from random import randint

        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor('black'))
        painter = QPainter(self.label.pixmap())
        painter.setPen(pen)
        painter.drawPoint(200+randint(-100, 100), 150+randint(-100, 100))
        painter.end()
        self.label.repaint()

    def on_button_clicked(self):

        painter = QPainter(self.label.pixmap())
        painter.fillRect(0,0,400,300,QColor('white'))
        painter.end()
        self.label.repaint()

if __name__=='__main__':

    app = QApplication([])

    principal = JanelaPrincipal()
    principal.show()

    app.exec_()