from base import Ui_MainWindow
from PyQt5 import QtWidgets , QtCore
import time
import os
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()


class Ui_MainWindow(Ui_MainWindow):
   def __init__(self):
      super().setupUi(MainWindow)
      self.setupSignals()
      self.progressBar.setProperty("value", 0)
      self.timer = QtCore.QTimer()
      self.timer.timeout.connect(self.update_progress)
      
   def setupSignals(self):
      self.recordButton.clicked.connect(self.record)
      
   def record(self):
      self.progressBar.setProperty("value", 0)
      self.update_progress()
   
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
         
   def update_progress(self):
      current = self.progressBar.value()
      self.timer.start(100)  
      if current >= 100: 
         self.timer.stop()
         self.recordButton.setEnabled(True)
         self.progressBar.setProperty("value", 100)
         self.save_file()
      else:
         self.recordButton.setEnabled(False)
         self.progressBar.setProperty("value", current + (100/10))

if __name__ == "__main__":
    ui = Ui_MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())