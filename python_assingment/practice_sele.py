from basicofselenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Navigate to the given URL
    driver.get("https://resilient-cendol-01c60b.netlify.app/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    print("Website loaded successfully.")

    # Test Carousel Functionality
    try:
        print("Testing carousel functionality...")
        carousel = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.carousel"))
        )
        next_button = driver.find_element(By.CSS_SELECTOR, ".carousel-control-next")
        prev_button = driver.find_element(By.CSS_SELECTOR, ".carousel-control-prev")
        
        # Navigate through the slides
        for _ in range(3):
            next_button.click()
            time.sleep(2)
            print("Moved to the next slide")
        
        for _ in range(3):
            prev_button.click()
            time.sleep(2)
            print("Moved to the previous slide")

        # Verify the active slide
        active_slide = driver.find_element(By.CSS_SELECTOR, ".carousel-item.active")
        print("Current active slide content:", active_slide.text)

    except Exception as carousel_error:
        print(f"Error testing carousel: {carousel_error}")

    # Function to test login functionality
    def login_and_test(email, password, expected_result):
        try:
            print(f"Testing login with email='{email}' and password='{password}'...")
            
            # Locate elements
            email_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            password_field = driver.find_element(By.ID, "password")
            submit_button = driver.find_element(By.ID, "submit")
            
            # Clear fields and enter credentials
            email_field.clear()
            password_field.clear()
            email_field.send_keys(email)
            password_field.send_keys(password)
            submit_button.click()
            
            # Check the expected result
            if expected_result == "success":
                WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
                print(f"Test Passed: Login succeeded with email='{email}' and password='{password}'")
            else:
                error_message = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".error-message"))
                )
                assert error_message.is_displayed(), "Error message not displayed."
                print(f"Test Passed: Correctly detected invalid input for email='{email}' and password='{password}'")
        except Exception as login_error:
            print(f"Test Failed: {login_error}")
        finally:
            # Refresh and ensure the login page is ready
            driver.refresh()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn"))).click()

    # Ensure the login page is accessible
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
    
    # Test cases for login functionality
    test_cases = [
        {"email": "valid_user@example.com", "password": "ValidPassword123", "expected_result": "success"},
        {"email": "invalid_user@example.com", "password": "WrongPassword", "expected_result": "failure"},
        {"email": "", "password": "ValidPassword123", "expected_result": "failure"},
        {"email": "valid_user@example.com", "password": "", "expected_result": "failure"},
    ]
    
    for test_case in test_cases:
        login_and_test(test_case["email"], test_case["password"], test_case["expected_result"])
    
    print("All test cases completed successfully.")

except Exception as main_error:
    print(f"An unexpected error occurred: {main_error}")
finally:
    driver.quit()
