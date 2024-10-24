from PIL import Image
import pytesseract
import cv2
import numpy as np

# (for Windows users only)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract_text_from_image(image_path):
    # Load the image using OpenCV
    img = cv2.imread(image_path)

    # Convert to grayscale (helps improve OCR accuracy)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Binarization (thresholding to make text stand out more)
    _, binary_image = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # adaptive thresholding:
    binary_image = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    # denoising image
    denoised_image = cv2.medianBlur(binary_image, 3)

    # Resize image to improve OCR accuracy (especially for small fonts)
    scale_percent = 150  # scaling by 150% for example
    width = int(denoised_image.shape[1] * scale_percent / 100)
    height = int(denoised_image.shape[0] * scale_percent / 100)
    resized_image = cv2.resize(
        denoised_image, (width, height), interpolation=cv2.INTER_LINEAR)

    # Convert processed image to PIL format for pytesseract
    pil_image = Image.fromarray(resized_image)

    # Perform OCR on the preprocessed image
    extracted_text = pytesseract.image_to_string(pil_image, lang='kan')

    return extracted_text


# Path to your image (photo of a textbook page)
image_path = input("Enter the path to the image: ")

# Extract text from the image
text = extract_text_from_image(image_path)

# Print extracted text
print("Extracted Text:\n", text)
