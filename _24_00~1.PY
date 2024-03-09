import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from threading import Thread
import time

# extracting sensitive data from environment variables:
linkedin_login_url = os.environ.get('linkedin_login_url', 'URL does not exist')
filter_search_url = os.environ.get('filter_search_url', 'URL does not exist')
first_name = os.environ.get('first_name', 'First name does not exist')
last_name = os.environ.get('last_name', 'Last name does not exist')
email = os.environ.get('email', 'Email does not exist')
linkedin_password = os.environ.get('linkedin_password', 'Password does not exist')
phone_number = os.environ.get('phone_number', 'Phone number does not exist')
college_or_university_attended = os.environ.get('college_or_university_attended', 'Education does not exist')
degree = os.environ.get('degree', 'Degree does not exist')
linked_in_profile_url = os.environ.get('linked_in_profile_url', 'LinkedIn profile URL does not exist')
git_or_github_repo = os.environ.get('git_or_github_repo', 'Git/GitHub repo does not exist')

print(f"The LinkedIn login URL is: {linkedin_login_url}")
print(f"The filter search URL is: {filter_search_url}")
print(f"First name: {first_name}")
print(f"Last name: {last_name}")
print(f"Email: {email}")
print(f"LinkedIn Password: {linkedin_password}")
print(f"Phone number: {phone_number}")
print(f"College or University attended: {college_or_university_attended}")
print(f"Degree: {degree}")
print(f"LinkedIn Profile URL: {linked_in_profile_url}")
print(f"Git/GitHub Repo: {git_or_github_repo}")

def setup_chrome_driver_for_selenium():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(linkedin_login_url)
    return driver

driver = setup_chrome_driver_for_selenium()

# -------------------------- beginning at the website ---------------------------#

time.sleep(2)

Email_or_phone_id = driver.find_element(By.ID, "username")
Email_or_phone_id.send_keys(email)

Password_id = driver.find_element(By.ID, "password")
Password_id.send_keys(linkedin_password + Keys.ENTER)

# sign in button:
sign_in_button = driver.find_element(By.XPATH, "//button[@type='submit']")
sign_in_button.click()

time.sleep(2)

driver.get(filter_search_url)

# the easy apply button:
'''
<span class="artdeco-button__text">
    easy apply
</span>
'''

# close the browser
# driver.quit()