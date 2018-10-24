#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
from subprocess import check_output
import subprocess
import urllib
import json
import re


subprocess.call(['chmod a+x ../../app/1-source-retrieve.sh'], shell=True)
subprocess.call(['chmod a+x ../../app/2-build.sh'], shell=True)
subprocess.call(['chmod a+x ../../app/3-artifacts-push.sh'], shell=True)
#making shell scripts available for calls


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

@application.route('/api/build/<passwd>', methods=['POST'])
def build_test(passwd):
    """
    test build
    """ 
    print ('hello world')
    print ('password is ' + passwd)
    
    subprocess.call(['../../app/1-source-retrieve.sh '], shell=True)
    subprocess.call(['../../app/2-build.sh '], shell=True)
    subprocess.call(['../../app/3-artifacts-push.sh ' + passwd], shell=True)
    
#    subprocess.call(['1-source-retrieve.sh '], shell=True)
#    subprocess.call(['2-build.sh '], shell=True)
#    subprocess.call(['3-artifacts-push.sh ' + passwd], shell=True)
    
    return ("hello world", 200, None)    

if __name__ == '__main__':
    application.run(debug=True, use_reloader=True)