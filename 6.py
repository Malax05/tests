
import unittest
from selenium import webdriver
from selenium.webdriver.common import keys


class InitDriverTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    print("=========================================================")

    #initializing browser and verifying if the selected URL is accessible and has correct content by key values
    def testInit_driver_and_url(self):
        driver = self.driver
        driver.get("somesite.com")
        assert "Some title" in driver.title

        print("Init driver and url: PASS")

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()