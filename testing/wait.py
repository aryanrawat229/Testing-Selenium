from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Edge WebDriver
service = Service("./msedgedriver.exe")
options = Options()
driver = webdriver.Edge(service=service, options=options)

# 🔸 Add Implicit Wait
driver.implicitly_wait(5)  # Applies globally to all find_element calls

# Open the page
driver.get("https://the-internet.herokuapp.com/download")

# 🔸 Use Explicit Wait for the specific link
link_text = "WhatsApp Image 2025-07-01 at 3.47.51 PM.jpeg"

# Wait until the link is visible AND clickable
download_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, link_text))
)

# Click the download link
download_link.click()

# Optional: brief pause to let download complete
time.sleep(5)

# Close browser
driver.quit()