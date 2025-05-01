import pandas as pd
import os

def save_results(filename, extracted, ground_truth, accuracy, output_file):
    """Append OCR result to CSV."""
    data = {
        "Filename": filename,
        "Extracted_Text": extracted.strip(),
        "Ground_Truth": ground_truth.strip(),
        "Accuracy": f"{accuracy:.2%}"
    }

    df = pd.DataFrame([data])
    write_header = not os.path.exists(output_file)
    df.to_csv(output_file, mode="a", header=write_header, index=False)
