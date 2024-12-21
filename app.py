import os
from flask import Flask, request, render_template, send_from_directory, redirect, url_for
from rembg import remove
from io import BytesIO
from PIL import Image

app = Flask(__name__)

# Folder untuk menyimpan gambar hasil
OUTPUT_FOLDER = "static/processed_images"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def upload_page():
    return render_template('index.html')

@app.route('/remove-bg', methods=['POST'])
def remove_background():
    if 'image' not in request.files:
        return "No image uploaded!", 400

    file = request.files['image']
    input_image = file.read()

    # Hapus background
    output_image = remove(input_image)

    # Simpan hasil ke file di folder static
    output_filename = os.path.join(OUTPUT_FOLDER, "output.png")
    with open(output_filename, "wb") as f:
        f.write(output_image)

    # Redirect ke halaman download
    return redirect(url_for('download_page'))

@app.route('/download')
def download_page():
    return render_template('download.html', image_url=url_for('static', filename='processed_images/output.png'))

@app.route('/download-image')
def download_image():
    # Kirim file hasil untuk diunduh
    return send_from_directory(OUTPUT_FOLDER, "output.png", as_attachment=True)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8000)
