import requests

BASE_URL = "https://tineclxy.github.io/hello-world-site/"

TIMEOUT = 10  # Timeout after 10 seconds for the requests

def test_homepage_status():
    """Test if the homepage loads successfully."""
    response = requests.get(BASE_URL, timeout=TIMEOUT)
    assert response.status_code == 200, f"Homepage did not load properly, got {response.status_code}"

def test_homepage_content():
    """Check if key phrases exist in the homepage content."""
    response = requests.get(BASE_URL, timeout=TIMEOUT)
    assert "Welcome to the Penguin Party!" in response.text, "Expected homepage content not found"
    assert "This is the website for Devops LP1" in response.text, "DevOps LP1 text not found"
    assert "Hello C270 Devops👋" in response.text, "C270 greeting not found"

def test_penguin_exists():
    """Check if the Penguin character is in the HTML."""
    response = requests.get(BASE_URL, timeout=TIMEOUT)
    assert 'id="penguin"' in response.text, "Penguin element not found in the HTML"

def test_score_box_exists():
    """Check if the score box is present."""
    response = requests.get(BASE_URL, timeout=TIMEOUT)
    assert 'id="scoreBox"' in response.text, "Score box not found"

def test_igloo_exists():
    """Check if the igloo section is present."""
    response = requests.get(BASE_URL, timeout=TIMEOUT)
    assert 'class="igloo"' in response.text, "Igloo section not found"

def test_snow_exists():
    """Check if the snow section is present."""
    response = requests.get(BASE_URL, timeout=TIMEOUT)
    assert 'class="snow"' in response.text, "Snow section not found"
