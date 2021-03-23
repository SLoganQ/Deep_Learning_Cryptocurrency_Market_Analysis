import time
from pynput.keyboard import Key, Controller
from selenium import webdriver


option = webdriver.ChromeOptions()
option.add_argument("--incognito")
option.add_argument("--window-size=1024x768")

browser = webdriver.Chrome(executable_path = "/usr/local/Caskroom/chromedriver/89.0.4389.23/chromedriver", options = option)
browser.get("https://www.bitstamp.net/market/tradeview/")

user_response = input("\nPrepare webpage for image capture then press ENTER to begin")
arrow_presses = int(input("\nEnter the number of left arrow key presses to imitate between screenshots: "))
num_to_collect = int(input("\nEnter number of images to collect: "))
time.sleep(5)

keyboard = Controller()
time_start = time.time()
image_num = 0

while image_num < num_to_collect:
    image_num += 1
    time_now = time.time()
    time_elapsed_min = (time_now - time_start) / 60
    filename = "images/image_" + str(image_num) + ".png"

    for i in range(int(arrow_presses)):
        keyboard.press(Key.right)
        time.sleep(0.005)
        keyboard.release(Key.right)
        time.sleep(0.005)

    browser.save_screenshot(filename)
    print("Captured image " + str(image_num) + ", elapsed time (min): " + str(time_elapsed_min))