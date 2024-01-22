import pyautogui
import cv2
import numpy as np
import time

# Define your templates
first_image_path = 'iScreen Shoter - 20240119141900913.jpg'  # Replace with your first image file
second_image_path = 'iScreen Shoter - Numbers - 240119154020.jpg'  # Replace with your second image file

# Set the timeout period (seconds)
timeout = 10
import pyautogui
import cv2
import numpy as np
import time

def find_click_and_copy(template_path, timeout):
    start_time = time.time()  # Record the start time
    found = False  # Flag to indicate if the image was found
    
    while (time.time() - start_time) < timeout and not found:
        # Take a screenshot
        screenshot = pyautogui.screenshot()

        # Convert the screenshot to a NumPy array for OpenCV to process
        screen = np.array(screenshot)
        screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

        # Read the template image
        template = cv2.imread(template_path, 0)
        if template is None:
            print(f"Template image {template_path} not found or not readable.")
            break

        # Perform template matching
        res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # Check if a good match was found
        if max_val >= 0.6:
            found = True  # Set the flag to True
            # Calculate the center of the matched area
            w, h = template.shape[::-1]
            center_x = max_loc[0] + w // 2
            center_y = max_loc[1] + h // 2

            # Apply the scale factor for Retina display
            scale_factor = 0.5  # Adjust if necessary
            center_x *= scale_factor
            center_y *= scale_factor

            # Move the mouse to the center of the matched area and click
            pyautogui.moveTo(center_x, center_y, duration=0.1)
            
            pyautogui.doubleClick()  # Double-click to select the text

            time.sleep(0.5)  # Wait for the text to be selected

            pyautogui.hotkey('command', 'a')
            time.sleep(0.5)
            pyautogui.hotkey('command', 'c')
            print(f"Clicked and copied at ({center_x}, {center_y})")
        else:
            time.sleep(0.5)  # Wait a bit before trying again to avoid high CPU usage

    return found


def find_and_click(template_path, timeout):
    start_time = time.time()  # Record the start time
    found = False  # Flag to indicate if the image was found
    
    while (time.time() - start_time) < timeout and not found:
        # Take a screenshot
        screenshot = pyautogui.screenshot()

        # Convert the screenshot to a NumPy array for OpenCV to process
        screen = np.array(screenshot)
        screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

        # Read the template image
        template = cv2.imread(template_path, 0)
        if template is None:
            print(f"Template image {template_path} not found or not readable.")
            break

        # Perform template matching
        res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # Check if a good match was found
        if max_val >= 0.6:
            found = True  # Set the flag to True
            # Calculate the center of the matched area
            w, h = template.shape[::-1]
            center_x = max_loc[0] + w // 2
            center_y = max_loc[1] + h // 2

            # Apply the scale factor for Retina display
            scale_factor = 0.5  # Adjust if necessary
            center_x *= scale_factor
            center_y *= scale_factor

            # Move the mouse to the center of the matched area and click
            pyautogui.moveTo(center_x, center_y, duration=0.1)
            # pyautogui.click()
            print(f"Clicked on {template_path} at ({center_x}, {center_y})")
        else:
            time.sleep(0.5)  # Wait a bit before trying again to avoid high CPU usage

    return found

# Run the find_and_click function for the first image
if find_and_click(first_image_path, timeout):
    print("First image found, now looking for second image.")
    # After finding the first image, run it for the second image
    find_click_and_copy(second_image_path, timeout)
else:
    print("First image not found within the timeout period.")

