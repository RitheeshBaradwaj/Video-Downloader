from __future__ import unicode_literals
from flask import Flask, render_template, redirect, url_for, request
import os
import youtube_dl
global link
app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/download', methods=['POST'])
def download():
    path=request.form.get("path")
    link=request.form.get("link")
    #link = [str(x) for x in request.form.values()]
    #link=link[0]
    try:
        ydl_opts = {}
        os.chdir(path)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(['{}'.format(link)])
        return render_template('index.html', status_text='Downloaded succesfully!!')
    except:
        return render_template('index.html', status_text='hey mate its an invalid Input :( ')
if __name__ == '__main__':
	app.run(port = 5000, debug=True)
    