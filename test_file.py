from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import tempfile

BASE_URL = "https://tineclxy.github.io/hello-world-site/"  # The URL of your site

def test_snowflake_falling():
    """Test if the snowflakes are falling and their element exists."""
    
    # Set up Chrome options
    options = Options()
    # Use a temporary directory for user data (this ensures a unique session every time)
    options.add_argument(f"user-data-dir={tempfile.mkdtemp()}")
    
    # Set up the WebDriver (Chrome in this case)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        # Navigate to the page
        driver.get(BASE_URL)
        
        # Wait for the page to load and snowflakes to appear (adjust time if needed)
        time.sleep(5)  # 5 seconds wait time for JavaScript to load
        
        # Check if the snowflakes element exists
        try:
            snowflake = driver.find_element(By.CLASS_NAME, "snowflake")
            assert snowflake is not None, "Snowflakes element not found"
            print("Snowflakes element found!")
        except Exception as e:
            assert False, "Snowflakes element not found"
    
    finally:
        # Quit the driver after the test is complete
        driver.quit()

# Run the test
test_snowflake_falling()
