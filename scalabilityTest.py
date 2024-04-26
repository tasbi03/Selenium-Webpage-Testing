import threading
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def simulate_user_actions(user_id, num_actions):
    start_time = time.time()

    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:5500/RealEstatePredictor.html')

    for action in range(num_actions):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'next' if action % 2 == 0 else 'prev'))).click()

        username_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'username')))
        comment_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'comment')))
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'submit')))

        username_input.send_keys(f'User_{user_id}_Action_{action}')
        comment_input.send_keys(f'Comment for action {action} by User {user_id}')
        submit_button.click()

    end_time = time.time()  # End timing
    driver.quit()

    print(f'User {user_id} completed {num_actions} actions in {end_time - start_time} seconds.')

def scalability_test(num_users, num_actions_per_user):
    threads = []
    for user_id in range(num_users):
        thread = threading.Thread(target=simulate_user_actions, args=(user_id, num_actions_per_user))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

scalability_test(5, 1500)
