from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import base64
import io
import time
import algorithm1  # Henon Map
import algorithm2  # Rossler Attractor

app = Flask(__name__)
CORS(app)

def image_to_base64(img):
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

@app.route('/process', methods=['POST'])
def process_image():
    try:
        file = request.files.get('image')
        if not file:
            return jsonify({"error": "No file uploaded"}), 400

        img = Image.open(file).convert("L")

        # Validasi ukuran gambar
        if img.size[0] < 64 or img.size[1] < 64:
            return jsonify({"error": "Image size must be at least 64x64 pixels"}), 400

        # Proses dengan Algoritma 1
        start = time.time()
        algo1_result, algo1_perf = algorithm1.process(img)
        algo1_perf["time"] = time.time() - start

        # Proses dengan Algoritma 2
        start = time.time()
        algo2_result, algo2_perf = algorithm2.process(img)
        algo2_perf["time"] = time.time() - start

        return jsonify({
            "algorithm1": {
                "image": image_to_base64(algo1_result),
                "performance": algo1_perf
            },
            "algorithm2": {
                "image": image_to_base64(algo2_result),
                "performance": algo2_perf
            }
        })
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
