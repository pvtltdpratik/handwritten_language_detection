# pip install transformers torch torchvision timm pillow
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import requests

# Load the model and processor
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")

# Load your image (replace 'handwritten_sample.jpg' with your image path)
image_path = "handwritten_sample.jpg"
image = Image.open(image_path).convert("RGB")

# Preprocess and perform text detection
pixel_values = processor(images=image, return_tensors="pt").pixel_values
generated_ids = model.generate(pixel_values)

# Decode output text
detected_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
print("Detected Handwritten Text:", detected_text)
