from selenium import webdriver
from selenium.webdriver.edge.service import Service

# Initialize the EdgeDriver using local path
service = Service("./msedgedriver.exe")
driver = webdriver.Edge(service=service)

# Open a website
driver.get("https://www.google.com")

# Print the page title
print("Page Title:", driver.title)

# Close the browser
driver.quit()