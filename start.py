#from selenium import webdriver
# The URL we want to browse to
#url = "https://unsplash.com"
# Using Selenium's webdriver to open the page
#driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
#driver.get(url)
import requests
import time
from selenium import webdriver
from PIL import Image
from io import BytesIO

chrome_path = r'C:\Users\Dell\Documents\Python Scripts\Sublime script\chromedriver'
driver = webdriver.Chrome(chrome_path)
url = "https://unsplash.com"
driver.get(url)

driver.execute_script("window.scrollTo(0,1000);")
time.sleep(5)
# Select image elements and print their URLs
image_elements = driver.find_elements_by_css_selector("#gridMulti img")
i = 0


for image_element in image_elements:
    image_url = image_element.get_attribute("src")
    # Send an HTTP GET request, get and save the image from the response
    image_object = requests.get(image_url)
    image = Image.open(BytesIO(image_object.content))
    image.save("./images/image" + str(i) + "." + image.format, image.format)
    i += 1