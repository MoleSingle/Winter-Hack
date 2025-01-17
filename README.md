# Laser Pointer Detection using OpenCV

This project is a Python application designed to detect laser pointers using a webcam. The application leverages OpenCV to identify laser pointers up to 2 meters away, allowing for a tolerance of 10 cm. It demonstrates fundamental computer vision concepts, including color detection and contour analysis.

## Features

- **Real-Time Detection**: Utilizes a webcam to process video frames in real time.
- **Multicolor Detection**: Capable of detecting red, green, and blue laser pointers.
- **Contour Analysis**: Implements contour detection to identify and track the brightest point matching the laser pointer.
- **Adjustable Parameters**: Easily modify HSV color ranges to calibrate detection settings for different lighting conditions or laser colors.

## Setup and Installation

To run this project, you'll need Python installed on your machine as well as the necessary libraries. Follow the steps below to get started:

1. **Install Python** (if not already installed):
   - Download and install Python from [python.org](https://www.python.org/).

2. **Install Required Libraries**:
   - Open a terminal or command prompt.
   - Run the following command to install OpenCV and NumPy:
     ```bash
     pip install opencv-python numpy
     ```

3. **Clone or Download the Repository**:
   - You can clone this repository using Git:
     ```bash
     git clone https://github.com/MoleSingle/Winter-Hack.git
     ```
   - Alternatively, download the ZIP of the repository and extract it.

4. **Run the Application**:
   - Navigate to the directory containing the code.
   - Use the command below to execute the script:
     ```bash
     python laser_pointer_detection.py
     ```

## How It Works

1. **Capture Frames**: Continuously capture frames from the webcam feed.
2. **Convert to HSV**: Convert each frame from BGR to HSV color space to facilitate color detection.
3. **Create Masks**: Define HSV color ranges for red, green, and blue and generate masks to isolate these colors.
4. **Contour Detection**: Apply contour detection to identify potential laser pointer locations.
5. **Enclosing Circle**: For each detected contour, compute the minimum enclosing circle to determine the size and location of the laser pointer.
6. **Display Results**: Annotate the frame with circles and coordinates, displaying real-time detection results in a window.

## Usage Notes

- **Adjust HSV Ranges**: Depending on the environment and laser pointer type, you may need to adjust HSV values for better performance.
- **Distance and Lighting**: Laser pointer detection accuracy may vary with distance and lighting conditions. Experiment with setups for optimal results.

## Contact

For further questions or contributions, please contact [Your Name] at [Your Email Address].
