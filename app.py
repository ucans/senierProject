import logging
import os
from flask import Flask, render_template, request
from flask import send_from_directory

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

    return render_template('predict.html', image_file_name=file.filename)


@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == '__main__':
    # 0.0.0.0 외부 접속 허용
    app.run(host = "0.0.0.0", port = 5000, debug=True)