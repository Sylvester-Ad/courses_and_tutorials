from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# === Configuration ===
YOUTUBE_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Replace with your target video
COMMENT_TEXT = ["This is an automated comment via Selenium!", "This is an interesting story. Hoping to see more of this!"]
WATCH_DURATION = 10  # 
PROFILE_PATH = r"mnt/c/Users/USER/AppData/Local/Google/Chrome/User Data/Default"  # <-- Replace with your actual path
PROFILE_NAME = "Default"  # or 'Profile 1', etc.

# === Chrome Options ===
chrome_options = Options()
chrome_options.add_argument(f"--user-data-dir={PROFILE_PATH}")
chrome_options.add_argument(f"--profile-directory={PROFILE_NAME}")
chrome_options.add_argument("--start-maximized")

# Path to Windows ChromeDriver
chromedriver_path = r"./chromedriver.exe"

service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open video
    driver.get(YOUTUBE_URL)
    print("Opened YouTube video. Waiting for it to load...")
    time.sleep(WATCH_DURATION)

    # Wait for the "Like" button to be visible
    print("Waiting for the 'Like' button to load...")
    like_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//ytd-toggle-button-renderer[1]//button'))
    )

    # Scroll to the "Like" button to ensure it's in view
    print("Scrolling to the 'Like' button...")
    ActionChains(driver).move_to_element(like_button).perform()

    # Click the "Like" button
    print("Clicking the 'Like' button...")
    like_button.click()
    print("✅ Video liked.")

    # Scroll to comment section
    print("Scrolling to comment section...")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    # Find the comment box
    print("Locating comment box...")
    comment_area = driver.find_element(By.ID, 'placeholder-area')
    comment_area.click()
    time.sleep(1)

    # Type comment
    print("Typing comment...")
    contenteditable = driver.find_element(By.XPATH, '//div[@id="contenteditable-root" and @contenteditable="true"]')
    contenteditable.send_keys(COMMENT_TEXT)
    time.sleep(1)

    # Click "Comment" button
    print("Posting comment...")
    comment_button = driver.find_element(By.ID, 'submit-button')
    comment_button.click()
    print("✅ Comment posted successfully.")

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    time.sleep(5)
    driver.quit()
