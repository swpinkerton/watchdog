from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'c:/tools/tesseract/tesseract'

img = Image.open(r"C:/Users/swpin/Downloads/result.png")
img_Falls_risk_estimate_sensor= img.crop((300, 300, 500, 375))
img_num = img.crop((350, 460, 450, 500))
img_time = img.crop((650, 90, 720, 120))
# img_Falls_risk_estimate_sensor.show()
# img_num.show()
img_time.show()

# text=(pytesseract.image_to_string(img_num))
# print(text)