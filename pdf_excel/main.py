import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import pandas as pd

# Specify the path to the PDF file
pdf_path = './data/example1.pdf'

# Convert PDF pages to images
pages = convert_from_path(pdf_path, dpi=300)

# Extract text from each page using Tesseract OCR
text_data = []
for page_number, page in enumerate(pages, start=1):
    # Use pytesseract to extract text from the image
    text = pytesseract.image_to_string(page)
    text_data.append({'page_number': page_number, 'text': text})

# Convert the extracted text data into a DataFrame
df = pd.DataFrame(text_data)
df.to_csv('example1.csv', index=True)