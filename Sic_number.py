from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service

# Set the path to the Edge WebDriver you downloaded
driver_path = 'C:/Users/TV04727P/OneDrive - Miller Insurance Services LLP/Desktop/msedgedriver.exe'

# Set the URL of the webpage you want to scrape
url = 'https://www.sec.gov/edgar/searchedgar/companysearch'

# Initialize the Edge WebDriver with the specified path
edge_service = Service(driver_path)
driver = webdriver.Edge(service=edge_service)

# Open the webpage
driver.get(url)

# Find the search input field and enter the company name
search_input = driver.find_element(By.ID, 'edgar-company-person')  # box search to be filled
company_name = 'Soleno Therapeutics Inc'  # Replace with the actual company name
search_input.send_keys(company_name)
search_input.send_keys(Keys.ENTER)


# Wait for the element to be present
wait = WebDriverWait(driver, 10)
sic_element = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'SIC=')]")))

# Get the text content of the <a> element, which represents the SIC number
sic_number = sic_element.text

print("SIC number:", sic_number)


# Close the browser
driver.quit()
