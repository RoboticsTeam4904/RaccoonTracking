# -*- coding: utf-8 -*-    
import xml.etree.ElementTree as ET
import sys
import os

#takes in path to xml file and new folder to put .txt in
def convertToTxt(xmlFilePath, newTxtFolder):
	tree = ET.parse(xmlFilePath)
	xs = []
	ys = []

	imgWidth = 0
	imgHeight = 0

	#finds x and y coordinates of corners of every polygon and adds them to list xs and ys
	for polygon in tree.iter("polygon"):
		polygonXs = []
		polygonYs = []
		for pt in polygon.iter('pt'):
			x = pt.find('x').text
			y = pt.find('y').text
			polygonXs.append(x)
			polygonYs.append(y)
		xs.append(polygonXs)
		ys.append(polygonYs)

	for a in tree.iter("imagesize"): #finding img width and height
	    x = a.find('nrows').text
	    y = a.find('ncols').text
	    imgWidth = int(y)
	    imgHeight = int(x)
	txtFormat = ""

	#formatting txt
	for xTuple, yTuple in zip(xs, ys):
		try:
			width = abs(int(xTuple[0]) - int(xTuple[1]))
			height = abs(int(yTuple[0]) - int(yTuple[2]))
		except:
			width = 0
			height = 0
		xCenter = int(min(xTuple)) + width / 2
		yCenter = int(min(yTuple)) + height / 2
		txtFormat += "0 " + str(float(xCenter)/imgWidth) + " " + str(float(yCenter)/imgHeight) + " " + str(float(width)/imgWidth) + " " + str(float(height)/imgHeight) + "\n"
	
	#writing xml onto txt file
	newPath = newTxtFolder + "/" + os.path.basename(xmlFilePath).split('.')[0] + ".txt"
	newFile = open(newPath, "w")
	newFile.write(txtFormat)
	newFile.close()

#converts entire folder to txt
def convertXMLToText(xmlFolder=sys.argv[1],newTxtFolder=sys.argv[2]):
	for fn in os.listdir(xmlFolder):
		qualifiedName = xmlFolder + "/" + fn
		convertToTxt(qualifiedName,newTxtFolder)

convertXMLToText()