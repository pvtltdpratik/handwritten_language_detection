# pip install tensorflow keras opencv-python pytesseract easyocr numpy matplotlib
import cv2
import numpy as np
import pytesseract
import easyocr
import matplotlib.pyplot as plt

# Load image
def load_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    return img, gray

# Perform OCR using Tesseract
def tesseract_ocr(gray):
    custom_config = r'--oem 3 --psm 6'  # Optimize for sparse text
    text = pytesseract.image_to_string(gray, config=custom_config)
    return text

# Perform OCR using EasyOCR
def easyocr_detection(image_path, lang_list=['en']):
    reader = easyocr.Reader(lang_list, gpu=True)  # Define languages to detect
    result = reader.readtext(image_path, detail=0)
    return " ".join(result)

# Main function to detect handwritten text
def detect_handwritten_text(image_path):
    img, gray = load_image(image_path)

    print("\n--- Tesseract OCR Result ---")
    print(tesseract_ocr(gray))

    print("\n--- EasyOCR Result ---")
    print(easyocr_detection(image_path))

    # Display image
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Handwritten Text Detection")
    plt.axis("off")
    plt.show()

# Example usage
image_path = "com_sample.jpg"  # Replace with your image path
detect_handwritten_text(image_path)# pip install tensorflow keras opencv-python pytesseract easyocr numpy matplotlib