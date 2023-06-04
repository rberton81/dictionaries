# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.utils import initialize_django

initialize_django()

from backend.models import RegisteredCompany
import collections


Company = collections.namedtuple("Company", "name symbol industry offer_date shares offer_price")

def to_Company(columns):
    return Company(*[column.text for column in columns[:6]])

def init_chrome_driver():
    driver = webdriver.Firefox()
    return driver

def main():
    driver=None
    try:
        driver=init_chrome_driver()
        url = "https://www.iposcoop.com/last-100-ipos/"
        driver.get(url)

        table = driver.find_element(By.ID, "DataTables_Table_0")
        rows = table.find_elements(By.TAG_NAME, "tr")

        first = True
        for row in rows:
            if first:
                first=False
                continue
            columns = row.find_elements(By.TAG_NAME, "td")
            company_tuple = to_Company(columns)
            RegisteredCompany.objects.create(
                name=company_tuple.name,
                industry=company_tuple.industry,
                integration='IPO',
                is_active = True,
                ipo_date = company_tuple.offer_date,
                ticker=company_tuple.symbol,
            )

    except Exception as error:
        print(f"error {error}")
    finally:
        driver.close()
        driver.quit()

if __name__ == "__main__":
    main()
