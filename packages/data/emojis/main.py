import os
import json
import requests
import re


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


# ✅ NEW: Convert URL → Emoji
def url_to_emoji(url: str) -> str:
    match = re.search(r"/unicode/([a-f0-9\-]+)\.png", url)
    if not match:
        return ""  # non-unicode (custom GitHub emoji)

    codes = match.group(1).split("-")
    try:
        return "".join(chr(int(code, 16)) for code in codes)
    except Exception:
        return ""


# ✅ NEW: Transform dataset
def transform_emojis(data: dict) -> dict:
    transformed = {}

    for key, url in data.items():
        emoji = url_to_emoji(url)

        # fallback to original URL if cannot convert
        transformed[key] = emoji if emoji else url

    return transformed


def save_json(data, filename):
    """Save JSON data to a file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved JSON data to {filename}")


def save_list(data, filename):
    """Save all keys (emoji names) to a text file with :key: format"""
    keys: list[str] = sorted(data.keys())
    formatted_keys = [f"- :{key}: `:{key}:`" for key in keys]
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(formatted_keys))
    print(f"Saved all emoji keys (with colons) to {filename}")


def save_images(data, filename):
    """Save all keys (emoji names) to a text file with image markdown"""
    IMAGES_URL = (
        "https://raw.githubusercontent.com/hieudoanm/emojis/refs/heads/master/images"
    )
    keys: list[str] = sorted(data.keys())
    formatted_keys = [f"- ![{key}]({IMAGES_URL}/{key}.png)" for key in keys]
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(formatted_keys))
    print(f"Saved all emoji image markdown to {filename}")


def download_images(data, skip_existing=True):
    """Download all emoji images from GitHub"""
    print("Downloading emoji images...")
    for name, url in data.items():
        image_path = os.path.join(IMAGES_DIR, f"{name}.png")

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


# =========================
# Run
# =========================

# Fetch data
emojis = fetch_emojis()

# ✅ Transform URLs → emoji characters
converted_emojis = transform_emojis(emojis)

# Save JSON (converted)
save_json(converted_emojis, JSON_FILE)

# Save keys
save_list(converted_emojis, EMOJIS_LIST_FILE)

# Save image markdown
save_images(converted_emojis, EMOJIS_IMAGE_FILE)

# Download images (still use original URLs)
download_images(emojis)
