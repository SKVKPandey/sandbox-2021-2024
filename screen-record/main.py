import cv2
import pyautogui
import numpy as np

# Set the screen resolution (you may need to adjust this)
screen_width, screen_height = pyautogui.size()

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'mp4v' codec for MP4 format
out = cv2.VideoWriter('screen_record.mp4', fourcc, 20.0, (screen_width, screen_height))

while True:
    # Capture a screenshot
    screenshot = pyautogui.screenshot()

    # Convert the screenshot to a NumPy array
    frame = np.array(screenshot)

    # Convert BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write the frame to the video file
    out.write(frame)

    # Break the loop when the user presses 'q' key
    if cv2.waitKey(1) == ord('q'):
        break

# Release the VideoWriter and close all OpenCV windows
out.release()
cv2.destroyAllWindows()
