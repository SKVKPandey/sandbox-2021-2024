import requests

response = requests.post(
    f"https://api.stability.ai/v2beta/image-to-video",
    headers={
        "authorization": f"REDACTED"
    },
    files={
        "image": open("./creators.png", "rb")
    },
    data={
        "seed": 0,
        "cfg_scale": 1.8,
        "motion_bucket_id": 127
    },
)

print("Generation ID:", response.json().get('id'))