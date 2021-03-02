import shelve
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAddperson:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_addperson(self):
        db = shelve.open("./mydbs/cookies")
        cookies = db['cookie']
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        self.driver.find_element(By.ID, "js_upload_file_input").send_keys('D:\outlooks\mybook.xlsx')
        assert "mybook.xlsx" == self.driver.find_element(By.ID, "upload_file_name").text
