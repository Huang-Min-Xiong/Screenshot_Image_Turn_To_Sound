import keyboard
import pyautogui
import pytesseract
from gtts import gTTS

#設置tesseract.exe安裝路徑
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

#左上角座標
def Upper_left_corner():
    pyautogui.alert('請移至欲截圖之左上角按下z鍵!')
    while True:
        if keyboard.is_pressed('z'):
            global pos1
            pos1=pyautogui.position()
            print(pos1)
            break

#右下角座標
def Lower_right_corner():
    pyautogui.alert('請移至欲截圖之右下角按下x鍵!')
    while True:
        if keyboard.is_pressed('x'):
            global pos2
            pos2=pyautogui.position()
            print(pos2)
            break

#偵測圖像文字且轉為音檔
def Detect_image_text_and_turn_to_sound():
    Img_path=r'.\img.png'
    Detect_Text=pytesseract.image_to_string(Img_path) #偵測文字
    print('內容:\n'+Detect_Text)

    with open(r".\Detect_Text.txt","w") as f:
        f.write(Detect_Text) #寫入文字檔
        #print('已寫入文字檔!')
        pyautogui.alert('已寫入文字檔!')

    Convert_Sound=gTTS(Detect_Text,lang='en') #轉為音檔
    Convert_Sound.save(r'.\Sound.mp3') #儲存音檔
    pyautogui.alert('已存成音檔!')
    #print('已存成音檔!')

if __name__ == "__main__":
    Upper_left_corner()
    Lower_right_corner()
    x=pos1.x
    y=pos1.y
    w=pos2.x-pos1.x
    h=pos2.y-pos1.y
    img=pyautogui.screenshot(region=(x,y,w,h))
    img.save(r'.\img.png')
    pyautogui.alert('截圖已成功!')
    Detect_image_text_and_turn_to_sound()