from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
import logging 

# Load the model and processor once and reuse them
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generateCaptions(image_path):
    try:
        image = Image.open(image_path).convert("RGB")
        inputs = processor(image, return_tensors="pt")
        with torch.no_grad():
            output = model.generate(**inputs)
        caption = processor.decode(output[0], skip_special_tokens=True)
        return caption
    except Exception as e:
        logging.error(f"Failed to generate caption: {str(e)}")
        return None
