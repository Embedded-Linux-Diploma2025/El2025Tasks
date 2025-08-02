import subprocess
import pyautogui
import smtplib
import yagmail

link = "https://www.linkedin.com/in/ahmed-f-madian-12ab63316?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BwnpO1tmSS3aoK5uXJesFeg%3D%3D"
subprocess.run(["start", "msedge", link], shell=True)

def find_image1(image_path):
    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if location is not None:
                print("Image found on screen.")
                break
        
        except Exception as e:
            print(f"Error locating image: {e}")

image_path = r"C:\Users\fouad\OneDrive\Images\Screenshots\Screenshot 2025-07-28 175653.png"
image_path2= r"C:\Users\fouad\OneDrive\Images\Screenshots\Screenshot 2025-07-28 180229.png"
find_image1(image_path)

center = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
if center:
    pyautogui.click(center)
else:
    print("Could not find image1 center on screen.")
    exit()
pyautogui.sleep(1)
def find_image2(image_path2):
 while True:
    try:
     location2=pyautogui.locateOnScreen(image_path2,confidence=0.8)
     if location2 is not None:
        print("Image found on screen.")
        break
    except Exception as e:
            print(f"Error locating image: {e}")

find_image2(image_path2)

center2 = pyautogui.locateCenterOnScreen(image_path2, confidence=0.8)
if center2:
    pyautogui.click(center2)
else:
    print("Could not find image2 center on screen.")
    exit()

pyautogui.sleep(1)
pyautogui.write("Embedded Linux Jobs")
pyautogui.sleep(1)
pyautogui.press("enter")
pyautogui.sleep(3)

screenshot1=pyautogui.screenshot()
screenshot1.save(r"C:\Users\fouad\OneDrive\Images\Screenshots\my_screenshot1.png")

print("Screenshot saved!")
pyautogui.sleep(1)
pyautogui.moveTo(1343,686,duration=1)
pyautogui.sleep(1)
pyautogui.scroll(-1300)
pyautogui.sleep(1)

screenshot2=pyautogui.screenshot()
screenshot2.save(r"C:\Users\fouad\OneDrive\Images\Screenshots\my_screenshot2.png")


receiver = "amadian2005@gmail.com"
subject = "Linkedin Embedded Linux screenshots"
body = "Hi Ahmed,\n\nAttached are the LinkedIn screenshots.\n\nBest regards,\nPython Bot"
attachments = [
    r"C:\Users\fouad\OneDrive\Images\Screenshots\my_screenshot1.png",
    r"C:\Users\fouad\OneDrive\Images\Screenshots\my_screenshot2.png"
]

yag = yagmail.SMTP("amadian2005@gmail.com", "hpjz erao iqhj mazz")
yag.send(to=receiver, subject=subject, contents=body, attachments=attachments)

print("Email sent!")