from flask import Flask
from flask import url_for
from flask import request
from flask import render_template
from flask import flash
from pytube import YouTube
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aksndkasnd'


def write_to_file(content):
    with open("text.txt","w+") as f:
        if content == None:
            pass
        else:
            f.write(content)
            f.write('\n')
        f.close()


@app.route('/', methods=['GET', 'POST'])
def hello():
    data = request.form.get('song')
    write_to_file(data)
    os.system('python music.py')
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(debug=True)
    