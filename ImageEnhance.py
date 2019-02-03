from PIL import ImageEnhance
from PIL import Image

image=Image.open('card.jpg')
image.show()
enhancer = ImageEnhance.Sharpness(image)


#for i in range(8):
factor = 8 / 4.0
image=enhancer.enhance(factor).show("Sharpness %f" % factor)

enhancer2=ImageEnhance.Color(image)
factor = 8 / 4.0
image=enhancer.enhance(factor).show("color %f" % factor)