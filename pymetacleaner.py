from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow , QWidget, QListWidget, QListWidgetItem, QMessageBox
from PyQt5.QtWidgets import QApplication

import sys
import os
from os import path
from PIL import Image

def resource_path(relative_path):
	""" Get absolute path to resource , works for dev and for PyInstaller """
	base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
	return os.path.join(base_path,relative_path)

from PyQt5.uic import loadUiType

FORM_CLASS,_=loadUiType(resource_path("main.ui"))

class Main(QMainWindow,QListWidget, FORM_CLASS):
	def __init__(self,parent=None):
		super(Main,self).__init__(parent)
		QMainWindow.__init__(self)
		width = 533
		height = 508
		self.setFixedSize(width,height) #Used to stop resizing of the window
		self.setupUi(self)
		self.Handel_Buttons()
	
	def Handel_Buttons(self):
		self.selectimg_btn.clicked.connect(self.GET_IMAGES)
		self.removeimg_btn.clicked.connect(self.Removefrom_list)
		self.removemetainfo_btn.clicked.connect(self.removemetainfo)
		self.selectoutputdir_btn.clicked.connect(self.selectoutputdir)
		
	def Removefrom_list(self):
		self.listoffiles.takeItem(self.listoffiles.currentRow())

	def Addto_list(self,path):
		for x in path:
			if self.listoffiles.findItems(x,Qt.MatchExactly):
				pass
			else:
				self.listoffiles.addItem(x)

	def removemetainfo(self):
		items = []
		processlist = []
		for index in range(self.listoffiles.count()):
			items.append(self.listoffiles.item(index))
		for item in items:
			#print(item.text())
			processlist.append(item.text())
		#print(processlist)

		outputdir = self.outputdirtextbox.toPlainText()

		if len(outputdir) < 5:
			QMessageBox.critical(self,"Error","Invalid Output Path")
		
		else:

			for filename in processlist:
				directory, filename1 = os.path.split(filename)
				#print(filename)
				image = Image.open(filename)
				data = list(image.getdata())
				#getMeta(image_file)
				image_without_exif = Image.new(image.mode, image.size)
				image_without_exif.putdata(data)
				image_without_exif.save("{}\Clean_".format(outputdir) + filename1)

			self.listoffiles.clear()
			QMessageBox.about(self,"Succesful","Your images have been save at '{}'".format(outputdir))
	def selectoutputdir(self):
		outputdir = QFileDialog.getExistingDirectory()
		#print(outputdir)
		self.outputdirtextbox.insertHtml(outputdir)
		

	def GET_IMAGES(self):
		filename = QFileDialog.getOpenFileNames(filter = "Images (*.png *.xpm *.jpg *.jpeg)")
		path = filename[0]
		#print(path)
		self.Addto_list(path)


def main():

	app = QApplication(sys.argv)
	window = Main()
	window.show()
	app.exec_()
	

if __name__ == '__main__':
	main()