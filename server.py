#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
from subprocess import check_output
import subprocess
import urllib
import json
import re


application = Flask(__name__)


def parse_request(req):
    """
    Parses application/json request body data into a Python dictionary
    """
    payload = req.get_data()
    payload = urllib.parse.unquote_plus(payload)
    payload = p.encode()
    payload = re.sub('payload=', '', payload)
    payload = json.loads(payload)

    return payload


@application.route('/', methods=['GET'])
def index():
    """
    Go to localhost:5000 to see a message
    """
    return ('This is a website.', 200, None)

@application.route('/api/build', methods=['POST'])
def build_test():
    """
    test build
    """
#    payload = parse_request(request)
    print ('hello world')
    subprocess.call(['build.bat'], shell=True)
    return ("hello world", 200, None)    

if __name__ == '__main__':
    application.run(debug=True, use_reloader=True)