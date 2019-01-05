from google.cloud import vision
from google.cloud.vision import types
from PIL import Image
import os
import requests
import sys
import io


def ocr_main(file, lang):
    lines = []

    if not os.environ["GOOGLE_APPLICATION_CREDENTIALS"]:
        print("Please make sure the environment variable GOOGLE_APPLICATIONS_CREDENTIALS is set to the path of your "
              "credentials file", file=sys.stderr)
        exit(1)
    client = vision.ImageAnnotatorClient()

    col = Image.open(file)
    bw = col.convert('L')
    bw.save("newfile.png")
    file = "newfile.png"

    with io.open(file, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)
    document = response.full_text_annotation

    for page in document.pages:
        for block in page.blocks:
            print('\n\n')

            for paragraph in block.paragraphs:

                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])




   # print(paragraphs)
   # print(lines)




"""
    headers = {
        "Authorization": "Bearer AIzaSyBvmh8i8Xenxa64k-DIo27nF6zykGK1zCU",
        "Content-Type": "application/json; charset=utf-8"
    }
    data = {
        'requests': [
            {
                'image': {
                    'source': {
                        'imageUri': file
                    }
                },
                'features': [
                    {
                        'type': 'TEXT_DETECTION'
                    }
                ]
            }
        ]
    }
    req = requests.post(url='https://vision.googleapis.com/v1/images:annotate', headers=headers, json=data)
    print(req.reason)
"""

if __name__ == "__main__":
    ocr_main('python_code.png', 'python')
