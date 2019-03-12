# -*- coding: utf-8 -*-
# __author__="ZJL"

from flask import Flask
from flask import request
from flask import Response
import json
import demo02_2

app = Flask(__name__)


def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/')
def hello_world():
    return Response_headers('hello world!!!')


@app.route('/run', methods=['POST'])
def run():
    if request.method == 'POST' and request.form['code']:
        code = request.form['code']
        jsondata = demo02_2.main(code)
        return Response_headers(str(jsondata))


@app.errorhandler(403)
def page_not_found(error):
    content = json.dumps({"error_code": "403"})
    resp = Response_headers(content)
    return resp


@app.errorhandler(404)
def page_not_found(error):
    content = json.dumps({"error_code": "404"})
    resp = Response_headers(content)
    return resp


@app.errorhandler(400)
def page_not_found(error):
    content = json.dumps({"error_code": "400"})
    resp = Response_headers(content)
    return resp


@app.errorhandler(405)
def page_not_found(error):
    content = json.dumps({"error_code": "405"})
    resp = Response_headers(content)
    return resp


@app.errorhandler(410)
def page_not_found(error):
    content = json.dumps({"error_code": "410"})
    resp = Response_headers(content)
    return resp


@app.errorhandler(500)
def page_not_found(error):
    content = json.dumps({"error_code": "500"})
    resp = Response_headers(content)
    return resp


if __name__ == '__main__':
    app.run(debug=True)
