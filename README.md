# ocr

## Installation

### 1. Install Tesseract OCR for Windows

1. Download and install Tesseract OCR by following the instructions from this [Tesseract Installation Guide](https://github.com/UB-Mannheim/tesseract/wiki).
2. During installation, make sure to set the Tesseract path in your system environment variables. The default installation path is:

   ```
   C:\Program Files\Tesseract-OCR
   ```

3. Verify the installation by running the following command in the command prompt:

   ```
    tesseract -v
   ```

### 2. Download Kannada Language File

To extract Kannada text, download the `kan.traineddata` file:

- Download the Kannada language file from [here](https://github.com/tesseract-ocr/tessdata/blob/main/kan.traineddata).
- Place this file in the `tessdata` folder of your Tesseract installation directory:
  ```
  C:\Program Files\Tesseract-OCR\tessdata\
  ```

### 3. Set up Python Environment

1. Clone the repository:

   ```bash
   git clone https://github.com/Shriram-11/ocr.git
   ```

2. Navigate to the repository directory:

   ```bash
   cd ocr
   ```

3. Set up a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment:

   - **Windows**:
     ```bash
     .venv\Scripts\activate
     ```

5. Install the required dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Running the OCR Script

After installation, you can run the OCR script (`test.py`) to extract text from images.

1. Place your image in the repository folder (if not already done).
2. Run the script:

   ```bash
   python test.py
   ```

3. The script will prompt you for the image path. Enter the path to your image (e.g., `tallip1904-60-f07.jpg`) to extract text from it.
