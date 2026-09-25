# Image Downloader

A simple Python utility that downloads a list of images from the internet and saves them to a local folder. Downloads run concurrently with up to five workers, making the process faster than downloading each image one at a time.

## Features

- Downloads multiple images from configured URLs.
- Uses the filename from each image URL automatically.
- Creates the output directory if it does not already exist.
- Downloads up to five images concurrently.
- Reports successful and failed downloads in the terminal.
- Uses a 15-second timeout for each request.

## Requirements

- Python 3.8 or newer
- Internet connection
- The Python `requests` package

## Installation

1. Install Python from [python.org](https://www.python.org/downloads/) if it is not already installed.
2. Open PowerShell or Command Prompt.
3. Move to the project folder:

   ```powershell
   cd "C:\Users\UNMESH\Desktop\image downloader"
   ```

4. Install the required packages:

   ```powershell
   python -m pip install -r requirements.txt
   ```

### Optional virtual environment

Using a virtual environment keeps this project's dependencies separate from other Python projects:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If PowerShell prevents activation, run the script with the virtual environment's Python executable instead:

```powershell
.\.venv\Scripts\python.exe "image downloader.py"
```

## Configuration

Before running the program, open `image downloader.py` and update these values as needed:

- `IMAGE_URLS`: the list of image URLs to download.
- `OUTPUT_DIR`: the folder where downloaded images will be saved. By default, this is a `downloads` folder next to the script, so the project works on other computers without changing a machine-specific path.

The default output folder is:

```text
downloads/
```

The program creates this folder automatically if it does not exist. Make sure the URLs are direct links to image files and that you have permission to download and use the content.

## Usage

Run the program from the project folder:

```powershell
python "image downloader.py"
```

On Windows, the Python launcher can also be used:

```powershell
py "image downloader.py"
```

Downloaded files are saved in the folder configured by `OUTPUT_DIR`. The terminal displays a success message for each completed download and an error message for any failed download.

## Troubleshooting

### `ModuleNotFoundError: No module named 'requests'`

Install the dependencies with:

```powershell
python -m pip install -r requirements.txt
```

### A download fails or times out

Check your internet connection and confirm that the URL is still valid and points directly to an image. The program gives each request 15 seconds to complete.

### Files are not saved where expected

Check the value of `OUTPUT_DIR`. On Windows, use a raw string such as `r"C:\path\to\folder"` or escape backslashes as `C:\\path\\to\\folder`.

## Project Files

```text
image downloader.py   # Main downloader script
README.md             # Project documentation
requirements.txt      # Python dependencies
```