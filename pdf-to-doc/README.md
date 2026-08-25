# PDF TO DOC - Convert your PDF files to DOCX format

It automatically converts all PDF files in the "pdfs" folder to DOCX format and saves them in the "docs" folder.
It uses the CloudConvert API to perform the conversion.

## Requirements

- Python 3.7 or higher
- CloudConvert API key (you can get it from [CloudConvert](https://cloudconvert.com/))

## Installation

1. Clone this repository or download the source code.

2. Install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. Get your CloudConvert API key 

4. Create a `.env` file in the root directory of the project and add your API key:
   ```
   CLOUDCONVERT_API_KEY=your_api_key_here
   ```

## Usage

Place your PDF files in the folder named "pdfs" and run the script:

```bash
python pdf2doc.py
```