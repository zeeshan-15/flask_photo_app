import os

from flask import Flask, send_from_directory, url_for, json
from flask import request, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def hello_world():
    return render_template('index.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/uploadajax', methods=['GET', 'POST'])
def uploadajax():
    files = request.files.getlist('file')
    files_path = []
    for file in files:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        files_path.append({'file_name': filename, 'path': url_for('uploaded_file', filename=filename)})
    return render_template('files_data.html', files=files_path)


if __name__ == '__main__':
    app.run()





# import os
# from flask import Flask, flash, request, redirect, render_template, jsonify, send_from_directory, url_for, json
# from werkzeug.utils import secure_filename
#
# app = Flask(__name__)
#
# app.secret_key = "secret key"
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
#
# path = os.getcwd()
#
# UPLOAD_FOLDER = os.path.join(path, 'uploads')
#
# if not os.path.isdir(UPLOAD_FOLDER):
#     os.mkdir(UPLOAD_FOLDER)
#
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#
# ALLOWED_EXTENSIONS = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv']
#
#
# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
#
#
# @app.route('/')
# def upload_form():
#     return render_template('upload.html')
#
#
# @app.route('/', methods=['POST'])
# def upload_file():
#
#     if request.method == 'POST':
#
#         if 'files[]' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#
#         files = request.files.getlist('files[]')
#
#         for file in files:
#             if file and allowed_file(file.filename):
#                 filename = secure_filename(file.filename)
#                 file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#                 return jsonify({'file':file})
#             return jsonify({'error': 'Missing detail'})
#
#         flash('File(s) successfully uploaded')
#         return redirect('/')
#
#
# if __name__ == "__main__":
#     app.run(host='127.0.0.1', port=5000, debug=False, threaded=True)


