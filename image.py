
from PIL import Image

def reduce():
        img = Image.open('simple.jpg').convert('L')  # convert image to 8-bit grayscale
        basewidth , height = img.size
        basewidth=50
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
        img.save('small.jpg')


        img = Image.open('small.jpg').convert('L')  # convert image to 8-bit grayscale
        WIDTH, HEIGHT = img.size

        data = list(img.getdata()) # convert image data to a list of integers
        # convert that to 2D list (list of lists of integers)
        data = [data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]

        # At this point the image's pixels are all in memory and can be accessed
        # individually using data[row][col].

        # For example:
        for row in data:
            print(' '.join('{:3}'.format(value) for value in row))

        #Here's another more compact representation.
        #chars = '@%#*+=-:. '  # Change as desired.
        #scale = (len(chars)-1)/255.
        #print()
        #for row in data:
        #        print(' '.join(chars[int(value*scale)] for value in row))

if __name__=="__main__":
        reduce()
