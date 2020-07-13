from requests import get
from PIL import Image
from os import remove

def download_img(url):
  with open('thumb.jpg', 'wb') as handle:
    response = get(url, stream=True)

    if not response.ok:
      print(response)

    for block in response.iter_content(1024):
      if not block:
        break

      handle.write(block)

def convert_to_png():
  size = 564, 564

  im = Image.open("thumb.jpg")
  im.thumbnail(size, Image.ANTIALIAS)
  im.save("thumb.png", "png")

def delete_thumb():
  remove("thumb.jpg")
  remove("thumb.png")