#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request, send_from_directory
from flask import make_response
import codecs, os


app = Flask(__name__)

base_path = os.path.dirname(os.path.realpath(__file__))  # 获取脚本路径

temp_file_name = 'file_name'

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
    f = codecs.open(os.path.join(upload_path, temp_file_name), 'r', encoding='utf-8')
    file_name = f.read().encode("latin-1").decode('utf-8')
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
        file_name =  filedata.filename.encode("utf-8").decode('latin-1')
        file_path = os.path.join(upload_path,file_name)
        f = codecs.open(os.path.join(upload_path, temp_file_name), 'w', encoding='utf-8')
        f.write(file_name)
        f.close()
        try:
            filedata.save(file_path)  #  上传文件写入
        except IOError:
            return '上传文件失败'
        return u'上传文件成功, 文件名: {}'.format(file_path)
    else:
        return '上传文件失败'


@app.route('/downloadFile', methods=['GET'])
def downloadFile():
    f = codecs.open(os.path.join(upload_path, temp_file_name), 'r', encoding='utf-8')
    file_name = f.read()
    f.close()
    response = make_response(send_from_directory(upload_path, file_name))
    response.headers["Content-Disposition"] = u"attachment; filename={}".format(file_name)
    return response # 返回要下载的文件内容给客户端
