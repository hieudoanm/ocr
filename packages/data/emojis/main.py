import os
import json
import requests


# API endpoint
API_URL = "https://api.github.com/emojis"


# Output files
JSON_FILE = "json/emojis.json"
EMOJIS_LIST_FILE = "docs/emojis_list.txt"
EMOJIS_IMAGE_FILE = "docs/emojis_image.txt"
IMAGES_DIR = "images"


# Ensure images directory exists
os.makedirs(IMAGES_DIR, exist_ok=True)


def fetch_emojis():
    """Fetch emojis from GitHub API and return as JSON"""
    print("Fetching emojis from GitHub API...")
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()


def save_json(data, filename):
    """Save JSON data to a file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"Saved JSON data to {filename}")


def save_list(data, filename):
    """Save all keys (emoji names) to a text file with :key: format"""
    keys: list[str] = sorted(data.keys())
    formatted_keys = [
        f"- :{key}: `:{key}:`" for key in keys
    ]  # Wrap each key with colons
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(formatted_keys))
    print(f"Saved all emoji keys (with colons) to {filename}")


def save_images(data, filename):
    """Save all keys (emoji names) to a text file with :key: format"""
    IMAGES_URL = (
        "https://raw.githubusercontent.com/hieudoanm/emojis/refs/heads/master/images/"
    )
    keys: list[str] = sorted(data.keys())
    formatted_keys = [
        f"- ![{key}]({IMAGES_URL}/{key}.png)" for key in keys
    ]  # Wrap each key with colons
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(formatted_keys))
    print(f"Saved all emoji keys (with colons) to {filename}")


def download_images(data, skip_existing=True):
    """
    Download all emoji images from GitHub.

    Args:
        data (dict): Mapping of emoji name to image URL.
        skip_existing (bool): If True, skip downloading files that already exist.
    """
    print("Downloading emoji images...")
    for name, url in data.items():
        image_path = os.path.join(IMAGES_DIR, f"{name}.png")

        # Skip if file exists
        if skip_existing and os.path.exists(image_path):
            print(f"Skipping (already exists): {name}")
            continue

        try:
            img_data = requests.get(url, timeout=10)
            img_data.raise_for_status()
            with open(image_path, "wb") as img_file:
                img_file.write(img_data.content)
            print(f"Downloaded: {name}")
        except Exception as e:
            print(f"Failed to download {name}: {e}")


# Fetch data
emojis = fetch_emojis()

# Save JSON
save_json(emojis, JSON_FILE)

# Save keys to text file
save_list(emojis, EMOJIS_LIST_FILE)

# Save image markdown links to text file
save_images(emojis, EMOJIS_IMAGE_FILE)

# Download images
download_images(emojis)
