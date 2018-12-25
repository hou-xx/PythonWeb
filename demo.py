#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request, send_from_directory
import codecs, os

app = Flask(__name__)

base_path = os.path.dirname(os.path.realpath(__file__))  # 获取脚本路径

upload_path = os.path.join(base_path, 'upload')  # 上传文件目录
if not os.path.exists(upload_path):
    os.makedirs(upload_path)


@app.route('/', methods=['GET', 'POST'])
def home():
    f = codecs.open(os.path.join(os.path.join(base_path, 'html'), 'demo.html'), 'r', encoding='utf-8')
    txt = f.read()
    f.close()
    return txt


@app.route('/getContent', methods=['GET', 'POST'])
def getContent():
    f = codecs.open(os.path.join(os.path.join(base_path, 'work'), 'work.txt'), 'r', encoding='utf-8')
    txt = f.read()
    f.close()
    return txt


@app.route('/getFileName', methods=['GET', 'POST'])
def getFileName():
    f = codecs.open(os.path.join(upload_path, 'filename.txt'), 'r', encoding='utf-8')
    file_name = f.read()
    f.close()
    return file_name


@app.route('/update', methods=['POST'])
def update():
    # 需要从request对象读取表单内容：
    content = request.form['content']
    f = codecs.open(os.path.join(os.path.join(base_path, 'work'), 'work.txt'), 'w', encoding='utf-8')
    f.write(content)
    f.close()
    return ''


@app.route('/uploadFile', methods=['POST'])
def uploadFile():
    # 需要从request对象读取表单内容：
    filedata = request.files.get('file')
    if filedata:
        filePath = os.path.join(upload_path, filedata.filename)
        f = codecs.open(os.path.join(upload_path, 'filename.txt'), 'w', encoding='utf-8')
        f.write(filedata.filename)
        f.close()
        try:
            filedata.save(filePath)  #  上传文件写入
        except IOError:
            return '上传文件失败'
        return '上传文件成功, 文件名: {}'.format(filePath)
    else:
        return '上传文件失败'


@app.route('/downloadFile', methods=['GET'])
def downloadFile():
    f = codecs.open(os.path.join(upload_path, 'filename.txt'), 'r', encoding='utf-8')
    file_name = f.read()
    print(file_name)
    f.close()
    return send_from_directory(upload_path, file_name, as_attachment=True)  # 返回要下载的文件内容给客户端
