
import requests
from .models import ImageMetadata
from celery import shared_task
from django.core.files.base import ContentFile
from django.apps import apps
from dotenv import load_dotenv
import os
import base64


load_dotenv()
STABILITY_API_KEY=os.getenv("STABILITY_API_KEY")
STABILITY_API_URL=os.getenv("STABILITY_API_URL")

@shared_task
def image_gen_worker(prompt: str):
    """
    This Celery task worker function generates an image using a provided prompt 
    and saves it.

    Args:
        prompt (str): The text prompt for the image generation.

    Returns:
        str: A message indicating success or failure with the image generation.
    """
    
    try:

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {STABILITY_API_KEY}",  # Replace with actual API key
        }

        # Prepare the data for the API request
        data = {
            "text_prompts": [
                {
                    "text": prompt,
                }
            ],
            "cfg_scale": 7,  # Adjust this parameter for image generation quality
            "height": 1024,
            "width": 1024,
            "samples": 1,  # Number of images to generate (set to 1 here)
            "steps": 30,  # Number of steps for image generation process
        }

        # Send a POST request to the image generation API
        response = requests.post(STABILITY_API_URL, headers=headers, json=data)

        # Check for successful response
        if response.status_code == 200:
            result = response.json()

            # Extract base64 encoded image data
            image_data = result['artifacts'][0]['base64']
            image_data = base64.b64decode(image_data)

            # Save the image using the ImageMetadata object 
            generated_image = ImageMetadata(prompt=prompt)
            file_name = f"generated_image_{generated_image.id}.png"
            generated_image.image_generated.save(file_name, ContentFile(image_data), save=False)
            generated_image.save()

            # Return a success message with the generated image ID
            return f"Image generated and saved with ID: {generated_image.id}"
        else:
            return f"API request failed with status code {response.status_code}"

    except Exception as e:
        # Handle any errors during the process
        return str(e)
