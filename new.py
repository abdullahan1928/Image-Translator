from google.cloud import vision_v1
from google.cloud import translate_v2 as translate
from google.protobuf.json_format import MessageToDict
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Set up the credentials (replace 'your-credentials.json' with your actual JSON key file)
credentials_path = 'credentials.json'

# Initialize Vision API client
vision_client = vision_v1.ImageAnnotatorClient.from_service_account_json(
    credentials_path)

# Initialize Translation API client
translation_client = translate.Client.from_service_account_json(
    credentials_path)

# Load your image
image_path = 'image.jpg'
target_language = 'en'  # Replace with your target language code

# Perform OCR on the image
with open(image_path, 'rb') as image_file:
    content = image_file.read()

image = vision_v1.Image(content=content)
response = vision_client.text_detection(image=image)
annotations = response.text_annotations

# Extract the detected text
if annotations:
    detected_text = annotations[0].description

    # Translate the detected text
    translation = translation_client.translate(
        detected_text, target_language=target_language)
    translated_text = translation['translatedText']
    print(f"Translation ({target_language}): {translated_text}")

    # Open the original image using Pillow
    original_image = Image.open(image_path)

    # Get the bounding box of the detected text to apply blur
    vertices = annotations[0].bounding_poly.vertices
    left_top = (vertices[0].x, vertices[0].y)
    right_bottom = (vertices[2].x, vertices[2].y)

    # Crop the area containing the detected text and apply blur
    text_area = original_image.crop(
        (left_top[0], left_top[1], right_bottom[0], right_bottom[1]))
    text_area = text_area.filter(ImageFilter.GaussianBlur(radius=10))

    # Paste the blurred text area back onto the original image
    original_image.paste(text_area, (left_top[0], left_top[1]))

    # Set the position and font for the translated text
    position = (50, 50)  # Adjust the coordinates as needed
    # Adjust the font and size as needed
    font = ImageFont.truetype("arial.ttf", 24)

    # Draw the translated text on the image
    draw = ImageDraw.Draw(original_image)
    draw.text(position, translated_text, (255, 255, 255), font=font)

    # Save the new image with translated text and blurred original text
    output_image_path = 'translated_image.jpg'
    original_image.save(output_image_path)
    print(f"Translated image saved as {output_image_path}")
else:
    print('No text found in the image.')
