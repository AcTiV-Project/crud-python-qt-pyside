# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(535, 580)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbldni = QLabel(self.centralwidget)
        self.lbldni.setObjectName(u"lbldni")

        self.verticalLayout.addWidget(self.lbldni)

        self.linedni = QLineEdit(self.centralwidget)
        self.linedni.setObjectName(u"linedni")
        self.linedni.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.linedni)

        self.lblnombre = QLabel(self.centralwidget)
        self.lblnombre.setObjectName(u"lblnombre")

        self.verticalLayout.addWidget(self.lblnombre)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.lineEdit)

        self.lblemail = QLabel(self.centralwidget)
        self.lblemail.setObjectName(u"lblemail")

        self.verticalLayout.addWidget(self.lblemail)

        self.lineemail = QLineEdit(self.centralwidget)
        self.lineemail.setObjectName(u"lineemail")
        self.lineemail.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.lineemail)

        self.lblrol = QLabel(self.centralwidget)
        self.lblrol.setObjectName(u"lblrol")

        self.verticalLayout.addWidget(self.lblrol)

        self.linerol = QLineEdit(self.centralwidget)
        self.linerol.setObjectName(u"linerol")
        self.linerol.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.linerol)

        self.btnnuevo = QPushButton(self.centralwidget)
        self.btnnuevo.setObjectName(u"btnnuevo")
        self.btnnuevo.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.btnnuevo)

        self.btnmodificar = QPushButton(self.centralwidget)
        self.btnmodificar.setObjectName(u"btnmodificar")
        self.btnmodificar.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.btnmodificar)

        self.btneliminar = QPushButton(self.centralwidget)
        self.btneliminar.setObjectName(u"btneliminar")
        self.btneliminar.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.btneliminar)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 535, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CRUD", None))
        self.lbldni.setText(QCoreApplication.translate("MainWindow", u"DNI", None))
        self.lblnombre.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.lblemail.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None))
        self.lblrol.setText(QCoreApplication.translate("MainWindow", u"ROL", None))
        self.btnnuevo.setText(QCoreApplication.translate("MainWindow", u"NUEVO", None))
        self.btnmodificar.setText(QCoreApplication.translate("MainWindow", u"MODIFICAR", None))
        self.btneliminar.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR", None))
    # retranslateUi

