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
wd_until(wd5, EC.element_to_be_clickable((By.ID, "btnQuickSetup")))
driver.find_element(By.ID, "btnQuickSetup").click()
print("Setup")
wd_until(wd5, EC.element_to_be_clickable((By.ID, "btnNext")))
driver.find_element(By.ID, "btnNext").click()

wd_until(wd5, EC.element_to_be_clickable((By.ID, "btnNext1")))
if not driver.find_element(By.ID, "AutoConfigureAPNCheckBox").is_selected():
    driver.find_element(By.ID, "AutoConfigureAPNCheckBox").click()
driver.find_element(By.ID, "btnNext1").click()

print("Saving..")
wd_until(wd15, EC.element_to_be_clickable((By.ID, "btnExit3")))
print("Complete")
driver.quit()