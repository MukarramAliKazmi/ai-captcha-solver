from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import whisper
import warnings
import time

warnings.filterwarnings("ignore")

model = whisper.load_model("base")

driver = webdriver.Chrome()
driver.get("https://www.google.com/recaptcha/api2/demo")

driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element(By.XPATH, ".//iframe[@title='reCAPTCHA']"))
driver.find_element(By.ID, "recaptcha-anchor-label").click()
driver.switch_to.default_content()

time.sleep(1)

driver.switch_to.default_content()
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, ".//iframe[@title='recaptcha challenge expires in two minutes']")))
driver.find_element(By.ID, "recaptcha-audio-button").click()

time.sleep(1)

url = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "audio-source"))).get_attribute('src')
with open('.temp', 'wb') as f:
    f.write(requests.get(url).content)
result = model.transcribe('.temp')
text = result["text"].strip()
driver.find_element(By.ID, "audio-response").send_keys(text)
driver.find_element(By.ID, "recaptcha-verify-button").click()

time.sleep(10)
