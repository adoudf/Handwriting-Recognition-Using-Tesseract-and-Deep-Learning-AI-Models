 # Functions for running Tesseract OCR
 
import pytesseract
import cv2


pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

def run_ocr(image):
    config = "--oem 1 --psm 7"#tuning psm (Page Segmentation Mode) and oem (OCR Engine Mode
    text = pytesseract.image_to_string(image, config=config)
    return text
#Try different --psm modes like:

#6: Assume a single uniform block of text
#11: Sparse text
#13: Raw line by line OCR (can help with handwriting)