import requests
import cv2
import os
from django.utils.text import slugify


API_KEY = "8e649acd"


def fetch_poster(movie_title):

    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={API_KEY}"

    response = requests.get(url).json()

    if response.get("Poster") and response["Poster"] != "N/A":
        return response["Poster"]

    return None


def save_resized_poster(image_url, movie_title):

    if not image_url:
        return None

    filename = slugify(movie_title) + ".jpg"

    folder_path = "static/posters"

    os.makedirs(folder_path, exist_ok=True)

    filepath = os.path.join(folder_path, filename)

    # Skip download if already exists
    if os.path.exists(filepath):
        return filepath

    try:

        img_data = requests.get(image_url).content

        with open(filepath, "wb") as file:
            file.write(img_data)

        img = cv2.imread(filepath)

        if img is None:
            return None

        resized = cv2.resize(img, (300, 450))

        cv2.imwrite(filepath, resized)

        return filepath

    except Exception as e:

        print("Poster download failed:", e)

        return None