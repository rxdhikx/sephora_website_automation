from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        # Locators
       
        self.search_box = (By.CSS_SELECTOR, "[data-comp='TextInput']")
        self.search_button = (By.CSS_SELECTOR, "button[data-comp='SearchButton']")
        self.modal_close = (By.CLASS_NAME, "modal-close")
        
    def navigate_to_home(self):
        """Navigate to Sephora homepage"""
        self.driver.get("https://www.sephora.com")
        self.handle_popups()
        return self
        
    def handle_popups(self):
        """Handle any popups that appear on page load"""
        try:
            alert = Alert(self.driver)
            alert.accept()
        except:
            pass
            
        try:
            close_button = self.wait.until(EC.element_to_be_clickable(self.modal_close))
            close_button.click()
        except TimeoutException:
            pass
            
    def search_product(self, product_name):
        """Search for a product and return SearchResultsPage"""
        try:
            search_input = self.wait.until(EC.element_to_be_clickable(self.search_box))
            search_input.clear()
            search_input.send_keys(product_name)
            
            search_btn = self.wait.until(EC.element_to_be_clickable(self.search_button))
            search_btn.click()
            
            # Return SearchResultsPage instance
            from search_results_page import SearchResultsPage
            return SearchResultsPage(self.driver)
            
        except TimeoutException as e:
            print(f"Error during search: {e}")
            return None
