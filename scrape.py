from bs4 import BeautifulSoup
from selenium import webdriver
import flight
import time, requests

#Get web page
matrix_url = 'https://matrix.itasoftware.com/#view-flights:research=CHIMUC-MUCCHI'
flights_url = 'https://www.google.com/flights?hl=en#flt=/m/01snm./m/02_286.2019-08-20*/m/02_286./m/01snm.2019-08-20;c:USD;e:1;sd:1;t:f'
#browser = webdriver.PhantomJS('C://Users//mattc//Documents//phantomjs-2.1.1-windows//bin//phantomjs.exe')
browser = webdriver.Chrome('C://Users//mattc//Documents//phantomjs-2.1.1-windows//chromedriver.exe')
browser.implicitly_wait(10000)

browser.get(flights_url)
time.sleep(5)
html = browser.page_source
content = BeautifulSoup(html, 'lxml')
results = content.find('div', class_='gws-flights-results__best-flights')
results = results.find('ol')
current_flight = results.find('li')

flights = []
flights.append(current_flight)

while current_flight is not None:
    current_flight = current_flight.find_next_sibling()
    flights.append(current_flight)

browser.quit()