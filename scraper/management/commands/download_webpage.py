import asyncio
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.core.management.base import BaseCommand



SITOWEB = "https://sportitaliabet.it/scommesse/prematch/calcio/1/palinsesto/calcio-popolari-calcio-48h-top-200/33/true"
POPUP = "iubenda-cs-reject-btn.iubenda-cs-btn-primary"
PREMATCHMASTERGROUP = "prematch-group-filters__mastergroup.filter-collapsible__item.ng-star-inserted"
TEAMNAMELABEL = "match-row__match__headings__team__label"

class Command(BaseCommand):
    help = 'Asynchronously scrapes sports betting data from a dynamic webpage using Selenium'

    def handle(self, *args, **options):
        asyncio.run(self.main())

    async def main(self):
        loop = asyncio.get_running_loop()
        with ThreadPoolExecutor() as pool:
            driver = await loop.run_in_executor(pool, self.setup_driver)
            await self.process_all_groups(driver, loop, pool)
            driver.quit()

    def setup_driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(SITOWEB)
        self.close_popup(driver)
        return driver

    def close_popup(self, driver):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, POPUP))
        ).click()

    async def process_all_groups(self, driver, loop, pool):
        master_groups = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, PREMATCHMASTERGROUP))
        )
        for group in master_groups:
            await loop.run_in_executor(pool, self.process_group, driver, group)

    def process_group(self, driver, group):
        group.click()
        # Additional processing and handling
        elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, TEAMNAMELABEL))
        )
        for element in elements:
            print(f"Team: {element.text}")
