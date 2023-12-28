
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_tl_excluir(object):
    def setupUi(self, tl_excluir):
        tl_excluir.setObjectName("tl_excluir")
        tl_excluir.resize(580, 524)
        tl_excluir.setFixedSize(tl_excluir.size())
        tl_excluir.setStyleSheet("background-color: rgb(195, 187, 255);")
        self.centralwidget = QtWidgets.QWidget(tl_excluir)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 40, 181, 81))
        self.label.setStyleSheet("font: 22pt \"Tw Cen MT Condensed Extra Bold\";")
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(140, 160, 321, 161))
        self.groupBox.setStyleSheet("\n"
"background-color: rgb(226, 221, 255);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(40, 20, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font: 25 10pt \"Perpetua Titling MT\";\n"
"")
        self.label_9.setObjectName("label_9")
        self.excluir_id = QtWidgets.QLineEdit(self.groupBox)
        self.excluir_id.setGeometry(QtCore.QRect(80, 30, 201, 20))
        self.excluir_id.setObjectName("excluir_id")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 281, 91))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.botao_excluir_voltar_principal = QtWidgets.QPushButton(self.centralwidget)
        self.botao_excluir_voltar_principal.setGeometry(QtCore.QRect(130, 380, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.botao_excluir_voltar_principal.setFont(font)
        self.botao_excluir_voltar_principal.setStyleSheet("QPushButton{background-color: rgb(177, 138, 225);\n"
"border-radius: 20px 20px 20px;}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(193, 102, 216);\n"
"border-radius: 20px 20px 20px;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/tela excluir/go-back-arrow (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_excluir_voltar_principal.setIcon(icon)
        self.botao_excluir_voltar_principal.setObjectName("botao_excluir_voltar_principal")
        self.botao_excluir_final = QtWidgets.QPushButton(self.centralwidget)
        self.botao_excluir_final.setGeometry(QtCore.QRect(330, 380, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.botao_excluir_final.setFont(font)
        self.botao_excluir_final.setStyleSheet("QPushButton{background-color: rgb(177, 138, 225);\n"
"border-radius: 20px 20px 20px;}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(193, 102, 216);\n"
"border-radius: 20px 20px 20px;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/tela excluir/bin (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_excluir_final.setIcon(icon1)
        self.botao_excluir_final.setObjectName("botao_excluir_final")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(230, 20, 47, 51))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("roupas.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 60, 51, 41))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("image/tela excluir/delete.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        tl_excluir.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(tl_excluir)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 21))
        self.menubar.setObjectName("menubar")
        tl_excluir.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(tl_excluir)
        self.statusbar.setObjectName("statusbar")
        tl_excluir.setStatusBar(self.statusbar)

        self.retranslateUi(tl_excluir)
        QtCore.QMetaObject.connectSlotsByName(tl_excluir)

    def retranslateUi(self, tl_excluir):
        _translate = QtCore.QCoreApplication.translate
        tl_excluir.setWindowTitle(_translate("tl_excluir", "Gerenciamento de Loja de Roupas - Excluir"))
        self.label.setText(_translate("tl_excluir", "Excluir produto:"))
        self.label_9.setText(_translate("tl_excluir", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">ID:</span></p></body></html>"))
        self.label_3.setText(_translate("tl_excluir", "<html><head/><body><p align=\"center\">Antes de prosseguirmos com a exclusão do produto, precisamos confirmar se esta é realmente sua decisão. A exclusão removerá permanentemente todas as informações associadas. Por favor, confirme sua escolha. </p></body></html>"))
        self.botao_excluir_voltar_principal.setText(_translate("tl_excluir", " Voltar"))
        self.botao_excluir_final.setText(_translate("tl_excluir", " EXCLUIR"))

        #botão ultilizado para abrir a tela principal
        self.botao_excluir_voltar_principal.clicked.connect(self.abrir_tela_principal)
        #mesmo botão tambem usado para fecha a tela excluir
        self.botao_excluir_voltar_principal.clicked.connect(tl_excluir.close)

        #botão que exclui a peça do banco de dados
        self.botao_excluir_final.clicked.connect(self.excluir_peca)

    #função a que vai para a tela principal
    def abrir_tela_principal(self):
        from tela_principal import Ui_tl_prinicipal
        self.janela = QtWidgets.QWidget()
        self.abrir = Ui_tl_prinicipal()
        self.abrir.setupUi(self.janela)
        self.janela.show()

    #função que exclui os dados daquela peça do banco de dados
    def excluir_peca(self):
        Id = self.excluir_id.text()

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

            #verifica se o id existe
            cursor.execute("SELECT COUNT(*) FROM estoque WHERE Id = %s", (Id,))
            resultado = cursor.fetchone()

            if resultado[0] == 0:
                QtWidgets.QMessageBox.warning(None, "Aviso", "ID não encontrado no sistema.")
                return

                # Excluir a peça se o ID existir
            cursor.execute("DELETE FROM estoque WHERE Id = %s", (Id,))

            #se sucesso exibir uma mensagem
            QtWidgets.QMessageBox.information(None, "Sucesso", "Item excluído com sucesso!")

            #se der errado exibir outra mensagem
        except pymysql.Error as e:

            QtWidgets.QMessageBox.critical(None, "Erro", f"Erro ao excluir item: {str(e)}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tl_excluir = QtWidgets.QMainWindow()
    ui = Ui_tl_excluir()
    ui.setupUi(tl_excluir)
    tl_excluir.show()
    sys.exit(app.exec_())
