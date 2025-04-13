# Performance evaluation functions

from difflib import SequenceMatcher

def calculate_accuracy(extracted_text, ground_truth):
    """Calculate similarity between OCR output and actual text."""
    return SequenceMatcher(None, extracted_text, ground_truth).ratio()
