from flask import Flask, render_template, request
import os
from PIL import Image
import pytesseract
from threading import Timer
import webbrowser

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
    
# function "index" applies template to open browser tab
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
    
# function "upload" uses pytesseract to extract and display text 
# function "upload" includes error handling
def upload():
    if 'image' not in request.files:
        return "No image uploaded", 400
    image_file = request.files['image']
    if image_file.filename == '':
        return "No selected file", 400

    image_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
    image_file.save(image_path)

    text = pytesseract.image_to_string(Image.open(image_path))
    return f"<h3>Extracted Text:</h3><pre>{text}</pre>"

# function "open_browser" activates new tab, containing user interface, in default browser using provided URL
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")
    
if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run()
