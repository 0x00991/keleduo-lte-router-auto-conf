from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
print("Starting driver..")
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

driver.get("http://192.168.0.1")
def wd_until(wd, ec):
    try:
        wd.until(ec)
    except Exception as e:
        driver.quit()
        raise e
wd15 = WebDriverWait(driver, 15)
wd5 = WebDriverWait(driver, 5)

wd_until(wd15, EC.presence_of_element_located((By.ID, "tbarouter_username")))
print("Login..")
driver.find_element(By.ID, "tbarouter_username").send_keys("admin")
driver.find_element(By.ID, "tbarouter_password").send_keys("admin")
driver.find_element(By.ID, "btnSignIn").click()
print("Login Success")
wd_until(wd5, EC.element_to_be_clickable((By.ID, "btnSkip")))
driver.find_element(By.ID, "btnSkip").click()
print("Navigating..")
wd_until(wd5, EC.presence_of_element_located((By.ID, "menu")))
driver.execute_script("createMenu(7);")
print("'Router'")
wd_until(wd5, EC.presence_of_element_located((By.ID, "mainColumn")))

driver.execute_script("mPowerOffRouter.childNodes[0].click();")
print("Click 'Power Off Router'")

print("Click 'Power Off'")
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "btPowerOffRouter")))
driver.find_element(By.ID, "btPowerOffRouter").click()

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "btnPowerOffOK")))
driver.find_element(By.ID, "btnPowerOffOK").click()

print("Completed")
driver.implicitly_wait(1)

driver.quit()