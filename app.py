from flask import Flask, render_template, request
import os
import base64
import subprocess
from script import process_image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        image_path = os.path.join('uploads', uploaded_file.filename)
        uploaded_file.save(image_path)
        # Perform OCR on the uploaded image using script.py
        ocr_result = process_image(image_path)
        # Convert input image to base64 for displaying in HTML
        # with open(image_path, "rb") as img_file:
        #     img_data = base64.b64encode(img_file.read()).decode('utf-8')
        # return render_template('result.html', image=f"data:image/jpeg;base64,{img_data}", ocr_result=ocr_result)
        return render_template('result.html',ocr_result=ocr_result)
    return 'No file uploaded'

if __name__ == '__main__':
    app.run(debug=True)
