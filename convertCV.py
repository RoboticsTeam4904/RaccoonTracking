import numpy as np
from label_cubes import labelFolder

'''Takes in a list of bounding boxes and outputs txt files for neural net in supplied txtFolder'''
def convertCV(boundingBoxList, txtFolder):
	imgNum = 0
	for img in boundingBoxList:
		txtInfo = ""
		fileName = txtFolder + "/" + "img" + str(imgNum) + ".txt"
		newFile = open(fileName, 'w')

		for boundingBox in img:
			txtInfo += "0 " + str(boundingBox[0]) + " " + str(boundingBox[1]) + " " + str(boundingBox[2]) + " " + str(boundingBox[3]) + "\n"
		
		newFile.write(txtInfo)
		newFile.close()
		imgNum += 1

if __name__ == '__main__':
	convertCV(labelFolder("data/images"), "data/CVTxt")