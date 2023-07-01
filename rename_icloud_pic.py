import os
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime
import argparse

def handle_image(file_path, original_name):
    image = Image.open(file_path)
    exif_data = image._getexif()
    if not exif_data:
        return

    for tag, value in exif_data.items():
        tag_name = TAGS.get(tag, tag)
        if tag_name == 'DateTime':
             # Parse the date and time from the original format
            dt = datetime.strptime(value, "%Y:%m:%d %H:%M:%S")

            # Format the date as "YYYYMMDD"
            formatted_date = dt.strftime("%Y%m%d")

            new_file_name = formatted_date + '_' + original_name
            new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)
            os.rename(file_path, new_file_path)

parser = argparse.ArgumentParser(description="A program to change the name of image files to their creation dates")
parser.add_argument('folder_path', type=str, help='The path of the image folder to process')

args = parser.parse_args()

for file_name in os.listdir(args.folder_path):
    if file_name.lower().endswith(".jpeg"):  # You can also add other image file types
        file_path = os.path.join(args.folder_path, file_name)
        handle_image(file_path, file_name)
