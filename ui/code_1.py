from base import Ui_MainWindow # import มาจากไฟล์ base.py UI ที่ถูกสร้างจาก pyuic5
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os 
import time # นำเข้า Library time

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()


class Code(Ui_MainWindow):
   def __init__(self):
      super().setupUi(MainWindow)
      self.ButtonSignal()
   
   def ButtonSignal(self):
      self.recordButton.clicked.connect(self.save_file)
      
   def save_file(self):
      name = self.nameInput.toPlainText()
      surname = self.surName.toPlainText()
      student_id = self.studentID.toPlainText()
      file_name = self.fileName.toPlainText()
      path = self.pathEditor.toPlainText()
      time_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) # ดึงเวลาปัจจุบัน
      print("Saving")

      os.makedirs(path, exist_ok=True)
      path_file = f"{path}{file_name}.csv"
      path_file = path+file_name+".csv"
      path_file = "%s%s.csv" % (path, file_name)
      with open(path_file, "w") as f:
         f.write("Time Stamp,Name,Surname,Student ID\n")
         f.write(f"{time_stamp},{name},{surname},{student_id}\n")

if __name__ == "__main__":
   code = Code()
   MainWindow.show()
   sys.exit(app.exec_())