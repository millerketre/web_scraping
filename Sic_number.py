from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from ms import retrieve_company


def connect_to_website():
    company_names = retrieve_company()
    sic_company= {}
    try: 
        # Set the path to the Edge WebDriver you downloaded
        driver_path = 'C:/Users/TV04727P/OneDrive - Miller Insurance Services LLP/Desktop/msedgedriver.exe'

        # Set the URL of the webpage you want to scrape
        url = 'https://www.sec.gov/edgar/searchedgar/companysearch'

        # Initialize the Edge WebDriver with the specified path
        edge_service = Service(driver_path)
        driver = webdriver.Edge(service=edge_service)

        # Open the webpage
        driver.get(url)
    except Exception as e:
        print(f"An error occurred: {e}")

    
    # Find the search input field and enter each of the company names one at the time
    for company_name in company_names:
        # Wait for the page to load
        wait = WebDriverWait(driver, 10)
        search_input = wait.until(EC.presence_of_element_located((By.ID, 'edgar-company-person')))  # box search to be filled
        search_input.clear()  # clear the search box
        search_input.send_keys(company_name)
        
        
        # Click the search button
        search_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Search']")))
        search_button.click()
        
        
         # Dismiss the alert if it appears
        try:
            alert = driver.switch_to.alert
            alert.dismiss()
        except:
            pass
       
        # use xpath to find the sic number on page
        sic_element = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'SIC=')]")))
        
        # add company name and sic number to dictionary
        sic_number = sic_element.text
        sic_company[company_name] = sic_number
        print("SIC number:", sic_number)
        
        #go back to homepage
        driver.back()
 

    # Close the browser
    driver.quit()
    return sic_company


print(connect_to_website())