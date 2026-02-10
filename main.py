import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from interfaces.home import Ui_MainWindow 
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QAbstractItemView
from utils.conexion_db import conectar

class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableView.setSelectionMode(QAbstractItemView.SingleSelection)

        self.id_seleccionado = None #metodo de seleccion de id

        #Conectar a la BD
        self.db = conectar()
        self.cursor = self.db.cursor()

        #Crear el modelo
        self.modelo = QStandardItemModel()
        self.ui.tableView.setModel(self.modelo)

        #Cargar datos (AHORA sí)
        self.cargar_datos()

        #Conectar eventos
        self.eventos()

    def eventos(self):
        self.ui.btnnuevo.clicked.connect(self.nuevo)
        self.ui.btnmodificar.clicked.connect(self.modificar)
        self.ui.btneliminar.clicked.connect(self.eliminar)
        self.ui.tableView.clicked.connect(self.fila_seleccionada) #señal para detectar seleccion en las row


    def nuevo(self):
        dni = self.ui.linedni.text()
        nombre = self.ui.lineEdit.text()
        email = self.ui.lineemail.text()
        rol = self.ui.linerol.text()

        sql = "INSERT INTO usuarios (dni, nombre, email, rol) VALUES (%s, %s, %s, %s)"
        valores = (dni, nombre, email, rol)

        self.cursor.execute(sql, valores)
        self.db.commit()
        self.cargar_datos()


        #LIMPIAR CAMPOS
        self.ui.linedni.clear()
        self.ui.lineEdit.clear()
        self.ui.lineemail.clear()
        self.ui.linerol.clear()

        print("Registro insertado")

    def fila_seleccionada(self, index):
        fila = index.row()

        id_item = self.modelo.item(fila, 0).text()
        dni = self.modelo.item(fila, 1).text()
        nombre = self.modelo.item(fila, 2).text()
        email = self.modelo.item(fila, 3).text()
        rol = self.modelo.item(fila, 4).text()

        self.id_seleccionado = id_item

        self.ui.linedni.setText(dni)
        self.ui.lineEdit.setText(nombre)
        self.ui.lineemail.setText(email)
        self.ui.linerol.setText(rol)


    def cargar_datos(self):
        self.modelo.clear()

        self.modelo.setHorizontalHeaderLabels([
            "ID", "DNI", "Nombre", "Email", "Rol"
        ])

        sql = "SELECT id, dni, nombre, email, rol FROM usuarios"
        self.cursor.execute(sql)
        registros = self.cursor.fetchall()

        for fila in registros:
            items = []
            for dato in fila:
                items.append(QStandardItem(str(dato)))
            self.modelo.appendRow(items)


    def modificar(self):
        if not self.id_seleccionado:
            print("Seleccione un registro")
            return

        dni = self.ui.linedni.text()
        nombre = self.ui.lineEdit.text()
        email = self.ui.lineemail.text()
        rol = self.ui.linerol.text()

        sql = """
            UPDATE usuarios
            SET dni=%s, nombre=%s, email=%s, rol=%s
            WHERE id=%s
        """
        valores = (dni, nombre, email, rol, self.id_seleccionado)

        self.cursor.execute(sql, valores)
        self.db.commit()
        self.cargar_datos()


    def eliminar(self):
        if not self.id_seleccionado:
            print("Seleccione un registro")
            return

        sql = "DELETE FROM usuarios WHERE id=%s"
        self.cursor.execute(sql, (self.id_seleccionado,))
        self.db.commit()
        self.cargar_datos()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Home()
    ventana.show()
    sys.exit(app.exec())
