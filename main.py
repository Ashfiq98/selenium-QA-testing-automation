# main.py
from currency_check import CurrencySelectionBot  # Adjust the import path accordingly
from check_urls import run_tests_url
from upto_alt import run_tests
from scraped_data import ScrapeData


def main():
    # Run all tests in sequence
    # URL of the page you want to test
    currency_url = "https://www.alojamiento.io/property/cabrils/BC-1178728"
    url = "https://www.alojamiento.io/"

    # 1
    run_tests(url)
    # 2
    run_tests_url(url)
    # 3
    # Create an instance of CurrencySelectionBot
    bot = CurrencySelectionBot(currency_url)
    # Run the test
    if bot.run_currency_selection_test():
        print("✅ Currency Selection Test Completed Successfully!")
        # Generate the Excel report
        bot.generate_excel_report()
    else:
        print("❌ Currency Selection Test Failed")
    # 4
    scraper = ScrapeData(url)
    scraper.scrape_data()
    scraper.close()


if __name__ == "__main__":
    main()
