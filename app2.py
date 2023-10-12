from google.cloud import vision_v1
from googletrans import Translator

translator = Translator()

# Set up the credentials (replace 'your-credentials.json' with your actual JSON key file)
credentials_path = 'credentials.json'

# Initialize Vision API client
vision_client = vision_v1.ImageAnnotatorClient.from_service_account_json(
    credentials_path)

# Load your image
image_path = '56450045_p2.jpg'
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
    print(f'Detected text: {detected_text}')

    translations = translator.translate(detected_text, dest='en')
    print(f'Translated text: {translations.text}')
else:
    print('No text found in the image.')
