from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generateCaptions(imagePath):
    image = Image.open(imagePath).convert("RGB")

    inputs = processor(image, return_tensors="pt")

    output = model.generate(**inputs)

    caption = processor.decode(output[0], skip_special_tokens = True)

    return caption