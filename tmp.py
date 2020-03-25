import numpy as np
import cv2
import matplotlib.pyplot as plt

def generate():
	img = np.zeros([200,2560],np.uint8)

	color = 0
	n = 0
	for i in range(2560):
		for j in range(200):
			img[j][i] = color
		n = n + 1
		if n>=10:
			n = 0
			color = color + 1
	cv2.imshow('123',img)
	print(img)
	cv2.waitKey()

	cv2.imwrite('grade.jpg',img)

def snip(img_path):
	result = []
	img = cv2.imread(img_path)
	col = img.shape[1]
	row = img.shape[0]

	step = int(col / 256)

	for i in range(256):
		result.append(img[0][i * step][0])

	return result
	
def plot(U, Y):
	plt.title('$curve$')
	plt.plot(U, Y, c = 'c')
	plt.show()

if __name__ == '__main__':
	Y = snip('grade.jpg')

	U = np.linspace(0,255,256)
	plot(U,Y)
