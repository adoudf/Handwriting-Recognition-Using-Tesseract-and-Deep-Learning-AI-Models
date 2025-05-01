# Performance evaluation functions

from difflib import SequenceMatcher
import pytesseract
import cv2

from difflib import SequenceMatcher

def calculate_accuracy(extracted_text, ground_truth):
    """Returns similarity ratio between predicted and actual text."""
    return SequenceMatcher(None, extracted_text.strip(), ground_truth.strip()).ratio()
