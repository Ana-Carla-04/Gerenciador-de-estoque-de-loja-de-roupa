#imports usados na tabela
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

#class objeto, gerador a partir de uma tela .ui
class Ui_tl_prinicipal(object):
    def setupUi(self, tl_prinicipal):
        tl_prinicipal.setObjectName("tl_prinicipal")
        tl_prinicipal.resize(782, 713)
        tl_prinicipal.setFixedSize(tl_prinicipal.size())
        tl_prinicipal.setStyleSheet("background-color: rgb(195, 187, 255);")

        self.label = QtWidgets.QLabel(tl_prinicipal)
        self.label.setGeometry(QtCore.QRect(242, 0, 551, 713))
        self.label.setStyleSheet("background-color: rgb(226, 221, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(tl_prinicipal)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 242, 713))
        self.label_2.setStyleSheet("background-color: rgb(195, 187, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(tl_prinicipal)
        self.label_3.setGeometry(QtCore.QRect(70, 20, 161, 31))
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(tl_prinicipal)
        self.label_4.setGeometry(QtCore.QRect(80, 50, 131, 41))
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.caixa_de_pesquisa = QtWidgets.QLineEdit(tl_prinicipal)
        self.caixa_de_pesquisa.setGeometry(QtCore.QRect(40, 130, 191, 20))
        self.caixa_de_pesquisa.setObjectName("caixa_de_pesquisa")
        self.label_5 = QtWidgets.QLabel(tl_prinicipal)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 21, 21))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("image/tela principal/search.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.check_quantidade = QtWidgets.QRadioButton(tl_prinicipal)
        self.check_quantidade.setGeometry(QtCore.QRect(30, 190, 131, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.check_quantidade.setFont(font)
        self.check_quantidade.setObjectName("check_quantidade")
        self.check_dataDeInsercao = QtWidgets.QRadioButton(tl_prinicipal)
        self.check_dataDeInsercao.setGeometry(QtCore.QRect(30, 240, 171, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.check_dataDeInsercao.setFont(font)
        self.check_dataDeInsercao.setObjectName("check_dataDeInsercao")
        self.check_tamanho = QtWidgets.QRadioButton(tl_prinicipal)
        self.check_tamanho.setGeometry(QtCore.QRect(30, 290, 171, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.check_tamanho.setFont(font)
        self.check_tamanho.setObjectName("check_tamanho")
        self.check_tipo = QtWidgets.QRadioButton(tl_prinicipal)
        self.check_tipo.setGeometry(QtCore.QRect(30, 340, 131, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.check_tipo.setFont(font)
        self.check_tipo.setObjectName("check_tipo")
        self.check_cor = QtWidgets.QRadioButton(tl_prinicipal)
        self.check_cor.setGeometry(QtCore.QRect(30, 390, 131, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.check_cor.setFont(font)
        self.check_cor.setObjectName("check_cor")
        self.check_estampa = QtWidgets.QRadioButton(tl_prinicipal)
        self.check_estampa.setGeometry(QtCore.QRect(30, 440, 131, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.check_estampa.setFont(font)
        self.check_estampa.setObjectName("check_estampa")
        self.botao_pesquisar = QtWidgets.QPushButton(tl_prinicipal)
        self.botao_pesquisar.setGeometry(QtCore.QRect(40, 490, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.botao_pesquisar.setFont(font)
        self.botao_pesquisar.setStyleSheet("QPushButton{\n"
"background-color: rgb(177, 138, 225);\n"
"border-radius: 20px 20px 20px}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(193, 102, 216);\n"
"border-radius: 20px 20px 20px;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/tela principal/mouse2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_pesquisar.setIcon(icon)
        self.botao_pesquisar.setObjectName("botao_pesquisar")
        self.label_6 = QtWidgets.QLabel(tl_prinicipal)
        self.label_6.setGeometry(QtCore.QRect(260, 10, 511, 551))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.botao_voltar_inicial = QtWidgets.QPushButton(tl_prinicipal)
        self.botao_voltar_inicial.setGeometry(QtCore.QRect(40, 620, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.botao_voltar_inicial.setFont(font)
        self.botao_voltar_inicial.setStyleSheet("QPushButton{\n"
"background-color: rgb(177, 138, 225);\n"
"border-radius: 20px 20px 20px}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(193, 102, 216);\n"
"border-radius: 20px 20px 20px;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/tela principal/go-back-arrow (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_voltar_inicial.setIcon(icon1)
        self.botao_voltar_inicial.setObjectName("botao_voltar_inicial")
        self.label_7 = QtWidgets.QLabel(tl_prinicipal)
        self.label_7.setGeometry(QtCore.QRect(10, 560, 231, 51))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("image/tela principal/dashed-line.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.botao_adicionar_inicial = QtWidgets.QPushButton(tl_prinicipal)
        self.botao_adicionar_inicial.setGeometry(QtCore.QRect(260, 610, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.botao_adicionar_inicial.setFont(font)
        self.botao_adicionar_inicial.setStyleSheet("QPushButton{\n"
"background-color: rgb(177, 138, 225);\n"
"border-radius: 20px 20px 20px}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(193, 102, 216);\n"
"border-radius: 20px 20px 20px;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image/tela principal/adicionar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_adicionar_inicial.setIcon(icon2)
        self.botao_adicionar_inicial.setObjectName("botao_adicionar_inicial")
        self.botao_atualizar_inicial = QtWidgets.QPushButton(tl_prinicipal)
        self.botao_atualizar_inicial.setGeometry(QtCore.QRect(430, 610, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.botao_atualizar_inicial.setFont(font)
        self.botao_atualizar_inicial.setStyleSheet("QPushButton{\n"
"background-color: rgb(177, 138, 225);\n"
"border-radius: 20px 20px 20px;}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(193, 102, 216);\n"
"border-radius: 20px 20px 20px;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("image/tela principal/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_atualizar_inicial.setIcon(icon3)
        self.botao_atualizar_inicial.setObjectName("botao_atualizar_inicial")
        self.botao_excluir_inicial = QtWidgets.QPushButton(tl_prinicipal)
        self.botao_excluir_inicial.setGeometry(QtCore.QRect(600, 610, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.botao_excluir_inicial.setFont(font)
        self.botao_excluir_inicial.setStyleSheet("QPushButton{\n"
"background-color: rgb(177, 138, 225);\n"
"border-radius: 20px 20px 20px;}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(193, 102, 216);\n"
"border-radius: 20px 20px 20px;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("image/tela principal/bin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_excluir_inicial.setIcon(icon4)
        self.botao_excluir_inicial.setObjectName("botao_excluir_inicial")
        self.label_8 = QtWidgets.QLabel(tl_prinicipal)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 61, 61))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("image/tela principal/search (1).png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.table_Widget = QtWidgets.QTableWidget(tl_prinicipal)
        self.table_Widget.setGeometry(QtCore.QRect(265, 21, 491, 531))
        self.table_Widget.setObjectName("table_Widget")
        self.table_Widget.setColumnCount(7)
        self.table_Widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_Widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Widget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Widget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Widget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Widget.setHorizontalHeaderItem(6, item)

        self.retranslateUi(tl_prinicipal)
        QtCore.QMetaObject.connectSlotsByName(tl_prinicipal)

    def retranslateUi(self, tl_prinicipal):
        _translate = QtCore.QCoreApplication.translate

        #nome do layout
        tl_prinicipal.setWindowTitle(_translate("tl_prinicipal", "Gerenciamento de Loja de Roupas"))

        self.label_3.setText(_translate("tl_prinicipal", "<html><head/><body><p><span style=\" font-size:18pt;\">Gerenciamento</span></p></body></html>"))
        self.label_4.setText(_translate("tl_prinicipal", "<html><head/><body><p><span style=\" font-size:18pt;\">de estoque</span></p></body></html>"))
        self.check_quantidade.setText(_translate("tl_prinicipal", "Quantidade"))
        self.check_dataDeInsercao.setText(_translate("tl_prinicipal", "Data de inserção"))
        self.check_tamanho.setText(_translate("tl_prinicipal", "Tamanho da peça"))
        self.check_tipo.setText(_translate("tl_prinicipal", "Tipo"))
        self.check_cor.setText(_translate("tl_prinicipal", "Cor"))
        self.check_estampa.setText(_translate("tl_prinicipal", "Estampa"))
        self.botao_pesquisar.setText(_translate("tl_prinicipal", " Pesquisar"))
        self.botao_voltar_inicial.setText(_translate("tl_prinicipal", "  Voltar"))
        self.botao_adicionar_inicial.setText(_translate("tl_prinicipal", " Adicionar"))
        self.botao_atualizar_inicial.setText(_translate("tl_prinicipal", " Atualizar"))
        self.botao_excluir_inicial.setText(_translate("tl_prinicipal", " Excluir"))
        item = self.table_Widget.horizontalHeaderItem(0)
        item.setText(_translate("tl_prinicipal", "ID"))
        item = self.table_Widget.horizontalHeaderItem(1)
        item.setText(_translate("tl_prinicipal", "Quantidade"))
        item = self.table_Widget.horizontalHeaderItem(2)
        item.setText(_translate("tl_prinicipal", "Data de inserção"))
        item = self.table_Widget.horizontalHeaderItem(3)
        item.setText(_translate("tl_prinicipal", "Tamanho"))
        item = self.table_Widget.horizontalHeaderItem(4)
        item.setText(_translate("tl_prinicipal", "Tipo"))
        item = self.table_Widget.horizontalHeaderItem(5)
        item.setText(_translate("tl_prinicipal", "Cor"))
        item = self.table_Widget.horizontalHeaderItem(6)
        item.setText(_translate("tl_prinicipal", "Estampa"))

        #botão usado para voltar para a tela inicial
        self.botao_voltar_inicial.clicked.connect(self.abrir_tela_inicial)
        #mesmo botão de voltar usado para  fechar a tela quando pular para a proxima janela
        self.botao_voltar_inicial.clicked.connect(tl_prinicipal.close)

        #botão usado para ir para tela adicionar
        self.botao_adicionar_inicial.clicked.connect(self.abri_tela_adicionar)
        #mesmo botão usado para  fechar a tela quando pular para a proxima janela
        self.botao_adicionar_inicial.clicked.connect(tl_prinicipal.close)

        #botão usado para ir para a tela atualizar
        self.botao_atualizar_inicial.clicked.connect(self.abri_tela_atualizar)
        # mesmo botão usado para  fechar a tela quando pular para a proxima janela
        self.botao_atualizar_inicial.clicked.connect(tl_prinicipal.close)

        #botão usado para ir para a  tela excluir
        self.botao_excluir_inicial.clicked.connect(self.abri_tela_excluir)
        # mesmo botão usado para  fechar a tela quando pular para a proxima janela
        self.botao_excluir_inicial.clicked.connect(tl_prinicipal.close)

        #comando onde puxa a função listar e inseri na tela
        self.listar_estoque()

        #botão usado para realizar pesquisa na tela
        self.botao_pesquisar.clicked.connect(self.realizar_pesquisa)

    #criar função listar pesquisa
    def realizar_pesquisa(self):
        try:
            #definindo o texto inserido na caixa de pesquisa como termo_pesquisa
            termo_pesquisa = self.caixa_de_pesquisa.text()

            #caso a caixa de pesquisa estiver vazia mostrar que a pesquisa não pode ser realizada
            if not termo_pesquisa:
                QtWidgets.QMessageBox.warning(None, "Aviso", "Digite um termo de pesquisa")

            #checa qual dos campos foi selecionado
            if self.check_quantidade.isChecked():
                campo_pesquisa = 'quantidade'
            elif self.check_dataDeInsercao.isChecked():
                campo_pesquisa = 'data_de_insercao'
            elif self.check_tamanho.isChecked():
                campo_pesquisa = 'tamanho_da_peca'
            elif self.check_tipo.isChecked():
                campo_pesquisa = 'tipo'
            elif self.check_cor.isChecked():
                campo_pesquisa = 'cor'
            elif self.check_estampa.isChecked():
                campo_pesquisa = 'estampa'
            else:
                #caso nenhum campo for selecionado avisar que não foi possivel realizar a pesquisa
                QtWidgets.QMessageBox.warning(None, "Aviso", "Selecione um critério de pesquisa.")


            #faz conexão com o banco de dados externo
            conexao = pymysql.Connect(
                host='localhost',
                user='root',
                password='',
                autocommit=True,
                database='Loja_Roupa')

            #cria o cursor
            cursor = conexao.cursor()

            #reliza a consulta dentro do banco de dados executando o cursor
            consulta_sql = f"SELECT * FROM estoque WHERE {campo_pesquisa} = %s"
            cursor.execute(consulta_sql, (termo_pesquisa))

            #exibi o resultado do cursor
            resultados = cursor.fetchall()

            #chama a função atualizar_tabela e execulta o resultado do cursor nela
            self.atualizar_tabela(resultados)

        #caso algo der errado mostrar o erro
        except Exception as e:
            QtWidgets.QMessageBox.warning(None, "Erro", f"Erro na pesquisa: {str(e)}")

        #fechar a execução
        finally:
            cursor.close()
            conexao.close()

    #criar uma função onde vai organizar as informações do banco de dados na tela visualizavel
    def atualizar_tabela(self, resultados):
        self.table_Widget.setRowCount(0)
        for linha, Loja_Roupa in enumerate(resultados):
            self.table_Widget.insertRow(linha)

            for coluna, estoque in enumerate(Loja_Roupa):
                item = QtWidgets.QTableWidgetItem(str(estoque))
                self.table_Widget.setItem(linha, coluna, item)


    #função onde direciona da tela princiapal para a tela incial
    def abrir_tela_inicial(self):
        #faz a ligação da tela que esta em outro documento
        from tela_inicial import Ui_tl_inicial
        self.janela = QtWidgets.QMainWindow()
        self.abrir = Ui_tl_inicial()
        self.abrir.setupUi(self.janela)
        #deixa visualizavel a tela
        self.janela.show()

    #função onde direciona a tela principal para  a tela adicionar
    def abri_tela_adicionar(self):
        from tela_adicionar import Ui_tl_adicionar
        self.janela = QtWidgets.QMainWindow()
        self.abrir = Ui_tl_adicionar()
        self.abrir.setupUi(self.janela)
        self.janela.show()

    # função onde direciona a tela principal para  a tela atualizar
    def abri_tela_atualizar(self):
        from tela_atualizar import Ui_tl_atualizar
        self.janela = QtWidgets.QMainWindow()
        self.abrir = Ui_tl_atualizar()
        self.abrir.setupUi(self.janela)
        self.janela.show()

    # função onde direciona a tela principal para  a tela excluir
    def abri_tela_excluir(self):
        from tela_excluir import Ui_tl_excluir
        self.janela = QtWidgets.QMainWindow()
        self.abrir = Ui_tl_excluir()
        self.abrir.setupUi(self.janela)
        self.janela.show()

    #função que lista o banco de dados ao abrir a tela
    def listar_estoque(self):
        #conexão com o banco de dados
        conexao = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            autocommit=True,
            database='Loja_Roupa'
        )

        cursor = conexao.cursor()

        listar = 'SELECT * FROM estoque'
        cursor.execute(listar)
        resultado = cursor.fetchall()
        self.table_Widget.setRowCount(0)

        for linha, Loja_Roupa in enumerate(resultado):
            self.table_Widget.insertRow(linha)

            for coluna, estoque in enumerate(Loja_Roupa):
                item = QtWidgets.QTableWidgetItem(str(estoque))
                self.table_Widget.setItem(linha, coluna, item)

        cursor.close()
        conexao.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tl_prinicipal = QtWidgets.QWidget()
    ui = Ui_tl_prinicipal()
    ui.setupUi(tl_prinicipal)
    tl_prinicipal.show()
    sys.exit(app.exec_())
