
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import time

class Custom_Webdriver:
# class Webdriver(MALT_URL, MALT_USERNAME, MALT_PASSWORD):

    def __init__(self, MALT_URL, MALT_USERNAME, MALT_PASSWORD):
        self.MALT_URL       = MALT_URL
        self.MALT_USERNAME  = MALT_USERNAME
        self.MALT_PASSWORD  = MALT_PASSWORD

    def generate_browser(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.MALT_URL)
        time.sleep(5)

    def login(self):
        element = self.driver.find_element_by_id('signinlink')
        time.sleep(10)
        element.click()

        ##### USERNAME #####
        time.sleep(2)
        username_element = self.driver.find_element_by_id('j_username')
        time.sleep(2)
        username_element.send_keys(self.MALT_USERNAME)
        time.sleep(2)

        ##### PASSWORD #####
        password_element = self.driver.find_element_by_id('signin_password')
        time.sleep(2)
        password_element.send_keys(self.MALT_PASSWORD)
        time.sleep(2)

        ##### SIGNIN #####
        self.driver.find_element_by_id('btnSignin').click()

    def search(self, MALT_SEARCH_KEYWORD, MALT_SEARCH_LOCATION):
        ##### SEARCH #####
        time.sleep(5)
        self.driver.find_element_by_id('main-header-search').click()

        ##### ENTERING KEY WORDS #####
        time.sleep(5)
        self.driver.find_element_by_id('q2').clear()
        self.driver.find_element_by_id('q2').send_keys(MALT_SEARCH_KEYWORD)
        #self.driver.find_element_by_id('q2').send_keys(self.MALT_SEARCH_KEYWORD)

        ##### ENTERING THE LOCATION #####
        ##### Need to clear the field first #####
        time.sleep(4)
        length_current_search = len(self.driver.find_element_by_id('location2').get_attribute('value'))
        self.driver.find_element_by_id('location2').click()
        while length_current_search > 0:
            # Gets to the middle of the text, so need to delete what's on the left (BACK_SPACE) and what's on the right (DELETE)
            self.driver.find_element_by_id('location2').send_keys(Keys.BACK_SPACE)
            self.driver.find_element_by_id('location2').send_keys(Keys.DELETE)
            length_current_search = len(self.driver.find_element_by_id('location2').get_attribute('value'))
        time.sleep(2)
        #self.driver.find_element_by_id('location2').send_keys(self.MALT_SEARCH_LOCATION)
        self.driver.find_element_by_id('location2').send_keys(MALT_SEARCH_LOCATION)

        ##### VALIDATING THE SEARCH #####
        time.sleep(5)
        self.driver.find_element_by_id('searchBtn2').click()

    def getting_num_pages(self):
        html_code = self.driver.page_source
        soup = BeautifulSoup(html_code, 'html.parser')
        freelance_list = soup.findAll("section", {"class": "profile-card"})

        pages_list = soup.find('ul', 'results-pager__list').find_all('a','results-pager__item')
        pages_list = [x.text.strip() for x in pages_list]
        num_pages = int(pages_list[-1])
        return num_pages

    def generate_paged_url_and_go(self,page_number):
        original_url = self.driver.current_url
        if original_url.find('&p=') != -1:
            index_page = original_url.find('&p=')
            paged_url = original_url[:index_page] + f'&p={page_number}' #str(page_number)
        else:
            paged_url = original_url + f'&p={page_number}'
        # Go, and return the URL we went to
        self.driver.get(paged_url)
        return paged_url # Output is the URL with the page number

    def getting_freelance_list(self):
        #original_url = self.driver.current_url
        #url = self.generate_paged_url(original_url, page_number)
        #self.driver.get(url)
        html_code = self.driver.page_source
        soup = BeautifulSoup(html_code, 'html.parser')
        freelance_list = soup.findAll("section", {"class": "profile-card"})
        return freelance_list # This is a list of HTML code. Each element reprensenting 1 freelance
