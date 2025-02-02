
# Squid Game Mask Detection

This project uses OpenCV and Python to detect and classify Squid Game masks in an image based on the contours and shapes present in the image. The program identifies the largest and second-largest contours in the image, detects their shape (e.g., triangle, square, circle), and displays the results.

## Requirements

- Python 3.x
- OpenCV
- NumPy

You can install the necessary dependencies using the following commands:

```bash
pip install opencv-python numpy
```

## Setup

1. Clone this repository to your local machine.
2. Place the image you want to analyze (e.g., `masksg.png`) in the `./data/` directory.

## How to Run

1. After setting up, run the Python script:

```bash
python mask_detection.py
```

2. The program will:
   - Read the input image (`masksg.png`).
   - Detect the mask's contours (based on black color).
   - Draw bounding boxes around the largest and second-largest contours.
   - Classify the shape of the second-largest contour (Triangle, Square, Rectangle, Pentagon, Circle).
   - Display the result with the shape labels.

## How It Works

1. **Image Processing**:
   - The image is converted from BGR to HSV color space for better mask detection.
   - A binary mask is created to detect the black areas in the image.
   
2. **Contour Detection**:
   - The contours of the binary mask are found.
   - The contours are sorted by area to find the largest and second-largest.

3. **Shape Classification**:
   - The second-largest contour is approximated to a polygon using `cv2.approxPolyDP`.
   - Based on the number of vertices, the shape is classified (Triangle, Square, Rectangle, Pentagon, or Circle).

4. **Result Display**:
   - Bounding boxes are drawn around detected shapes.
   - The detected shape is labeled on the image.

## Example Output

When the program is executed, it will display the input image with bounding boxes around the detected shapes. The detected shape will also be labeled on the image.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork this project and submit pull requests if you have improvements or suggestions!

---

You can save this as a `README.md` file in your project directory. It will guide others on how to set up, run, and understand the project.
