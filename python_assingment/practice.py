from basicofselenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome WebDriver with WebDriver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL of the login page
login_url = "https://mymedia718.netlify.app"

try:
    # Step 1: Open the login page
    driver.get(login_url)
    time.sleep(2)  # Wait for the page to load

    # Step 2: Locate the username and password fields
    username_field = driver.find_element(By.NAME, "username")  # Update with actual HTML name or ID
    password_field = driver.find_element(By.NAME, "password")  # Update with actual HTML name or ID

    # Step 3: Enter credentials
    username_field.send_keys("testuser")  # Replace with a valid username
    password_field.send_keys("testpassword")  # Replace with a valid password

    # Step 4: Locate and click the login button
    login_button = driver.find_element(By.ID, "login-button")  # Update with actual button ID
    login_button.click()

    # Step 5: Verify successful login
    time.sleep(3)  # Wait for the page to load
    current_url = driver.current_url
    if "dashboard" in current_url:  # Check if redirected to a dashboard page
        print("Login successful!")
    else:
        print("Login failed!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()