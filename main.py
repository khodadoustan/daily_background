#!/usr/bin/env python3

import requests
import os
import subprocess

TIMEOUT = 30
BING_BASE_URL = 'http://bing.com'
DAILY_IMG = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
DOWNLOAD_AT = 'daily_images'
IMAGE_DIR = "{}/{}".format(os.path.dirname(os.path.realpath(__file__)), DOWNLOAD_AT)


if __name__ == '__main__':
    bing_response = requests.get(DAILY_IMG).json()
    # response comes back as a list of one
    img_url = bing_response.get('images')[0].get('url')
    full_img_url = BING_BASE_URL + img_url
    img = requests.get(full_img_url, stream=True)
    file_name = '{image_dir}/{file_name}'.format(
        image_dir=IMAGE_DIR,
        file_name=img_url.split('/')[-1])

    os.makedirs(IMAGE_DIR, exist_ok=True)
    with open(file_name, 'wb') as f:
        for chunk in img.iter_content(chunk_size=1024):
            f.write(chunk)

    # sets ubuntu background image
    subprocess.run([
        'gsettings',
        'set',
        'org.gnome.desktop.background',
        'picture-uri',
        'file://{}'.format(file_name)])
