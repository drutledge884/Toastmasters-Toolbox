from re import A
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pynput.keyboard import Key, Listener
import os
import sys
import time
import keyboard

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		#self.centralwidget = QtWidgets.QWidget(MainWindow)
          
        # adding pushbutton
		#self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		#self.pushButton.setGeometry(QtCore.QRect(200, 150, 93, 28))
  
        # adding signal and slot 
		#self.pushButton.clicked.connect(self.changelabeltext)
    
		#self.label = QtWidgets.QLabel(self.centralwidget)
		#self.label.setGeometry(QtCore.QRect(140, 90, 221, 20))      
  
        # keeping the text of label empty before button get clicked
		#self.label.setText("")     

		self.setGeometry(400, 100, 3000, 1800)
		self.setStyleSheet("background : lightgrey;")
		self.available_cameras = QCameraInfo.availableCameras()
		if not self.available_cameras:
			sys.exit()
		self.status = QStatusBar()
		self.status.setStyleSheet("background : white;")
		self.setStatusBar(self.status)
		self.save_path = ""
		self.viewfinder = QCameraViewfinder()
		self.viewfinder.show()
		self.setCentralWidget(self.viewfinder)
		self.select_camera(0)
		toolbar = QToolBar("Camera Tool Bar")
		#self.addToolBar(toolbar)
		click_action = QAction("Screenshot", self)
		click_action.setStatusTip("This will capture picture")
		click_action.setToolTip("Capture picture")
		click_action.triggered.connect(self.click_photo)
		toolbar.addAction(click_action)
		change_folder_action = QAction("Change Save Location", self)
		change_folder_action.setStatusTip("Change folder where picture will be saved saved.")
		change_folder_action.setToolTip("Change save location")
		change_folder_action.triggered.connect(self.change_folder)
		#toolbar.addAction(change_folder_action)
		camera_selector = QComboBox()
		camera_selector.setStatusTip("Choose camera to take pictures")
		camera_selector.setToolTip("Select Camera")
		camera_selector.setToolTipDuration(2500)
		camera_selector.addItems([camera.description() for camera in self.available_cameras])
		camera_selector.currentIndexChanged.connect(self.select_camera)
		#toolbar.addWidget(camera_selector)
		#toolbar.setStyleSheet("background : white;")
		self.setWindowTitle("Toastmaster Toolbox -- Daniel Rutledge")
		#self.retranslateUi(self)
		self.UIComponents()
		
		#self.on_press(Key)
		#self.on_release()

		

		self.show()

	def select_camera(self, i):
		self.camera = QCamera(self.available_cameras[i])
		self.camera.setViewfinder(self.viewfinder)
		self.camera.setCaptureMode(QCamera.CaptureStillImage)
		self.camera.error.connect(lambda: self.alert(self.camera.errorString()))
		self.camera.start()
		self.capture = QCameraImageCapture(self.camera)
		self.capture.error.connect(lambda error_msg, error, msg: self.alert(msg))
		self.capture.imageCaptured.connect(lambda d, i: self.status.showMessage("Image captured : " + str(self.save_seq)))
		self.current_camera_name = self.available_cameras[i].description()
		self.save_seq = 0

	def time_convert(sec):
		mins = sec // 60
		sec = sec % 60
		hours = mins // 60
		mins = mins % 60
		result = "Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec)
		return result

	

	def UIComponents(self):
		self.count1 = 0
		self.count2 = 0
		self.count3 = 0
		self.count4 = 0
		self.count5 = 0
		self.count6 = 0
		self.count7 = 0
		self.count8 = 0
		self.count9 = 0
		self.count10 = 0
		self.count11 = 0
		self.count12 = 0

		self.jobs = ["Nobody", "Speaker 1", "Speaker 2", "Speaker 3", "Speaker 4", "President", "Nobody"]
		self.jobsIndex = 1

		self.flag1 = False
		self.flag2 = False
		self.flag3 = False
		self.flag4 = False

		self.label1 = QLabel(self) # Timer Report for Speaker 1
		self.label2 = QLabel(self) # Timer Report for Speaker 2
		self.label3 = QLabel(self) # Timer Report for Speaker 3
		self.label4 = QLabel(self) # Timer Report for Speaker 4
		self.label5 = QLabel(self) # Previous Speaker
		self.label6 = QLabel(self) # Currerntly Speaking
		self.label7 = QLabel(self) # Next Speaker
		self.label8 = QLabel(self) # Toast Mooster
		self.label9 = QLabel(self) # Speaker 1 Ahs
		self.label10 = QLabel(self) # Speaker 1 Vocab
		self.label11 = QLabel(self) # Speaker 2 Ahs
		self.label12 = QLabel(self) # Speaker 2 Vocab
		self.label13 = QLabel(self) # Speaker 3 Ahs
		self.label14 = QLabel(self) # Speaker 3 Vocab
		self.label15 = QLabel(self) # Speaker 4 Ahs
		self.label16 = QLabel(self) # Speaker 4 Vocab
		self.label17 = QLabel(self) # Timing column label
		self.label18 = QLabel(self) # Ahs/Vocab column label

		self.label1.setGeometry(100, 500, 600, 100)
		self.label2.setGeometry(100, 700, 600, 100)
		self.label3.setGeometry(100, 900, 600, 100)
		self.label4.setGeometry(100, 1100, 600, 100)
		self.label5.setGeometry(0, 100, 800, 100)
		self.label6.setGeometry(1000, 100, 1000, 100)
		self.label7.setGeometry(2200, 100, 800, 100)
		self.label8.setGeometry(1000, 1600, 1000, 100)
		self.label9.setGeometry(2300, 500, 300, 100)
		self.label10.setGeometry(2600, 500, 300, 100)
		self.label11.setGeometry(2300, 700, 300, 100)
		self.label12.setGeometry(2600, 700, 300, 100)
		self.label13.setGeometry(2300, 900, 300, 100)
		self.label14.setGeometry(2600, 900, 300, 100)
		self.label15.setGeometry(2300, 1100, 300, 100)
		self.label16.setGeometry(2600, 1100, 300, 100)
		self.label17.setGeometry(100, 300, 600, 100)
		self.label18.setGeometry(2300, 300, 600, 100)

		self.label1.setStyleSheet("border : 4px solid green;")
		self.label2.setStyleSheet("border : 4px solid green;")
		self.label3.setStyleSheet("border : 4px solid green;")
		self.label4.setStyleSheet("border : 4px solid green;")
		self.label5.setStyleSheet("border : 4px solid blue;")
		self.label6.setStyleSheet("border : 4px solid blue;")
		self.label7.setStyleSheet("border : 4px solid blue;")
		self.label8.setStyleSheet("border : 4px solid blue;")
		self.label9.setStyleSheet("border : 4px solid green;")
		self.label10.setStyleSheet("border : 4px solid green;")
		self.label11.setStyleSheet("border : 4px solid green;")
		self.label12.setStyleSheet("border : 4px solid green;")
		self.label13.setStyleSheet("border : 4px solid green;")
		self.label14.setStyleSheet("border : 4px solid green;")
		self.label15.setStyleSheet("border : 4px solid green;")
		self.label16.setStyleSheet("border : 4px solid green;")
		self.label17.setStyleSheet("border : 4px solid blue;")
		self.label18.setStyleSheet("border : 4px solid blue;")

		self.label1.setText("Speaker 1: " + str(self.count1))
		self.label2.setText("Speaker 2: " + str(self.count2))
		self.label3.setText("Speaker 3: " + str(self.count3))
		self.label4.setText("Speaker 4: " + str(self.count4))
		self.label5.setText("Previous: " + self.jobs[self.jobsIndex - 1])
		self.label6.setText("Current Speaker: " + self.jobs[self.jobsIndex])
		self.label7.setText("Up Next: " + self.jobs[self.jobsIndex + 1])
		self.label8.setText("Toast Mooster: Nobody")		
		self.label9.setText("0")
		self.label10.setText("0")
		self.label11.setText("0")
		self.label12.setText("0")		
		self.label13.setText("0")
		self.label14.setText("0")
		self.label15.setText("0")
		self.label16.setText("0")	
		self.label17.setText("Timing")
		self.label18.setText("Ahs/Vocab")		

		self.label1.setFont(QFont('Arial', 25))
		self.label2.setFont(QFont('Arial', 25))
		self.label3.setFont(QFont('Arial', 25))
		self.label4.setFont(QFont('Arial', 25))
		self.label5.setFont(QFont('Arial', 25))
		self.label6.setFont(QFont('Arial', 25))
		self.label7.setFont(QFont('Arial', 25))
		self.label8.setFont(QFont('Arial', 25))
		self.label9.setFont(QFont('Arial', 25))
		self.label10.setFont(QFont('Arial', 25))
		self.label11.setFont(QFont('Arial', 25))
		self.label12.setFont(QFont('Arial', 25))
		self.label13.setFont(QFont('Arial', 25))
		self.label14.setFont(QFont('Arial', 25))
		self.label15.setFont(QFont('Arial', 25))
		self.label16.setFont(QFont('Arial', 25))
		self.label17.setFont(QFont('Arial', 25))
		self.label18.setFont(QFont('Arial', 25))

		self.label1.setAlignment(Qt.AlignLeft)
		self.label2.setAlignment(Qt.AlignLeft)
		self.label3.setAlignment(Qt.AlignLeft)
		self.label4.setAlignment(Qt.AlignLeft)
		self.label5.setAlignment(Qt.AlignLeft)
		self.label6.setAlignment(Qt.AlignLeft)
		self.label7.setAlignment(Qt.AlignLeft)
		self.label8.setAlignment(Qt.AlignLeft)
		self.label9.setAlignment(Qt.AlignLeft)
		self.label10.setAlignment(Qt.AlignLeft)
		self.label11.setAlignment(Qt.AlignLeft)
		self.label12.setAlignment(Qt.AlignLeft)
		self.label13.setAlignment(Qt.AlignLeft)
		self.label14.setAlignment(Qt.AlignLeft)
		self.label15.setAlignment(Qt.AlignLeft)
		self.label16.setAlignment(Qt.AlignLeft)
		self.label17.setAlignment(Qt.AlignCenter)
		self.label18.setAlignment(Qt.AlignCenter)

		timer1 = QTimer(self)
		timer1.timeout.connect(self.showTime1)
		timer1.start(100)

		timer2 = QTimer(self)
		timer2.timeout.connect(self.showTime2)
		timer2.start(100)

		timer3 = QTimer(self)
		timer3.timeout.connect(self.showTime3)
		timer3.start(100)

		timer4 = QTimer(self)
		timer4.timeout.connect(self.showTime4)
		timer4.start(100)	

		#self.time_convert(self.time_lapsed)
		#print(self.time_convert())

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.pushButton.setText(_translate("MainWindow", "Push Button"))

	def on_press(key, self):
		print('{0} pressed'.format(key))
		if key == "a":
			self.flag1 == True
		else:
			print("kj")

	def on_release(key):
		print('{0} release'.format(key))
		if key == Key.esc:
        # Stop listener
			return False

	#with Listener(
    #    on_press=on_press,
    #    on_release=on_release) as listener: listener.join()

	def showTime1(self):
		if self.flag1:
			self.count1+= 1
		text1 = str(self.count1 / 10)
		self.label1.setText("Speaker 1: " + text1)

	def showTime2(self):
		if self.flag2:
			self.count2+= 1
		text2 = str(self.count2 / 10)
		self.label2.setText("Speaker 2: " + text2)

	def showTime3(self):
		if self.flag3:
			self.count3+= 1
		text3 = str(self.count3 / 10)
		self.label3.setText("Speaker 3: " + text3)

	def showTime4(self):
		if self.flag4:
			self.count4+= 1
		text4 = str(self.count4 / 10)
		self.label4.setText("Speaker 4: " + text4)

	def Start1(self):
		print("hi")
		self.flag1 = True
		
	def Start2(self):
		self.flag2 = True

	def Start3(self):
		self.flag3 = True

	def Start4(self):
		self.flag4 = True

	def Pause1(self):
		self.flag1 = False

	def Pause2(self):
		self.flag2 = False

	def Pause3(self):
		self.flag3 = False

	def Pause4(self):
		self.flag4 = False

	def Reset1(self):
		self.flag1 = False
		self.count1 = 0
		self.label1.setText("Speaker 1: " + str(self.count1))

	def Reset2(self):
		self.flag2 = False
		self.count2 = 0
		self.label2.setText("Speaker 2: " + str(self.count2))

	def Reset3(self):
		self.flag3 = False
		self.count3 = 0
		self.label3.setText("Speaker 3: " + str(self.count3))

	def Reset4(self):
		self.flag4 = False
		self.count4 = 0
		self.label4.setText("Speaker 4: " + str(self.count4))

	def click_photo(self):

		# time stamp
		timestamp = time.strftime("%d-%b-%Y-%H_%M_%S")

		# capture the image and save it on the save path
		self.capture.capture(os.path.join(self.save_path,
										"%s-%04d-%s.jpg" % (
			self.current_camera_name,
			self.save_seq,
			timestamp
		)))

		# increment the sequence
		self.save_seq += 1

	def change_folder(self):

		# open the dialog to select path
		path = QFileDialog.getExistingDirectory(self,
												"Picture Location", "")

		# if path is selected
		if path:

			# update the path
			self.save_path = path

			# update the sequence
			self.save_seq = 0

	def alert(self, msg):

		# error message
		error = QErrorMessage(self)

		# setting text to the error message
		error.showMessage(msg)

if __name__ == "__main__" :
	
    App = QApplication(sys.argv)
window = MainWindow()
sys.exit(App.exec())
