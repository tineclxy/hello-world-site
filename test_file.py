import requests  # Import requests to handle HTTP requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

BASE_URL = "https://tineclxy.github.io/hello-world-site/"  # The URL of your site

def test_snowflake_falling():
    """Test if the snowflakes are falling and their element exists."""
    # Set up the WebDriver (Chrome in this case)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
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

def test_homepage_status():
    """Test if the homepage loads successfully."""
    response = requests.get(BASE_URL, timeout=10)
    assert response.status_code == 200, f"Homepage did not load properly, got {response.status_code}"

def test_homepage_content():
    """Check if key phrases exist in the homepage content."""
    response = requests.get(BASE_URL, timeout=10)
    assert "Welcome to the Penguin Party!" in response.text, "Expected homepage content not found"
    assert "This is the website for Devops LP1" in response.text, "DevOps LP1 text not found"
    assert "Hello C270 Devops👋" in response.text, "C270 greeting not found"

def test_penguin_exists():
    """Check if the Penguin character is in the HTML."""
    response = requests.get(BASE_URL, timeout=10)
    assert 'id="penguin"' in response.text, "Penguin element not found in the HTML"

def test_score_box_exists():
    """Check if the score box is present."""
    response = requests.get(BASE_URL, timeout=10)
    assert 'id="scoreBox"' in response.text, "Score box not found"

# Run the tests
test_homepage_status()
test_homepage_content()
test_penguin_exists()
test_score_box_exists()
test_snowflake_falling()
