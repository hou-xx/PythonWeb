#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
import codecs

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    f = codecs.open('/home/cxwh/flask/html/demo.html', 'r',encoding='utf-8')
    txt = f.read()
    f.close()
    return txt

@app.route('/getContent', methods=['GET', 'POST'])
def getContent():
    f = codecs.open('/home/cxwh/flask/work.txt', 'r',encoding='utf-8')
    txt = f.read()
    f.close()
    return txt

@app.route('/update', methods=['POST'])
def update():
    # 需要从request对象读取表单内容：
    content = request.form['content']
    f = codecs.open('/home/cxwh/flask/work.txt', 'w',encoding='utf-8')
    f.write(content)
    f.close()
    return ''
