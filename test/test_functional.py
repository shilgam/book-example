from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    url = 'http://web:8000/'

    def setUp(self):
        selenium_hub_url = 'http://hub:4444/wd/hub'
        self.browser = webdriver.Remote(
            command_executor=selenium_hub_url,
            desired_capabilities=DesiredCapabilities.CHROME)

    def teamDown(self):
        self.browser.quit()

    def test_can_start_a_list(self):
        self.browser.get(self.url)

        # page title and header
        self.assertEqual('To-Do list', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # user is invited to enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # type into a text box
        inputbox.send_keys('Buy peacock feathers')

        # when user hits enter, the page updates, and now entered item
        # appears in the list table
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertTrue(
        #     any(row.text == '1: Buy peacock feathers' for row in rows),
        #     "New to-do item did not appear in table"
        # )


if __name__ == '__main__':
    unittest.main(warnings='ignore')