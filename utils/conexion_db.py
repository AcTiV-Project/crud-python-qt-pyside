import sys
import mysql.connector

def conectar():
      return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="crud_qt"
      )