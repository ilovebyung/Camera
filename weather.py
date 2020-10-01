import cv2
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import requests
import json

api_key = 'f3ab316647c65ca1c6cf480133963775'

url = f"https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid={api_key}"


lat = "48.208176"
lon = "16.373819"
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (
    lat, lon, api_key)

response = requests.get(url)
json.loads(response.text)


data = json.loads(response.text)
print(data)

data.keys()

im = cv.imread('test.jpg')
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(
    thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
plt.imshow(imgray)
cv2.line()
