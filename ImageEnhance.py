#4features branch
from PIL import ImageEnhance
from PIL import Image
import cv2
import numpy as np

image=Image.open('card.jpg')
image.show()
enhancer = ImageEnhance.Sharpness(image)


#for i in range(8):
factor = 8 / 4.0
sharpimage=enhancer.enhance(factor)#.show("Sharpness %f" % factor)
#Image._show(sharpimage)


enhancer = ImageEnhance.Color(sharpimage)
#enhancer = ImageEnhance.Sharpness(image)
# Both Color and Sharpness has same 'enhance(factor)' method.
factor = 1.0*1.5
colored=enhancer.enhance(factor)#.show('colored',"color %f" % factor)
#Image._show(colored)

enhancer=ImageEnhance.Brightness(colored)
factor=1.2
bright=enhancer.enhance(factor)
#Image._show(bright)

enhancer=ImageEnhance.Contrast(bright)
factor=1.1223
contra=enhancer.enhance(factor)
#Image._show(contra)
contra.save('save.jpg')

#gamma correction
def adjust_gamma(image, gamma=1.0):
   invGamma = 1.0 / gamma
   table = np.array([((i / 255.0) ** invGamma) * 255
      for i in np.arange(0, 256)]).astype("uint8")

   return cv2.LUT(image, table)
original = cv2.imread('save.jpg',1)
gamma = 1.1                            # change the value here to get different result
adjusted = adjust_gamma(original, gamma=gamma)
cv2.imwrite('save.jpg',adjusted)
#cv2.imshow("gammam image 1", adjusted)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
Image.open('save.jpg').show()