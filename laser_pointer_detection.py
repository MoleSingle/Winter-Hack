import cv2
import numpy as np
import sys

# Initialize the webcam capture
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Webcam cannot be accessed.")
    sys.exit()

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to read the frame.")
        break

    # Optionally resize the frame for performance
    frame = cv2.resize(frame, (640, 480))

    # Convert frame from BGR to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # HSV ranges for detecting different laser colors
    # Define red color ranges in HSV space
    red_hsv_lower_1 = np.array([0, 100, 100])
    red_hsv_upper_1 = np.array([10, 255, 255])
    red_hsv_lower_2 = np.array([160, 100, 100])
    red_hsv_upper_2 = np.array([180, 255, 255])

    # Define green color range
    green_hsv_lower = np.array([40, 100, 100])
    green_hsv_upper = np.array([80, 255, 255])

    # Define blue color range
    blue_hsv_lower = np.array([100, 100, 100])
    blue_hsv_upper = np.array([140, 255, 255])

    # Create masks for the defined colors
    mask_red_1 = cv2.inRange(hsv, red_hsv_lower_1, red_hsv_upper_1)
    mask_red_2 = cv2.inRange(hsv, red_hsv_lower_2, red_hsv_upper_2)
    mask_green = cv2.inRange(hsv, green_hsv_lower, green_hsv_upper)
    mask_blue = cv2.inRange(hsv, blue_hsv_lower, blue_hsv_upper)

    # Combine masks to include all colors
    combined_mask = cv2.bitwise_or(mask_red_1, mask_red_2)
    combined_mask = cv2.bitwise_or(combined_mask, mask_green)
    combined_mask = cv2.bitwise_or(combined_mask, mask_blue)

    # Apply morphological operations to reduce noise in the mask
    combined_mask = cv2.erode(combined_mask, None, iterations=2)
    combined_mask = cv2.dilate(combined_mask, None, iterations=2)

    # Detect contours within the mask
    contours, _ = cv2.findContours(combined_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Ensure contours have been found
    if contours:
        # Find the contour with the brightest appearance
        brightest_contour = max(contours, key=lambda c: cv2.mean(hsv, mask=cv2.drawContours(np.zeros_like(combined_mask), [c], -1, 255, thickness=cv2.FILLED))[2])

        # Compute the minimum enclosing circle for contour
        ((x, y), radius) = cv2.minEnclosingCircle(brightest_contour)

        # Threshold the detected laser pointer size
        if radius > 3:
            # Mark the laser position on the frame
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 0), 2)
            cv2.circle(frame, (int(x), int(y)), 5, (0, 0, 255), -1)

            # Display laser pointer coordinates
            cv2.putText(frame, f"Laser Pointer: ({int(x)}, {int(y)})", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Show the processed frame in a window
    cv2.imshow('Laser Pointer Detection', frame)

    # Exit if 'q' is pressed or window is closed
    if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty('Laser Pointer Detection', cv2.WND_PROP_VISIBLE) < 1:
        break

# Release resources and close windows
cap.release()
cv2.destroyAllWindows()
sys.exit()
