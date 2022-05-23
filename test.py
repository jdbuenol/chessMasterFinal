from PIL import Image

im = Image.open('./test1.png')
print(type(im.tobytes("xbm", "rgb")))