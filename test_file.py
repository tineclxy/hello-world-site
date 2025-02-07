import requests

# Set the base URL for the GitHub Pages site
BASE_URL = "https://tineclxy.github.io/hello-world-site/"

def test_homepage_status():
    """Test if the homepage loads successfully (HTTP 200 OK)."""
    response = requests.get(BASE_URL)
    print(f"Status Code: {response.status_code}")  # Debugging
    assert response.status_code == 200, "Homepage did not load properly"

def test_homepage_content():
    """Check if a key phrase exists in the homepage content."""
    response = requests.get(BASE_URL)
    print(f"Response Text: {response.text[:500]}")  # Debugging, prints first 500 chars
    assert "Welcome to the Penguin Party!" in response.text, "Expected content not found"

def test_css_loading():
    """Ensure the CSS file is loading properly."""
    css_url = BASE_URL + "styles.css"  # Adjust the path if necessary
    response = requests.get(css_url)
    print(f"CSS Status Code: {response.status_code}")  # Debugging
    assert response.status_code == 200, "CSS file is not loading properly"

def test_clickable_penguin():
    """Test if the penguin element exists in the HTML."""
    response = requests.get(BASE_URL)
    print(f"Response Text: {response.text[:500]}")  # Debugging
    assert 'id="penguin"' in response.text, "Penguin element not found in the HTML"
