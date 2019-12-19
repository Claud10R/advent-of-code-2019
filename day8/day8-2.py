import os
import matplotlib.pyplot as plt
fileDir = os.path.dirname(os.path.abspath(__file__))

def matrix_to_img(img,w,h):
	mtx = [img[i : i+w] for i in range(0,len(img),w)]
	return mtx

def day8_2(width, height):
	with open(fileDir + "/input.txt") as file:
		line = file.readline().strip()
		chars = [int(char) for char in line]

	dim_layer = width * height
	layers = [chars[i:i+dim_layer] for i in range(0,len(chars),dim_layer)]

	final_image = []
	for i in range(dim_layer):
		curr_pixel = layers[0][i]

		cnt_layer = 1
		while curr_pixel == 2:
			curr_pixel = layers[cnt_layer][i]
			cnt_layer += 1

		final_image.append(curr_pixel)

	img = matrix_to_img(final_image, width, height)

	plt.imshow(img)
	plt.show()

day8_2(25,6)