# Image-Translator

<br/>

## Introduction

Welcome to the Image Translator project, a tool that can recognize and translate text from images. This project uses follwoing two libraries:
- [Google Cloud Vision API](https://cloud.google.com/vision?hl=en)
- [Google Cloud Translation API](https://cloud.google.com/translate/docs/reference/rest)

<br/>

## Getting Started

### Prerequisites

Before you can run this project, make sure you have the following prerequisites in place:

- Python 3.6 or higher
- Google Cloud Platform (GCP) account with billing enabled
- Enabled [Cloud Vision API](https://console.cloud.google.com/marketplace/product/google/vision.googleapis.com?project=translating-images-api) and [Cloud Translation API](https://console.cloud.google.com/apis/library/translate.googleapis.com?project=translating-images-api) in your GCP project
- `pip` installed


### Installation

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/abdullahan1928/Image-Translator.git
   ```

2. Navigate to the project directory:

   ```
   cd image-translator
   ```
3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

### Setting Up Google Cloud Credentials

In order to use the Google Cloud APIs, you need to set up the credentials.json file:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).

2. Create a new project or select an existing one.

3. In the left sidebar, navigate to "APIs & Services" > "Credentials."

4. Click on "Create Credentials" and select "Service Account Key."

5. Choose a service account name, set the role to "Project" > "Editor," and select "JSON" as the key type.

6. Click "Create" to download the JSON file. Rename it to credentials.json and move it to the project's root directory.

7. Go to the "API Marketplace" and enable both [Cloud Vision API](https://console.cloud.google.com/marketplace/product/google/vision.googleapis.com?project=translating-images-api) and [Cloud Translation API](https://console.cloud.google.com/apis/library/translate.googleapis.com?project=translating-images-api)

Note: Make sure to keep your credentials.json file secure and do not share it publicly.

<br/>

## Running the Project

To run the Image Translator project, follow these steps:

1. Open a terminal and navigate to the project directory.

2. Copy the `credentials.json` file in the folder.

3. Change image path in the `app.py` file to select desired image to translate.

4. Run the main Python script:

    ```
    python app.py
    ```

5. After processing, the translated text will be displayed in terminal.

