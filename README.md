
# Enhanced Handwriting OCR with Tesseract and Deep Learning

This project aims to improve the accuracy of Tesseract OCR on messy, real-world handwriting using advanced image preprocessing techniques, optimized recognition models, and post-processing error correction. We treat this as a research-driven initiative, with the goal of improving on the state-of-the-art for handwritten text recognition.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Directory Structure](#directory-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Evaluation](#evaluation)
- [Future Work](#future-work)
- [License](#license)

---

## Overview

Out-of-the-box Tesseract OCR struggles with poor handwriting. This project explores whether a combination of preprocessing, OCR tuning, and post-processing can lead to more robust and scalable handwriting recognition, suitable for use in accessibility tools, archival digitization, and real-time mobile applications.

## Features

- Image denoising and enhancement for handwriting
- Configurable Tesseract OCR with multiple `--psm` modes
- Accuracy evaluation via string similarity metrics
- CSV logging of results
- Modular structure for easier testing and benchmarking

## Directory Structure

```
OCR_PROJECT/
├── data/                  # Input images and ground truth text files
├── results/               # Output directory for results CSV
├── preprocess.py          # Image preprocessing pipeline
├── ocr.py                 # Tesseract OCR wrapper
├── evaluate.py            # Accuracy and metrics calculation
├── utils.py               # Helper functions (e.g., save_results)
├── main.py                # Main script to run OCR pipeline
└── README.md              # Project description and instructions
```

## Setup Instructions

**Tested Environment:**  
- Ubuntu 22.04.5 LTS  
- Python 3.10  
- Tesseract 5.x built from source

### 1. Install Tesseract

Follow the [official GitHub guide](https://github.com/tesseract-ocr/tesseract) to build and install Tesseract from source.

Make sure the binary is available in your system PATH:

```bash
which tesseract
# Should output: /usr/local/bin/tesseract
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```
pytesseract
opencv-python
numpy
pandas
```

## Usage

Run the OCR pipeline on sample data:

```bash
python3 main.py
```

- Input images are loaded from the `data/` directory.
- Extracted text is compared to ground truth.
- Results are saved in `results/ocr_results.csv`.

## Evaluation

The current evaluation metric is character-level similarity (SequenceMatcher). Accuracy is reported as a percentage:

```python
from difflib import SequenceMatcher
accuracy = SequenceMatcher(None, ocr_output, ground_truth).ratio() * 100
```

Future versions may implement:
- Word Error Rate (WER)
- Character Error Rate (CER)

## Future Work

- Incorporate handwriting enhancement using deep learning (e.g., ESRGAN)
- Support for multiple datasets (IAM, CVL)
- Visualization dashboard for metrics
- Auto ground-truth alignment from paired files

## License

This project is open-source 
