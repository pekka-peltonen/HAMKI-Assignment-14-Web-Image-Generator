# HAMKI-Assignment-14-Web-Image-Generator# HAMKI Assignment #14 - Web-based Image Generator

Author: Pekka Peltonen

## Description
A Streamlit web application that generates images from text prompts using the OpenAI image-generation API.

## Features
- Enter an image description.
- Select image size and quality.
- Generate and display an image.
- Download the generated image as a PNG file.
- Handle empty prompts and API errors.

## Requirements
- Python
- streamlit
- openai
- OpenAI API key

## Installation
Install the required packages:

```bash
pip install streamlit openai
```

Set your OPENAI_API_KEY environment variable.

## Run
```bash
python -m streamlit run app.py
```

Open the local Streamlit address in your browser.

## Model
OpenAI gpt-image-2

## Testing
Image generation, image display, PNG download and empty-prompt validation were successfully tested.
