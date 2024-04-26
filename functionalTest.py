import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

images = ["images/5906ChurchillMeadows.PNG", "images/3956Beacham.PNG", "images/1540Elite.PNG", "images/3761Trelawny.PNG", "images/50-7430Copenhagen.PNG"]

# Helper Function
def image_src_contains(expected_filename, driver):
    try:
        image_element = driver.find_element(By.ID, 'picture')
        return expected_filename in image_element.get_attribute('src')
    except NoSuchElementException:
        return False

class RealEstatePredictorTest(unittest.TestCase):

    # The setUp() and tearDown() methods allow you to define instructions that will be executed 
    # before and after each test method. (from documentation)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:5500/RealEstatePredictor.html')

    def test_display(self):
        # RE-01 The webpage must show an image of the house with its estimated value.
        # RE-06	Each webpage will have a comments section consisting of a username text area, a comment text area, and a submit button.

        driver = self.driver
        image = driver.find_element(By.ID, 'picture')
        value = driver.find_element(By.ID, 'value')
        username = driver.find_element(By.CLASS_NAME, 'username')
        comment = driver.find_element(By.CLASS_NAME, 'comment')
        submit_button = driver.find_element(By.ID, 'submit')

        self.assertTrue(image.is_displayed())
        self.assertTrue(value.is_displayed())
        self.assertTrue(username.is_displayed())
        self.assertTrue(comment.is_displayed())
        self.assertTrue(submit_button.is_displayed())

    def test_navigation_buttons(self):
        # RE-02	The webpage must have a PREV button to go to the previous image.
        # RE-03	The webpage must have a NEXT button to go to the next image.

        driver = self.driver
        prev_button = driver.find_element(By.ID, 'prev')
        next_button = driver.find_element(By.ID, 'next')
            
        next_button.click()
        WebDriverWait(driver, 10).until(lambda d: image_src_contains(images[1], driver))
        
        prev_button.click()
        WebDriverWait(driver, 10).until(lambda d: image_src_contains(images[0], driver))

    def test_wrap_around(self):
        # RE-04	If we are at the first image, PREV will wrap around and take us to the last image.
        # RE-05	If we are at the last image, NEXT will wrap around and take us to the first image.

        driver = self.driver
        prev_button = driver.find_element(By.ID, 'prev')
        next_button = driver.find_element(By.ID, 'next')
        
        # When the page loads in the beginning of the this test, by default we will be at the first image
        # clicking on the previous button should take us to the last image
        prev_button.click()
        WebDriverWait(driver, 10).until(lambda d: image_src_contains(images[-1], driver))

        # on sucessfully clicking on the previous button we should be on the last image
        # clicking on the next button should take us to the first image
        next_button.click()
        WebDriverWait(driver, 10).until(lambda d: image_src_contains(images[0], driver))

    def test_comment_submission(self):
        # RE-07	All submitted comments will be displayed below the submit button.
        # RE-08	All submitted comments will display as username first and comment after.
        # RE-11	The username and comment text areas should clear after a submit.

        driver = self.driver
        username_input = driver.find_element(By.CLASS_NAME, 'username')
        comment_input = driver.find_element(By.CLASS_NAME, 'comment')
        submit_button = driver.find_element(By.ID, 'submit')
        
        # Submitting a coment
        test_username = 'Testing'
        test_comment = 'This is a test comment.'
        username_input.send_keys(test_username)
        comment_input.send_keys(test_comment)
        submit_button.click()
    
        # Checking the comment
        comments_section = driver.find_element(By.ID, 'blogs')
        comments_html = comments_section.get_attribute('innerHTML')

        # Check if the username(bold) and is before the comment text
        expected_comment_html = f'<b>{test_username}</b>: {test_comment}'
        self.assertIn(expected_comment_html, comments_html)

        # are text areas cleared after submission
        self.assertEqual(username_input.text, '')
        self.assertEqual(comment_input.text, '')

    def test_comments_persistence(self):
        # RE-09 All submitted comments will be permanent, they will not be deleted if we go to the next image.

        driver = self.driver

        # Submitting three different comments on three different images
        test_username = ['Aeraf', 'Madhur', 'Tasbi']
        test_comment = ['Aeraf was here', 'Madhur was here', 'Tasbi was here']

        for i in range(3):
            username_input = driver.find_element(By.CLASS_NAME, 'username')
            comment_input = driver.find_element(By.CLASS_NAME, 'comment')
            submit_button = driver.find_element(By.ID, 'submit')

            username_input.send_keys(test_username[i])
            comment_input.send_keys(test_comment[i])
            submit_button.click()

            # Navigate to the next image
            next_button = driver.find_element(By.ID, 'next')
            next_button.click()
            
            WebDriverWait(driver, 10).until(lambda d: image_src_contains(images[(i + 1) % len(images)], driver))

        # navigating back to check for persistence
        prev_button = driver.find_element(By.ID, 'prev')
        for i in reversed(range(3)):
            # Navigate back to the previous image
            prev_button.click()
            WebDriverWait(driver, 10).until(lambda d: image_src_contains(images[(i % len(images))], driver))

            # Check if the submitted comment is still there
            comments_section = driver.find_element(By.ID, 'blogs')
            expected_comment = f'<b>{test_username[i]}</b>: {test_comment[i]}'
            assert expected_comment in comments_section.get_attribute('innerHTML')

    def test_1000_comments(self):
        # RE-10: Each webpage should be able to accommodate at least 1000 comments.
        # RE-12: The comments should be scrollable.
        driver = self.driver
        username_input = driver.find_element(By.CLASS_NAME, 'username')
        comment_input = driver.find_element(By.CLASS_NAME, 'comment')
        submit_button = driver.find_element(By.ID, 'submit')
        comments_section = driver.find_element(By.ID, 'blogs')

        # Submitting 1000 comments in a loop
        for i in range(1000):
            username_input.send_keys(f'User {i}')
            comment_input.send_keys(f'Comment number {i}')
            submit_button.click()

            # input fields will be cleared after sumit is pressed

        # for manual validation
        # time.sleep(60)

        comments = comments_section.find_elements(By.TAG_NAME, 'b')  # tag <b> as every username is bolded (line 13 in Homes.js)
        self.assertTrue(len(comments) >= 1000, "Not all comments are displayed")


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
