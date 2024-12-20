from selenium import webdriver
from home_page import HomePage

def main():
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    try:
        # Initialize HomePage and navigate
        home_page = HomePage(driver)
        home_page.navigate_to_home()
        
        # Search for a product
        search_term = input("Enter product to search: ")
        results_page = home_page.search_product(search_term)
        
        if results_page:
            # Optional: Filter results
            filter_pattern = input("Enter regex pattern to filter (or press Enter to skip): ")
            if filter_pattern:
                filtered_products = results_page.filter_products(filter_pattern)
                print(f"\nFound {len(filtered_products)} matching products")
            
            # Click first product and get details
            product_page = results_page.click_product(0)
            if product_page:
                details = product_page.get_product_details()
                if details:
                    print("\nProduct Details:")
                    for key, value in details.items():
                        print(f"{key.capitalize()}: {value}")
        
        input("\nPress Enter to close browser...")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
