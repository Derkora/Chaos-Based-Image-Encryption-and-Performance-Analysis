from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import base64
import io
import time
import algHenon  # Henon Map
import algRossler  # Rossler Attractor

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

        # Proses dengan Henon Map
        start = time.time()
        henon_result, henon_perf = algHenon.process(img)
        henon_perf["time"] = time.time() - start

        # Proses dengan Rossler Attractor
        start = time.time()
        rossler_result, rossler_perf = algRossler.process(img)
        rossler_perf["time"] = time.time() - start

        return jsonify({
            "henon": {
                "image": image_to_base64(henon_result),
                "performance": henon_perf
            },
            "rossler": {
                "image": image_to_base64(rossler_result),
                "performance": rossler_perf
            }
        })
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
