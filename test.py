from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

# Step a: Login
def login(username, password):
    #driver = webdriver.Chrome()  # Change this if using a different browser
    driver.get("https://development.app.koolio.ai")  # Replace with your login page URL

    time.sleep(5)

    username_field = driver.find_element(By.CSS_SELECTOR,"[placeholder='User name or Email']")  # Replace with actual element ID
    password_field = driver.find_element(By.CSS_SELECTOR,"[id='lfpwd']")  # Replace with actual element ID

    time.sleep(1)
    username_field.send_keys(username)
    time.sleep(1)
    password_field.send_keys(password)

    time.sleep(5)
    #password_field.send_keys(Keys.RETURN)
    login_btn = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login-form > button.line-height-input.btn-padding.text-l.auth-button.login-button")))
    login_btn.click()
    #driver.find_element(By.CSS_SELECTOR, "#login-form > button.line-height-input.btn-padding.text-l.auth-button.login-button").click()
    time.sleep(20)
    print("Login")

# Step b: Upload Audio File
def upload_audio(file_path):
    #driver = webdriver.Chrome()
    add_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-btn"]')))
    time.sleep(15)
    add_btn.click()
    print("click add")
    time.sleep(5)
   
   # driver.find_element(By.XPATH, '//*[@id="add-btn"]').click()
    upload_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "upbtn")))
    upload_button.click()
    print("Hello")
    time.sleep(5)
    #upload_button.send_keys(file_path)
    #pyautogui.typewrite(file_path)
    #pyautogui.press('enter')

    keyboard = Controller()

    keyboard.type(file_path)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

   # driver.find_element(By.CSS_SELECTOR, '#upbtn > img').click()
    print("Clicked Upload")
    #driver.find_element(By.CSS_SELECTOR, '#upbtn > img').send_keys(file_path)
   # driver.find_element_by_id("upload_button").send_keys(file_path)  # Replace with actual element ID
    time.sleep(15)

    driver.find_element(By.XPATH, '//*[@id="half-modals-content"]/div[2]/div[1]/button').click()
    print("Yes clicked")
    time.sleep(5)

    driver.find_element(By.XPATH, '//*[@id="half-modals-content"]/div[2]/div[1]/button').click()
    print("2nd Yes clicked")
    time.sleep(20)

# Step c: Play Uploaded Audio
def play_audio():
    # Find the element to hover over
    time.sleep(20)
    file_play = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'ad34457c-9253-403d-be17-0e2585300ab3')))
    time.sleep(15)
    #driver.find_element(By.XPATH, '//*[@id="4e814a3e-766f-429e-ae45-ab6fb987c047"]/a[1]')

    # Create an instance of ActionChains
    actions = ActionChains(driver)

    # Perform the hover action
    actions.move_to_element(file_play).perform()
    print("Hover")
    time.sleep(10)

    # After performing the hover, you can do other actions (e.g., click, etc.)
    # For example, you can click on an element that appears after hovering
    element_to_click = driver.find_element(By.XPATH, '//*[@id="ad34457c-9253-403d-be17-0e2585300ab3_view"]')
    time.sleep(5)
    element_to_click.click()
    print("Viewed")
    time.sleep(30)
    #driver.find_element_by_id("play_button").click()  # Replace with actual element ID

    #play_btn = driver.find_element(By.ID, 'btn-play')
    #time.sleep(5)
    #play_btn.click()
    #print("Played")
    #time.sleep(30)

# Step d: Select Area from SPK Track
def select_area():
    edit_btn = driver.find_element(By.ID, 'control-opt-edit')
    edit_btn.click()
    print("Edit clicked")
    time.sleep(5)

    # Assuming 'canvas' is the class of the time scale
    time_scale = driver.find_element(By.CSS_SELECTOR, '#c67a04f4-b747-4666-adaa-62288f8602b2 > div.waveform > div.cursor.top')
    time.sleep(5)
    print("Find Audio track")

    # Get the coordinates of the starting and ending points of the selection
    start_x = 150  # Example coordinates, adjust as needed
    start_y = 0
    end_x = 300
    end_y = 0

    # Perform mouse actions to select the portion
    action_chains = ActionChains(driver)
    action_chains.move_to_element_with_offset(time_scale, start_x, start_y)
    action_chains.click_and_hold()
    time.sleep(5)
    print("Clicked")
    action_chains.move_by_offset(end_x - start_x, end_y - start_y)
    action_chains.release()
    time.sleep(5)
    print("mouce release")
    action_chains.perform()

    time.sleep(5)

# Step e: Copy & Paste to Another Inside the Same Track
def copy_paste():
    copy_btn = driver.find_element(By.XPATH, '//*[@id="btn-copy-cont"]')
    paste_btn = driver.find_element(By.XPATH, '//*[@id="btn-insert"]')

    copy_btn.click()
    print("copy clicked")
    time.sleep(5)

    time_scale = driver.find_element(By.CSS_SELECTOR, '#c67a04f4-b747-4666-adaa-62288f8602b2 > div.waveform > div.cursor.top')

    paste_x = 700
    paste_y = 50
    action_chains = ActionChains(driver)
    action_chains.move_to_element_with_offset(time_scale, paste_x, paste_y)
    action_chains.click()
    action_chains.perform()

    # Trigger paste action
    paste_btn.click()
    time.sleep(5)
    print("Paste timescale")

# Step f: Add SFX on SFX Track
def add_sfx(sfx_path):
    driver.find_element_by_id("sfx_track").click()  # Replace with actual element ID
    driver.find_element_by_id("upload_sfx_button").send_keys(sfx_path)  # Replace with actual element ID

# Step g: Apply Fade on SFX
def apply_fade():
    driver.find_element_by_id("fade_button").click()  # Replace with actual element ID
    # Write code to adjust fade settings

# Example Usage
login("Paykoolio", "123Abc!@")
#upload_audio(r"C:\Users\pc\Downloads\1user_2.wav")
play_audio()
select_area()
copy_paste()
# add_sfx("/path/to/your/sfx/file.wav")
# apply_fade()

# Remember to add proper waits, error handling, and finalize the script according to your application's behavior.
