# Main script to run OCR

import cv2
import os
from preprocess import preprocess_image
from ocr import run_ocr
from evaluate import calculate_accuracy
from utils import save_results

# Directory containing images
image_dir = "data/"
images = [f for f in os.listdir(image_dir) if f.endswith((".png", ".jpg", ".jpeg"))]

for image_name in images:
    image_path = os.path.join(image_dir, image_name)

    # Preprocess the image
    preprocessed_image = preprocess_image(image_path)

    # Run OCR
    extracted_text = run_ocr(preprocessed_image)

    # (Manually replace with actual text for now)
    ground_truth = "Actual handwritten text"

    # Evaluate OCR accuracy
    accuracy = calculate_accuracy(extracted_text, ground_truth)

    # Save results
    save_results(image_name, extracted_text, ground_truth)

    print(f"Processed {image_name}: OCR Accuracy = {accuracy:.2%}")

#Visulation
cv2.imshow("Preprocessed", preprocessed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

