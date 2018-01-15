# -*- coding: utf-8 -*-    
import xml.etree.ElementTree as ET
import sys
import os

#takes in paths to file to convert, dir with corresponding img inside, and xml dir to write new file in
def convert(xmlFilePath, imgFolder, newXmlFolder): 
	tree = ET.parse(xmlFilePath)
	xs = []
	ys = []

	imgWidth = 0
	imgHeight = 0

	for a in tree.iter("polygon"): #finding x and y in formatting
	    x = a.find('pt').find('x').text
	    y = a.find('pt').find('y').text
	    xs.append(x)
	    ys.append(y)

	for a in tree.iter("imagesize"): #finding img width and height
	    x = a.find('nrows').text
	    y = a.find('ncols').text
	    imgWidth = x
	    imgHeight = y

	try:
		width = str(abs(int(xs[1]) - int(xs[0])))
		height = str(abs(int(ys[1]) - int(ys[0])))
	except IndexError:
		width = 0
		height = 0

	#if there are no xs or ys, set the min and max to 0
	if (xs != []):
		minx = min(xs)
		maxx = max(xs)
	else:
		minx = 0
		maxx = 0
	if (ys !=[]):
		miny = min(ys)
		maxy = max(ys)
	else:
		miny = 0
		maxy = 0


	#Finding corresponding img for xml file
	head, tail = os.path.split(xmlFilePath)
	filename = os.path.basename(imgFolder).split('.')[0] + ".jpg"
	path = os.path.join(head, filename)
	name = "cube"

	#output xml format
	updatedXML = "<annotationverified='yes'><folder>images</folder><filename>"+filename+"</filename><path>"+path+"</path><source><database>Unknown</database></source><size><width>"+imgWidth+"</width><height>"+imgHeight+"</height><depth>3</depth></size><segmented>0</segmented><object><name>"+name+"</name><pose>Unspecified</pose><truncated>0</truncated><difficult>0</difficult><bndbox><xmin>"+str(minx)+"</xmin><ymin>"+str(miny)+"</ymin><xmax>"+str(maxx)+"</xmax><ymax>"+str(maxy)+"</ymax></bndbox></object></annotation>"
	
	#writing xml onto new xml file
	newPath = newXmlFolder + "/" + os.path.basename(xmlFilePath)
	newFile = open(newPath, "w")
	newFile.write(updatedXML)
	newFile.close()

#converts an entire folder
def convertFolder(xmlFolder=sys.argv[1], imgFolder=sys.argv[2], newXmlFolder=sys.argv[3]):
	for fn in os.listdir(xmlFolder):
		qualifiedName = xmlFolder + "/" + fn
		convert(qualifiedName, imgFolder, newXmlFolder)

convertFolder()
#convertFolder("/Users/niksure/Documents/workspace/RaccoonTracking/data/annotations", "/Users/niksure/Documents/workspace/RaccoonTracking/data/images", "/Users/niksure/Documents/workspace/RaccoonTracking/data/updatedXMLs")