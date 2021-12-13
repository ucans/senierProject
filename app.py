import logging
import os
from flask import Flask, render_template, request
from flask import send_from_directory
from inference import LInference
from PIL import Image
from io import BytesIO
import urllib.request
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse

# flask 객체 instance 생성
app = Flask(__name__)

dir_path = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = 'uploads'
STATIC_FOLDER = 'static'
PREDICT_FOLDER = 'predicts'


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
        predict_file = os.path.join(dir_path, PREDICT_FOLDER, file.filename)
        save_latex_img(latex_data, predict_file)

    return render_template('predict.html', image_file_name=file.filename, latex_data=latex_data)


@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


@app.route('/predicts/<filename>')
def send_latex_img(filename):
    return send_from_directory(PREDICT_FOLDER, filename)


def save_latex_img(latex_data, predict_file):
    urlString = "http://www.sciweavers.org/tex2img.php?eq=%5Csqrt%5B3%5D%7Bx%5E3%2By%5E3%20%5Cover%202%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0"
    url = urlparse(urlString)
    qs = dict(parse_qsl(url.query))
    qs['eq'] = latex_data
    parts = url._replace(query=urlencode(qs))
    url = urlunparse(parts)

    latex_hex_img = urllib.request.urlopen(url).read()
    Image.open(BytesIO(latex_hex_img)).convert('RGB').save(predict_file)


if __name__ == '__main__':
    inf = LInference()
    # 0.0.0.0 외부 접속 허용
    app.run(host = "0.0.0.0", port = 5000, debug=True)