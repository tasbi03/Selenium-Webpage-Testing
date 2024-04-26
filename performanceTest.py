import threading
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def user_actions(num_comments_per_page, url, results, index):
    driver = webdriver.Chrome()
    driver.get(url)

    overall_start_time = time.time()
    navigation_times = []
    comment_submission_times = []

    for x in range(num_comments_per_page):
        # Measuring navigation time
        nav_start_time = time.time()
        driver.find_element(By.ID, 'next').click()
        # Wait for the page to load (if these elements are present on the page then its loaded)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'picture')))
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'value')))
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'next')))
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'blogs')))
        
        nav_end_time = time.time()
        
        navigation_times.append(nav_end_time - nav_start_time)

        # Measuring comment submission time
        username_input = driver.find_element(By.CLASS_NAME, 'username')
        comment_input = driver.find_element(By.CLASS_NAME, 'comment')
        submit_button = driver.find_element(By.ID, 'submit')

        username_input.send_keys('TestUser')
        comment_input.send_keys('This is a test comment')
        comment_start_time = time.time()
        submit_button.click()

        # after submitting when the blog reappears, the omment is submitted
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'blogs')))
        comment_end_time = time.time()
        comment_submission_times.append(comment_end_time - comment_start_time)

    overall_end_time = time.time()

    driver.quit()

    results[index] = {
        'overall_time': overall_end_time - overall_start_time,
        'average_navigation_time': sum(navigation_times) / len(navigation_times),
        'average_comment_time': sum(comment_submission_times) / len(comment_submission_times)
    }

def simulate_users(num_users, num_comments_per_page, url):
    results = [None] * num_users  # list to store results from each thread
    threads = []

    for i in range(num_users):
        thread = threading.Thread(target=user_actions, args=(num_comments_per_page, url, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results

url = 'http://127.0.0.1:5500/RealEstatePredictor.html'

def simulate_tester(num_users, totalcomments):
    for num_comments_per_page in [totalcomments]:
        results = simulate_users(num_users, num_comments_per_page, url)
        total_time = sum(result['overall_time'] for result in results)
        average_user_time = sum(result['overall_time'] for result in results) / num_users
        average_nav_time = sum(result['average_navigation_time'] for result in results) / num_users
        average_comment_time = sum(result['average_comment_time'] for result in results) / num_users

        print(f"{num_users} users with {num_comments_per_page / 5} comments on each page:")
        print(f"Total time taken: {total_time} seconds")
        print(f"Average time taken by each user: {average_user_time} seconds")
        print(f"Average navigation time per user: {average_nav_time} seconds")
        print(f"Average comment submission time per user: {average_comment_time} seconds")

# Testing with different user counts and comment volumes
for num_users in [1, 5, 10]:
    simulate_tester(num_users, 500)    # 100 comments on each page
for num_users in [1, 5, 10]:
    simulate_tester(num_users, 1000)   # 200 comments on each page
for num_users in [1, 5, 10]:
    simulate_tester(num_users, 1500)   # 300 comments on each page
