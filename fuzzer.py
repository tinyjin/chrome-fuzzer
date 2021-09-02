import subprocess
import time
import selenium
from selenium import webdriver


URL = 'http://localhost:8080'
driver = webdriver.Chrome(executable_path='./chromedriver')


while True:
  time.sleep(0.5)
  subprocess.call('./venv/bin/python ./domato/generator.py index.html', shell=True)
  driver.get(URL)
