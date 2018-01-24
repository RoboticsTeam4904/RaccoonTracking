import numpy as np
from label_cubes import labelFolder, label
import os

'''Takes in a list of bounding boxes and outputs txt files for neural net in supplied txtFolder'''
def convertCV(boundingBoxList, txt_names):
	for img, fileName in zip(boundingBoxList, txt_names):
		newFile = open(fileName, 'w')
		txtInfo = ""

		for boundingBox in img:
			txtInfo += "0 " + str(boundingBox[0]) + " " + str(boundingBox[1]) + " " + str(boundingBox[2]) + " " + str(boundingBox[3]) + "\n"
		
		newFile.write(txtInfo)
		newFile.close()

def convertCVXML(boundingBoxList, xmlFolder):
	imgNum = 0
	for img in boundingBoxList:
		boundingBoxes, info = img[0], img[1]
		imgWidth, imgHeight, imgPath = info[0], info[1], info[2]
		filename = os.path.basename(imgPath)
		xmlPath = xmlFolder + "/" + filename.split('.')[0] + ".xml"
		xmlFile = open(xmlPath, 'w')
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
	img_folder = "data/images"
	xml_folder = "data/cvXMLs"
	convertCVXML(labelFolder(img_folder), xml_folder)