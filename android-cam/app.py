from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stitch', methods=['POST'])
def stitch_images():
    images = request.files.getlist('images')

    if not images:
        return jsonify({'error': 'No images provided'})

    # Read and stitch images
    stitched_image = stitch_images_opencv(images)

    # Save the stitched image (optional)
    cv2.imwrite('stitched_image.jpg', stitched_image)

    # Convert the stitched image to base64 for sending to the client
    _, img_encoded = cv2.imencode('.jpg', stitched_image)
    img_base64 = img_encoded.tobytes().decode('utf-8')

    return jsonify({'result': img_base64})

def stitch_images_opencv(images):
    imgs = [cv2.imdecode(np.fromstring(img.read(), np.uint8), cv2.IMREAD_COLOR) for img in images]
    
    # Perform stitching using OpenCV
    stitcher = cv2.Stitcher_create()
    status, stitched_image = stitcher.stitch(imgs)

    if status == cv2.Stitcher_OK:
        return stitched_image
    else:
        return np.zeros((1, 1, 3), dtype=np.uint8)

if __name__ == '__main__':
    app.run(debug=True)
