from selenium import webdriver

driver = webdriver.Firefox(executable_path="./geckodriver") # https://www.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/16249510#overview
driver.get('http://localhost:5000')
