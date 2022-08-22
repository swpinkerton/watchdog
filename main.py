from PIL import Image
from ppadb.client import Client as AdbClient
import time
from ppadb.client import Client as AdbClient
import pytesseract
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# SCOPE:
scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize((creds))
sheet = client.open('QTUG results').worksheet('Kinesis QTUG Results')
row = sheet.row_values(2)

pytesseract.pytesseract.tesseract_cmd = r'c:/tools/tesseract/tesseract'

previousfall = 0
previousfalltime = ''

def connect():
    client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037

    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]

    print(f'Connected to {device}')

    return device, client

def fallriskcrop():
    global img_Falls_risk_estimate_sensor
    global img_num
    global img_time
    img = Image.open(r"C:/Users/swpin/Downloads/result.png")
    img_Falls_risk_estimate_sensor = img.crop((300, 300, 500, 375))
    img_num = img.crop((350, 460, 450, 500))
    img_time = img.crop((650, 90, 720, 120))
    # img_Falls_risk_estimate_sensor.show()
    # img_num.show()

def readimage(img):
    text = (pytesseract.image_to_string(img))
    return(text)

def previousfallrisk():
    return int(sheet.cell(2,1).value)

def previousfalltime():
    return str(sheet.cell(2,2).value)

def insert(fallrisk,time):
    insertRow = [fallrisk,time]
    sheet.insert_row(insertRow, 2)

if __name__ == '__main__':
    device, client = connect()
    previousfall = previousfallrisk()
    previousfalltime = previousfalltime()
    print(previousfall)
    while(1):

        screenshot = device.screencap()

        with open('c:/users/swpin/downloads/result.png', 'wb') as f:  # save the screenshot as result.png
            f.write(screenshot)
            print('Saved screenshot!')

        fallriskcrop()

        txt_Falls_risk_estimate_sensor = readimage(img_Falls_risk_estimate_sensor)
        split = txt_Falls_risk_estimate_sensor.split('\n')
        if split[0] == 'Falls risk estimate' and split[1] == 'sensor':
            txt_num = readimage(img_num)
            txt_time = readimage(img_time)
            fallRisk = int(txt_num.split('%')[0])
            if (previousfalltime!= txt_time or previousfall != fallRisk):
                previousfalltime = txt_time
                previousfall = fallRisk
                insert(fallRisk, txt_time)
                print(str(fallRisk) + 'inserted')

        time.sleep(5)