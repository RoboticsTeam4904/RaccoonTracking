import numpy as np
from label_cubes import label
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

if __name__ == '__main__':
	img_folder = "data/unlabeled"
	txt_folder = "data/label_txts"
	img_names = os.listdir(img_folder)
	names = []
	for name in img_names:
		if name[-3:] == "jpg" or name[-3:] == "JPG" or name[-3:] == "png":
			names.append(name)
	convertCV(label([img_folder + "/" + name for name in names]), [txt_folder + "/" + name[:-3] + "txt" for name in names])