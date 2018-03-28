from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_quote_and_retrieve_it_later(self):
        # Anna has heard about a cool new online quotation app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention get-quote
        self.assertIn('Self-Care', self.browser.title)


# She is invited to enter a service item to request straight away

# She sees "Basic Website" text. (Anna's startup company
# needs a basic website)

# When she clicks "Add +" button, the page updates, and now the page lists
# "1: Basic Website - Home, About, Services, Contact" as an item in a quotation

# There is still a list of services inviting her to add another item. She
# clicks "Add +" besides "Contact Form"
# (Anna is very methodical)

# The page updates again, and now shows both items on her quotation
# with prices and total cost.

# Anna wonders whether the site will remember her list. Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.

# She visits that URL - her quotation is still there.

# Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
