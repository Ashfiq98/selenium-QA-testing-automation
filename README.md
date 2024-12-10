Here is a well-structured README.md file for your Vacation Rental Home Page Automation Testing project:

# Vacation Rental Home Page Automation Testing

## Project Description
This project automates the testing of a vacation rental details page to validate essential elements and functionality. The script checks for SEO-impacted test cases such as h1 tag existence, HTML tag sequence, image alt attribute validation, checking for broken URLs, currency filter functionality, and scraping script data. The results are recorded in an Excel file.

## Requirements
- **Tools:** Python with Selenium and Pandas libraries
- **Browser:** Google Chrome or Firefox with WebDriver
- **Test Site URL:** https://www.alojamiento.io/

## Tests Performed
1. **H1 Tag Existence Test:** Checks if the H1 tag is present, and reports a failure if it is missing.
2. **HTML Tag Sequence Test:** Checks if the [H1-H6] tag sequence is correct, and reports a failure if the sequence is broken or missing.
3. **Image Alt Attribute Test:** Checks if the image alt attribute is present, and reports a failure if it is missing.
4. **URL Status Code Test:** Checks the status code of all URLs, and reports a failure if any URL has a 404 status.
5. **Currency Filtering Test:** Checks if the property tiles' currency changes according to the selected currency.
6. **Data Scraping:** Scrapes data from the script and records it in an Excel file, including SiteURL, CampaignID, SiteName, Browser, CountryCode, and IP.

## Acceptance Criteria
1. The code and methods should be reusable.
2. The report model should include page_url, testcase, passed/fail, and comments.

## Getting Started

1. Clone the repository:
   ```
   git clone https://github.com/Ashfiq98/selenium-QA-testing-automation.git
   ```
   ```
   cd selenium-QA-testing-automation
   ```
2. Create a virtual environment and activate it:
   ```
   python -m venv my_env
   ```
   ```
   source my_env/bin/activate  # On Windows, use `my_env\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the main script:
   ```
   python main.py
   ```

5. If the WebDriver is not working, update the ChromeDriver or provide the local path:
   ```python
   # If it's not working:
   self.service = Service(ChromeDriverManager().install())
   # Then use the local path like this , where your updated driver is located:
   self.service = Service("C:/<Your drivers path>/chromedriver.exe")
   ```

The results will be stored in the `report/all_the_reports.xlsx` file.

## Author
Ashfiq98