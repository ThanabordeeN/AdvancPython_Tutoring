from base import Ui_MainWindow
from PyQt5 import QtWidgets
import time
import os
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

class Ui_MainWindow(Ui_MainWindow):
   def __init__(self):
      super().setupUi(MainWindow)
      self.setupSignals()
   
   def setupSignals(self):
      self.recordButton.clicked.connect(self.record)
      
   def record(self):
      self.save_file()
      
   def save_file(self):
      name = self.nameInput.toPlainText()
      surname = self.surName.toPlainText()
      student_id = self.studentID.toPlainText()
      path = self.pathEditor.toPlainText()
      file_name = self.fileName.toPlainText()
      formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
      os.makedirs(os.path.dirname(path), exist_ok=True)
      file_path = path + "/" + file_name + ".csv"
      with open(file_path, "w", encoding="utf-8") as file:
         file.write(f"Name , Surname, Student ID, Time\n")
         file.write(f"{name}, {surname}, {student_id}, {formatted_time}\n")

   

if __name__ == "__main__":
    ui = Ui_MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())