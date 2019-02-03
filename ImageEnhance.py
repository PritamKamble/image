from PIL import ImageEnhance
from PIL import Image

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
Image._show(contra)
