import numpy as np
from label_cubes import labelFolder
import os

'''Takes in a list of bounding boxes and outputs txt files for neural net in supplied txtFolder'''
def convertCVTxt(boundingBoxList, txtFolder):
	imgNum = 0
	for img in boundingBoxList:
		#print(img)
		txtInfo = ""
		fileName = txtFolder + "/" + "img" + str(imgNum) + ".txt"
		newFile = open(fileName, 'w')

		for boundingBox in img:
			txtInfo += "0 " + str(boundingBox[0]) + " " + str(boundingBox[1]) + " " + str(boundingBox[2]) + " " + str(boundingBox[3]) + "\n"
		
		newFile.write(txtInfo)
		newFile.close()
		imgNum += 1

def convertCVXML(boundingBoxList, xmlFolder):
	imgNum = 0
	for img in boundingBoxList:
		boundingBoxes, info = img[0], img[1]
		imgPath = info[2]
		filename = os.path.basename(imgPath)
		xmlPath = xmlFolder + "/" + filename.split('.')[0] + ".xml"
		xmlFile = open(xmlPath, 'w')
		imgWidth = info[0]
		imgHeight = info[1]
		xmlInfo =  "<annotationverified='yes'><folder>images</folder><filename>"+filename+"</filename><path>"+imgPath+"</path><source><database>Unknown</database></source><size><width>"+str(imgWidth)+"</width><height>"+str(imgHeight)+"</height><depth>3</depth></size><segmented>0</segmented>"
		
		for boundingBox in boundingBoxes:
			xCenter = boundingBox[0]
			yCenter = boundingBox[1]
			width = boundingBox[2]
			height = boundingBox[3]
			name = "cube"
			minx = xCenter - width/2
			miny = yCenter - height/2
			maxx = xCenter + width/2
			maxy = yCenter + height/2
			xmlInfo += "<object><name>"+name+"</name><pose>Unspecified</pose><truncated>0</truncated><difficult>0</difficult><bndbox><xmin>"+str(minx)+"</xmin><ymin>"+str(miny)+"</ymin><xmax>"+str(maxx)+"</xmax><ymax>"+str(maxy)+"</ymax></bndbox></object>"
		
		xmlInfo += "</annotation>"
		xmlFile.write(xmlInfo)

if __name__ == '__main__':
	convertCVXML(labelFolder("data/images"), "data/CVXML")
	#convertCVTxt(labelFolder("data/images"), "data/CVTxt")