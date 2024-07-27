import requests
from PIL import Image

# Replace 'your_api_key' with your actual API key from Stability AI
api_key = 'REDACTED'
endpoint = 'https://api.stability.ai/v2beta/image-to-video'

# Resize the image to one of the supported dimensions
def resize_image(input_path, output_path, size):
    with Image.open(input_path) as img:
        img = img.resize(size, Image.Resampling.LANCZOS)
        img.save(output_path)

# Path to your input image
input_image_path = 'creators.png'
# Path to save the resized image
resized_image_path = 'resized_creators.png'
# Resize to one of the supported dimensions (e.g., 768x768)
resize_image(input_image_path, resized_image_path, (768, 768))

headers = {
    'Authorization': f'Bearer {api_key}'
}

# Prepare the resized image file to upload
files = {
    'image': open(resized_image_path, 'rb')
}

# Additional parameters as data
data = {
    'output_format': 'mp4',
    'frame_rate': 24,
    'duration': 2  # Duration in seconds
}

response = requests.post(endpoint, headers=headers, files=files, data=data)

if response.status_code == 200:
    with open('generated_video.mp4', 'wb') as video_file:
        video_file.write(response.content)
    print("Video generated successfully!")
else:
    print("Failed to generate video:", response.status_code, response.text)
