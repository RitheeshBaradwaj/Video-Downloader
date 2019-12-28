from flask import Flask, render_template, redirect, url_for, request
import os
global link
app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/download', methods=['POST'])
def download():
    link = [str(x) for x in request.form.values()]
    link=link[0]
    try:
        with open('link.bat','w') as down_load:
            down_load.write(f'youtube-dl {link}')
            down_load.close()
        os.startfile('link.bat')
        return render_template('index.html', status_text='Downloaded succesfully!!')
    except:
        return render_template('index.html', status_text='hey mate its an invalid Input :( ')
if __name__ == '__main__':
	app.run(port = 5000, debug=True)
    