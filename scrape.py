import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import openpyxl

class ScrapeSecondarySlider:
    def __init__(self, url):
        """
        Initialize the scraper with the provided URL and set up WebDriver.
        """
        options = Options()
        options.headless = False  # Set to True to run in headless mode
        # Initialize the WebDriver with the correct options
        self.driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()), options=options)
        self.url = url
        self.driver.get(self.url)

    def scrape_data(self):
        """
        Scrapes data from the SecondarySlider JSON and saves it in an Excel file.
        """
        data = []

        # Find the <script> element containing the SecondarySliderData (adjust selector if needed)
        script_element = self.driver.find_element(By.XPATH, "//script[contains(text(), 'SecondarySliderData')]")
        script_content = script_element.get_attribute('innerHTML')

        # Extract the JSON data using string manipulation (this assumes the JSON is within the <script> tag)
        try:
            # Find the start and end of the JSON data
            start_index = script_content.index('SecondarySliderData = ') + len('SecondarySliderData = ')
            end_index = script_content.index('];', start_index) + 1
            json_data = script_content[start_index:end_index]

            # Parse the JSON data
            secondary_slider_data = json.loads(json_data)
            print(secondary_slider_data)

            # Iterate through each item and extract required information
            for item in secondary_slider_data:
                row = {
                    "SiteURL": item.get('SiteURL', ''),
                    "CampaignID": item.get('CampaignID', ''),
                    "SiteName": item.get('SiteName', ''),
                    "Browser": item.get('Browser', ''),
                    "CountryCode": item.get('CountryCode', ''),
                    "IP": item.get('IP', '')
                }
                data.append(row)

            # Save the data to an Excel file
            self.save_to_excel(data)

        except Exception as e:
            print(f"Error extracting JSON data: {e}")

    def save_to_excel(self, data):
        """
        Saves the scraped data to an Excel file.
        """
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Secondary Slider Data"

        # Define the headers for the Excel file
        headers = ['SiteURL', 'CampaignID', 'SiteName', 'Browser', 'CountryCode', 'IP']
        sheet.append(headers)

        # Write the rows of data into the sheet
        for row in data:
            sheet.append([row['SiteURL'], row['CampaignID'], row['SiteName'], row['Browser'], row['CountryCode'], row['IP']])

        # Save the workbook to a file
        file_path = "reports/secondary_slider_data.xlsx"
        workbook.save(file_path)
        print(f"Data saved to {file_path}")

    def close(self):
        """
        Close the WebDriver.
        """
        self.driver.quit()

# Entry point for running the scraper
if __name__ == "__main__":
    url = "https://www.alojamiento.io/"
    scraper = ScrapeSecondarySlider(url)
    scraper.scrape_data()
    scraper.close()
