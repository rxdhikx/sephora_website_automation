from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Define the query and open the search page
query = "lipstick"
driver.get(f"https://www.sephora.com/search?keyword={query}")

# Wait for the page to load
time.sleep(6)

# Handling JavaScript Alert/Confirm/Prompt pop-ups
try:
    # If an alert is present, switch to it and accept or dismiss it
    alert = Alert(driver)
    alert.accept()  # Accept the alert (click OK)
    print("Alert handled.")
except:
    print("No alert found.")

#Handling modal dialogs (custom pop-ups)
try:
    #the modal has a button with class "modal-close" to close it
    close_button = driver.find_element(By.CLASS_NAME, "modal-close")
    close_button.click()
    print("Modal closed.")
except:
    print("No modal found.")

#Find the search results or element
try:
    elems_firstfew = driver.find_elements(By.CLASS_NAME, "css-foh208") #lipstick
    print("Printing first few product details:")
    for elem in elems_firstfew:
        print(elem.text)

    elems_next = driver.find_elements(By.CLASS_NAME, "css-1qe8tjm") #lipstick
    # print(f"{len(elems_firstfew)} items found")
    # print(f"{len(elems_next)} items found")
    
    total_elements = len(elems_firstfew) + len(elems_next)
    print(f"Total elements found across the page: {total_elements}")
    
except Exception as e:
    print(f"An error occurred while fetching the element: {e}")

# Keep the browser open indefinitely
print("Browser will stay open indefinitely. Press Ctrl+C to exit.")
try:
    while True:
        time.sleep(1)  # Keeps the loop running to hold the browser open
except KeyboardInterrupt:
    print("\nExiting script...")

# Gracefully close the browser
driver.quit()
