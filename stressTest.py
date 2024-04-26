import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class RealEstateStressTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:5500/RealEstatePridictor.html')

    def test_stress_comments(self):
        driver = self.driver
        num_comments_per_page = 1500    # changed this value to get the results
        num_pages = 5

        for page in range(num_pages):
            start_time = time.time()
            for comment_num in range(num_comments_per_page):
                username_input = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, 'username')))
                comment_input = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, 'comment')))
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, 'submit')))

                # Submit a comment
                username_input.send_keys(f'User {comment_num}')
                comment_input.send_keys(f'Stress comment {comment_num} on page {page}')
                submit_button.click()

                if (comment_num + 1) % 100 == 0:
                    end_time = time.time()
                    print(f"Submitted {comment_num + 1} comments on page {page}, time taken: {end_time - start_time} seconds")
                    start_time = time.time()

            # going to the next page
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'next'))).click()


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


