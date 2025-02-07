import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest

# Setup WebDriver
@pytest.fixture
def driver():
    options = Options()
    # Uncomment for headless mode
    # options.add_argument("--headless")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

# Test to check the penguin wobble animation
def test_penguin_wobble(driver):
    driver.get("file:///" + "/path/to/your/index.html")  # Replace with actual file path
    penguin = driver.find_element(By.ID, "penguin")
    
    # Click on penguin and test wobble
    penguin.click()
    
    # Wait for the animation to complete
    time.sleep(3)
    
    # Check if penguin is in wobble position (rotate is applied)
    assert penguin.value_of_css_property('transform') != 'matrix(1, 0, 0, 1, 0, 0)'  # Not the default transform matrix

# Test to check snowflakes
def test_snowflake_creation(driver):
    driver.get("file:///" + "/path/to/your/index.html")  # Replace with actual file path
    
    initial_snowflakes = len(driver.find_elements(By.CLASS_NAME, "snowflake"))
    
    # Wait a bit to allow snowflakes to appear
    time.sleep(5)
    
    new_snowflakes = len(driver.find_elements(By.CLASS_NAME, "snowflake"))
    
    # Ensure that new snowflakes were created
    assert new_snowflakes > initial_snowflakes
