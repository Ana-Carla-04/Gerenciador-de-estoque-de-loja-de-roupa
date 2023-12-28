
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


class Ui_tl_adicionar(object):
    def setupUi(self, tl_adicionar):
        tl_adicionar.setObjectName("tl_adicionar")
        tl_adicionar.resize(800, 600)
        tl_adicionar.setFixedSize(tl_adicionar.size())
        tl_adicionar.setStyleSheet("background-color: rgb(195, 187, 255);")
        self.centralwidget = QtWidgets.QWidget(tl_adicionar)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 20, 231, 51))
        self.label.setStyleSheet("font: 22pt \"Tw Cen MT Condensed Extra Bold\";")
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(160, 90, 491, 351))
        self.groupBox.setStyleSheet("\n"
"background-color: rgb(226, 221, 255);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 111, 31))
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
        self.caixa_quantidade = QtWidgets.QSpinBox(self.groupBox)
        self.caixa_quantidade.setGeometry(QtCore.QRect(220, 60, 221, 22))
        self.caixa_quantidade.setObjectName("caixa_quantidade")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 25 10pt \"Perpetua Titling MT\";")
        self.label_3.setObjectName("label_3")
        self.caixa_data = QtWidgets.QDateEdit(self.groupBox)
        self.caixa_data.setGeometry(QtCore.QRect(220, 100, 221, 22))
        self.caixa_data.setObjectName("caixa_data")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(40, 150, 151, 16))
        self.label_4.setStyleSheet("font: 25 10pt \"Perpetua Titling MT\";")
        self.label_4.setObjectName("label_4")
        self.caixa_tamanho = QtWidgets.QComboBox(self.groupBox)
        self.caixa_tamanho.setGeometry(QtCore.QRect(220, 150, 221, 22))
        self.caixa_tamanho.setObjectName("caixa_tamanho")
        self.caixa_tamanho.addItem("")
        self.caixa_tamanho.addItem("")
        self.caixa_tamanho.addItem("")
        self.caixa_tamanho.addItem("")
        self.caixa_tamanho.addItem("")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(40, 190, 91, 21))
        self.label_5.setStyleSheet("font: 25 10pt \"Perpetua Titling MT\";")
        self.label_5.setObjectName("label_5")
        self.caixa_tipo = QtWidgets.QComboBox(self.groupBox)
        self.caixa_tipo.setGeometry(QtCore.QRect(220, 190, 221, 21))
        self.caixa_tipo.setObjectName("caixa_tipo")
        self.caixa_tipo.addItem("")
        self.caixa_tipo.addItem("")
        self.caixa_tipo.addItem("")
        self.caixa_tipo.addItem("")
        self.caixa_tipo.addItem("")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(40, 240, 47, 13))
        self.label_6.setStyleSheet("font: 25 10pt \"Perpetua Titling MT\";")
        self.label_6.setObjectName("label_6")
        self.caixa_cor = QtWidgets.QComboBox(self.groupBox)
        self.caixa_cor.setGeometry(QtCore.QRect(220, 240, 221, 22))
        self.caixa_cor.setObjectName("caixa_cor")
        self.caixa_cor.addItem("")
        self.caixa_cor.addItem("")
        self.caixa_cor.addItem("")
        self.caixa_cor.addItem("")
        self.caixa_cor.addItem("")
        self.caixa_cor.addItem("")
        self.caixa_cor.addItem("")
        self.caixa_cor.addItem("")
        self.caixa_cor.addItem("")
        self.caixa_cor.addItem("")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(40, 290, 111, 16))
        self.label_7.setStyleSheet("font: 25 10pt \"Perpetua Titling MT\";")
        self.label_7.setObjectName("label_7")
        self.caixa_estampa = QtWidgets.QComboBox(self.groupBox)
        self.caixa_estampa.setGeometry(QtCore.QRect(218, 290, 221, 22))
        self.caixa_estampa.setObjectName("caixa_estampa")
        self.caixa_estampa.addItem("")
        self.caixa_estampa.addItem("")
        self.botao_voltar_principal = QtWidgets.QPushButton(self.centralwidget)
        self.botao_voltar_principal.setGeometry(QtCore.QRect(170, 470, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.botao_voltar_principal.setFont(font)
        self.botao_voltar_principal.setStyleSheet("QPushButton{background-color: rgb(177, 138, 225);\n"
"border-radius: 20px 20px 20px;}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(193, 102, 216);\n"
"border-radius: 20px 20px 20px;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/tela adicionar/go-back-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_voltar_principal.setIcon(icon)
        self.botao_voltar_principal.setObjectName("botao_voltar_principal")
        self.botao_adicionar_final = QtWidgets.QPushButton(self.centralwidget)
        self.botao_adicionar_final.setGeometry(QtCore.QRect(530, 470, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.botao_adicionar_final.setFont(font)
        self.botao_adicionar_final.setStyleSheet("QPushButton{background-color: rgb(177, 138, 225);\n"
"border-radius: 20px 20px 20px;}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(193, 102, 216);\n"
"border-radius: 20px 20px 20px;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/tela adicionar/mais (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_adicionar_final.setIcon(icon1)
        self.botao_adicionar_final.setObjectName("botao_adicionar_final")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(230, 20, 47, 51))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("image/tela adicionar/roupas.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        tl_adicionar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(tl_adicionar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        tl_adicionar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(tl_adicionar)
        self.statusbar.setObjectName("statusbar")
        tl_adicionar.setStatusBar(self.statusbar)

        self.retranslateUi(tl_adicionar)
        QtCore.QMetaObject.connectSlotsByName(tl_adicionar)

    def retranslateUi(self, tl_adicionar):
        _translate = QtCore.QCoreApplication.translate
        tl_adicionar.setWindowTitle(_translate("tl_adicionar", "Gerenciamento de Loja de Roupas - Adicionar"))
        self.label.setText(_translate("tl_adicionar", "Adicione o produto:"))
        self.label_2.setText(_translate("tl_adicionar", "<html><head/><body><p><span style=\" font-weight:600;\">Quantidade:</span></p></body></html>"))
        self.label_3.setText(_translate("tl_adicionar", "<html><head/><body><p><span style=\" font-weight:600;\">Data de inserção:</span></p></body></html>"))
        self.label_4.setText(_translate("tl_adicionar", "<html><head/><body><p><span style=\" font-weight:600;\">Tamanho da peça:</span></p></body></html>"))
        self.caixa_tamanho.setItemText(0, _translate("tl_adicionar", "PP"))
        self.caixa_tamanho.setItemText(1, _translate("tl_adicionar", "P"))
        self.caixa_tamanho.setItemText(2, _translate("tl_adicionar", "M"))
        self.caixa_tamanho.setItemText(3, _translate("tl_adicionar", "G"))
        self.caixa_tamanho.setItemText(4, _translate("tl_adicionar", "GG"))
        self.label_5.setText(_translate("tl_adicionar", "<html><head/><body><p><span style=\" font-weight:600;\">Tipo:</span></p></body></html>"))
        self.caixa_tipo.setItemText(0, _translate("tl_adicionar", "Camiseta"))
        self.caixa_tipo.setItemText(1, _translate("tl_adicionar", "Calça"))
        self.caixa_tipo.setItemText(2, _translate("tl_adicionar", "Short"))
        self.caixa_tipo.setItemText(3, _translate("tl_adicionar", "Saia"))
        self.caixa_tipo.setItemText(4, _translate("tl_adicionar", "Vestido"))
        self.label_6.setText(_translate("tl_adicionar", "<html><head/><body><p><span style=\" font-weight:600;\">Cor:</span></p></body></html>"))
        self.caixa_cor.setItemText(0, _translate("tl_adicionar", "Azul"))
        self.caixa_cor.setItemText(1, _translate("tl_adicionar", "Roxo"))
        self.caixa_cor.setItemText(2, _translate("tl_adicionar", "Rosa"))
        self.caixa_cor.setItemText(3, _translate("tl_adicionar", "Amarelo"))
        self.caixa_cor.setItemText(4, _translate("tl_adicionar", "Laranja"))
        self.caixa_cor.setItemText(5, _translate("tl_adicionar", "Verde"))
        self.caixa_cor.setItemText(6, _translate("tl_adicionar", "Vermelho"))
        self.caixa_cor.setItemText(7, _translate("tl_adicionar", "Preto"))
        self.caixa_cor.setItemText(8, _translate("tl_adicionar", "Branco"))
        self.caixa_cor.setItemText(9, _translate("tl_adicionar", "Marrom"))
        self.label_7.setText(_translate("tl_adicionar", "<html><head/><body><p><span style=\" font-weight:600;\">Estampada:</span></p></body></html>"))
        self.caixa_estampa.setItemText(0, _translate("tl_adicionar", "Sim"))
        self.caixa_estampa.setItemText(1, _translate("tl_adicionar", "Não"))
        self.botao_voltar_principal.setText(_translate("tl_adicionar", "Voltar"))
        self.botao_adicionar_final.setText(_translate("tl_adicionar", "Adicionar"))
        self.botao_adicionar_final.clicked.connect(self.adicinar_peca)
        self.botao_voltar_principal.clicked.connect(self.abrir_tela_principal)
        self.botao_voltar_principal.clicked.connect(tl_adicionar.close)


    #função de voltar a tela principal
    def abrir_tela_principal(self):
        from tela_principal import Ui_tl_prinicipal
        self.janela = QtWidgets.QWidget()
        self.abrir = Ui_tl_prinicipal()
        self.abrir.setupUi(self.janela)
        self.janela.show()


    #função de inserir uma nova peça no banco de dados
    def adicinar_peca(self):
        #usa o que foi colocado na caixa de texto para se referir a coluna quantidade no banco de dados
        quantidade = self.caixa_quantidade.value()

        #usa o que foi colocado na caixa de texto para se referir a coluna tamanho da peca no banco de dados
        tamanho_da_peca = self.caixa_tamanho.currentText()

        #usa o que foi colocado na caixa de texto para se referir a coluna tipo no banco de dados
        tipo = self.caixa_tipo.currentText()

        #usa o que foi colocado na caixa de texto para se referir a coluna cor no banco de dados
        cor = self.caixa_cor.currentText()

        #usa o que foi colocado na caixa de texto para se referir a coluna estampa no banco de dados
        estampa = self.caixa_estampa.currentText()

        #garante que na caixa de texto de quantidade, o valor inserido seja um numero inteiro
        if int(quantidade) == 0:
            QtWidgets.QMessageBox.warning(None, "Aviso", "A quantidade deve ser um número inteiro maior que zero.")
            return

        quantidade = int(quantidade)

        try:
            #condição onde define se é uma data valida
            data_de_insercao = self.caixa_data.date().toPyDate()
            if not (
                    1 <= data_de_insercao.day <= 31 and 1 <= data_de_insercao.month <= 12 and data_de_insercao.year != 0):

                #se a data n for valida aparecer uma mensagem avisando
                QtWidgets.QMessageBox.warning(None, "Aviso", "Data de inserção inválida.")
                return
        except ValueError:
            QtWidgets.QMessageBox.warning(None, "Aviso", "Data de inserção inválida.")
            return

        try:
            #conexão com o banco de dados
            conexao = pymysql.Connect(
                host='localhost',
                user='root',
                password='',
                autocommit= True,
                database='Loja_Roupa'
            )

            cursor = conexao.cursor()

            #usado para verificar se o produto ja existe no banco de dados
            cursor.execute('''SELECT * FROM estoque 
                                      WHERE quantidade=%s AND data_de_insercao=%s AND tamanho_da_peca=%s AND tipo=%s AND cor=%s AND estampa=%s''',
                           (quantidade, data_de_insercao, tamanho_da_peca, tipo, cor, estampa))

            if cursor.fetchone():
                QtWidgets.QMessageBox.warning(None, "Aviso", "Produto já existente no sistema.")
            else:
                # Insere o produto se não existir
                cursor.execute('''INSERT INTO estoque (quantidade, data_de_insercao, tamanho_da_peca, tipo, cor, estampa )
                                        VALUES (%s,%s,%s,%s,%s,%s)''',
                               (quantidade, data_de_insercao, tamanho_da_peca, tipo, cor, estampa))

                #se der tudo certo avisará com uma mensagem
                conexao.commit()
                QtWidgets.QMessageBox.information(None, "Sucesso", "Adicionado com sucesso!")

        #se der tudo errado avisará com outra mensagem
        except pymysql.Error as e:
            QtWidgets.QMessageBox.critical(None, "Erro", f"Erro ao adicionar peça: {str(e)}")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tl_adicionar = QtWidgets.QMainWindow()
    ui = Ui_tl_adicionar()
    ui.setupUi(tl_adicionar)
    tl_adicionar.show()
    sys.exit(app.exec_())
