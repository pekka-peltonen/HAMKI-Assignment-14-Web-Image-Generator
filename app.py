
import base64
import binascii

import streamlit as st
import openai
from openai import OpenAI

MODEL = "gpt-image-2"

st.title("AI Image Generator")
st.write("HAMKI Assignment #14")
st.write("Generate and download images using OpenAI.")

prompt = st.text_area(
    "Describe the image you want to generate"
)

size = st.selectbox(
    "Image size",
    ["1024x1024", "1536x1024", "1024x1536"]
)

quality = st.selectbox(
    "Image quality",
    ["low", "medium", "high"],
    index=1
)

if st.button("Generate image"):
    if not prompt.strip():
        st.warning("Please enter an image description.")
    else:
        try:
            client = OpenAI()

            with st.spinner("Generating image..."):
                result = client.images.generate(
                    model=MODEL,
                    prompt=prompt,
                    size=size,
                    quality=quality,
                    n=1,
                )

            if not result.data or not result.data[0].b64_json:
                raise RuntimeError("No image data returned.")

            image_bytes = base64.b64decode(
                result.data[0].b64_json,
                validate=True
            )

            st.image(
                image_bytes,
                caption="Generated image"
            )

            st.download_button(
                "Download image",
                data=image_bytes,
                file_name="generated_image.png",
                mime="image/png"
            )

        except (
            openai.OpenAIError,
            RuntimeError,
            binascii.Error
        ) as error:
            st.error(f"Image generation failed: {error}")
