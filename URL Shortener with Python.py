# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 13:34:46 2023

@author: User
"""

from flask import Flask, request, redirect, render_template
import string
import random

app = Flask(__name__)

url_database = {}
short_url_length = 6

def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(short_url_length))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form.get('original_url')

    if not original_url:
        return "URL is required", 400

    short_url = generate_short_url()
    url_database[short_url] = original_url

    short_url = request.url_root + short_url
    return render_template('result.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_to_original(short_url):
    original_url = url_database.get(short_url)

    if original_url:
        return redirect(original_url)
    else:
        return "Short URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)
            

