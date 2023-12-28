
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_tl_atualizar(object):
    def setupUi(self, tl_atualizar):
        tl_atualizar.setObjectName("tl_atualizar")
        tl_atualizar.resize(800, 600)
        tl_atualizar.setFixedSize(tl_atualizar.size())
        tl_atualizar.setStyleSheet("background-color: rgb(195, 187, 255);")
        self.centralwidget = QtWidgets.QWidget(tl_atualizar)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 30, 231, 51))
        self.label.setStyleSheet("font: 22pt \"Tw Cen MT Condensed Extra Bold\";")
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(160, 90, 491, 351))
        self.groupBox.setStyleSheet("\n"
"background-color: rgb(226, 221, 255);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 25 10pt \"Perpetua Titling MT\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.atualizar_quantidade = QtWidgets.QSpinBox(self.groupBox)
        self.atualizar_quantidade.setGeometry(QtCore.QRect(220, 120, 221, 22))
        self.atualizar_quantidade.setObjectName("atualizar_quantidade")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(40, 180, 151, 16))
        self.label_4.setStyleSheet("font: 25 10pt \"Perpetua Titling MT\";")
        self.label_4.setObjectName("label_4")
        self.atualizar_tamanho = QtWidgets.QComboBox(self.groupBox)
        self.atualizar_tamanho.setGeometry(QtCore.QRect(220, 180, 221, 22))
        self.atualizar_tamanho.setObjectName("atualizar_tamanho")
        self.atualizar_tamanho.addItem("")
        self.atualizar_tamanho.addItem("")
        self.atualizar_tamanho.addItem("")
        self.atualizar_tamanho.addItem("")
        self.atualizar_tamanho.addItem("")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(40, 240, 47, 13))
        self.label_6.setStyleSheet("font: 25 10pt \"Perpetua Titling MT\";")
        self.label_6.setObjectName("label_6")
        self.atualizar_cor = QtWidgets.QComboBox(self.groupBox)
        self.atualizar_cor.setGeometry(QtCore.QRect(220, 240, 221, 22))
        self.atualizar_cor.setObjectName("atualizar_cor")
        self.atualizar_cor.addItem("")
        self.atualizar_cor.addItem("")
        self.atualizar_cor.addItem("")
        self.atualizar_cor.addItem("")
        self.atualizar_cor.addItem("")
        self.atualizar_cor.addItem("")
        self.atualizar_cor.addItem("")
        self.atualizar_cor.addItem("")
        self.atualizar_cor.addItem("")
        self.atualizar_cor.addItem("")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(40, 60, 47, 13))
        self.label_9.setStyleSheet("font: 25 10pt \"Perpetua Titling MT\";")
        self.label_9.setObjectName("label_9")
        self.atualizar_id = QtWidgets.QLineEdit(self.groupBox)
        self.atualizar_id.setGeometry(QtCore.QRect(220, 60, 221, 20))
        self.atualizar_id.setObjectName("atualizar_id")
        self.botao_atualizar_voltar_principal = QtWidgets.QPushButton(self.centralwidget)
        self.botao_atualizar_voltar_principal.setGeometry(QtCore.QRect(170, 470, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.botao_atualizar_voltar_principal.setFont(font)
        self.botao_atualizar_voltar_principal.setStyleSheet("QPushButton{background-color: rgb(177, 138, 225);\n"
"border-radius: 20px 20px 20px;}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(193, 102, 216);\n"
"border-radius: 20px 20px 20px;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/tela atualizar/go-back-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_atualizar_voltar_principal.setIcon(icon)
        self.botao_atualizar_voltar_principal.setObjectName("botao_atualizar_voltar_principal")
        self.botao_atualizar_final = QtWidgets.QPushButton(self.centralwidget)
        self.botao_atualizar_final.setGeometry(QtCore.QRect(520, 470, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.botao_atualizar_final.setFont(font)
        self.botao_atualizar_final.setStyleSheet("QPushButton{background-color: rgb(177, 138, 225);\n"
"border-radius: 20px 20px 20px;}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(193, 102, 216);\n"
"border-radius: 20px 20px 20px;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/tela atualizar/atualizar (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_atualizar_final.setIcon(icon1)
        self.botao_atualizar_final.setObjectName("botao_atualizar_final")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(250, 30, 51, 51))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("image/tela atualizar/atualizar.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        tl_atualizar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(tl_atualizar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        tl_atualizar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(tl_atualizar)
        self.statusbar.setObjectName("statusbar")
        tl_atualizar.setStatusBar(self.statusbar)

        self.retranslateUi(tl_atualizar)
        QtCore.QMetaObject.connectSlotsByName(tl_atualizar)

    def retranslateUi(self, tl_atualizar):
        _translate = QtCore.QCoreApplication.translate
        tl_atualizar.setWindowTitle(_translate("tl_atualizar", "Gerenciamento de Loja de Roupas - Atualizar"))
        self.label.setText(_translate("tl_atualizar", "Atualizar produto:"))
        self.label_2.setText(_translate("tl_atualizar", "<html><head/><body><p><span style=\" font-weight:600;\">Quantidade:</span></p></body></html>"))
        self.label_4.setText(_translate("tl_atualizar", "<html><head/><body><p><span style=\" font-weight:600;\">Tamanho da peça:</span></p></body></html>"))
        self.atualizar_tamanho.setItemText(0, _translate("tl_atualizar", "PP"))
        self.atualizar_tamanho.setItemText(1, _translate("tl_atualizar", "P"))
        self.atualizar_tamanho.setItemText(2, _translate("tl_atualizar", "M"))
        self.atualizar_tamanho.setItemText(3, _translate("tl_atualizar", "G"))
        self.atualizar_tamanho.setItemText(4, _translate("tl_atualizar", "GG"))
        self.label_6.setText(_translate("tl_atualizar", "<html><head/><body><p><span style=\" font-weight:600;\">Cor:</span></p></body></html>"))
        self.atualizar_cor.setItemText(0, _translate("tl_atualizar", "Azul"))
        self.atualizar_cor.setItemText(1, _translate("tl_atualizar", "Roxo"))
        self.atualizar_cor.setItemText(2, _translate("tl_atualizar", "Rosa"))
        self.atualizar_cor.setItemText(3, _translate("tl_atualizar", "Amarelo"))
        self.atualizar_cor.setItemText(4, _translate("tl_atualizar", "Laranja"))
        self.atualizar_cor.setItemText(5, _translate("tl_atualizar", "Verde"))
        self.atualizar_cor.setItemText(6, _translate("tl_atualizar", "Vermelho"))
        self.atualizar_cor.setItemText(7, _translate("tl_atualizar", "Preto"))
        self.atualizar_cor.setItemText(8, _translate("tl_atualizar", "Branco"))
        self.atualizar_cor.setItemText(9, _translate("tl_atualizar", "Marrom"))
        self.label_9.setText(_translate("tl_atualizar", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">ID:</span></p></body></html>"))
        self.botao_atualizar_voltar_principal.setText(_translate("tl_atualizar", "Cancelar"))
        self.botao_atualizar_final.setText(_translate("tl_atualizar", "Atualizar"))

        #botao que abre a tela principal
        self.botao_atualizar_voltar_principal.clicked.connect(self.abrir_tela_principal)
        #mesmo botão usa para fechar a tela atualizar
        self.botao_atualizar_voltar_principal.clicked.connect(tl_atualizar.close)

        #botão que atualiza os dados inseridos na tela no banco de dados
        self.botao_atualizar_final.clicked.connect(self.atualizar_peca)

    #função de voltar para a tela principal
    def abrir_tela_principal(self):
        from tela_principal import Ui_tl_prinicipal
        self.janela = QtWidgets.QWidget()
        self.abrir = Ui_tl_prinicipal()
        self.abrir.setupUi(self.janela)
        self.janela.show()

    #função onde atualiza os dados do banco de dados
    def atualizar_peca(self):
        quantidade = self.atualizar_quantidade.value()
        tamanho_da_peca = self.atualizar_tamanho.currentText()
        cor = self.atualizar_cor.currentText()
        Id = self.atualizar_id.text()

        try:

            conexao = pymysql.Connect(
                host='localhost',
                user='root',
                password='',
                autocommit=True,
                database='Loja_Roupa'
            )

            cursor = conexao.cursor()

            # Verificar se o ID existe
            cursor.execute("SELECT COUNT(*) FROM estoque WHERE Id = %s", (Id,))
            resultado = cursor.fetchone()

            # Se o ID não existir, exibir uma mensagem e sair da função
            if resultado[0] == 0:
                QtWidgets.QMessageBox.warning(None, "Aviso", "ID não encontrado no sistema.")
                return
            #update nos dados do banco
            cursor.execute('''UPDATE estoque SET quantidade = %s, tamanho_da_peca = %s, cor = %s WHERE Id = %s''',
                           ( quantidade, tamanho_da_peca, cor, Id))

            # se tudo der certo avisar com uma mensagem na tela
            conexao.commit()
            QtWidgets.QMessageBox.information(None, "Sucesso", "Atualizado com sucesso!")

            #caso contrario, se der errado, avisar com outra mensagem na tela
        except pymysql.Error as e:
            QtWidgets.QMessageBox.critical(None, "Erro", f"Erro ao atualizar peça: {str(e)}")




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tl_atualizar = QtWidgets.QMainWindow()
    ui = Ui_tl_atualizar()
    ui.setupUi(tl_atualizar)
    tl_atualizar.show()
    sys.exit(app.exec_())
