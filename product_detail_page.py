from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re

class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        # Locators
        self.product_cards = (By.CLASS_NAME, "css-foh208")
        self.additional_products = (By.CLASS_NAME, "css-1qe8tjm")
        self.product_links = (By.CSS_SELECTOR, "a[data-comp='ProductCard']")
        
    def get_all_products(self):
        """Get all products from the search results"""
        products = []
        try:
            # Wait for and get initial products
            initial_products = self.wait.until(
                EC.presence_of_all_elements_located(self.product_cards)
            )
            products.extend(initial_products)
            
            # Get additional products if they exist
            try:
                additional_products = self.driver.find_elements(*self.additional_products)
                products.extend(additional_products)
            except:
                pass
                
            return products
        except TimeoutException:
            print("No products found on the page")
            return []
            
    def filter_products(self, pattern):
        """Filter products based on regex pattern"""
        products = self.get_all_products()
        return [
            product for product in products
            if re.search(pattern, product.text, re.IGNORECASE)
        ]
        
    def click_product(self, index=0):
        """Click on a product by index and return ProductDetailPage"""
        try:
            products = self.wait.until(
                EC.presence_of_all_elements_located(self.product_links)
            )
            if 0 <= index < len(products):
                products[index].click()
                from product_detail_page import ProductDetailPage
                return ProductDetailPage(self.driver)
            else:
                raise IndexError("Product index out of range")
        except TimeoutException as e:
            print(f"Error clicking product: {e}")
            return None
