# **Automated Product Search and Scraping on Sephora using Selenium and Python**

## **Project Overview**

This project automates product searches on **Sephora’s website**, scraping results based on a user-defined query (e.g., *Lipstick*). <br>
It validates the search functionality and retrieves product details like name, price, and the number of products found on the webpage.

## **Technologies Used**

- **Python**: The scripting language used to develop the automation workflow.
- **Selenium WebDriver**: Automates browser interactions (search, data scraping) to simulate real user behavior.
- **ChromeDriver**: A necessary component for Selenium to interface with Chrome, allowing browser interactions.
- **WebDriverWait**: To handle dynamic page loading and ensure elements are present before interacting with them, improving script reliability.


## **Use Case**
As e-commerce websites like **Sephora** handle an enormous amount of product data and user interactions, ensuring that their search functionalities work as expected is crucial. This project automates the process of testing how many products appear when a user searches for a product, verifying that the search functionality returns the correct results. The automation covers the following tasks:

- Navigate to **www.sephora.com**
- Input a search query (e.g., *Lipstick*) in the search bar
- Retrieve and display the number of products related to the search term
- Automatically interact with search results, and scrape product data (name, price, etc.)

This automated workflow can be extended for regression testing, helping QA teams and developers ensure that search functionalities are not broken during updates or deployments.



## **Implementation**

1. **Navigate to Sephora**: Opens the homepage with `driver.get()`.
2. **Search Bar Input**: Locates and enters a query into the search bar.
3. **Scrape Results**: Extracts product details like name and price.
4. **Dynamic Input**: User provides the search query before running the script.

## **Test Case & Results**
The script checks that the search results match the expected number of products, validating the search functionality.


![image](https://github.com/user-attachments/assets/0b2ebd95-111d-46f1-ab3a-3edf253327f5)



