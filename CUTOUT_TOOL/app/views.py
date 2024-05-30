from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
from rembg import remove
from django.core.files.storage import FileSystemStorage
from datetime import datetime
import os

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}

def home(request):
    return render(request, 'home.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def remove_background(input_path, output_path):
    input_image = Image.open(input_path)
    output = remove(input_image)
    output = output.convert("RGBA")
    output.save(output_path, "PNG")

import os
import shutil

def remback(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        if file and allowed_file(file.name):
            # Deleting old files
            for filename in os.listdir(UPLOAD_FOLDER):
                file_path = os.path.join(UPLOAD_FOLDER, filename)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")

            fs = FileSystemStorage(location=UPLOAD_FOLDER)  # Specify the upload directory
            filename = fs.save(file.name, file)
            input_path = fs.path(filename)
            output_path = os.path.join(UPLOAD_FOLDER, filename.split('.')[0] + "_rembg.png")
            remove_background(input_path, output_path)
            # Your additional processing or database insertion code here
            return render(request, 'home.html', {
                'org_img_name': filename,
                'rembg_img_name': filename.split('.')[0] + "_rembg.png",
                'download_link': output_path
            })
    return HttpResponse("Invalid request")


def download(request, filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type="image/png")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    return HttpResponse("File not found")
