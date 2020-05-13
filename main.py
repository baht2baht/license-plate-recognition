# License Plate Recognition
# Thai license plate recognition with Python
# - Pillow
# - Tesseract
#
# By Kanatat Asipong
#
# Revision
# 10/05/2020 - Kanatat
#   - Initial base code.

# Import packages
import os
import numpy as np
import pandas as pd
import LicensePlateOCR as lp

# Load image
image_path = './license-images/example-license.jpg'
text_result = lp.OCR(image_path)

print(text_result.license_text)
print(text_result.province_text)