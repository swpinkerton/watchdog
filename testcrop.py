from PIL import Image

img = Image.open(r"C:/Users/swpin/Downloads/result.png")
left = 0
top = 50
right = 510
bottom = 292
img_res = img.crop((left, top, right, bottom))
img_res.show()