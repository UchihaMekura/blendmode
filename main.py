import numpy as np
import matplotlib.pyplot as plt

def p_screen(): # 255 - (((255 - A) * (255 - B)) >> 8))
	c = 0
	cstep = 0.08

	plt.title('$screen$')

	for N in [0, 31, 63, 95, 127, 159, 191, 223, 255]:

		D = np.linspace(0,255,256)
		Y = 255 - (((255 - N) * (255 - D)) / (2^8))

		plt.plot(D, Y, c = str(c))

		c = c+cstep

	plt.show()
	

def p_softLight(): # ((B < 128)?(2*((A>>1)+64))*((float)B/255):(255-(2*(255-((A>>1)+64))*(float)(255-B)/255)))
	c = 0.9
	cstep = 0.08

	plt.title('$Soft Light$')

	for N in [0, 31, 63, 95, 127, 159, 191, 223, 255]:

		D1 = np.linspace(0,127,128)
		D2 = np.linspace(128,255,128)

		Y1 = (2*((N>>1)+64))*(D1/255)
		Y2 = 255-(2*(255-((N>>1)+64))*((255-D2)/255))

		
		plt.plot(D1, Y1, c = str(c))
		plt.plot(D2, Y2, c = str(c))

		c = c-cstep

	plt.show()


def softlight(n, d): # ((B < 128)?(2*((A>>1)+64))*((float)B/255):(255-(2*(255-((A>>1)+64))*(float)(255-B)/255)))
	if d < 128:
		y = (2*((n>>1)+64))*(float(d)/255)
	else:
		y = 255-2*(255-((n>>1)+64))*(float(255-d)/255)

	return int(y)

if __name__ == '__main__':
	y = softlight(255,140)
	print(y)