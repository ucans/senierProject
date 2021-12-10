import logging
import os

import cv2
import numpy
from flask import Flask, render_template, request
from flask import send_from_directory
from inference import LInference
from PIL import Image

# flask 객체 instance 생성
app = Flask(__name__)

dir_path = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = 'uploads'
STATIC_FOLDER = 'static'


@app.route('/')
def home():
    return render_template('index.html')


# procesing uploaded file and predict it
@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        file = request.files['image']
        print('The dir path', dir_path)
        full_name = os.path.join(dir_path, UPLOAD_FOLDER, file.filename)
        file.save(full_name)
        # 업로드한 사진 불러오기
        read_img = Image.open(file)
        # Latex 문자열로 변환
        latex_data = inf.getLatext(read_img)[0]
        # Todo : Latex 이미지로 변환

    return render_template('predict.html', image_file_name=file.filename, latex_data=latex_data)


@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == '__main__':
    inf = LInference()
    # 0.0.0.0 외부 접속 허용
    app.run(host = "0.0.0.0", port = 5000, debug=True)