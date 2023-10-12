from google.cloud import vision_v1
from google.cloud import translate_v2 as translate
from google.protobuf.json_format import MessageToDict

# Set up the credentials (replace 'your-credentials.json' with your actual JSON key file)
credentials_path = 'credentials.json'

# Initialize Vision API client
vision_client = vision_v1.ImageAnnotatorClient.from_service_account_json(
    credentials_path)

# Initialize Translation API client
translation_client = translate.Client.from_service_account_json(
    credentials_path)

# Load your image
image_path = 'img.jpg'
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

    # print detected text language
    print(f'Detected text language: {annotations[0].locale}')

    # Translate the detected text
    translation = translation_client.translate(
        detected_text, target_language=target_language)
    translated_text = translation['translatedText']

    print(f"Translation ({target_language}): {translated_text}")
else:
    print('No text found in the image.')
