import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Set up Chrome WebDriver with the path to chromedriver
service = Service(executable_path='C:/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)


try:
    # Open the login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Wait for the username and password fields to be present
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']"))
    )
    password_field = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']"))
    )

    # Enter credentials
    username_field.send_keys("Admin")
    password_field.send_keys("admin123")

    # Wait for the login button to be clickable
    login_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit' and contains(@class, 'orangehrm-login-button')]"))
    )
    login_button.click()

    print("Login action performed successfully!")

    # Wait for the dashboard to load and the Admin link to be clickable
    admin_link = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@href='/web/index.php/admin/viewAdminModule' and contains(@class, 'oxd-main-menu-item')]"))
    )

    # Click on the Admin link
    admin_link.click()
    print("Admin link clicked successfully!")

    # Wait for the search results to load (Modify this based on what you expect)
    time.sleep(20)  # Adjust the time as needed to observe the results

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
