import os
from preprocess import preprocess_image
from ocr import run_ocr
from evaluate import calculate_accuracy
from utils import save_results

data_dir = "data/"
results_file = "results/ocr_results.csv"

# Load truth values
with open(os.path.join(data_dir, "truthValue_upper.txt"), "r") as f:
    truth_upper = f.read().strip()

with open(os.path.join(data_dir, "truthValue_lower.txt"), "r") as f:
    truth_lower = f.read().strip()
    
print("\n--- OCR Evaluation Report ---\n")

# Process all sample images
for filename in sorted(os.listdir(data_dir)):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")) and "sample_" in filename:
        print(f" Processing: {filename}")
        
        image_path = os.path.join(data_dir, filename)
        image = preprocess_image(image_path)
        extracted_text = run_ocr(image)

        if "upper" in filename:
            ground_truth = truth_upper
        else:
            ground_truth = truth_lower

        accuracy = calculate_accuracy(extracted_text, ground_truth)

        print(f" Ground Truth : {ground_truth.strip()}")
        print(f" OCR Output   : {extracted_text.strip()}")
        print(f" Accuracy     : {accuracy:.2%}\n")

        accuracy = calculate_accuracy(extracted_text, ground_truth)

        # Save results
        save_results(filename, extracted_text, ground_truth, accuracy, results_file)

        print(f"{filename}: Accuracy = {accuracy:.2%}")
