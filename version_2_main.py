import cv2
import easyocr
import numpy as np
import matplotlib.pyplot as plt

def preprocess_image(image_path):
    # Load the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    
    # Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Apply Adaptive Thresholding for better text contrast
    processed = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      cv2.THRESH_BINARY, 11, 2)
    
    return processed

def detect_text(image_path):
    reader = easyocr.Reader(['en'], gpu=True)  # Load EasyOCR model for English
    processed_image = preprocess_image(image_path)
    
    # Run OCR on processed image
    result = reader.readtext(processed_image)
    
    # Extract and format detected text
    detected_text = "\n".join([text[1] for text in result])
    
    return detected_text

# Load image and run detection
image_path = "handwritten_sample.jpg"  # Update with the correct file path
text_output = detect_text(image_path)

# Display output
print("--- Handwritten Text Detection Result ---")
print(text_output)
