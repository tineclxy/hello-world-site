import requests

# Define the base URL of your deployed site
BASE_URL = "https://your-github-username.github.io/your-repo-name/"

def test_homepage_status():
    """Test if the homepage loads successfully."""
    response = requests.get(BASE_URL)
    assert response.status_code == 200, "Homepage did not load properly"

def test_homepage_content():
    """Check if a key phrase exists in the homepage content."""
    response = requests.get(BASE_URL)
    assert "Welcome to the Penguin Party!" in response.text, "Expected content not found"

def test_css_loading():
    """Ensure the CSS file is loading properly."""
    css_url = BASE_URL + "styles.css"  # Change if your CSS file is named differently
    response = requests.get(css_url)
    assert response.status_code == 200, "CSS file is not loading properly"

def test_clickable_penguin():
    """Test if the penguin click interaction works."""
    response = requests.get(BASE_URL)
    assert 'id="penguin"' in response.text, "Penguin element not found in the HTML"
