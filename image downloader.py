import os
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse
import requests

# List of image URLs to download
IMAGE_URLS = [
    "https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/python.svg",
    "https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/c.svg",
    "https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/java.svg",
    "https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/cplusplus.svg",
    "https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/html5.svg",
    "https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/css3.svg",
    "https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/javascript.svg",
    "https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/react.svg",
    "https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/django.svg",
    "https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/nodedotjs.svg",
    "https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/postgresql.svg",
    "https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/mongodb.svg",
    "https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/amazonaws.svg",
    "https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/googlecloud.svg",
    "https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/render.svg",
    "https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/docker.svg",
    "https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/kubernetes.svg",
    "https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/git.svg",
    "https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/github.svg",
    "https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/gitlab.svg",
]

# Directory to save the downloaded pictures, relative to this script
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "downloads")


def download_image(url):
  try:
    response = requests.get(url, timeout=15)
    response.raise_for_status()

    # Extract filename from URL or generate a fallback name
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename or "." not in filename:
      filename = f"image_{abs(hash(url))}.jpg"

    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "wb") as f:
      f.write(response.content)
    print(f"Successfully downloaded: {filename}")
  except Exception as e:
    print(f"Failed to download {url}. Error: {e}")


def main():
  os.makedirs(OUTPUT_DIR, exist_ok=True)

  # Download concurrently using a thread pool (max 5 simultaneous downloads)
  with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(download_image, IMAGE_URLS)


if __name__ == "__main__":
  main()