# Utility functions (e.g., file handling)
import os
import pandas as pd

def save_results(image_name, extracted_text, ground_truth, output_file="results/ocr_results.csv"):
    """Save OCR results to a CSV file."""

    # Make sure the results directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    data = {
        "Image": image_name,
        "Extracted_Text": extracted_text,
        "Ground_Truth": ground_truth
    }

    df = pd.DataFrame([data])

    # Write to CSV, appending if it already exists
    if not os.path.exists(output_file):
        df.to_csv(output_file, index=False)
    else:
        df.to_csv(output_file, mode="a", header=False, index=False)
