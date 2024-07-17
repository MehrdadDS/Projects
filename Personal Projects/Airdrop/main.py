import pyautogui
import time
import os

def locate_image(image_name, confidence=0.8):
    try:
        return pyautogui.locateOnScreen(image_name, confidence=confidence)
    except pyautogui.ImageNotFoundException:
        return None

def track_and_perform_actions():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    while True:
        # Check for Dedacoin Airdrop screen
        if locate_image(os.path.join(script_dir, 'dedacoin_airdrop.png')):
            print("Dedacoin Airdrop screen detected. Performing actions...")
            pyautogui.moveTo(950, 590)
            pyautogui.click()
            #time.sleep(2)
        
        # Check for "One more spin?!" button
        elif locate_image(os.path.join(script_dir, 'one_more_spin.png')):
            print("One more spin button detected. Clicking...")
            pyautogui.moveTo(950, 590)
            pyautogui.click()
        
        # Check for "Close Video" button
        elif locate_image(os.path.join(script_dir, 'close_window.png')):
            print("Close Video button detected. Clicking...")
            pyautogui.moveTo(950, 790)
            pyautogui.click()
        
        # If none of the images are found
        else:
            print("Waiting for finding pictures...")
        
        # Short sleep to prevent high CPU usage
        time.sleep(0.5)

# Start the process
if __name__ == "__main__":
    time.sleep(5)
    print("Starting screen tracking...")
    try:
        track_and_perform_actions()
    except KeyboardInterrupt:
        print("\nScript terminated by user.")
    except Exception as e:
        print(f"An error occurred: {e}")