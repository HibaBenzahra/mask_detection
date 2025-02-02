import cv2
import numpy as np

# Load image
img = cv2.imread('./data/masksg.png')

# -------- Mask Detection Parameters --------
# Define the range of black color in HSV to detect the mask
lower_black = np.array([0, 0, 0])        # Pure black
upper_black = np.array([179, 150, 150])  # Light black

# Convert image to HSV color space
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Create a binary mask where black colors are detected
bmask = cv2.inRange(img_hsv, lower_black, upper_black)

# Find contours in the binary mask
contours, hierarchy = cv2.findContours(bmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Sort contours by area in descending order
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

# Get the biggest contour
biggest_cnt = sorted_contours[0]

# Draw a bounding rectangle around the largest contour (mask)
x1, y1, w, h = cv2.boundingRect(biggest_cnt)
cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)

# Check if a second-largest contour exists
if len(sorted_contours) > 1:
    sec_big_cnt = sorted_contours[1]
else:
    sec_big_cnt = None
    print("No second biggest contour found")

# -------- Shape Detection (for second largest contour) --------
if sec_big_cnt is not None:
    # Calculate perimeter of the second biggest contour
    perimeter = cv2.arcLength(sec_big_cnt, True)

    # Approximate the contour to a polygonal curve
    approx = cv2.approxPolyDP(sec_big_cnt, 0.02 * perimeter, True)

    # Detect the shape based on the number of vertices in the approximation
    shape = "None"
    if len(approx) == 3:
        shape = "Triangle"
    elif len(approx) == 4:
        (x, y, w, h) = cv2.boundingRect(approx)
        ar = w / float(h)  # Aspect ratio
        shape = "Square" if 0.95 <= ar <= 1.05 else "Rectangle"
    elif len(approx) == 5:
        shape = "Pentagon"
    else:
        shape = "Circle"

    # Draw the contour of the second biggest shape
    cv2.drawContours(img, [sec_big_cnt], -1, (0, 255, 0), 2)

    # Get bounding box and put the shape name as text
    x1, y1, w, h = cv2.boundingRect(sec_big_cnt)
    cv2.putText(img, shape, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# -------- Display the Result --------
cv2.imshow("Detected Mask and Shapes", img)

# Wait until a key is pressed and then close the image window
cv2.waitKey(0)
cv2.destroyAllWindows()
