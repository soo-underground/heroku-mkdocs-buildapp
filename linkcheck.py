#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
from subprocess import check_output
import subprocess
import urllib
import json
import re
from pylinkvalidator.api import crawl_with_options
import http.server
import socketserver
import os

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler
dir = "docpage-source/my-project/site"
time = "10"
os.chdir(dir)
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    
    httpd.serve_forever()
    crawled_site = crawl_with_options(["http://127.0.0.1:8080"], {"workers": 10, "test-outside": True, "progress": True},)
    number_of_crawled_pages = len(crawled_site.pages)
    number_of_errors = len(crawled_site.error_pages) 

    print (number_of_crawled_pages)
   


print ('hello world')


crawled_site = crawl_with_options(["https://soo-underground.github.io"], {"workers": 10, "test-outside": True, "progress": True},)
number_of_crawled_pages = len(crawled_site.pages)
number_of_errors = len(crawled_site.error_pages) 

print (number_of_crawled_pages)

#print (crawled_site.pages)
 
print (number_of_errors)

print (crawled_site.error_pages)