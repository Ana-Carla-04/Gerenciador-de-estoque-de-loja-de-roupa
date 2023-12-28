
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_tl_inicial(object):
    def setupUi(self, tl_inicial):
        tl_inicial.setObjectName("tl_inicial")

        tl_inicial.resize(800, 600)
        tl_inicial.setFixedSize(tl_inicial.size())
        tl_inicial.setStyleSheet("background-color: rgb(195, 187, 255);")
        self.centralwidget = QtWidgets.QWidget(tl_inicial)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 20, 541, 61))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 90, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(90, 43, 113);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 0, 161, 151))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("image/tela inicial/products.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.botao_acesso = QtWidgets.QPushButton(self.centralwidget)
        self.botao_acesso.setGeometry(QtCore.QRect(220, 280, 381, 91))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(14)
        self.botao_acesso.setFont(font)
        self.botao_acesso.setStyleSheet("QPushButton{\n"
"background-color: rgb(177, 138, 225);\n"
"border-radius: 20px 20px 20px;\n"
"box-shadow: 10px 5px 5px black;}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(193, 102, 216);\n"
"border-radius: 20px 20px 20px;\n"
"}")
        self.botao_acesso.setObjectName("botao_acesso")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 520, 51, 41))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("image/tela inicial/clothes-hanger.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 520, 51, 41))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("image/tela inicial/clothes-hanger.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(220, 520, 51, 41))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("image/tela inicial/clothes-hanger.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(280, 520, 51, 41))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("image/tela inicial/clothes-hanger.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(340, 520, 51, 41))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("image/tela inicial/clothes-hanger.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(400, 520, 51, 41))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("image/tela inicial/clothes-hanger.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(460, 520, 51, 41))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("image/tela inicial/clothes-hanger.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(520, 520, 51, 41))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("image/tela inicial/clothes-hanger.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(580, 520, 51, 41))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("image/tela inicial/clothes-hanger.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(640, 520, 51, 41))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("image/tela inicial/clothes-hanger.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(700, 520, 51, 41))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("image/tela inicial/clothes-hanger.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(760, 520, 51, 41))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("image/tela inicial/clothes-hanger.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(40, 520, 51, 41))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("image/tela inicial/clothes-hanger.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(-20, 520, 51, 41))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("image/tela inicial/clothes-hanger.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        tl_inicial.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(tl_inicial)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        tl_inicial.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(tl_inicial)
        self.statusbar.setObjectName("statusbar")
        tl_inicial.setStatusBar(self.statusbar)

        self.retranslateUi(tl_inicial)
        QtCore.QMetaObject.connectSlotsByName(tl_inicial)

    def retranslateUi(self, tl_inicial):
        _translate = QtCore.QCoreApplication.translate
        tl_inicial.setWindowTitle(_translate("tl_inicial", "Gerenciamento de Loja de Roupas"))
        self.label.setText(_translate("tl_inicial", "<html><head/><body><p><span style=\" font-size:36pt;\">SISTEMA DE GERENCIAMENTO</span></p></body></html>"))
        self.label_2.setText(_translate("tl_inicial", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">LOJA DE ROUPAS</span></p></body></html>"))
        self.botao_acesso.setText(_translate("tl_inicial", "ACESSAR GERENCIAMENTO"))

        #faz o botao de acesso abrir a tela principal
        self.botao_acesso.clicked.connect(self.abrir_tela_principal)
        #o mesmo botão faz a tela inicial fechar
        self.botao_acesso.clicked.connect(tl_inicial.close)





    #função onde vai da tela incial para a tela principal
    def abrir_tela_principal(self):
        from tela_principal import Ui_tl_prinicipal
        self.janela = QtWidgets.QWidget()
        self.abrir = Ui_tl_prinicipal()
        self.abrir.setupUi(self.janela)
        self.janela.show()






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tl_inicial = QtWidgets.QMainWindow()
    ui = Ui_tl_inicial()
    ui.setupUi(tl_inicial)
    tl_inicial.show()
    sys.exit(app.exec_())
